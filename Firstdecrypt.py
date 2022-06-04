import cv2
import numpy as np

#這份code會利用剛剛提出的LSB以及加密時的secondhashpicture
#加密時得hashpicture只要有圖片以及key皆可產生，所以我在這邊直接使用

secondhashpic = cv2.imread('secondhashpicture.bmp', cv2.IMREAD_GRAYSCALE)
exbit = cv2.imread('extractBit.bmp', cv2.IMREAD_GRAYSCALE) # 這個是抽出來的LSB

afterFirstDecrypt = np.empty((512, 512, 1), np.uint8) 
showAfterFirstDecrypt = np.empty((512, 512, 1), np.uint8) 
for i in range(512):
    for j in range(512):
        afterFirstDecrypt[i][j] = 0
        showAfterFirstDecrypt[i][j] = 0

for i in range(512):
    for j in range(512):
        if (secondhashpic[i][j] ^ exbit[i][j]):
            afterFirstDecrypt[i][j] = 1 #因為是第一次解密，還不能改成255，顯示watermark
            showAfterFirstDecrypt[i][j] = 255

            
cv2.imshow('showAfterFirstDecrypt', showAfterFirstDecrypt)
cv2.imwrite('showAfterFirstDecrypt.bmp', showAfterFirstDecrypt)
            
cv2.imshow('afterFirstDecrypt', afterFirstDecrypt)
cv2.imwrite('afterFirstDecrypt.bmp', afterFirstDecrypt)
