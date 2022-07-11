import os
os.chdir('/content/gdrive/MyDrive/mp3')

from pytube import Playlist, YouTube
playlist = Playlist('https://youtube.com/playlist?list=PLsyOSbh5bs15OXJIigNdRgK0za-JXwhz1')
print('download...')
for i in playlist.video_urls:
    print(i)
    yt = YouTube(i)
    yt.streams.filter().get_highest_resolution().download()  
print('ok!')

