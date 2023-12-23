import cv2
import numpy as np

img = np.zeros((400, 600, 3), dtype='uint8')

img[:] = (100, 20, 255)

height, width = img.shape[:2]

line = cv2.line(img, (50, height // 4), (170, height // 2), (49, 255, 20), 2)

rectangle = cv2.rectangle(img, (190, height // 2 + 20), (390, height // 2 + 100), (49, 255, 20), cv2.FILLED)

rectangle1 = cv2.rectangle(img, (190, height // 2 + 120), (210, height // 2 + 160), (49, 255, 20), cv2.FILLED)
rectangle2 = cv2.rectangle(img, (370, height // 2 + 120), (390, height // 2 + 160), (49, 255, 20), cv2.FILLED)

circle = cv2.circle(img, (430, height // 2), 30, (49, 255, 20), cv2.FILLED)

text = cv2.putText(img, 'cat', (260, height // 2 + 60), cv2.FONT_ITALIC, 1, (255, 0, 0), 1)



cv2.imshow('Result', img)
cv2.waitKey(0)
cv2.destroyAllWindows()