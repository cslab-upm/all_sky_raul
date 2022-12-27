import csv
import sys
import os
import configparser
import pandas as pd
from panoptes_client import SubjectSet, Subject, Project, Panoptes

video = '/home/raul/allsky_raul/imagenes/cam43-UPM-MAD-2022-11-13--00-04-01/2022111352.068.jpeg'

Panoptes.connect(username='', password='')

project = Project('19814')
image_set_name = 'Video_prueba'

try:
	subject_set = SubjectSet.where(project_id=project.id, display_name=image_set_name).next()
except StopIteration:
	subject_set = SubjectSet()
	subject_set.links.project = project
	subject_set.display_name = image_set_name
	subject_set.save()
	
print('Uploading frames')
subject = Subject()
subject.links.project = project
subject.add_location(video)
subject.save()
subject_set.add(subject.id)
