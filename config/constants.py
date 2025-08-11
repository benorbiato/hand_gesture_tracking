"""
Application constants and configuration parameters.
Centralized location for all magic numbers and strings.
"""

# Color definitions (BGR format)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (255, 0, 0)
GREEN = (0, 255, 0)
RED = (0, 0, 255)
LIGHT_BLUE = (255, 255, 0)

# Screen resolution
RES_X = 1280
RES_Y = 720

# Virtual keyboard configuration
BTN_SIZE = 50
OFFSET = 80
KEYS = [
    ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'O', 'P'],
    ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'K', 'L'],
    ['Z', 'X', 'C', 'V', 'B', 'N', 'M', 'M', ',', '.', ';']
]

# Font settings
FONT = cv2.FONT_HERSHEY_DUPLEX

# Finger gesture patterns
FINGER_1 = [False, True, False, False, False]  # Only index finger up
FINGER_1_2 = [False, True, True, False, False]  # Index and middle up
FINGER_1_2_3 = [False, True, True, True, False]  # First three fingers up
FINGER_1_4 = [False, True, False, False, True]  # Index and pinky up
FINGER_4 = [False, False, False, False, True]  # Only pinky up
FINGER_0 = [True, False, False, False, False]  # Only thumb up
FINGER_NONE = [False, False, False, False, False]  # All fingers down
FINGER_ALL = [True, True, True, True, True]  # All fingers up

# Application instructions
INSTRUCTION = """..."""  # (keep the same instruction text)