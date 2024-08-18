from pytube import YouTube

link = 'https://www.youtube.com/watch?v=FXX4KXKHOyU&t=58s'
youtube_vid = YouTube(link)

print(youtube_vid.title)
# print(youtube_vid.thumbnail_url)

videos = youtube_vid.streams.all()

vid = list(enumerate(videos))
for i in vid:
    print(i)
strm = int(input("Enter the quality for the video: "))
videos[strm].download()
print("Installed successfully!!!")

# import yt_dlp 

# link = 'https://www.youtube.com/watch?v=FXX4KXKHOyU&t=58s'

# name = {
#     'format' : 'bestvideo[height<=720] + bestaudio/best[height<=720]',
#     'name' : 'messi_highresolv.mp4'
# }

# with yt_dlp.YoutubeDL(name) as ydl:
#     ydl.download([link])

# print('Hurray!!!')

