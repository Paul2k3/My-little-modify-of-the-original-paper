import cv2
import numpy as np

lenna = cv2.imread('getridLSB.bmp', cv2.IMREAD_GRAYSCALE)
watermark = cv2.imread('bitmap.bmp', cv2.IMREAD_GRAYSCALE)


for i in range(512):
    for j in range(512):
        lenna[i][j] = lenna[i][j] + watermark[i][j]




        
cv2.imshow('lenna', lenna)
cv2.waitKey(1000)
cv2.imwrite('watermarked.bmp', lenna)
