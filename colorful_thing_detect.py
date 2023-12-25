import cv2
import numpy as np

# Создание двух пустых окон
cv2.namedWindow('HSV')
# cv2.namedWindow('Result')

def callback(*args):
    pass

# Создание шести ползунков
cv2.createTrackbar('h1', 'HSV', 0, 255, callback)
cv2.createTrackbar('s1', 'HSV', 0, 255, callback)
cv2.createTrackbar('v1', 'HSV', 0, 255, callback)
cv2.createTrackbar('h2', 'HSV', 255, 255, callback)
cv2.createTrackbar('s2', 'HSV', 255, 255, callback)
cv2.createTrackbar('v2', 'HSV', 255, 255, callback)


img = cv2.imread('images/picture1.jpg')
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
colors = [(240, 120, 0), (0, 0, 255), (120, 120, 255)]
texts = ['Blue', 'Red', 'Orange']
filter_colors = []

# Создаём цветовой фильтр
for i in range(len(colors)):
    while True:
        # Запись значений бегунков в переменные
        h1 = cv2.getTrackbarPos('h1', 'HSV')
        s1 = cv2.getTrackbarPos('s1', 'HSV')
        v1 = cv2.getTrackbarPos('v1', 'HSV')
        h2 = cv2.getTrackbarPos('h2', 'HSV')
        s2 = cv2.getTrackbarPos('s2', 'HSV')
        v2 = cv2.getTrackbarPos('v2', 'HSV')

        # Диапазон цветов
        hsv_min = np.array((h1, s1, v1), dtype='uint8')
        hsv_max = np.array((h2, s2, v2), dtype='uint8')
        filter_color = cv2.inRange(hsv, hsv_min, hsv_max)

        con, hir = cv2.findContours(filter_color, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        cv2.imshow(texts[i], filter_color)

        if cv2.waitKey(1) == 27:
            filter_colors.append(filter_color)
            cv2.destroyWindow(texts[i])
            break

    con, hir = cv2.findContours(filter_colors[i], cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # cv2.drawContours(img, con, -1, colors[i], 5) # рисуем контур

    for c in con:
        p = cv2.arcLength(c, True) # считаем длину контура

        if p > 200: # если больше 1100 px
            cv2.drawContours(img, [c], -1, colors[i], 5) # рисуем контур

            x, y = c[0][0][0], c[0][0][1] # создаём координаты для точки
            cv2.circle(img, (x,y), 10, colors[i], -1) # рисуем точку
            cv2.putText(img, texts[i], (x-10, y-20), cv2.FONT_HERSHEY_SIMPLEX, 0.8, colors[i], 2, cv2.LINE_AA) # подписываем цвет

cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows
