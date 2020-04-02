import cv2

image = cv2.imread('rubiks-cube.jpg')

image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY) # Converte para cinza
cv2.imshow('Image', image)

cv2.waitKey(0)
cv2.destroyAllWindows()