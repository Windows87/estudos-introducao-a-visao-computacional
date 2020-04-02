import cv2

image = cv2.imread('rubiks-cube.jpg')
valorPixel = image[150, 150] # Obtem valor [R, G, B]

print(valorPixel)