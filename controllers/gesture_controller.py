"""
Main controller that coordinates between models, services and views.
Handles the core application logic flow.
"""
from models.gesture_model import GestureModel
from services.app_service import AppService
from services.drawing_service import DrawingService
from services.text_service import TextService
from config import constants as const
from pynput.keyboard import Controller

class GestureController:
    def __init__(self):
        """Initialize all application components"""
        self.gesture_model = GestureModel()  # Hand detection model
        self.app_service = AppService()  # Application launcher
        self.drawing_service = DrawingService(const.RES_X, const.RES_Y)  # Drawing canvas
        self.text_service = TextService()  # Virtual keyboard
        self.keyboard = Controller()  # System keyboard controller
        self.view = MainView()  # Display manager
        
    def process_frame(self, frame):
        """Process each camera frame through the pipeline"""
        # Flip and add help tip
        frame = cv2.flip(frame, 1)
        frame = self.view.display_tip(frame, 
            "Raise right hand's fingers for instructions. Press 'ESC' to exit.")
        
        # Detect hands and process gestures
        frame, all_hands = self.gesture_model.detect_hands(frame)
        
        if len(all_hands) == 1:
            self._process_single_hand(frame, all_hands[0])
        elif len(all_hands) == 2:
            frame = self._process_two_hands(frame, all_hands)
        
        # Update displays
        self.view.display(frame)
        if hasattr(self.drawing_service, 'board'):
            self.view.show_drawing_board(self.drawing_service.board)
            
        return frame
    
    def _process_single_hand(self, frame, hand):
        """Handle single-hand gestures"""
        fingers = self.gesture_model.get_fingers_up(hand)
        
        if hand['side'] == 'Right':
            self.text_service.process_right_hand(frame, hand, fingers)
        else:
            self.app_service.process_left_hand(fingers)
    
    def _process_two_hands(self, frame, hands):
        """Handle two-hand interaction (drawing mode)"""
        left_hand = next((h for h in hands if h['side'] == 'Left'), None)
        right_hand = next((h for h in hands if h['side'] == 'Right'), None)
        
        if left_hand and right_hand:
            left_fingers = self.gesture_model.get_fingers_up(left_hand)
            right_fingers = self.gesture_model.get_fingers_up(right_hand)
            
            self.drawing_service.process_drawing_gestures(
                frame, left_hand, left_fingers, right_hand, right_fingers
            )
        return frame
    
    def cleanup(self):
        """Save results and release resources"""
        self.text_service.save_text()
        self.drawing_service.save_drawing()