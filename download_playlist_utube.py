from pytube import Playlist
from pyfiglet import Figlet


playlist = Playlist('https://www.youtube.com/watch?v=pCBx0De0iaA&list=PL8O0VBAvvwd0DX08kCxH6LZp27mnj3LrO')
#print('Number of videos in playlist: %s' % len(playlist.video_urls))


# change font of print
text='Number of videos in playlist: ' + str(len(playlist.video_urls))
cool_text=Figlet(font='slant')
print(str(cool_text.renderText(text)))

path=r'C:\Users\finiti\Desktop\יוטיוב\Node.Js With Express & MongoDB'

# Loop through all videos in the playlist and download them
for video in playlist.videos:
    video.streams.first().download(path)
