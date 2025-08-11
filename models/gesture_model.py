import cv2
import mediapipe as mp
from config import constants as const

class GestureModel:
    def __init__(self):
        self.mp_hands = mp.solutions.hands
        self.mp_draw = mp.solutions.drawing_utils
        self.hands = self.mp_hands.Hands()
        
    def detect_hands(self, img, flip_side=False):
        """Detect hand landmarks and return their coordinates and side."""
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        result = self.hands.process(img_rgb)
        all_hands = []
        
        if result.multi_hand_landmarks:
            for hand_side, hand_landmarks in zip(result.multi_handedness, result.multi_hand_landmarks):
                hand_info = {}
                coords = []
                for lm in hand_landmarks.landmark:
                    x, y, z = int(lm.x * const.RES_X), int(lm.y * const.RES_Y), int(lm.z * const.RES_X)
                    coords.append((x, y, z))
                hand_info['coords'] = coords
                hand_info['side'] = self._get_hand_side(hand_side, flip_side)
                all_hands.append(hand_info)
                self.mp_draw.draw_landmarks(img, hand_landmarks, self.mp_hands.HAND_CONNECTIONS)
        return img, all_hands
    
    def _get_hand_side(self, hand_side, flip_side):
        label = hand_side.classification[0].label
        return 'Right' if (flip_side and label == 'Left') or (not flip_side and label == 'Right') else 'Left'
    
    def get_fingers_up(self, hand):
        """Return a list indicating which fingers are up."""
        fingers = []
        coords = hand['coords']
        
        # Polegar
        if hand['side'] == 'Right':
            fingers.append(coords[4][0] < coords[3][0])
        else:
            fingers.append(coords[4][0] > coords[3][0])
        
        # Outros dedos
        for tip in [8, 12, 16, 20]:
            fingers.append(coords[tip][1] < coords[tip - 2][1])
            
        return fingers