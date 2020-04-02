import cv2
import numpy
from matplotlib import pyplot

image = cv2.imread('pokemon.jpg')
blue, green, red = cv2.split(image)

# Cria o gráfico
# 1: .ravel() -> transforma imagem em vetor
# 2: Número distintos representados
# 3: Intervalo dos elementos
pyplot.hist(blue.ravel(), 256, [0, 256])

pyplot.figure()
pyplot.hist(green.ravel(), 256, [0, 256])

pyplot.figure()
pyplot.hist(red.ravel(), 256, [0, 256])

pyplot.show()