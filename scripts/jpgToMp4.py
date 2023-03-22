# Convierte frames en videos

import cv2
import os
path = '../Escritorio/carpeta_comp/meteors-candidates/cand-10--cam13--cam16--2016-05-06--02-12-08'
path_videos = '../Escritorio/carpeta_comp/videos_dataset/cand-10'

carpetas = os.listdir(path)
for i in carpetas:
	print(i)
	img_array = []
	imagenes = os.listdir(path + '/' + i)
	imagenes.sort()
	for imagen in imagenes:
		img = cv2.imread(path + '/' + i + '/' + imagen)
		img_array.append(img)
	height, widht = img.shape[:2]
	nombre = '/V' + i + '.mp4'
	video = cv2.VideoWriter(path_videos + nombre, cv2.VideoWriter_fourcc(*'mp4v'),5,(widht, height))
	for l in range(len(img_array)):
		video.write(img_array[l])
	video.release()
