import cv2

image = cv2.imread('rubiks-cube.jpg')
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
valorPixel = image[150, 150] # Obtem valor de 0 (preto) á 255 (branco)

print(valorPixel)