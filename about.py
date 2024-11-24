from tkinter import *
from PIL import Image,ImageTk
import main_win

class about:
    def __init__(self,root):
        self.root=root
        self.root.title("About Us")
        self.root.geometry("1360x768")
        self.root.state('zoomed')

        # image and info
        img=Image.open(r"E:\Mashayaque\First Year\Sem 2\Project\Recruitment System\m7.jpg")
        img=img.resize((1360,768))
        self.photoimg=ImageTk.PhotoImage(img)
        lblimg=Label(self.root,image=self.photoimg,bd=4).place(x=0,y=0,width=1360,height=768)

        lb1=Label(self.root,text="About US !",font=("monaco",25,"bold"),bg="blue",fg="white",activebackground="blue",activeforeground="white",bd=4)
        lb1.place(x=100,y=100)

        lb2=Label(self.root,text="This project is made by Mashayaque Sayyad and Shaikh Saffan.",font=("times new roman",16,"bold"),bg="green",fg="white",bd=2)
        lb2.place(x=100,y=200)

        lb2=Label(self.root,text="Motive of this project is to give users a opportunity to create resumes in a user friendly environment",font=("times new roman",16,"bold"),bg="green",fg="white",bd=2)
        lb2.place(x=100,y=230)

        lb3=Label(self.root,text="Details of top companies are mentioned too.",font=("times new roman",16,"bold"),bg="green",fg="white",bd=2)
        lb3.place(x=100,y=260)

        lb4=Label(self.root,text="As this project mainly focuses on hiring and company related things, we named this project as",font=("times new roman",16,"bold"),bg="green",fg="white",bd=2)
        lb4.place(x=100,y=290)

        lb5=Label(self.root,text="HIREME",font=("times new roman",16,"bold"),bg="white",fg="blue",bd=4)
        lb5.place(x=940,y=288)

        lb6=Label(self.root,text="HOPE YOU LIKE IT :)",font=("times new roman",20,"bold"),bg="white",fg="blue",bd=2)
        lb6.place(x=970,y=600)

        b=Button(self.root,text="Home",command=self.hm,font=("monaco",22,"bold"),fg="white",bg="blue",activebackground="blue",activeforeground="white",bd=5)
        b.place(x=615,y=600)

    def hm(self):
        self.obj=main_win.RecruitmentSystem(self.root)

root=Tk()
app=about(root)
root.mainloop()