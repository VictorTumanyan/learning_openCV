import cv2
import numpy as np

# Загрузка и просмотр изображений
img = cv2.imread('images/stupino.jpg')

img = cv2.resize(img, (img.shape[1] // 2, img.shape[0] // 2))
img = cv2.GaussianBlur(img, (11, 11), 0)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

img = cv2.Canny(img, 30, 30)

kernel = np.ones((3, 3), np.uint8)
img = cv2.dilate(img, kernel, iterations=1)

# img = cv2.erode(img, kernel, iterations=1)



# img[0:100, 0:150]
cv2.imshow('Stupino:', img)

# print(img.shape)

cv2.waitKey(0)







# # Загрузка и просмотр видео
# # cap = cv2.VideoCapture('videos/ararat.mov')
# cap = cv2.VideoCapture(0)
# cap.set(3, 500)
# cap.set(4, 300)

# while True:
#     success, img = cap.read()
#     cv2.imshow('Ararat', img)

#     if cv2.waitKey(10) & 0xFF == ord('q'):
#         break
