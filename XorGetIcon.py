import cv2
import numpy as np

#這份code會利用剛剛XOR的LSB以及加密時的firsthashpicture
#加密時的hashpicture只要有圖片以及key皆可產生，所以我在這邊直接使用

hashpic = cv2.imread('firsthashpicture.bmp', cv2.IMREAD_GRAYSCALE)
exbit = cv2.imread('afterFirstDecrypt.bmp', cv2.IMREAD_GRAYSCALE) # 這個是抽出來的LSB

exwater = np.empty((512, 512, 1), np.uint8) # 目標浮水印

for i in range(512):
    for j in range(512):
        exwater[i][j] = 0

for i in range(512):
    for j in range(512):
        if (hashpic[i][j] ^ exbit[i][j]):
            exwater[i][j] = 255 #因為我要原本圖像，所以直接用255，不用為了操作方便改成1

cv2.imshow('exwater', exwater)
cv2.imwrite('extractedWatermark.bmp', exwater)