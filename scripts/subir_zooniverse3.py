# COnvierte videos a gifs

from moviepy.editor import VideoFileClip

video = VideoFileClip("Escritorio/carpeta_comp/meteoros/videos_fran/video1.mp4")

video.write_gif("Escritorio/carpeta_comp/meteoros/video1.gif")
