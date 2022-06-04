import cv2
import numpy as np




firsthash = cv2.imread('firsthashpicture.bmp', cv2.IMREAD_GRAYSCALE)
Icon = cv2.imread('Icon.bmp', cv2.IMREAD_GRAYSCALE) 

encryptIcon = np.empty((512, 512, 1), np.uint8) 
showEncryptIcon = np.empty((512, 512, 1), np.uint8) 

for i in range(512):
    for j in range(512):
        encryptIcon[i][j] = 0
        showEncryptIcon[i][j] = 0

for i in range(512):
    for j in range(512):
        if (firsthash[i][j] ^ Icon[i][j]):
            encryptIcon[i][j] = 1
            showEncryptIcon[i][j] = 255 

cv2.imshow('encryptIcon', encryptIcon)
cv2.imwrite('encryptIcon.bmp', encryptIcon)

cv2.imshow('showEncryptIcon', showEncryptIcon)
cv2.imwrite('showEncryptIcon.bmp', showEncryptIcon)
