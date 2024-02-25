import cv2
def get_video():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        raise IOError("Cannot open webcam")

    while True:
        ret, frame = cap.read()
        color_space = int(cap.get(cv2.CAP_PROP_CONVERT_RGB))
                        
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break
        if color_space == 0:
            cap.set(cv2.CAP_PROP_CONVERT_RGB, 1)

        cv2.imshow('frame', frame)
        if cv2.waitKey(1) == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()