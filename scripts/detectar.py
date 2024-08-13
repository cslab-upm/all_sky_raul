import cv2 as cv
import numpy as np
import os

path_videos = '/home/chamorropi/Desktop/videos/'
path_meteor = '/home/chamorropi/Desktop/meteor/'
path_no_meteor = '/home/chamorropi/Desktop/noMeteor/'

def img_processing (img, mask):
	blurred = cv.GaussianBlur(img,(17,17), 0)
	edges = cv.Canny(blurred,100,200)
	closed = cv.morphologyEx(edges, cv.MORPH_CLOSE, (7,7), iterations = 5)
	masked = cv.bitwise_and(closed, mask)
	lines = cv.HoughLinesP(masked, 1, np.pi/180, 30, maxLineGap=10)
	if lines is not None:
		return (True, lines)
	else:
		return(False, lines)

def detect(file, mask_image):
	if mask_image is None:
		mask = np.ones((1,1,1),dtype=np.uint8)*255
	else:
		mask = cv.imread(mask_image, cv.IMREAD_GRAYSCALE)
	vid = cv.VideoCapture(file)
	if (vid.isOpened() == False):
		print('Error opening video ' + file)
	while(vid.isOpened()):
		ret, frame = vid.read()
		if ret == True:
			dimensions = frame.shape
			height = dimensions[0]
			widht = dimensions[1]
			resizedMask = cv.resize(mask, (widht,height), interpolation = cv.INTER_AREA)
			detection = img_processing(frame, resizedMask)
			if detection[0] is True:
				vid.release()
				return detection
		else:
			break
	vid.release()
	return (False, None)


videos = os.listdir(path_videos)
for i in videos:
	if i == 'scripts':
		continue
	x = detect(path_videos + i, None)
	#print (type(x))
	if x[0]:
		os.system('mv ' + path_videos + i + ' ' + path_meteor)
	else:
		os.system('mv ' + path_videos + i + ' ' + path_no_meteor)

