import cv2
import os

path_video = '../Escritorio/carpeta_comp/meteoros/cam31-ObservatoireOukaimeden-MOR-2018-02-24--03-27-52.gif'

video = cv2.VideoCapture(path_video)

c_frame = 0

while True:
	ret, frame = video.read()
	if ret:
		name = 'frame'+str(c_frame)+'.jpg'
		print('Creating...'+name)
		cv2.imwrite(name,frame)
		c_frame += 1
		os.system('mv ' + name + ' ../Escritorio/carpeta_comp/frames/')
	else:	
		print('fin')
		break
	
video.release()
cv2.destroyAllWindows()
