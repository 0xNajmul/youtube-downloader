from tkinter import *

def main():
    root = Tk()
    root.iconbitmap('icon.ico')
    root.title("YouTube Video Downloader")
    root.minsize(width=600,height=400)
    root.maxsize(width=600,height=400)

    label1 = Label(root,text="Enter Video ID",width=36)
    label1.pack() 

    inp = Entry(root,width=36)
    inp.pack()
    inp_data = inp.get()
    
    button = Button(root,text="Download",width=30,command=video)
    button.pack()       
   
   


    root.mainloop()

def video():
    data = main()
    print(data)


if __name__ == "__main__":
    main()    
