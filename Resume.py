from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk 
import main_win
import show_data 
import mysql.connector

class resume:
    def __init__(self,root):
        self.root=root
        self.root.title("Resume Tab")   
        self.root.geometry("1360x768")

        # image and info
        img=Image.open(r"E:\Mashayaque\First Year\Sem 2\Project\Recruitment System\r1.jpg")
        img=img.resize((1360,768))
        self.photoimg=ImageTk.PhotoImage(img)
        lblimg=Label(self.root,image=self.photoimg,bd=4).place(x=0,y=0,width=1360,height=768)
        lb1=Label(self.root,text="Create Your Resume :)",font=("times new roman",20,"bold"),fg="blue",bg="white",bd=4)
        lb1.place(x=5,y=5)
    
        # Entries

            #--name
        name=Label(self.root,text="Name :",font=("times new roman",20,"bold"),fg="white",bg="blue",bd=3).place(x=40,y=150)
        name=ttk.Entry(self.root,font=("times new roman",15,"bold"))
        name.place(x=40,y=200)

            #--gender
        name=Label(self.root,text="gender :",font=("times new roman",20,"bold"),fg="white",bg="blue",bd=3).place(x=40,y=270)
        self.nameM=Radiobutton(self.root,text="Male",font=("monaco",18,"bold"),value="Male")
        self.nameM.place(x=40,y=320)
        self.nameF=Radiobutton(self.root,text="Female",font=("monaco",18,"bold"),value="Female")
        self.nameF.place(x=140,y=320)

            #--Qualification 
        qf=Label(self.root,text="Qualification :",font=("times new roman",20,"bold"),fg="white",bg="blue",bd=3).place(x=40,y=400)
        opt=["10th pass","12th pass","Under graduate","Post graduate","Masters"]
        listqf=StringVar(root)
        listqf.set("SELECT")
        list=OptionMenu(self.root,listqf,*opt)
        list.place(x=40,y=450,width=150)

           #--languages
        languages=Label(self.root,text="languages known:",font=("times new roman",20,"bold"),fg="white",bg="blue",bd=3).place(x=500,y=350)
        self.languages=Checkbutton(self.root,text="Java",variable="Java",font=("times new roman",15,"bold"),fg="black",bg="white",bd=2)
        self.languages.place(x=500,y=400)
        self.languages2=Checkbutton(self.root,text="Python",variable="Python",font=("times new roman",15,"bold"),fg="black",bg="white",bd=2)
        self.languages2.place(x=600,y=400)
        self.languages3=Checkbutton(self.root,text="C++",variable="C++",font=("times new roman",15,"bold"),fg="black",bg="white",bd=2)
        self.languages3.place(x=500,y=440)
        self.languages4=Checkbutton(self.root,text="HTML",variable="HTML",font=("times new roman",15,"bold"),fg="black",bg="white",bd=2)
        self.languages4.place(x=600,y=440)
        self.languages5=Checkbutton(self.root,text="Kotlin",variable="Kotlin",font=("times new roman",15,"bold"),fg="black",bg="white",bd=2)
        self.languages5.place(x=500,y=480)
        self.languages6=Checkbutton(self.root,text="CSS",variable="CSS",font=("times new roman",15,"bold"),fg="black",bg="white",bd=2)
        self.languages6.place(x=600,y=480)

        #--AGE
        age=Label(self.root,text="Age :",font=("times new roman",20,"bold"),fg="white",bg="blue",bd=3).place(x=40,y=590)
        self.age=ttk.Entry(self.root,font=("times new roman",15,"bold"))
        self.age.place(x=40,y=640)

        #--Post
        post=Label(self.root,text="Post :",font=("times new roman",20,"bold"),fg="white",bg="blue",bd=3).place(x=500,y=150)
        optp=["Student","Teacher","Professor","DR"]
        listp=StringVar(root)
        listp.set("SELECT")
        listpm=OptionMenu(self.root,listp,*optp)
        listpm.place(x=500,y=200,width=150)

        #--Achievements
        Achievements=Label(self.root,text="Achievements :",font=("times new roman",20,"bold"),fg="white",bg="blue",bd=3).place(x=500,y=590)
        self.Achievements=ttk.Entry(self.root,font=("times new roman",15,"bold"))
        self.Achievements.place(x=500,y=640)

        #--csc
        csc=Label(self.root,text="Country,State,City :",font=("times new roman",20,"bold"),fg="white",bg="blue",bd=3).place(x=940,y=150)
        self.csc=ttk.Entry(self.root,font=("times new roman",15,"bold"))
        self.csc.place(x=940,y=200)

        #--Email
        Email=Label(self.root,text="Email :",font=("times new roman",20,"bold"),fg="white",bg="blue",bd=3).place(x=940,y=300)
        self.Email=ttk.Entry(self.root,font=("times new roman",15,"bold"))
        self.Email.place(x=940,y=350)

        #--Hobby
        intrests=Label(self.root,text="Intrests/Hobby :",font=("times new roman",20,"bold"),fg="white",bg="blue",bd=3).place(x=940,y=450)
        self.intrests=ttk.Entry(self.root,font=("times new roman",15,"bold"))
        self.intrests.place(x=940,y=500)

        #Submit and home
        b1=Button(self.root,text="Submit",font=("monaco",22,"bold"),fg="white",bg="blue",activebackground="blue",activeforeground="white",bd=6)
        b1.place(x=920,y=595)
        b2=Button(self.root,text="Home",command=self.hm,font=("monaco",22,"bold"),fg="blue",bg="white",activebackground="white",activeforeground="blue",bd=6)
        b2.place(x=1100,y=595)
        b3=Button(self.root,text="Show Resume",command=self.dd,font=("monaco",20,"bold"),fg="black",bg="yellow",activebackground="yellow",activeforeground="black",bd=6)
        b3.place(x=1110,y=10)

    def dd(self):
        self.new_win4=Toplevel()
        self.obj4=show_data.data_display(self.new_win4)

    def hm(self):
        self.new_win11=Toplevel()
        self.obj11=main_win.RecruitmentSystem(self.new_win11)

root=Tk()
app=resume(root)
root.mainloop()

'''
    def name(self):
        if self.name_ent.get()=="" or self.age_ent.get()=="":
            messagebox.showerror("error!","Fill all Entries")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="mysql",database="hireme")
            cur=conn.cursor()
            cur.execute("insert into data values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                
                                                                                                    self.name_ent.get(),
                                                                                                    self.genm_ent.get(),
                                                                                                    self.genf_ent.get(),
                                                                                                    self.age_ent.get(),
                                                                                                    self.quali_ent.get(),
                                                                                                    self.post_ent.get(),
                                                                                                    self.lang1_ent.get(),
                                                                                                    self.lang2_ent.get(),
                                                                                                    self.lang3_ent.get(),
                                                                                                    self.lang4_ent.get(),
                                                                                                    self.lang5_ent.get(),
                                                                                                    self.lang6_ent.get(),
                                                                                                    self.ach_ent.get(),
                                                                                                    self.hobby_ent.get(),
                                                                                                    self.csc_ent.get(),
                                                                                                    self.email_ent.get()
                                                                                
                                                                                                    ))
            conn.commit()
            conn.close()   

    def connec(self):
        self.new_win=Toplevel()
        self.obj=show_data.data_display(self.new_win)
'''
'''
        self.name_ent=StringVar()
        self.age_ent=StringVar()
        self.genm_ent=StringVar()
        self.quali_ent=StringVar()
        self.post_ent=StringVar()
        self.lang1_ent=StringVar()
        self.ach_ent=StringVar()
        self.csc_ent=StringVar()
        self.email_ent=StringVar()
        self.hobby_ent=StringVar()
 '''       
