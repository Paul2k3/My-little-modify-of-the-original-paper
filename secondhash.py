import cv2
import numpy as np
import hashlib
key = 1000
#我的hash用圖像表示

secondhashpicture = np.empty((512, 512, 1), np.uint8)
secondhashsample = np.empty((512, 512, 1), np.uint8)
#我的hashpicture只處理LSB的部分
#sample 是轉成255來視覺化
for i in range(512):
    for j in range(512):
        secondhashpicture[i][j] = 0
        secondhashsample[i][j] = 0
m = hashlib.md5()

for i in range(512):
    for j in range(512):
        #這便找keystr不能用乘的
        key = key + i + j
        keystr = str(key)
        h = hashlib.md5(keystr.encode()).hexdigest()
        if (h[1] == '1' or h[1] == '3' or h[1] == '5' or h[1] == '7'
            or h[1] == '9' or h[1] == 'b' or h[1] == 'd' or h[1] == 'f'):
            secondhashpicture[i][j] = 1
            secondhashsample[i][j] = 255
 
cv2.imshow('secondhashpicture', secondhashpicture)
cv2.imshow('secondhashsample', secondhashsample)


cv2.imwrite('secondhashpicture.bmp', secondhashpicture)
cv2.imwrite('secondhashsample.bmp', secondhashsample)

#我的作法稍有改變，方便起見，取512*512次hash




