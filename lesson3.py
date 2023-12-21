import cv2
import numpy as np

img = cv2.imread('images/stupino.jpg')

new_img = np.zeros(img.shape, dtype='uint8')

img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img = cv2.GaussianBlur(img, (5, 5), 0)

img = cv2.Canny(img, 100, 140)

con, hierarchy = cv2.findContours(img, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

# print(con)

cv2.drawContours(new_img, con, -1, (255, 120, 164), 1)

cv2.imshow('Stupino', new_img)

cv2.waitKey(0)

# img = cv2.flip(img, 1)

# def rotate(img_param: img, angle: float):
#     height, width = img_param.shape[:2]
#     point = (width // 2, height // 2)

#     matrix = cv2.getRotationMatrix2D(point, angle, 0.5)
#     return cv2.warpAffine(img_param, matrix, (width, height))

# img = rotate(img, 30)

# def transform(img_param: img, x: int, y: int):
#     matrix = np.float32([[1, 0, x], [0, 1, y]])
#     return cv2.warpAffine(img_param, matrix, (img_param.shape[1], img_param.shape[0]))

# img = transform(img, 200, 200)