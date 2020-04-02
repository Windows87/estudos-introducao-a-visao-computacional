import	cv2

image = cv2.imread('rubiks-cube.jpg')
imagem = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
h, s, v = cv2.split(image)

cv2.imshow("H",	h)
cv2.imshow("S",	s)
cv2.imshow("V",	v)

image = cv2.merge((h, s, v))
image =	cv2.cvtColor(imagem, cv2.COLOR_HSV2BGR)

cv2.imshow("Image",	image)

cv2.waitKey(0)
cv2.destroyAllWindows()