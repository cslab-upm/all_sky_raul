import os

path = '/home/raul/all_sky_raul/imagenes/cam43-UPM-MAD-2022-11-13--00-04-01'
imagenes = os.listdir(path)

new_name = path[47:51] + path[52:54] + path[55:57]

for i in imagenes:
	os.rename(path + '/' + i, path + '/' + new_name + str(i[8:]))
