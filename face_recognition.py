import cv2

face_cascade = cv2.CascadeClassifier('cascades/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('cascades/haarcascade_eye.xml')

img = cv2.imread('images/photo3.jpg')
img = cv2.resize(img, (img.shape[1] // 3, img.shape[0] // 3))
img = cv2.flip(img, -1)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=2)



for x, y, w, h in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    roi_color = img[y:y+h, x:x+w]
    roi_gray = gray[y:y+h, x:x+w]
    eyes = eye_cascade.detectMultiScale(roi_gray, scaleFactor=1.2, minNeighbors=5)

    for x1, y1, w1, h1 in eyes:
        cv2.rectangle(roi_color, (x1, y1), (x1+w1, y1+h1), (0, 255, 0), 1)
    # cv2.imshow('Eye detect', roi_color)

cv2.imshow('Face detect', img)
cv2.waitKey(0)
cv2.destroyAllWindows()