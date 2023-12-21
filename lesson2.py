import cv2
import numpy as np

photo = np.zeros((500, 700, 3), dtype='uint8')

#BGR - формат в OpenCV
# photo[100:150, 100:150] = 150, 3, 89

cv2.rectangle(photo, (10, 10), (110, 110), (150, 3, 89), cv2.FILLED)

cv2.line(photo, (0, photo.shape[0] // 2), (photo.shape[1] // 2, photo.shape[0] // 2), (150, 3, 89), 1)

cv2.circle(photo, (photo.shape[1] // 2, photo.shape[0] // 2), 50, (150, 3, 89), 3)

cv2.putText(photo, "I'm a good programmer", (200, 400), cv2.FONT_HERSHEY_TRIPLEX, 1, (255, 255, 255), 1)

cv2.imshow('Photo', photo)
cv2.waitKey(0)