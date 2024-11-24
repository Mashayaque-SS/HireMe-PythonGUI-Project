from tkinter import *
from PIL import Image,ImageTk
import com_win
import show_data 
import about 

class RecruitmentSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Company Recruitment System")
        self.root.geometry("1360x768+0+0")
        self.root.state("zoomed")

        # main image
        img1=Image.open(r"E:\Mashayaque\First Year\Sem 2\Project\Recruitment System\main2.jpeg")
        img1=img1.resize((1360,768))
        self.photoimg1=ImageTk.PhotoImage(img1)
        lblimg1=Label(self.root,image=self.photoimg1,bd=4).place(x=0,y=0,width=1360,height=768)

        #logo
        img2=Image.open(r"E:\Mashayaque\First Year\Sem 2\Project\Recruitment System\Recruitment_logo.png")
        img2=img2.resize((150,125))
        self.photoimg2=ImageTk.PhotoImage(img2)
        lblimg2=Label(self.root,image=self.photoimg2,bd=6).place(x=0,y=0,width=150,height=125)

        # title
        lbl_title=Label(self.root,text="Company Recruitment System",font=("times new roman",35,"bold"),bg="white",fg="blue",bd=4).place(x=400,y=40)

        # Buttons (Options/Menu)

            #--Home
        b1=Button(self.root,text="Home",font=("monaco",28,"bold"),bg="blue",fg="white",bd=3,activebackground="blue",activeforeground="white").place(x=35,y=245,width=215,height=50)
            #--Companies
        b2=Button(self.root,text="Companies",command=self.com,font=("monaco",28,"bold"),bg="blue",fg="white",bd=3,activebackground="blue",activeforeground="white").place(x=35,y=315,width=215,height=50)
            #--Resume
        b3=Button(self.root,text="Application",command=self.res,font=("monaco",22,"bold"),bg="blue",fg="white",bd=3,activebackground="blue",activeforeground="white").place(x=35,y=385,width=215,height=50)
            #--about
        b4=Button(self.root,text="about",command=self.ab,font=("monaco",28,"bold"),bg="blue",fg="white",bd=3,activebackground="blue",activeforeground="white").place(x=35,y=455,width=215,height=50)

    def ab(self):
        self.obj=about.about(self.root)
    def res(self):
        self.obj=show_data.data_display(self.root)
    def com(self):
        self.obj=com_win.Company(self.root)

root=Tk()
app=RecruitmentSystem(root)
root.mainloop()