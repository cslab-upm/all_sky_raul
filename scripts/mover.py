import os

path_destino =  '../Escritorio/carpeta_comp/gifs_dataset2/pruebas/'
path_origen = '../Escritorio/carpeta_comp/gifs_dataset2/videos_2016_1/'

carpetas = os.listdir(path_origen)

for i in carpetas:
	imagenes = os.listdir(path_origen + i)
	for j in imagenes:
		os.system('mv ' + path_origen + i + '/' + j + ' ' + path_origen)
