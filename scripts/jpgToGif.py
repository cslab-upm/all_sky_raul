# Convierte frames en videos

import cv2
import os
from moviepy.editor import VideoFileClip

path = '../Escritorio/carpeta_comp/meteors-candidates/'
#path_videos = '../Escritorio/carpeta_comp/videos_dataset/'
path_gifs = '../Escritorio/carpeta_comp/gifs_dataset2/'

carp = os.listdir(path)
for j in carp:
	carpetas = os.listdir(path + j)
	print(j)
	nuevo_path_gifs = path_gifs + j[0:9]
	#print(nuevo_path_gifs)
	os.system('mkdir ' + nuevo_path_gifs)
	for i in carpetas:
		print(i)
		img_array = []
		imagenes = os.listdir(path + j + '/' + i)
		imagenes.sort()
		x = 0
		for imagen in imagenes:
			x += 1
			if x%2 == 0:
				continue
			img = cv2.imread(path + j + '/' + i + '/' + imagen)
			cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
			img_array.append(img)
		height, widht = img.shape[:2]
		nombre = '/V' + i + '.mp4'
		video = cv2.VideoWriter(nuevo_path_gifs + nombre, cv2.VideoWriter_fourcc(*'mp4v'),5,(widht, height))
		for l in range(len(img_array)):
			video.write(img_array[l])
		video.release()
		gif = VideoFileClip(nuevo_path_gifs + nombre)
		gif.write_gif(nuevo_path_gifs + '/G' + i + '.gif')
		os.system('rm ' + nuevo_path_gifs + nombre)
