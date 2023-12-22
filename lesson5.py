import cv2
import numpy as np

photo = cv2.imread('images/stupino.jpg')
img = np.zeros((photo.shape[:2]), dtype='uint8')

circle = cv2.circle(img.copy(), (50, 50), 50, 255, -1)

square = cv2.rectangle(img.copy(), (25, 25), (250, 250), 255, -1)

# img = cv2.bitwise_and(photo, photo, mask=square)
img = cv2.bitwise_or(circle, square, mask=square)
# img = cv2.bitwise_xor(circle, square)
# img = cv2.bitwise_not(photo, photo, mask=square)

cv2.imshow('Result', img)

cv2.waitKey(0)