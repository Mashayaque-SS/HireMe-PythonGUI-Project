from tkinter import *
from PIL import Image,ImageTk
import show_data 
import main_win

class google:
    def __init__(self,root):
        self.root=root
        self.root.title("google PVT LMT")
        self.root.geometry("1360x768")
        self.root.state('zoomed')

        # image and info
        img=Image.open(r"E:\Mashayaque\First Year\Sem 2\Project\Recruitment System\g4.png")
        img=img.resize((1360,768))
        self.photoimg=ImageTk.PhotoImage(img)
        lblimg=Label(self.root,image=self.photoimg,bd=4).place(x=0,y=0,width=1360,height=768)
        lb1=Label(self.root,text="google is a Multinational Company i.e. An MNC, which makes it one among the top companies",font=("times new roman",15),bg="white",fg="black")
        lb1.place(x=5,y=5)
        lb2=Label(self.root,text="CEO of google is Sundar Pichai",font=("times new roman",15),bg="white",fg="black")
        lb2.place(x=5,y=35)
        lb3=Label(self.root,text="You will Find all the requirements on the official Website",font=("times new roman",15),bg="white",fg="black")
        lb3.place(x=5,y=65)
        lb4=Label(self.root,text="Start your career journey by creating a resume :)",font=("times new roman",15),bg="white",fg="black")
        lb4.place(x=5,y=95)

        #button
        b1=Button(self.root,text="Create Resume",command=self.res,font=("monaco",20,"bold"),bg="white",fg="blue",bd=4,activebackground="white",activeforeground="blue")
        b1.place(x=450,y=575)
        b2=Button(self.root,text="Home",command=self.hm,font=("monaco",20,"bold"),bg="white",fg="blue",bd=4,activebackground="white",activeforeground="blue")
        b2.place(x=700,y=575)

    def res(self): 
        self.obj=show_data.data_display(self.root)

    def hm(self): 
        self.obj=main_win.RecruitmentSystem(self.root)

root=Tk()
app=google(root)
root.mainloop()