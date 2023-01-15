import cv2
import os

img_array = []
path = 'cam43-UPM-MAD-2023-01-13--19-25-00'

imagenes = os.listdir(path)

for imagen in imagenes:
	img = cv2.imread(path + '/' + imagen)
	#cv2.imshow(imagen)
	img_array.append(img)

	
height, width = img.shape[:2]
print (height, width)

video = cv2.VideoWriter('V03.mp4', cv2.VideoWriter_fourcc(*'mp4v'), 5, (width, height))

for i in range(len(img_array)):
	video.write(img_array[i])

video.release()
