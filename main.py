from pytube import YouTube

def Download(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download()
    except:
        print("error occurred, try again")
    print("Download completed")


link = input("YouTube video URL: ")
Download(link)
