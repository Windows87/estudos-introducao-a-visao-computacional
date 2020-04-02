import cv2

image = cv2.imread('rubiks-cube.jpg')

print(image.shape) # Linhas, Colunas e Número de Cores (RGB = 3, Gray = 1)
print(image.size) # Tamanho total da imagem (L x C x N)