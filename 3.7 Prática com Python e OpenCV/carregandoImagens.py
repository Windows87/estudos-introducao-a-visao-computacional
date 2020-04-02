import cv2 # Importa OpenCV

image = cv2.imread('image.png') # Lê a imagem
cv2.imshow('Image', image) # Mostra a Imagem
cv2.waitKey(0)
cv2.destroyAllWindows()