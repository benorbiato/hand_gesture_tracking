import numpy as np
import cv2
from config import constants as const

class DrawingService:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.reset_board()
        self.brush_color = const.BLUE
        self.brush_thickness = 1
        self.last_x, self.last_y = 0, 0
        
    def reset_board(self):
        self.board = np.ones((self.height, self.width, 3), np.uint8) * 255
        
    def process_drawing_gestures(self, frame, left_hand, left_fingers, right_hand, right_fingers):
        # Configura cor do pincel baseado na mão esquerda
        self._set_brush_color(left_fingers)
        
        # Configura espessura baseado na distância da mão direita
        idx_z = right_hand['coords'][8][2]
        self._set_brush_thickness(idx_z)
        
        # Desenha se o gesto estiver correto
        if right_fingers == const.FINGER_1:
            self._draw_line(right_hand['coords'][8][0], right_hand['coords'][8][1])
        else:
            self.last_x, self.last_y = 0, 0
            
        # Aplica o desenho no frame
        frame = cv2.addWeighted(frame, 1, self.board, 0.2, 0)
        
        return frame
    
    def _set_brush_color(self, fingers):
        finger_count = sum(fingers)
        if finger_count == 1:
            self.brush_color = const.BLUE
        elif finger_count == 2:
            self.brush_color = const.GREEN
        elif finger_count == 3:
            self.brush_color = const.RED
        elif finger_count == 4:
            self.brush_color = const.WHITE
        else:
            self.reset_board()
    
    def _set_brush_thickness(self, z):
        if z < -60:
            self.brush_thickness = 30
        elif z <= -40:
            self.brush_thickness = 20
        else:
            self.brush_thickness = 10
    
    def _draw_line(self, x, y):
        if self.last_x == 0 and self.last_y == 0:
            self.last_x, self.last_y = x, y
            
        cv2.line(self.board, (self.last_x, self.last_y), (x, y), 
                self.brush_color, self.brush_thickness)
        self.last_x, self.last_y = x, y
    
    def save_drawing(self):
        os.makedirs('results', exist_ok=True)
        cv2.imwrite('results/board.png', self.board)