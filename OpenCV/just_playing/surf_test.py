import numpy as np
import matplotlib.pyplot as plt
#matplotlib inline
import cv2 as cv
img = cv.imread('jim.JPG',0)
surf = cv.xfeatures2d.SURF_create(400)
kp, des = surf.detectAndCompute(img,None)
print(len(kp))
print( surf.getHessianThreshold() )
kp, des = surf.detectAndCompute(img,None)
surf.setHessianThreshold(50000) 
print( len(kp) )
img2 = cv.drawKeypoints(img,kp,None,(255,0,0),4)
plt.imshow(img2),plt.show()
print( surf.getUpright() )
surf.setUpright(True)
kp = surf.detect(img,None)
img2 = cv.drawKeypoints(img,kp,None,(255,0,0),4)
plt.imshow(img2),plt.show()

