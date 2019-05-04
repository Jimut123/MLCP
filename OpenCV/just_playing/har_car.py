import numpy as np
#import args
import cv2 as cv
#face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
#eye_cascade = cv.CascadeClassifier('haarcascade_eye.xml')
face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv.CascadeClassifier('haarcascade_eye.xml')
print(face_cascade.empty())
#cascade_fn = args.get('--cascade', "../../data/haarcascades/haarcascade_frontalface_alt.xml")
#nested_fn  = args.get('--nested-cascade', "../../data/haarcascades/haarcascade_eye.xml")

#cam = create_capture(video_src, fallback='synth:bg=../data/lena.jpg:noise=0.05')

img = cv.imread('jim.JPG')
#img = cv.resize(img, (400, 800))
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#cv.imshow('img',gray)
#cv.waitKey(0)
faces = face_cascade.detectMultiScale(gray, 1.3, 5)
for (x,y,w,h) in faces:
    cv.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
    eyes = eye_cascade.detectMultiScale(roi_gray)
    for (ex,ey,ew,eh) in eyes:
        cv.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

cv.imshow('img',img)
cv.resize(img, (200, 200))

cv.waitKey(0)
cv.destroyAllWindows()
