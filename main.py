import cv2

img = cv2.imread("resources/lena.png")

cv2.imshow("Lena", img)
cv2.waitkey(2000)