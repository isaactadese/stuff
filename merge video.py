from moviepy.editor import *
import os
from natsort import natsorted

L =[]

for root, dirs, files in os.walk(r"C:\Users\finiti\Desktop\יוטיוב\MongoDB"):

    #files.sort()
    files = natsorted(files)
    for file in files:
        if os.path.splitext(file)[1] == '.mp4':
            filePath = os.path.join(root, file)
            video = VideoFileClip(filePath)
            L.append(video)

final_clip = concatenate_videoclips(L)
final_clip.to_videofile(r"C:\Users\finiti\Desktop\יוטיוב\MongoDB.mp4", fps=24, remove_temp=False)