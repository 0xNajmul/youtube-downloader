from pytube import YouTube # pip install pytube 
import os

print("Youtube Video Downloader")  
inp = input("Enter Video Id : ") # example : 9bZkp7q19f0 , EHkozMIXZ8w , kJQP7kiw5Fk
print("Collecting Data...")
final = "https://www.youtube.com/watch?v="+inp
desktop_loc = os.path.expanduser("~/Desktop/")

yt = YouTube(final)
title = yt.title
print("Video Found !")    
print("Video Title : ",title)   
choice = input("Downlod Video or Audio 1/2 : ")

if(choice=='1'):
    print("Video is Downloading...") 
    dwn = yt.streams.first()
    dwn.download(desktop_loc)
    print("Downlod Complete !") 

elif(choice=='2'):
    print("Video is Downloading...") 
    dwn = yt.streams.filter(only_audio=True).first()
    dwn.download()
    print("Downlod Complete !")   

else:    
    print("Sorry Wrong Input !")


