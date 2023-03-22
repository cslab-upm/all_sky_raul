# Convierte las imagenes en un dataframe para subirlo a zoon

import csv
import os
import pandas as pd

path_images = "/home/raul/all_sky_raul/imagenes/cam43-UPM-MAD-2022-11-13--00-04-01"
images = os.listdir(path_images)
images.sort()
path_csv = "/home/raul/all_sky_raul/datos/"
data = pd.DataFrame()

date = ""
row = -1
column = 1
rows = 0

for i in range(len(images)):
	if images[i][0:7] == date:
		name = path_images + "/" + images[i]
		data.loc[row,"image_" + str(column)] = name
		column = column + 1
	else:
		date = images[i][0:7]
		data.loc[rows, "subject_id"] = images[i][0:13]
		row = row + 1
		column = 0
		name = path_images + "/" + images[i]
		data.loc[row, "image_" + str(column)] = name
		rows = rows + 1
		column = column + 1

data.to_csv(path_csv + "/images_manifest.csv", index=False)
