import cv2
from controllers.gesture_controller import GestureController
from views.main_view import MainView

def main():
    cap = cv2.VideoCapture(0)
    gesture_controller = GestureController()
    main_view = MainView()
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break
            
        processed_frame = gesture_controller.process_frame(frame)
        main_view.display(processed_frame)
        
        if cv2.waitKey(1) == 27:  # ESC key
            break
            
    gesture_controller.cleanup()
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()