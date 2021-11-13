import imutils
import numpy
from imutils import face_utils
import cv2
import dlib
import os
import numpy as np

p = "shape_predictor_68_face_landmarks.dat"
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(p)
path = '../faces'


if __name__ == '__main__':

    for filePath in sorted(os.listdir(path)):

        if filePath.endswith(".jpg"):
            image = cv2.imread(os.path.join(path, filePath))
            # convert to floating point?
            # image = np.float32(image) / 255.0

            # image = imutils.resize(image, 600, 600)
            rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

            rects = detector(rgb, 0)
            rects2 = detector(grey, 0)
            rect = rects[0]
            rect2 = rects2[0]
            landmarks = predictor(rgb, rect)
            landmarks = face_utils.shape_to_np(landmarks) #these are the 68 landmarks
            # print(landmarks)
            landmarks2 = predictor(grey, rect2)
            landmarks2 = face_utils.shape_to_np(landmarks2)
            # print(len(landmarks2))
            print(landmarks2) #this seems more accurate!
            newName = path + "/" + filePath + "G.txt"
            print(newName)
            file_object = open(newName, "w")
            np.savetxt(file_object, landmarks2, fmt = "%d", delimiter=" ")
            file_object.close()


## THIS FILE CONVERTS AN .jpg IMAGE TO ITS  68 DLIB FACIAL LANDMARKS G.txt FILES (68 coordinates)