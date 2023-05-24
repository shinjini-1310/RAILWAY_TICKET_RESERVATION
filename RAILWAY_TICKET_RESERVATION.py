#!/usr/bin/env python
# coding: utf-8

# In[4]:


from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
from tkinter import ttk
import pymysql
import random

class Login:
    

   def __init__(self,root):

      self.root=root

      self.root.title("IRCTC Portal")

      self.root.geometry("1200x1000+0+0")

      self.loginform()
        
      

   def loginform(self):

      Frame_login=Frame(self.root,bg="white")

      Frame_login.place(x=0,y=0,height=700,width=1366)

      

      self.img=ImageTk.PhotoImage(file="C:\\Users\\SHINJINI\\FINAL YEAR PROJECT\\train.png")

      img=Label(Frame_login,image=self.img).place(x=0,y=0,width=1366,height=700)

      
      frame_input=Frame(self.root,bg='white')

      frame_input.place(x=320,y=130,height=450,width=350)



      label1=Label(frame_input,text="Login Here",font=('impact',32,'bold'),

                   fg="black",bg='white')

      label1.place(x=75,y=20)



      label2=Label(frame_input,text="Username",font=("Goudy old style",20,"bold"),

                   fg='orangered',bg='white')

      label2.place(x=30,y=95)

      self.email_txt=Entry(frame_input,font=("times new roman",15,"bold"),

                       bg='lightgray')

      self.email_txt.place(x=30,y=145,width=270,height=35)

      

      label3=Label(frame_input,text="Password",font=("Goudy old style",20,"bold"),

                   fg='orangered',bg='white')

      label3.place(x=30,y=195)

      self.password=Entry(frame_input,font=("times new roman",15,"bold"),

                        bg='lightgray')

      self.password.place(x=30,y=245,width=270,height=35)


      btn2=Button(frame_input,text="Login",command=self.login,cursor="hand2",

                  font=("times new roman",15),fg="white",bg="orangered",

                  bd=0,width=15,height=1)

      btn2.place(x=90,y=340)

        

      btn3=Button(frame_input,command=self.Register,text="Not Registered?Register"

                  ,cursor="hand2",font=("calibri",10),bg='white',fg="black",bd=0)

      btn3.place(x=110,y=390)



   def login(self):

      if self.email_txt.get()=="" or self.password.get()=="":

         messagebox.showerror("Error","All fields are required",parent=self.root)

      else:

         try:

            con=pymysql.connect(host='localhost',user='root',password='',

                                database='pythongui')

            cur=con.cursor()

            cur.execute('select * from register where username=%s and password=%s'

                        ,(self.email_txt.get(),self.password.get()))
            

            row=cur.fetchone()

            if row==None:

               messagebox.showerror('Error','Invalid Username And Password'

                                    ,parent=self.root)

               self.loginclear()

               self.email_txt.focus()

            else:

               self.appscreen()

               con.close()

         except Exception as es:

            messagebox.showerror('Error',f'Error Due to : {str(es)}',parent=self.root)
            

   def Register(self):
    

      Frame_login1=Frame(self.root,bg="white")

      Frame_login1.place(x=0,y=0,height=700,width=1366)

      

      self.img=ImageTk.PhotoImage(file="C:\\Users\\SHINJINI\\FINAL YEAR PROJECT\\train.png")

      img=Label(Frame_login1,image=self.img).place(x=0,y=0,width=1366,height=700)

      

      frame_input2=Frame(self.root,bg='white')

      frame_input2.place(x=320,y=130,height=450,width=630)



      label1=Label(frame_input2,text="Register Here",font=('impact',32,'bold'),

                   fg="black",bg='white')

      label1.place(x=45,y=20)



      label2=Label(frame_input2,text="Username",font=("Goudy old style",20,"bold"),

                   fg='orangered',bg='white')

      label2.place(x=30,y=95)

      self.entry=Entry(frame_input2,font=("times new roman",15,"bold"),

                       bg='lightgray')

      self.entry.place(x=30,y=145,width=270,height=35)

      

      label3=Label(frame_input2,text="Password",font=("Goudy old style",20,"bold"),

                   fg='orangered',bg='white')

      label3.place(x=30,y=195)

      self.entry2=Entry(frame_input2,font=("times new roman",15,"bold"),

                        bg='lightgray')

      self.entry2.place(x=30,y=245,width=270,height=35)



      label4=Label(frame_input2,text="Email-id",font=("Goudy old style",20,"bold"),

                   fg='orangered',bg='white')

      label4.place(x=330,y=95)

      self.entry3=Entry(frame_input2,font=("times new roman",15,"bold"),

                       bg='lightgray')

      self.entry3.place(x=330,y=145,width=270,height=35)



      label5=Label(frame_input2,text="Confirm Password",

                   font=("Goudy old style",20,"bold"),fg='orangered',bg='white')

      label5.place(x=330,y=195)

      self.entry4=Entry(frame_input2,font=("times new roman",15,"bold"),

                       bg='lightgray')

      self.entry4.place(x=330,y=245,width=270,height=35)



      btn2=Button(frame_input2,command=self.register,text="Register"

                  ,cursor="hand2",font=("times new roman",15),fg="white",

                  bg="orangered",bd=0,width=15,height=1)

      btn2.place(x=90,y=340)

        

      btn3=Button(frame_input2,command=self.loginform,

                  text="Already Registered?Login",cursor="hand2",

                  font=("calibri",10),bg='white',fg="black",bd=0)

      btn3.place(x=110,y=390)



   def register(self):

      if self.entry.get()==""or self.entry2.get()==""or self.entry3.get()==""or self.entry4.get()=="":

         messagebox.showerror("Error","All Fields Are Required",parent=self.root)

      elif self.entry2.get()!=self.entry4.get():

         messagebox.showerror("Error","Password and Confirm Password Should Be Same"

                              ,parent=self.root)

      else:

         try:

            con=pymysql.connect(host="localhost",user="root",password='',

                                database="pythongui")

            cur=con.cursor()

            cur.execute("select * from register where emailid=%s"

                        ,self.entry3.get())

            row=cur.fetchone()

            if row!=None:

               messagebox.showerror("Error"

               ,"User already Exist,Please try with another Email"

                                    ,parent=self.root)

               self.regclear()

               self.entry.focus()

            else:

               cur.execute("insert into register values(%s,%s,%s,%s)"

                           ,(self.entry.get(),self.entry3.get(),

                           self.entry2.get(),

                           self.entry4.get()))

               con.commit()

               con.close()

               messagebox.showinfo("Success","Register Successful"

                                   ,parent=self.root)

               self.regclear()

         except Exception as es:

            messagebox.showerror("Error",f"Error due to:{str(es)}"

                                 ,parent=self.root)

            
   def put(self):
    
    if self.nm.get()=="" or self.a.get()=="" or self.des.get()=="" or self.pas.get()=="" or self.cl.get()=="" :

         messagebox.showerror("Error","All Fields Are Required",parent=self.root)


    else:
        
        try:
            
            #arrival and departure
            if self.des.get()=='Jammu' : 
                self.arrival='11:00 AM'
                self.departure='11:40 AM'
            else :
                self.arrival='11:30 AM'
                self.departure='12:10 PM'
            
            #pnrno
            self.name=self.nm.get()
            self.l=self.name.split(" ")
            #print(self.l)
            self.pnr_no=str(random.randint(1000,9999))+self.l[1][0].upper()+self.l[0][:2].upper()
            
            #train number 
            if self.des.get()=='Jammu' : self.train_no='JN00'
            else : self.train_no='GN00'
            
            #no of passengers
            self.n=self.pas.get()
            try : self.n=int(self.n)
            except ValueError as ve : self.n=1
                
            #fare incurred by the traveller
            if self.cl.get()=='AC1':
                if self.train_no=='JN00': self.amt=self.n*8000
                else : self.amt=self.n*6000

            elif self.cl.get()=='AC2':
                if self.train_no=='JN00': self.amt=self.n*4000
                else : self.amt=self.n*3000

            elif self.cl.get()=='AC3':
                if self.train_no=='JN00': self.amt=self.n*2000
                else : self.amt=self.n*1500

            elif self.cl.get()=='SLP':
                if self.train_no=='JN00': self.amt=self.n*1000
                else : self.amt=self.n*750


            con=pymysql.connect(host="localhost",user="root",password='',

                                database="railways")

            cur=con.cursor()

            cur.execute("insert into passengers values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                           ,(self.nm.get(),self.a.get(),self.train_no,self.pas.get(),self.cl.get(),self.des.get(),self.arrival,
                        self.departure,self.amt,'CONF',self.pnr_no))

            con.commit()
            con.close()

            messagebox.showinfo("Success","Ticket Reservation Successful\n PNR ID : "+str(self.pnr_no),parent=self.root)

            self.apclear()

        except Exception as es:

            messagebox.showerror("Error",f"Error due to :{str(es)}",parent=self.root)
            
            
   
   def apclear(self):

    self.nm.delete(0,END)

    self.a.delete(0,END)

    self.des.delete(0,END)

    self.pas.delete(0,END)
    
    self.cl.delete(0,END)
    
    
   def add_passenger(self):
    
    frame_ap=Frame(self.root,bg="white")

    frame_ap.place(x=0,y=0,height=700,width=1360)
    
    name=Label(frame_ap,text="Name").grid(row=0,column=0)
    age=Label(frame_ap,text="Age").grid(row=20,column=0)
    des=Label(frame_ap,text="Destination").grid(row=40,column=0)
    no_of_pas=Label(frame_ap,text="No of Passengers").grid(row=60,column=0)
    cls=Label(frame_ap,text="Class").grid(row=80,column=0)

    #passenger name
    self.nm=Entry(frame_ap)
    self.nm.grid(row=0,column=8)
    
    #passenger age
    self.a=Entry(frame_ap)
    self.a.grid(row=20,column=8)
    
    #destination
    self.des=ttk.Combobox(frame_ap,width = 15,values=('Jammu','Goa'))
    #self.des['values']=('Jammu','Goa')
    self.des.grid(row=40,column=8)
    
    
    #status of travel
    self.status='CONF'
    
    #number of passengers
    self.pas=Entry(frame_ap)
    self.pas.grid(row=60,column=8)
    
    
    #choice of class
    self.cl=ttk.Combobox(frame_ap, width = 8,values=('AC1','AC2','AC3','SLP'))
    #self.cl['values']=('AC1','AC2','AC3','SLP')
    self.cl.grid(row=80,column=8)
    
    
    btn=Button(frame_ap,command=self.put,text="Submit",cursor="hand2",font=("times new roman",15),fg="white",

                  bg="orangered",bd=0,width=8,height=1)

    btn.grid(row=9000,column=8)
    
    
   def show_traindetails(self):
    
    
    frame_td=Frame(self.root,bg="white")

    frame_td.place(x=0,y=0,height=700,width=1400)
     
 
    con=pymysql.connect(host="localhost",user="root",password='',database="railways")
    cur=con.cursor()

    cur.execute("select * from trainsdetail;")
    records = cur.fetchall()
    print(*records,sep="\n")

    cols = ('Train Name','Train ID','Source','Destination','Arrival','Departure','AC1 Fare','AC2 Fare',
            'AC3 Fare','Sleeper Fare')
    
    tree = ttk.Treeview(frame_td)
    tree['show']='headings'
    
    s=ttk.Style(frame_td)
    s.theme_use("clam")
    s.configure("Treeview.Heading",background='yellow')
    
    tree['columns']=['tname','tnum','source','destination','arrival','departure','ac1','ac2','ac3','slp']
    
    tree.column('tname',width=60)
    tree.column('tnum',width=60)
    tree.column('source',width=60)
    tree.column('destination',width=60)
    tree.column('arrival',width=60)
    tree.column('departure',width=60)
    tree.column('ac1',width=60)
    tree.column('ac2',width=60)
    tree.column('ac3',width=60)
    tree.column('slp',width=60)
    
    tree.heading('tname',text='Train Name',anchor="c")
    tree.heading('tnum',text='Train ID',anchor="c")
    tree.heading('source',text='Source',anchor="c")
    tree.heading('destination',text='Destination',anchor="c")
    tree.heading('arrival',text='Arrival',anchor="c")
    tree.heading('departure',text='Departure',anchor="c")
    tree.heading('ac1',text='AC1 Fare',anchor="c")
    tree.heading('ac2',text='AC2 Fare',anchor="c")
    tree.heading('ac3',text='AC3 Fare',anchor="c")
    tree.heading('slp',text='Sleeper Fare',anchor="c")
    
    
    for i, (tname,tnum,source,destination,arrival,departure,ac1,ac2,ac3,slp) in enumerate(records, start=1):
        tree.insert("", "end", values=(tname,tnum,source,destination,arrival,departure,ac1,ac2,ac3,slp))
    
    hsb=ttk.Scrollbar(frame_td,orient="horizontal")
    hsb.configure(command=tree.xview)
    tree.configure(xscrollcommand=hsb.set)
    hsb.pack(fill=X,side=BOTTOM)
    
    tree.pack(fill=BOTH, expand=1)
    
        
   def disp_pnrno(self):
    
    frame_pnr=Frame(self.root,bg="white")

    frame_pnr.place(x=0,y=0,height=700,width=1400)
     
 
    con=pymysql.connect(host="localhost",user="root",password='',database="railways")
    cur=con.cursor()

    cur.execute("select pnrno,train_no,no_of_pas,cl,destination,arrival,departure,amt,status from passengers")
    records = cur.fetchall()
    print(*records,sep="\n")

    tree = ttk.Treeview(frame_pnr)
    tree['show']='headings'
    
    s=ttk.Style(frame_pnr)
    s.theme_use("clam")
    s.configure("Treeview.Heading",background='#ff6666')
    
    tree['columns']=['pnrno','train_no','no_of_pas','cl','destination','arrival','departure','amt','status']
    
    tree.column('pnrno',width=60)
    tree.column('train_no',width=60)
    tree.column('no_of_pas',width=60)
    tree.column('cl',width=60)
    tree.column('destination',width=60)
    tree.column('arrival',width=60)
    tree.column('departure',width=60)
    tree.column('amt',width=60)
    tree.column('status',width=60)
  
    
    tree.heading('pnrno',text='PNR No',anchor="c")
    tree.heading('train_no',text='Train No',anchor="c")
    tree.heading('no_of_pas',text='Passengers',anchor="c")
    tree.heading('cl',text='Class',anchor="c")
    tree.heading('destination',text='Destination',anchor="c")
    tree.heading('arrival',text='Arrival',anchor="c")
    tree.heading('departure',text='Departure',anchor="c")
    tree.heading('amt',text='Amount',anchor="c")
    tree.heading('status',text='Status',anchor="c")
    
    for i, (pnrno,train_no,no_of_pas,cl,destination,arrival,departure,amt,status) in enumerate(records, start=1):
        tree.insert("", "end", values=(pnrno,train_no,no_of_pas,cl,destination,arrival,departure,amt,status))
        
    hsb=ttk.Scrollbar(frame_pnr,orient="horizontal")
    hsb.configure(command=tree.xview)
    tree.configure(xscrollcommand=hsb.set)
    hsb.pack(fill=X,side=BOTTOM)
    
    tree.pack(fill=BOTH, expand=1)
    
        
   def pnrclear(self): self.en.delete(0,END)
        
        
   def cancelling(self):
        
    if self.en.get()=="": messagebox.showerror("Error","Please Enter Your PNR No !",parent=self.root)


    else:
        
        try:

            con=pymysql.connect(host="localhost",user="root",password='',

                                database="railways")

            cur=con.cursor()
            
            pnr_no=self.en.get()
            
            qry=up_str="update passengers set status='CANC' where pnrno='"+pnr_no+"';"

            cur.execute(qry)

            con.commit()

            con.close()

            messagebox.showinfo("Success","Ticket Cancellation Successful",parent=self.root)

            self.pnrclear()

        except Exception as es:  messagebox.showerror("Error",f"Error due to:{str(es)}",parent=self.root)
        
        
   def cancel(self):
    
    
    frame_ct=Frame(self.root,bg="Light Blue")

    frame_ct.place(x=0,y=0,height=700,width=1360)
    
    Label(frame_ct,text="Enter PNR Number : ",font=('Calibri',32,'bold'),fg="black",bg='white').place(x=25,y=100)
    
    self.en = Entry(frame_ct, width=18,fg='purple',bg='yellow') 
    self.en.place(x=500,y=125)
    
    btn=Button(frame_ct,text="Cancel Reservation",command=self.cancelling,font=("Calibri",12),fg="black",bg="orangered",
               bd=0,width=15,height=1)

    btn.place(x=590,y=160)
    
        

   def appscreen(self):

    
    Frame_login=Frame(self.root,bg="white")

    Frame_login.place(x=0,y=0,height=700,width=1366)

    label1=Label(Frame_login,text="Hi! Welcome To IRCTC"

               ,font=('times new roman',32,'bold'),

               fg="black",bg='white')

    label1.place(x=375,y=100)

    label2=Label(Frame_login,text="Kindly enter your choice :"

               ,font=('times new roman',32,'bold'),

               fg="black",bg='white')

    label2.place(x=375,y=160)


    btn_rt=Button(Frame_login,text="Reserve Your Ticket",command=self.add_passenger,cursor="hand2",

              font=("times new roman",15),fg="white",bg="orangered",

              bd=0,width=25,height=1)

    btn_rt.place(x=25, y=350)


    btn_td=Button(Frame_login,text="Show Train Details",command=self.show_traindetails,cursor="hand2",

              font=("times new roman",15),fg="white",bg="orangered",

              bd=0,width=15,height=1)

    btn_td.place(x=400, y=350)


    btn_pnr=Button(Frame_login,text="Show PNR Status",command=self.disp_pnrno,cursor="hand2",

              font=("times new roman",15),fg="white",bg="orangered",

              bd=0,width=15,height=1)

    btn_pnr.place(x=650, y=350)


    btn_ct=Button(Frame_login,text="Cancel Ticket",command=self.cancel,cursor="hand2",

              font=("times new roman",15),fg="white",bg="orangered",

              bd=0,width=15,height=1)

    btn_ct.place(x=900, y=350)


    btn2=Button(Frame_login,text="Logout",command=self.loginform,cursor="hand2",

              font=("times new roman",15),fg="white",bg="orangered",

              bd=0,width=15,height=1)

    btn2.place(x=650,y=1200)


   def regclear(self):

      self.entry.delete(0,END)

      self.entry2.delete(0,END)

      self.entry3.delete(0,END)

      self.entry4.delete(0,END)


   def loginclear(self):

      self.email_txt.delete(0,END)

      self.password.delete(0,END)

root=Tk()

ob=Login(root)

root.mainloop()


# In[ ]:




