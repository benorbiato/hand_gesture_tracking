import os
from config import constants as const
from utils.drawing_utils import draw_button

class TextService:
    def __init__(self):
        self.text = ">"
        self.key_delay = 0
        self.key_to_type = ''
        
    def process_right_hand(self, frame, hand, fingers):
        idx_x, idx_y, idx_z = hand['coords'][8]
        
        # Desenha teclado virtual
        for row_idx, row in enumerate(const.KEYS):
            for col_idx, key in enumerate(row):
                key_disp = key.lower() if sum(fingers) <= 1 else key
                pos = (const.OFFSET + col_idx * (const.BTN_SIZE + 30), 
                       const.OFFSET + row_idx * (const.BTN_SIZE + 30))
                color = const.GREEN if self._is_key_pressed(idx_x, idx_y, pos) else const.WHITE
                draw_button(frame, pos, key_disp, const.BTN_SIZE, color)
                
                if self._is_key_pressed(idx_x, idx_y, pos) and idx_z < -65:
                    self._handle_key_press(key_disp)
        
        # Atualiza texto na tela
        self._update_text_display(frame)
        
        # Mostra instruções se todos os dedos estiverem levantados
        if fingers == const.FINGER_ALL:
            self._show_instructions(frame)
    
    def _is_key_pressed(self, x, y, pos):
        return (pos[0] < x < pos[0] + const.BTN_SIZE and 
                pos[1] < y < pos[1] + const.BTN_SIZE)
    
    def _handle_key_press(self, key):
        self.key_delay += 1
        if self.key_delay == 3:
            self.text += key
            self.key_delay = 0
    
    def _update_text_display(self, frame):
        cv2.rectangle(frame, (const.OFFSET, 450), (830, 500), const.WHITE, cv2.FILLED)
        cv2.rectangle(frame, (const.OFFSET, 450), (830, 500), const.BLUE, 1)
        cv2.putText(frame, self.text[-40:], (const.OFFSET, 480), const.FONT, 1, const.BLACK, 2)
    
    def _show_instructions(self, frame):
        x0, y0, w, h = const.OFFSET, const.OFFSET, (const.RES_X - 200), (const.RES_Y - 200)
        cv2.rectangle(frame, (x0, y0), (x0 + w, y0 + h), const.WHITE, cv2.FILLED)
        cv2.rectangle(frame, (x0, y0), (x0 + w, y0 + h), const.BLUE, 1)
        for i, line in enumerate(const.INSTRUCTION.split('\n')):
            cv2.putText(frame, line, (x0 + 15, y0 + 15 + i * 15), const.FONT, 0.7, const.BLACK, 1)
    
    def save_text(self):
        os.makedirs('results', exist_ok=True)
        with open('results/text.txt', 'w') as f:
            f.write(self.text)