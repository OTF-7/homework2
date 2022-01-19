import pafy
import pytube
url = input("Enter the URL of the video > ")

video = pafy.new(url)
best = video.getbest()
print(type(best))