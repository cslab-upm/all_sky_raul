import os

path = '../Escritorio/carpeta_comp/gifs_dataset2/1/'

carpeta = os.listdir(path)

i = 0
for j in carpeta:
	carp = os.listdir(path + j)
	for l in carp:
		i += 1

print (i)
