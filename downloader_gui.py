from tkinter import *
from tkinter import ttk

def main():
    root = Tk()
    root.iconbitmap('icon.ico')
    root.title("YouTube Video Downloader")
    root.minsize(width=600,height=300)
    root.maxsize(width=600,height=300)
    root.configure(background="white")

    label1 = Label(root,text="Youtube Downloader",width=60,font="none 12 bold")
    label1.pack() 
    label2 = Label(root,text="Enter Your Video ID",width=60,background="white")
    label2.pack() 

    inp = Entry(root,width=36)
    inp.pack(pady=5, padx=20)
    inp.configure(background="lightgrey")
    inp_data = inp.get()

     
    files = ('Audio', 'Video')
    combo = ttk.Combobox(root, values=files, state='readonly',width=33)
    combo.current(0)
    combo.pack(pady=10, padx=20)
    combo_data = combo.get()
    
    
    button = Button(root,text="Download",width=30,command=video)
    button.pack()       
   
   


    root.mainloop()

def video():
    pass


if __name__ == "__main__":
    main()    
