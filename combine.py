from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk


class start_window:
    def __init__ (self,root):

        #start Window
        self.root=root
        self.root.title("Start Window")
        self.root.geometry("900x600+0+0")
        self.root.minsize(900,600)
        self.root.maxsize(900,600)
        #background image
        self.bg=ImageTk.PhotoImage(file =r"E:\Mashayaque\First Year\Sem 2\Project\Recruitment System\login_bg.webp")
        lbl_bg = Label(self.root, image = self.bg).place(x=0, y=0, relwidth=1, relheight=1)
        lbl_2=Label(self.root,text="Welcome to Company Recruitment System",font=("Space Mono",20,"bold"),fg="black",bg='#E0FFFF').place(x=200,y=400)
        button1=Button(self.root,text="Login Page",font=("Space Mono",16,"bold"),bd=4,fg="white",bg='blue',activebackground='blue',activeforeground='white').place(x=400,y=500)      

class login_window:
    def __init__ (self,root):

        #login Window
        self.root=root
        self.root.title("Login Window")
        self.root.geometry("1100x700+0+0")
        self.root.minsize(800,670)
        self.root.maxsize(1100,700)
        
        self.bg=ImageTk.PhotoImage(file=r"E:\Mashayaque\First Year\Sem 2\Project\Recruitment System\login_form3.jpg")
        lbl_bg = Label(self.root, image = self.bg).place(x=0, y=0, relwidth=1, relheight=1)
        
        #frame
        frame=Frame(self.root,bg="white")
        frame.place(x=370,y=100,width=400,height=480)

        #frame inside
        img1=Image.open(r"E:\Mashayaque\First Year\Sem 2\Project\Recruitment System\6681204.png")
        img1=img1.resize((100,100))
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
        self.log_button=Button(frame,command=self.login,text="LOGIN",font=("times new roman",15,"bold"),bd=3,fg="white",bg="blue",activeforeground="white",activebackground="blue")
        self.log_button.place(x=160,y=400)
    
    # this function is for validation or showing popups for errors and success, basically will make login button work
    def login(self):
        if self.eusrname.get()=="" and self.epasswd.get()=="":
            messagebox.showerror("Error", "Enter the info to login !!")
        elif self.eusrname.get()=="SRK786" and self.epasswd.get()=="12345":
            messagebox.showinfo("Correct", "Login successful $$$")
        else:
            messagebox.showerror("Incorrect", "Enter correct Username and Password !!")

'''
class RecruitmentSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Company Recruitment System")
        self.root.geometry("1360x768")

        # main image
        img1=Image.open(r"E:\Mashayaque\First Year\Sem 2\Project\Recruitment System\main2.jpeg")
        img1=img1.resize((1360,768))
        self.photoimg1=ImageTk.PhotoImage(img1)
        lblimg1=Label(self.root,image=self.photoimg1,bd=4).place(x=0,y=0,width=1360,height=768)

        #logo
        img2=Image.open(r"E:\Mashayaque\First Year\Sem 2\Project\Recruitment System\Recruitment_logo.png")
        img2=img2.resize((150,125))
        self.photoimg2=ImageTk.PhotoImage(img2)
        lblimg2=Label(self.root,image=self.photoimg2,bd=6).place(x=0,y=0,width=155,height=130)

        # title
        lbl_title=Label(self.root,text="Company Recruitment System",font=("OPTIMA",35,"bold"),bg="white",fg="blue",bd=4).place(x=400,y=40)

root=Tk()
app=RecruitmentSystem(root)
root.mainloop()
'''

sw=start_window
sw.mainloop()

