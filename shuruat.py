from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk
import login_win 

class start_window:
    def __init__ (self,root):

        #start Window
        self.root=root
        self.root.title("Start Window")
        self.root.geometry("900x600+0+0")
        #background image
        self.bg=ImageTk.PhotoImage(file =r"E:\Mashayaque\First Year\Sem 2\Project\Recruitment System\login_bg.webp")
        lbl_bg = Label(self.root, image = self.bg).place(x=0, y=0, relwidth=1, relheight=1)
        lbl_2=Label(self.root,text="Welcome to Company Recruitment System",font=("times new roman",20,"bold"),fg="black",bg='#E0FFFF').place(x=200,y=400)
        button1=Button(self.root,text="Login Page",command=self.lw,font=("times new roman",16,"bold"),bd=4,fg="white",bg='blue',activebackground="blue",activeforeground='white')
        button1.place(x=400,y=500)  

    def lw(self):
        self.obj=login_win.login_window(self.root)

root = Tk()
app = start_window(root)
root.mainloop()