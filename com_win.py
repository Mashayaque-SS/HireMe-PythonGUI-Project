from tkinter import *
from PIL import Image,ImageTk
import main_win
import infosys 
import LT 
import wipro
import ggl 
import tcs 

class Company:
    def __init__(self,root):
        self.root=root
        self.root.title("Company Info")
        self.root.geometry("1360x768")

        # main image
        img=Image.open(r"E:\Mashayaque\First Year\Sem 2\Project\Recruitment System\m8.jpg")
        img=img.resize((1360,768))
        self.photoimg=ImageTk.PhotoImage(img)
        lblimg=Label(self.root,image=self.photoimg,bd=4).place(x=0,y=0,width=1360,height=768)
        lbl1=Label(self.root,text="Comapanies You would like :",font=("times new roman",20,"bold"),bg="white",fg="blue",bd=3)
        lbl1.place(x=5,y=5)

        # home button
        home_b=Button(self.root,text="Home",command=self.hm,font=("times new roman",20,"bold"),bg="white",fg="blue",bd=4,activebackground="white",activeforeground="blue")
        home_b.place(x=1250,y=5)

            #--Infosys
                #logo
        img1=Image.open(r"E:\Mashayaque\First Year\Sem 2\Project\Recruitment System\infosys.png")
        img1=img1.resize((75,50))
        self.photoimg1=ImageTk.PhotoImage(img1)
        lblimg1=Label(self.root,image=self.photoimg1,bd=6).place(x=510,y=325)
        b1=Button(self.root,text="Infosys",command=self.inf,font=("monaco",28,"bold"),bg="blue",fg="white",bd=3,activebackground="blue",activeforeground="white")
        b1.place(x=600,y=330,width=215,height=50)
            
            #--TCS
                #logo
        img2=Image.open(r"E:\Mashayaque\First Year\Sem 2\Project\Recruitment System\tcs.png")
        img2=img2.resize((75,50))
        self.photoimg2=ImageTk.PhotoImage(img2)
        lblimg2=Label(self.root,image=self.photoimg2,bd=6).place(x=100,y=150)
        b2=Button(self.root,text="TCS",command=self.tc,font=("monaco",28,"bold"),bg="blue",fg="white",bd=3,activebackground="blue",activeforeground="white")
        b2.place(x=190,y=155,width=215,height=50)

            #--Wipro
                #logo
        img3=Image.open(r"E:\Mashayaque\First Year\Sem 2\Project\Recruitment System\wipro.jpg")
        img3=img3.resize((75,50))
        self.photoimg3=ImageTk.PhotoImage(img3)
        lblimg3=Label(self.root,image=self.photoimg3,bd=6).place(x=100,y=520)
        b3=Button(self.root,text="Wipro",command=self.wipr,font=("monaco",28,"bold"),bg="blue",fg="white",bd=3,activebackground="blue",activeforeground="white")
        b3.place(x=190,y=525,width=215,height=50)
            
            #--L&T
                #logo
        img4=Image.open(r"E:\Mashayaque\First Year\Sem 2\Project\Recruitment System\L&T.png")
        img4=img4.resize((75,50))
        self.photoimg4=ImageTk.PhotoImage(img4)
        lblimg4=Label(self.root,image=self.photoimg4,bd=6).place(x=905,y=150)
        b4=Button(self.root,text="L & T",command=self.lt,font=("monaco",28,"bold"),bg="blue",fg="white",bd=3,activebackground="blue",activeforeground="white")
        b4.place(x=995,y=155,width=215,height=50)

            #--Google
                #logo
        img5=Image.open(r"E:\Mashayaque\First Year\Sem 2\Project\Recruitment System\google.png")
        img5=img5.resize((75,50))
        self.photoimg5=ImageTk.PhotoImage(img5)
        lblimg5=Label(self.root,image=self.photoimg5,bd=6).place(x=905,y=520)
        b5=Button(self.root,text="Google",command=self.gl,font=("monaco",28,"bold"),bg="blue",fg="white",bd=3,activebackground="blue",activeforeground="white")
        b5.place(x=995,y=525,width=215,height=50)

    def inf(self): 
        self.obj=infosys.infy(self.root)

    def tc(self): 
        self.obj=tcs.tcs(self.root)
    
    def wipr(self): 
        self.obj=wipro.wipro(self.root)

    def lt(self): 
        self.obj=LT.LT(self.root)

    def gl(self): 
        self.obj=ggl.google(self.root)

    def hm(self): 
        self.obj=main_win.RecruitmentSystem(self.root)

root=Tk()
app=Company(root)
root.mainloop()