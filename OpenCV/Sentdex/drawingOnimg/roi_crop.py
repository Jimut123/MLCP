import cv2
import numpy as np

img = cv2.imread('watch.jpg',cv2.IMREAD_COLOR)

# px = img[100:150,100:150]
# print(px)

print(img.shape)
print(img.size)
print(img.dtype)