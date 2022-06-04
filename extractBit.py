import cv2
import numpy as np

#get original picture


#get watermarked picture
watpic = cv2.imread('watermarked.bmp', cv2.IMREAD_GRAYSCALE)

#the LSB we extract
extract = np.empty((512, 512, 1), np.uint8)

#change 1 to 255 in order to show it
show = np.empty((512, 512, 1), np.uint8)

for i in range(512):
    for j in range(512):
        extract[i][j] = 0
        show[i][j] = 0

for i in range(512):
    for j in range(512):
        if (watpic[i][j] % 2 == 1):
            show[i][j] = 255
            extract[i][j] = 1


cv2.imshow('show', show)
cv2.imwrite('sampleExtractBit.bmp', show)
cv2.imshow('extract', extract)
cv2.imwrite('extractBit.bmp', extract)
