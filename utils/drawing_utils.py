import cv2
from config import constants as const

def draw_button(img, pos, key, size=50, rect_color=const.WHITE):
    """Draw a virtual keyboard button."""
    cv2.rectangle(img, pos, (pos[0] + size, pos[1] + size), rect_color, cv2.FILLED)
    cv2.rectangle(img, pos, (pos[0] + size, pos[1] + size), const.BLUE, 1)
    cv2.putText(img, key, (pos[0] + 15, pos[1] + 30), const.FONT, 1, const.BLACK, 2)
    return img