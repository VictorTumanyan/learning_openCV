import cv2

face_cascade = cv2.CascadeClassifier('cascades/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('cascades/haarcascade_eye.xml')
smile_cascade = cv2.CascadeClassifier('cascades/haarcascade_smile.xml')

cap = cv2.VideoCapture(0)
cap.set(3, 600)
cap.set(4, 400)

while True:
    success, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=10)

    for x, y, w, h in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 1)
        roi_color = img[y:y+h, x:x+w]
        roi_gray = gray[y:y+h, x:x+w]

        eyes = eye_cascade.detectMultiScale(roi_gray, scaleFactor=1.2, minNeighbors=20)
        smiles = smile_cascade.detectMultiScale(roi_gray, scaleFactor=1.2, minNeighbors=20)

        for x1, y1, w1, h1 in eyes:
            cv2.rectangle(roi_color, (x1, y1), (x1+w1, y1+h1), (0, 255, 0), 1)

        for x2, y2, w2, h2, in smiles:
            cv2.rectangle(roi_color, (x2, y2), (x2+w2, y2+h2), (0, 0, 255), 1)

    cv2.imshow('Face detected', img)

    if cv2.waitKey(10) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break