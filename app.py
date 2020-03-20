import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_alt2.xml')
cam = cv2.VideoCapture(0)
cv2.namedWindow("test")

while True:
    ret, frame = cam.read()
    cv2.imshow("test", frame)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)
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
                roi_gray = gray[y:y+h, x:x+w] # ROI = Region Of Interest
                img_item = 'my_image.png'
                cv2.imwrite(img_item,roi_gray)
                print('cara encontrada')
        elif len(faces)>1:
            print('hay mas de dos caras')
        else:
            print('no hay caras')

cam.release()
cv2.destroyAllWindows()