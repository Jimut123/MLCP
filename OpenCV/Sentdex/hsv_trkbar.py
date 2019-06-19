import cv2
import numpy as np


cap = cv2.VideoCapture(0)

def nothing(x):
    pass
# Creating a window for later use
cv2.namedWindow('result')

# Starting with 100's to prevent error while masking
h,s,v = 100,100,100

# Creating track bar
cv2.createTrackbar('lh', 'result',0,255,nothing)
cv2.createTrackbar('ls', 'result',0,255,nothing)
cv2.createTrackbar('lv', 'result',0,255,nothing)

cv2.createTrackbar('uh', 'result',0,255,nothing)
cv2.createTrackbar('us', 'result',0,255,nothing)
cv2.createTrackbar('uv', 'result',0,255,nothing)

while(1):

    _, frame = cap.read()

    #converting to HSV
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    # get info from track bar and appy to result
    lh = cv2.getTrackbarPos('h','result')
    ls = cv2.getTrackbarPos('s','result')
    lv = cv2.getTrackbarPos('v','result')

    # get info from track bar and appy to result
    uh = cv2.getTrackbarPos('uh','result')
    us = cv2.getTrackbarPos('us','result')
    uv = cv2.getTrackbarPos('uv','result')

    # Normal masking algorithm
    lower_blue = np.array([lh,ls,lv])
    upper_blue = np.array([uh,us,uv])

    mask = cv2.inRange(hsv,lower_blue, upper_blue)

    result = cv2.bitwise_and(frame,frame,mask = mask)

    cv2.imshow('result',result)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cap.release()

cv2.destroyAllWindows()