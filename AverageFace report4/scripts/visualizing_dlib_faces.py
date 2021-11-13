from imutils import face_utils
import dlib
import cv2

p = "shape_predictor_68_face_landmarks.dat"
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(p)



if __name__ == '__main__':
    image = cv2.imread('output1.jpg')
    if image is None:
        print("bro wtf")
    cv2.imshow('Input', image)
    grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    rects = detector(grey, 0)
    rect = rects[0]
    shape = predictor(grey, rect)
    shape = face_utils.shape_to_np(shape)
    for (x, y) in shape:
        cv2.circle(image, (x, y), 2, (0, 255, 0), -1)

    cv2.imshow("Output", image)
    cv2.waitKey(0)

    cv2.destroyAllWindows()
