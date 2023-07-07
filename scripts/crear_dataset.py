# Este script crea un dataset a partir de los datos clasificados en zooniverse

import os
import pandas as pd
import re
import math
import warnings

os.system('panoptes project download 19814 datos1.csv') # Es necesario panoptes config

path_candidatos = '../../Escritorio/carpeta_comp/gifs_dataset2/videos_2016_1/'
path_meteoros = '../../Escritorio/careta_comp/meteoros/'
path_otros = '../../Escritorio/carpeta_comp/otros/'

data = pd.DataFrame()
data = pd.read_csv('datos1.csv')

reg = pd.read_csv('registro.csv')

def buscar_filename (frase):
  out = ''
  j = frase.find('Filename')
  l = frase.find('}', j)
  for i in range (j + 11, l - 1):
    out = out +  frase[i]
  return out
  
#def buscar_retired (frase):
#  out = ''
#  j = frase.find('retired')
#  l = frase.find(',', j)
#  for i in range (j + 9, l):
#    out = out +  frase[i]
#  return out
  
def buscar_coordenadas(frase, palabra, pos):
  out = ''
  if pos == 1:
    j = frase.find(palabra)
    l = frase.find(',', j)
  elif pos == 2:
    j = frase.find(palabra, frase.find(palabra) + 100)
    l = frase.find(',', j)
  for i in range (j + 4, l - 1):
    out = out +  frase[i]
  if out == '':
      out = math.nan
  return out
  
def buscar_objeto (frase):
  j = frase.find('value', frase.find('value')+10)
  l = frase.find('}', j)
  out = ''
  for i in range (j+8, l-1):
    out = out +  frase[i]
  return out
  
def buscar_fecha (frase):
  out = ''
  j = frase.find('20')
  l = frase.find('.', j)
  for i in range (j, l - 1):
    out = out +  frase[i]
  if out == '':
      out = ''
  return out
  
colum = ['Fichero', 'Identificador', 'Fecha', 'Fecha_Clasificacion', 'Objeto', 'Trayectoria_1', 'Trayectoria_2', 'Grosor_1', 'Grosor_2', 'Retirada']
csv = pd.DataFrame(columns = colum)
dic = {}
warnings.simplefilter("ignore")
for i in range(696, len(data)): # Empieza en 10 para eliminar las primeras que fueron de pruebas
  fila = []
  fila.append('')#buscar_filename(data['subject_data'].iloc[i]))
  fila.append(data['subject_ids'].iloc[i])
  fila.append('')#buscar_fecha(fila[0]))
  fila.append(int(data['created_at'].iloc[i][:4] + data['created_at'].iloc[i][5:7] + data['created_at'].iloc[i][8:10]))
  frase = data['annotations'].iloc[i]
  if re.search('Yes', frase):
    fila.append('Meteoro')
    fila.append([float(buscar_coordenadas(frase, 'x1', 1)), float(buscar_coordenadas(frase, 'y1', 1))])
    fila.append([float(buscar_coordenadas(frase, 'x2', 1)), float(buscar_coordenadas(frase, 'y2', 1))])
    fila.append([float(buscar_coordenadas(frase, 'x1', 2)), float(buscar_coordenadas(frase, 'y1', 2))])
    fila.append([float(buscar_coordenadas(frase, 'x2', 2)), float(buscar_coordenadas(frase, 'y2', 2))])
  elif re.search('No está claro', frase):
    #print('No esta claro')
    fila.append('No esta claro')
    fila.append('')
    fila.append('')
    fila.append('')
    fila.append('')
  else:
    fila.append(buscar_objeto(frase))
    fila.append('')
    fila.append('')
    fila.append('')
    fila.append('')
  fila.append('')#buscar_retired(data['metadata'].iloc[i]))
  for l in range(len(colum)):
    dic[colum[l]] = fila[l]
  csv = csv.append(dic, ignore_index = True)
warnings.simplefilter("default")

def buscar_coincidencias(aux):
	z = 0
	for i in aux:
		if i == True:
			z +=1
			break
	if z > 0:
		return True
	else:
		return False

def media_puntos(datos):
  x, y = [], []
  for i in range (len(datos)):
    try:
      float(datos.iloc[i][0])
      if math.isnan(datos.iloc[i][0]):
        continue
      x.append(datos.iloc[i][0])
      y.append(datos.iloc[i][1])
    except:
      continue
  if len(x) == 0:
    return [0,0]
  else:
    return [sum(x)/len(x),sum(y)/len(y)]
    
#def contar_true(datos):
#  x = 0
#  for i in datos:
#    if i == 'true':
#      x += 1
#  return x > 3 or datos.iloc[-1] == 'true'
    
dataset = pd.DataFrame(columns = colum)
dic = {}
warnings.simplefilter("ignore")
for i in csv['Identificador'].unique():
  aux = pd.DataFrame(csv[csv.Identificador == i])
  fila = []
  if buscar_coincidencias(reg.id==i):
  	fila.append(list(reg[reg.id == i]['nombre_fichero'])[0])
  else:
  	fila.append('')
  fila.append(i)
  fila.append(buscar_fecha(fila[0]))
  fila.append(aux['Fecha_Clasificacion'].iloc[-1])
  obj = aux['Objeto'].value_counts().index[0]
  fila.append(obj)
  if obj == 'Meteoro':
    fila.append(media_puntos(aux['Trayectoria_1']))
    fila.append(media_puntos(aux['Trayectoria_2']))
    fila.append(media_puntos(aux['Grosor_1']))
    fila.append(media_puntos(aux['Grosor_2']))
  else:
    fila.append('')
    fila.append('')
    fila.append('')
    fila.append('')
  fila.append(csv[csv.Identificador==i]['Objeto'].value_counts()[0] > 10)
  for l in range(len(colum)):
    dic[colum[l]] = fila[l]
  dataset = dataset.append(dic, ignore_index = True)
warnings.simplefilter("default")

candidatos =  os.listdir(path_candidatos)
for i in dataset['Fichero'].unique():
	if dataset[dataset.Fichero == i]['Retirada'].iloc[0]:
		if i in candidatos:
      			print(i)
      			if dataset[dataset.Fichero == i]['Objeto'].iloc[0] == 'Meteoro':
        			os.system('mv ' + path_candidatos + i + ' ' + path_meteoros)
      			else:
        			os.system('mv ' + path_candidatos + i + ' ' + path_otros)

dataset.to_csv('datos2.csv')

