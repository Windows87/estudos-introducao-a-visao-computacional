import cv2

image = cv2.imread('rubiks-cube.jpg')
image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV) # Converte para HSV
h, s, v = cv2.split(image) # Faz o split

cv2.imshow('H', h)
cv2.imshow('S', s)
cv2.imshow('V', v)

cv2.waitKey(0)
cv2.destroyAllWindows()