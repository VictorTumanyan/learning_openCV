import cv2
import numpy as np

img = cv2.imread('images/cockerel.jpg')
new_img = np.zeros(img.shape, dtype='uint8')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(img, (5, 5), 0)

new_img = cv2.Canny(gray, 100, 140)

con, hir = cv2.findContours(new_img, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
cv2.drawContours(img, con, -1, (230, 111, 0), 2)
# print(con)

cv2.imshow('Result', img)
cv2.waitKey(0)
cv2.destroyAllWindows()