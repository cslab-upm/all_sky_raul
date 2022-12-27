from moviepy.editor import VideoFileClip

video = VideoFileClip("imagenes/187-20221205023424.mp4")

video.write_gif("imagenes/99-20221203235553.mp4")
