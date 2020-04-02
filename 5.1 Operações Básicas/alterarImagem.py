import cv2

image = cv2.imread('rubiks-cube.jpg')
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
shape = image.shape

for i in range(shape[0]): # Faz um for por Linha
    for i2 in range(shape[1]): # Faz um for por Coluna
        color = image[i, i2] # Pega o valor do pixel (0-255)

        if(color): # Se a cor não for zero, divide o valor por 3
            color = color / 3

        image[i, i2] = color # Altera o pixel da Imagem

cv2.imshow('Image', image)

cv2.waitKey(0)
cv2.destroyAllWindows()