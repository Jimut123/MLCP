import cv2
import numpy as np
img = cv2.imread('bookpage.jpg')
grayscaled = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)


retval2,threshold2 = cv2.threshold(grayscaled,125,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
cv2.imshow('original',img)
cv2.imshow('Otsu threshold',threshold2)
cv2.waitKey(0)
cv2.destroyAllWindows()