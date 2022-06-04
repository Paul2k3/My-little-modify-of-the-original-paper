import cv2
import numpy as np

picture = cv2.imread('secondhashpicture.bmp')
icon = cv2.imread('encryptIcon.bmp')
#picture 指的是利用key和圖像所產生的hash
#icon為我的watermark
bitmap = np.empty((512, 512, 1), np.uint8)
show = np.empty((512, 512, 1), np.uint8)

for i in range(512):
    for j in range(512):
        bitmap[i][j] = 0
        show[i][j] = 0

for i in range(512):
    for j in range(512):
        if(picture[i][j][0] ^ icon[i][j][0]):
            bitmap[i][j] = 1
            show[i][j] = 255

cv2.imshow('show', show)
cv2.imshow('bitmap', bitmap)

cv2.imwrite('showbitmap.bmp', show)
cv2.imwrite('bitmap.bmp', bitmap)

