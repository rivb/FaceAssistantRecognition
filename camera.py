import numpy as np
from face_comparison import face_comparison
import cv2

class FaceAssistant():

    def __init__(self):

        self.face_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_alt2.xml')

        self.cam = cv2.VideoCapture(0)

        cv2.namedWindow("test")

        while True:

            ret, frame = self.cam.read()
            cv2.imshow("test", frame)
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = self.face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)

            if not ret:
                break
            k = cv2.waitKey(1)

            if k%256 == 27:
                # ESC pressed
                print("Escape hit, closing...")
                break

            elif k%256 == 32:
                # SPACE pressed
                if len(faces)>0:

                    for (x, y, w, h) in faces:

                        self.roi_gray = gray[y:y+h, x:x+w] # ROI = Region Of Interest

                        try:
                            f=open("my_image.png")
                            self.recognice_face()
                        except:
                            self.save_image()


                elif len(faces)>1:

                    print('hay mas de dos caras')

                else:
                    print('no hay caras')

        self.cam.release()

        cv2.destroyAllWindows()

    def save_image(self):

                        img_item = 'my_image.png'
                        cv2.imwrite(img_item,self.roi_gray)
                        print('cara encontrada')

    def recognice_face(self):

                        img_item = 'unknown_face.jpg'
                        cv2.imwrite(img_item,self.roi_gray)
                        face_comparison('Matias','my_image.png',img_item)

FaceAssistant()
