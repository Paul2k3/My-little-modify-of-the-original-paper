import cv2
import numpy as np


img = np.empty((512, 512, 1), np.uint8)
sample = np.empty((512, 512, 1), np.uint8)
#我的image會是一個只處理LSB的部分
#sample 是轉成255來視覺化
for i in range(512):
    for j in range(512):
        img[i][j] = 0
        sample[i][j] = 0

for i in range(64):
    for j in range(64):
        img[8 * i + 1][8 * j + 1] = 1
        img[8 * i + 1][8 * j + 6] = 1
        img[8 * i + 6][8 * j + 1] = 1
        img[8 * i + 6][8 * j + 6] = 1
        img[8 * i + 2][8 * j + 2] = 1
        img[8 * i + 3][8 * j + 2] = 1
        img[8 * i + 4][8 * j + 2] = 1
        img[8 * i + 5][8 * j + 2] = 1
        img[8 * i + 2][8 * j + 3] = 1
        img[8 * i + 5][8 * j + 3] = 1
        img[8 * i + 2][8 * j + 4] = 1
        img[8 * i + 5][8 * j + 4] = 1
        img[8 * i + 2][8 * j + 5] = 1
        img[8 * i + 3][8 * j + 5] = 1
        img[8 * i + 4][8 * j + 5] = 1
        img[8 * i + 5][8 * j + 5] = 1

        sample[8 * i + 1][8 * j + 1] = 255
        sample[8 * i + 1][8 * j + 6] = 255
        sample[8 * i + 6][8 * j + 1] = 255
        sample[8 * i + 6][8 * j + 6] = 255
        sample[8 * i + 2][8 * j + 2] = 255
        sample[8 * i + 3][8 * j + 2] = 255
        sample[8 * i + 4][8 * j + 2] = 255
        sample[8 * i + 5][8 * j + 2] = 255
        sample[8 * i + 2][8 * j + 3] = 255
        sample[8 * i + 5][8 * j + 3] = 255
        sample[8 * i + 2][8 * j + 4] = 255
        sample[8 * i + 5][8 * j + 4] = 255
        sample[8 * i + 2][8 * j + 5] = 255
        sample[8 * i + 3][8 * j + 5] = 255
        sample[8 * i + 4][8 * j + 5] = 255
        sample[8 * i + 5][8 * j + 5] = 255
cv2.imshow('img', img)
cv2.waitKey(1000)
cv2.imshow('sample', sample)
cv2.imwrite('icon.bmp', img)
cv2.imwrite('iconSample.bmp', sample)


        
