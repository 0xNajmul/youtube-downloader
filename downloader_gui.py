from pytube import YouTube # pip install pytube 
from tkinter import *
from tkinter import ttk
import os

root = Tk()
desktop_loc = os.path.expanduser("~/Desktop/")

label1 = Label(root,text="Youtube Downloader",width=60,font="none 12 bold")
label1.pack() 

label2 = Label(root,text="Enter Your Video ID",width=60,background="white")
label2.pack()

inp = Entry(root,width=36)
inp.pack(pady=5, padx=20)
inp.configure(background="lightgrey")

files = ('Audio', 'Video')
combo = ttk.Combobox(root, values=files, state='readonly',width=33)
combo.current(0)
combo.pack(pady=10, padx=20)  

def dwn():
    inp_data = inp.get()
    combo_data = combo.get()
    final = "https://www.youtube.com/watch?v="+inp_data
    yt = YouTube(final)   
    if(combo_data=='Video'):       
        dwn = yt.streams.first()
        dwn.download(desktop_loc)
        label3 = Label(root,text="Download Complete",width=60,background="white")
        label3.pack()
    elif(combo_data=='Audio'):        
        dwn = yt.streams.filter(only_audio=True).first()
        dwn.download(desktop_loc)    
        label4 = Label(root,text="Download Complete",width=60,background="white")
        label4.pack()

button = Button(root,text="Download",width=30,command=dwn)
button.pack() 

def main():    
    root.iconbitmap('icon.ico')
    root.title("YouTube Video Downloader")
    root.minsize(width=600,height=300)
    root.maxsize(width=600,height=300)
    root.configure(background="white")

    root.mainloop()

if __name__ == "__main__":
    main()    
