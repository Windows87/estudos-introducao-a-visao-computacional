import cv2

image = cv2.imread('rubiks-cube.jpg')
blue, green, red = cv2.split(image) # Segmenta as cores

# Mostra as cores segmentadas
cv2.imshow('Red', red)
cv2.imshow('Green', green)
cv2.imshow('Blue', blue)

# Salva em arquivos
cv2.imwrite('red.jpg', red)
cv2.imwrite('green.jpg', green)
cv2.imwrite('blue.jpg', blue)

cv2.waitKey(0)
cv2.destroyAlWindows()