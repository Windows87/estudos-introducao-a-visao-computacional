import cv2

video = cv2.VideoCapture('video.mp4') # Abre o vídeo

while True:
    ret, frame = video.read() # Lê o video
    cv2.imshow('Image', frame) # Mostra um frame do vídeo

    keyQisPressed = cv2.waitKey(1) and 0xFF == ord('q') # Verifica se a tecla Q foi pressionada

    # Se sim, o programa é finalizado
    if(keyQisPressed):
        break

video.release()
cv2.destroyAllWindows()