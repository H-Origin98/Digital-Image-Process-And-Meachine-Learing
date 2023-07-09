"""使用python+OpenCV来绘制图像的直方图"""
import cv2
import numpy as np
import matplotlib.pyplot as plt

IMAGE_PATH="./Hist_test1.jpeg"
image=cv2.imread(IMAGE_PATH)
hist=cv2.calcHist([image],[0],None,[256],[0,255])
print(hist.size)
print(hist.shape)

#绘制直方图
image_gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
print(image_gray)
hist_image_gray=cv2.calcHist([image_gray],[0],None,[256],[0,255])
plt.plot(hist_image_gray,color='b')
plt.legend()
plt.show()