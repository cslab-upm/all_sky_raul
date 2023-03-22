# COnvierte videos a gifs

from moviepy.editor import VideoFileClip

video = VideoFileClip("Escritorio/carpeta_comp/videos_dataset/cand-1/Vcam3-teleferico-PNteide-CAN-2016-05-03--00-16-17.mp4")

video.write_gif("Escritorio/carpeta_comp/gifs_dataset/cand-1/Vcam3-teleferico-PNteide-CAN-2016-05-03--00-16-17.gif")
