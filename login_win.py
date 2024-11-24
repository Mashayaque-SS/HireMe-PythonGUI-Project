from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk 
import subprocess
import sys
import main_win 

class login_window:

    def __init__ (self,root):

        #login Window
        self.root=root
        self.root.title("Login Window")
        self.root.geometry("1100x690+110+0")
        #self.root.state("zoomed")
        #self.root.minsize(800,670)
        #self.root.maxsize(1100,700)
        
        self.bg=ImageTk.PhotoImage(file=r"E:\Mashayaque\First Year\Sem 2\Project\Recruitment System\login_form3.jpg")
        lbl_bg = Label(self.root, image = self.bg).place(x=0, y=0, relwidth=1, relheight=1)
        
        #frame
        frame=Frame(self.root,bg="white")
        frame.place(x=370,y=100,width=400,height=480)

        #frame inside
        img1=Image.open(r"E:\Mashayaque\First Year\Sem 2\Project\Recruitment System\6681204.png")
        img1=img1.resize((100,100),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lblimg1=Label(self.root,image=self.photoimage1,bg="white",borderwidth=0).place(x=525,y=110,width=100,height=100)

        #username button
        usrname=lbl=Label(frame,text="USERNAME : ",font=("times new roman",15,"bold"),fg="black",bg="white").place(x=40,y=150)
        self.eusrname=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.eusrname.place(x=40,y=200)

        #password button
        passwd=lbl=Label(frame,text="PASSWORD : ",font=("times new roman",15,"bold"),fg="black",bg="white").place(x=40,y=250)
        self.epasswd=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.epasswd.place(x=40,y=300)

        #login button also given reference of login function using self.login
        self.log_button=Button(frame,command=self.rs,text="LOGIN",font=("times new roman",15,"bold"),bd=3,fg="white",bg="blue",activeforeground="white",activebackground="blue")
        self.log_button.place(x=160,y=400)

    def rs(self):
        self.obj=main_win.RecruitmentSystem(self.root)

root=Tk()
app=login_window(root)
root.mainloop()

'''
    # this function is for validation or showing popups for errors and success, basically will make login button work
    def login(self):
        if self.eusrname.get()=="" and self.epasswd.get()=="":
            messagebox.showerror("Error", "Enter the info to login !!")
            return False
        elif (self.eusrname.get()=="SRK786" and self.epasswd.get()=="12345"):
            messagebox.showinfo("Correct", "Login successful $$$")
            self.root.destroy()
            subprocess.call([sys.executable,'main_win.py','RecruitmentSystem'])
            return True
        else:
            messagebox.showerror("Incorrect", "Enter correct Username and Password !!")
            return False
'''