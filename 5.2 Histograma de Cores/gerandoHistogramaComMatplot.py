import cv2
import numpy
from matplotlib import pyplot

image = cv2.imread('rubiks-cube.jpg')
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

(thresh, image) = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY) # Converte para Imagem Binária

# Cria o gráfico
# 1: .ravel() -> transforma imagem em vetor
# 2: Número distintos representados
# 3: Intervalo dos elementos
pyplot.hist(image.ravel(), 256, [0, 256])
pyplot.show()