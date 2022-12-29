import os
import pandas as pd
import matplotlib.pyplot as plt


os.system('panoptes project download 19814 datos1.csv')
os.system('mv datos1.csv datos/')

data = pd.DataFrame()
data = pd.read_csv('datos/datos1.csv')

df = pd.DataFrame(columns=['index', 'subject_ids', 'Meteoro_No', 'Trayectoria', 'Grosor', 'Que_es'])

def buscar_si (frase):
	aux = False
	for i in frase:
		if i == 'S':
			 aux = True
			 continue
		elif aux == True:
			if i == 'i' or i == 'ì':
				salida = True
				break
			else:
				salida = False
		else:
			salida = False
	return salida
	
def buscar_primer_x1 (frase):
	j = frase.find('x1')
	l = frase.find('tool')
	out = ''
	for i in range(j, l-1):
		out = out + frase[i]
	return out

def buscar_segundo_x1 (frase):
	j = frase.find('x1', frase.find('x1')+100)
	l = frase.find('tool', frase.find('tool')+100)
	out = ''
	for i in range(j, l-1):
		out = out + frase[i]
	return out
	
def buscar_otro (frase):
	j = frase.find('value', frase.find('value')+10)
	l = frase.find('}', 100)
	out = ''
	for i in range(j + 8, l-1):
		out = out + frase[i]
	return out
	
######################################################
# Crear un nuevo dataFrame con datos especificos
for i in range(len(data)):
	fecha = data['created_at'].iloc[i]
	if fecha[5:10] == '11-17':
		fila = []
		fila.append(data.index[i])
		fila.append(data['subject_ids'].iloc[i])
		frase = data['annotations'].iloc[i]
		if buscar_si(frase):
			fila.append('Si')
			fila.append(buscar_primer_x1(frase))
			fila.append(buscar_segundo_x1(frase))
			fila.append('-')
		else:
			fila.append('No')
			fila.append('-')
			fila.append('-')
			fila.append(buscar_otro(frase))
		df = df.append({'index':fila[0], 'subject_ids': int(fila[1]), 'Meteoro_No': fila[2], 'Trayectoria': fila[3], 'Grosor': fila[4], 'Que_es': fila[5]}, ignore_index=True)
	
##########################################################
# Clasificar datos	
#x = []
#y = []
#for i in df['subject_ids'].unique():
#	serie = df[df.subject_ids == i].Meteoro_No == 'Si'
#	s = 0
#	for j in serie.index:
#		if serie[j] == True:
#			s = s+1
#	y.append(s/serie.shape[0])
#	x.append(i)
	
##########################################################
# Graficar Meteorito vs No_Meteorito
#fig, ax = plt.subplots()
#plt.bar(x,y)
#ax.set_xticklabels(x)
#plt.xticks(x, rotation = 90)
#plt.show()

##########################################################
# Clasificar no Meteoritos
dic = {}
for i in df['subject_ids'].unique():
	#serie = df[df.subject_ids == i].Meteoro_No == 'Si'
	#s = 0
	#for j in serie.index:
	#	if serie[j] == True:
	#		s = s+1
	#if s/serie.shape[0] > 0.8: # Descarta las clasificaciones por encima del 80% como meteoritos
	#	continue
	serie2 = df[df.subject_ids == i]['Que_es']
	Nub = 0
	Avio = 0
	Bich = 0
	Met = 0
	Otr = 0
	for l in serie2.index:
		if serie2[l] == 'Nubes':
			Nub = Nub + 1
		elif serie2[l] == 'Avion':
			Avio = Avio + 1
		elif serie2[l] == 'Bicho':
			Bich = Bich + 1
		elif serie2[l] == '-':
			Met = Met + 1
		else:
			Otr = Otr + 1
	dic[i] = [Nub/serie2.shape[0], Avio/serie2.shape[0], Bich/serie2.shape[0], Met/serie2.shape[0], Otr/serie2.shape[0]]
	
##########################################################
# Graficar
auc = pd.DataFrame(dic)
fig, ax = plt.subplots()

plt.bar(auc.columns, auc.iloc[0] + auc.iloc[1] + auc.iloc[2] + auc.iloc[3] + auc.iloc[4], label = 'Otro')
plt.bar(auc.columns, auc.iloc[0] + auc.iloc[1] + auc.iloc[2] + auc.iloc[3], label = 'Meteorito')
plt.bar(auc.columns, auc.iloc[0] + auc.iloc[1] + auc.iloc[2], label = 'Bicho')
plt.bar(auc.columns, auc.iloc[0] + auc.iloc[1], label = 'Avion')
plt.bar(auc.columns, auc.iloc[0], label = 'Nubes')

plt.legend(loc = 'best')
ax.set_xticklabels(auc.columns)
plt.xticks(auc.columns, rotation=90)
plt.show()

