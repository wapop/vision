import cv2
import numpy as np

img=cv2.imread('lenna.bmp')
R=img[:,:,2]
RR= np.zeros(img.shape)
RR[:,:,2]= R/255.0

cv2.imshow('src',img)
cv2.imshow('dest', RR)

cv2.waitKey()
cv2.destroyAllWindow()
