import csv
import sys
import os
import configparser
import pandas as pd
from panoptes_client import SubjectSet, Subject, Project, Panoptes

#try:
	#config = configparser.ConfigParser()
	#config.read('/home/raul/all_sky_raul/scripts/configuracion.properties')
	
	#user = config.get('Credentials', 'username')
	#passwd = config.get('Credentials', 'password')
	
	#manifest_path = config.get('Directorios', 'manifest_path')
#except:
#	print('ERROR: No se ha podido leer el fichero de configuracion.')
#	sys.exit(1)
	
manifest_images_file = "/home/raul/all_sky_raul/datos/images_manifest.csv"

image_set_name = 'Frames_prueba'

Panoptes.connect(username=sys.argv[1], password=sys.argv[2])

project = Project('19814')

try:
	subject_set = SubjectSet.where(project_id=project.id, display_name=image_set_name).next()
except StopIteration:
	subject_set = SubjectSet()
	subject_set.links.project = project
	subject_set.display_name = image_set_name
	subject_set.save()
	
with open(manifest_images_file, 'r') as mani_file:
	print('Uploading frames')
	r = csv.DictReader(mani_file)
	for line in r:
		subject = Subject()
		subject.links.project = project
		
		df = pd.read_csv("/home/raul/all_sky_raul/datos/images_manifest.csv")
		
		for i in range(len(df.axes[1]) - 1):
			subject.add_location(line['image_' + str(i)])
		
		subject.metadata['subject_id'] = line['subject_id']
		
		subject.save()
		subject_set.add(subject.id)
