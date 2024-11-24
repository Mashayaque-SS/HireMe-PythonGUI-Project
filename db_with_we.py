from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
#import main_win

class data_display:
    def __init__(self,root):

        self.root=root
        self.root.title("Resume")
        self.root.geometry("1360x768+0+0")
        self.root.config(bg="pink")
        self.root.state("zoomed")

        #stringvar
        self.name_ent=StringVar()
        self.workexp_ent=StringVar()
        self.age_ent=StringVar()
        self.gen_ent=StringVar()
        self.quali_ent=StringVar()
        self.post_ent=StringVar()
        self.lang_ent=StringVar()
        self.ach_ent=StringVar()
        self.csc_ent=StringVar()
        self.email_ent=StringVar()
        self.hobby_ent=StringVar()

        #details_frame *************************
        self.deframe=LabelFrame(self.root,text="Enter Details",font=("times new roman",15,"bold"),fg="blue",relief=RIDGE,bd=15)
        self.deframe.place(x=5,y=5,width=1350,height=430)

        # Entries

            #--name
        name=Label(self.deframe,text="Name :",font=("times new roman",15,"bold"),fg="white",bg="#1877f2",bd=3).place(x=20,y=20)
        namee=ttk.Entry(self.deframe,textvariable=self.name_ent,font=("times new roman",15,"bold"))
        namee.place(x=20,y=55)


            #--gender
        gen=Label(self.deframe,text="Gender :",font=("times new roman",15,"bold"),fg="white",bg="#1877f2",bd=3).place(x=20,y=115)
        gene=ttk.Entry(self.deframe,textvariable=self.gen_ent,font=("times new roman",15,"bold"))
        gene.place(x=20,y=150)

            #--Qualification 
        qf=Label(self.deframe,text="Qualification :",font=("times new roman",15,"bold"),fg="white",bg="#1877f2",bd=3).place(x=20,y=210)
        qfe=ttk.Entry(self.deframe,textvariable=self.quali_ent,font=("times new roman",15,"bold"))
        qfe.place(x=20,y=245)
        #opt=["10th pass","12th pass","Under graduate","Post graduate","Masters"]
        #self.quali_ent=StringVar(root)
        #self.quali_ent.set("SELECT")
        #list=OptionMenu(self.deframe,self.quali_ent,*opt)
        #list.place(x=20,y=245,width=150)

            #--AGE
        age=Label(self.deframe,text="Age :",font=("times new roman",15,"bold"),fg="white",bg="#1877f2",bd=3).place(x=320,y=20)
        self.agee=ttk.Entry(self.deframe,textvariable=self.age_ent,font=("times new roman",15,"bold"))
        self.agee.place(x=320,y=55)

           #--languages
        languages=Label(self.deframe,text="languages known:",font=("times new roman",15,"bold"),fg="white",bg="#1877f2",bd=3).place(x=320,y=145)
        lange=ttk.Entry(self.deframe,textvariable=self.lang_ent,font=("times new roman",15,"bold"))
        lange.place(x=320,y=180)

            #--work experience
        we=Label(self.deframe,text="Working Experience:",font=("times new roman",15,"bold"),fg="white",bg="#1877f2",bd=3).place(x=320,y=260)
        wee=ttk.Entry(self.deframe,textvariable=self.workexp_ent,font=("times new roman",15,"bold"))
        wee.place(x=320,y=295)

        #--Post
        post=Label(self.deframe,text="Post :",font=("times new roman",15,"bold"),fg="white",bg="#1877f2",bd=3).place(x=630,y=20)
        poste=ttk.Entry(self.deframe,textvariable=self.post_ent,font=("times new roman",15,"bold"))
        poste.place(x=630,y=55)
        #optp=["Student","Teacher","Professor","DR"]
        #self.post_ent=StringVar(root)
        #self.post_ent.set("SELECT")
        #listpm=OptionMenu(self.deframe,self.post_ent,*optp)
        #listpm.place(x=630,y=55,width=150)

        #--Achievements
        Achievements=Label(self.deframe,text="Achievements :",font=("times new roman",15,"bold"),fg="white",bg="#1877f2",bd=3).place(x=630,y=180)
        self.Achievementse=ttk.Entry(self.deframe,textvariable=self.ach_ent,font=("times new roman",15,"bold"))
        self.Achievementse.place(x=630,y=215)

        #--csc
        csc=Label(self.deframe,text="Country,State,City :",font=("times new roman",15,"bold"),fg="white",bg="#1877f2",bd=3).place(x=630,y=285)
        self.csce=ttk.Entry(self.deframe,textvariable=self.csc_ent,font=("times new roman",15,"bold"))
        self.csce.place(x=630,y=320)

        #--Email
        Email=Label(self.deframe,text="Email :",font=("times new roman",15,"bold"),fg="white",bg="#1877f2",bd=3).place(x=940,y=20)
        self.Emaile=ttk.Entry(self.deframe,textvariable=self.email_ent,font=("times new roman",15,"bold"))
        self.Emaile.place(x=940,y=55)

        #--Hobby
        intrests=Label(self.deframe,text="Intrests/Hobby :",font=("times new roman",15,"bold"),fg="white",bg="#1877f2",bd=3).place(x=940,y=110)
        self.intrestse=ttk.Entry(self.deframe,textvariable=self.hobby_ent,font=("times new roman",15,"bold"))
        self.intrestse.place(x=940,y=145)

        #buttonframe and buttons ******************
        btnframe=Frame(self.deframe,relief=RIDGE,bd=10)
        btnframe.place(x=940,y=200,width=350,height=180)

        b1=Button(btnframe,text="Save",fg="white",bg="blue",command=self.save,activebackground="blue",activeforeground="white",bd=4,
                    font=("times new roman",18,"bold"))
        b1.place(x=10,y=10,width=145,height=45)

        b2=Button(btnframe,text="Update",fg="white",bg="blue",activebackground="blue",activeforeground="white",bd=4,
                    font=("times new roman",18,"bold"))
        b2.place(x=170,y=10,width=145,height=45)

        b3=Button(btnframe,text="Delete",fg="white",bg="blue",activebackground="blue",activeforeground="white",bd=4,
                    font=("times new roman",18,"bold"))
        b3.place(x=10,y=60,width=145,height=45)

        b4=Button(btnframe,text="Reset",fg="white",bg="blue",activebackground="blue",activeforeground="white",bd=4,
                    font=("times new roman",18,"bold"))
        b4.place(x=170,y=60,width=145,height=45)

        b5=Button(btnframe,text="Exit",fg="white",bg="blue",activebackground="blue",activeforeground="white",bd=4,
                    font=("times new roman",18,"bold"))
        b5.place(x=60,y=110,width=210,height=45)

        #dataframe ******************
        dataframe=LabelFrame(self.root,text="Stored Resumes",font=("times new roman",15,"bold"),fg="blue",relief=RIDGE,bd=15)
        dataframe.place(x=5,y=440,width=1350,height=263)

        #   Scrollbar
        scrollx=ttk.Scrollbar(dataframe,orient=HORIZONTAL)
        scrolly=ttk.Scrollbar(dataframe,orient=VERTICAL)
        self.info_table=ttk.Treeview(dataframe,column=("name","gender","age",
                                    "qualification","post","languages","workexp","achievements","csc","email","hobby"
                                    ),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)

        scrollx=ttk.Scrollbar(command=self.info_table.xview)
        scrolly=ttk.Scrollbar(command=self.info_table.yview)

        self.info_table.heading("name",text="Name")
        self.info_table.heading("gender",text="Gender")
        self.info_table.heading("age",text="Age")
        self.info_table.heading("qualification",text="Qualification")
        self.info_table.heading("post",text="Post")
        self.info_table.heading("workexp",text="Working Experience")
        self.info_table.heading("languages",text="Languages known")
        self.info_table.heading("achievements",text="Achievements")
        self.info_table.heading("hobby",text="Hobby")
        self.info_table.heading("csc",text="Contry,State,City")
        self.info_table.heading("email",text="Email")

        self.info_table["show"]="headings"

        self.info_table.column("name",width=100)
        self.info_table.column("gender",width=100)
        self.info_table.column("age",width=100)
        self.info_table.column("qualification",width=100)
        self.info_table.column("post",width=100)
        self.info_table.column("workexp",width=100)
        self.info_table.column("languages",width=100)
        self.info_table.column("achievements",width=100)
        self.info_table.column("hobby",width=100)
        self.info_table.column("csc",width=100)
        self.info_table.column("email",width=100)

        self.info_table.pack(fill=BOTH,expand=1)
        self.fetchdata()



    def save(self):
        if self.name_ent.get()=="" or self.age_ent.get()=="":
            messagebox.showerror("error!","Fill all Entries")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="mysql",database="hireme")
            cur=conn.cursor()
            cur.execute("insert into data values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                
                                                                                                        self.name_ent.get(),
                                                                                                        self.gen_ent.get(),
                                                                                                        self.age_ent.get(),
                                                                                                        self.quali_ent.get(),
                                                                                                        self.post_ent.get(),
                                                                                                        self.workexp_ent.get(),
                                                                                                        self.lang_ent.get(),
                                                                                                        self.ach_ent.get(),
                                                                                                        self.hobby_ent.get(),
                                                                                                        self.csc_ent.get(),
                                                                                                        self.email_ent.get(),
                                                                                
                                                                                                        ))

            
            conn.commit()
            self.fetchdata()
            conn.close() 
            messagebox.showinfo("Success","Record has been Saved !")  

    def fetchdata(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="mysql",database="hireme")
        cur=conn.cursor()
        cur.execute("select * from data")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.info_table.delete(*self.info_table.get_children())
            for i in rows:
                self.info_table.insert("",END,values=i)
            conn.commit()
        conn.close()
            

root = Tk()
app = data_display(root)
root.mainloop()




'''
        def hm(self):
        self.new_win=Toplevel()
        self.obj=main_win.RecruitmentSystem(self.new_win)
        '''

'''

        #Submit and home
        b1=Button(self.deframe,text="Submit",font=("monaco",22,"bold"),fg="white",bg="blue",activebackground="blue",activeforeground="white",bd=6)
        b1.place(x=920,y=595)
        b2=Button(self.deframe,text="Home",command=self.hm,font=("monaco",22,"bold"),fg="blue",bg="white",activebackground="white",activeforeground="blue",bd=6)
        b2.place(x=1100,y=595)
        b3=Button(self.deframe,text="Show Resume",command=self.dd,font=("monaco",20,"bold"),fg="black",bg="yellow",activebackground="yellow",activeforeground="black",bd=6)
        b3.place(x=1110,y=10)
'''