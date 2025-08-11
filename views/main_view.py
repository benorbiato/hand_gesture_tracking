"""
Handles all display logic and window management for the application.
Separates visualization concerns from business logic.
"""
import cv2
from config import constants as const

class MainView:
    def __init__(self):
        """Initialize main application window"""
        self.window_name = 'Hand Gesture Control'
        cv2.namedWindow(self.window_name, cv2.WINDOW_NORMAL)
        cv2.resizeWindow(self.window_name, const.RES_X, const.RES_Y)
        
    def display(self, frame):
        """Display main frame with all annotations"""
        cv2.imshow(self.window_name, frame)
        
    def show_drawing_board(self, drawing_board):
        """Display separate drawing board window"""
        cv2.imshow('Drawing Board', drawing_board)
        
    def display_tip(self, frame, tip_text):
        """Display help tip at the top of the screen"""
        x_tip, y_tip, w_tip, h_tip = 0, 0, const.RES_X, 30
        cv2.rectangle(frame, (x_tip, y_tip), (x_tip + w_tip, y_tip + h_tip), const.WHITE, cv2.FILLED)
        cv2.rectangle(frame, (x_tip, y_tip), (x_tip + w_tip, y_tip + h_tip), const.BLUE, 1)
        cv2.putText(frame, tip_text, (x_tip + 5, y_tip + 20), const.FONT, 0.6, const.BLACK, 1)
        return frame
        
    def close_all(self):
        """Close all OpenCV windows"""
        cv2.destroyAllWindows()