"""
Main entry point for the Hand Gesture Control application.
Initializes the camera, controller and main loop.
"""
import cv2
from controllers.gesture_controller import GestureController

def main():
    # Initialize video capture
    cap = cv2.VideoCapture(0)
    gesture_controller = GestureController()
    
    try:
        while True:
            # Read frame from camera
            ret, frame = cap.read()
            if not ret:
                break
                
            # Process frame through controller
            gesture_controller.process_frame(frame)
            
            # Exit on ESC key
            if cv2.waitKey(1) == 27:
                break
    finally:
        # Cleanup resources
        gesture_controller.cleanup()
        cap.release()
        gesture_controller.view.close_all()

if __name__ == "__main__":
    main()