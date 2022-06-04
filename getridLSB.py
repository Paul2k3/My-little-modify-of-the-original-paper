import cv2 
import numpy as np
import random

img = cv2.imread('gray.bmp')
cmp = cv2.imread('gray.bmp')
for i in range(512):
    for j in range(512):
        if (img[i][j][0] % 2 == 1):
            img[i][j] = img[i][j] - 1
for i in range(512):
    for j in range(512):
        if (img[i][j][0] % 2 == 1):
            print('fe')
cv2.imwrite('getridLSB.bmp', img)

      
