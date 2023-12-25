import cv2

number_cascade = cv2.CascadeClassifier('cascades/haarcascade_russian_plate_number.xml')

img = cv2.imread('images/number_3.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

numbers = number_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=15)
for x, y, w, h in numbers:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

cv2.imshow('Result', img)
cv2.waitKey(0)
cv2.destroyAllWindows()