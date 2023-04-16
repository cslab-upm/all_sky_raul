import csv
import sys
import os
import configparser
import pandas as pd
from panoptes_client import SubjectSet, Subject, Project, Panoptes

path = '../Escritorio/carpeta_comp/gifs_dataset2/'
carpetas = os.listdir(path)

Panoptes.connect(username='CSLab-UPM', password='Ph03n1x;')

project = Project('19814')
image_set_name = 'Videos_Definitivos'

try:
	subject_set = SubjectSet.where(project_id=project.id, display_name=image_set_name).next()
except StopIteration:
	subject_set = SubjectSet()
	subject_set.links.project = project
	subject_set.display_name = image_set_name
	subject_set.save()
	
print('Uploading frames')
for i in carpetas:
	print(i)
	video = os.listdir(path + i)
	for l in video:
		print(l)
		subject = Subject()
		subject.links.project = project
		subject.add_location(path + i + '/' + l)
		subject.save()
		subject_set.add(subject.id)
