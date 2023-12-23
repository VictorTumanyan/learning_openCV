import cv2

# #dz1
# img = cv2.imread('images/photo1.jpg')

# img = cv2.flip(img, 1)

# img = cv2.bilateralFilter(img, 15, 125, 125)

# cv2.imshow('Result', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# # dz2
# img = cv2.imread('images/photo3.jpg')

# def rotate(img: img, angle: float):
#     height, width = img.shape[:2]
#     point = (width // 2, height // 2)
#     mat = cv2.getRotationMatrix2D(point, angle, 1)
#     return cv2.warpAffine(img, mat, (width, height))

# img = cv2.resize(img, (img.shape[1] // 2, img.shape[0] // 2))

# img = rotate(img, 180)

# img = img[150:550, 175:425]

# cv2.imshow('Result', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()