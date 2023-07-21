from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
import random
import mysql.connector
from tkinter import messagebox



class Customer_win:
   def __init__(self,root):
      self.root=root
      self.root.title("Hotel Management System")
      self.root.geometry("1295x555+232+224")


      #===============variables=================
      self.var_ref=StringVar()
      x=random.randint(1000,9999)
      self.var_ref.set(str(x))

   

      self.var_custo_name=StringVar()
      self.var_mother=StringVar()
      self.var_gender=StringVar()
      self.var_post=StringVar()
      self.var_mobile=StringVar()
      self.var_email=StringVar()
      self.var_nationality=StringVar()
      self.var_id_proof=StringVar()
      self.var_id_number=StringVar()



      #================title========================
      lbl_title=Label(self.root,text="ADD CUSTOMER DETAILS ", font=("Arial",18,"bold"),bg="black" ,fg="gold")
      lbl_title.place(x=0,y=0,width=1295,height=50)

      #================logo========================
      img2=Image.open(r"C:\Users\91790\Desktop\hotel\hotel images\logohotel.png")
      img2=img2.resize((100,40),Image.ANTIALIAS)
      self.photoimg2=ImageTk.PhotoImage(img2)
      lblimg=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
      lblimg.place(x=5,y=2,width=100,height=40)

      #===============LABEL FRAME======================
      LabelFrameleft=LabelFrame(self.root, bd=2,relief=RIDGE,text="Customer Details",font=("Arial",12,"bold"), padx=2)
      LabelFrameleft.place(x=5,y=50,width=425,height=490)

      #customer reference
      lbl_cust_ref=Label(LabelFrameleft,text="Customer Reference",font=("Arial",12,"bold"), padx=2,pady=6)
      lbl_cust_ref.grid(row=0, column=0,sticky=W)
      

      entry_ref=ttk.Entry(LabelFrameleft,textvariable=self.var_ref,width=29,font=("Arial",13,"bold"),state="disabled" )
      entry_ref.grid(row=0, column=1)

     #customer name
      cname=Label(LabelFrameleft,text="Customer Name",font=("Arial",12,"bold"), padx=2,pady=6 )
      cname.grid(row=1, column=0,sticky=W)

      txtcname=ttk.Entry(LabelFrameleft,textvariable=self.var_custo_name,width=29,font=("Arial",13,"bold"))
      txtcname.grid(row=1, column=1)

     #motherr name
      mname=Label(LabelFrameleft,text="Mother's Name",font=("Arial",12,"bold"), padx=2,pady=6 )
      mname.grid(row=2, column=0,sticky=W)

      txtmname=ttk.Entry(LabelFrameleft,textvariable=self.var_mother,width=29,font=("Arial",13,"bold"))
      txtmname.grid(row=2, column=1)

     #gender combobox
      gender=Label(LabelFrameleft,text="Gender",font=("Arial",12,"bold"), padx=2,pady=6 )
      gender.grid(row=3, column=0,sticky=W)
      combo_gender=ttk.Combobox(LabelFrameleft,textvariable=self.var_gender,font=("Arial",12,"bold"),width=27) 
      combo_gender['state']='readonly'
      combo_gender["value"]=("Male","Female","Others")
      combo_gender.current(0)
      combo_gender.grid(row=3, column=1)                  

     #postcode
      postno=Label(LabelFrameleft,text="Postcode",font=("Arial",12,"bold"), padx=2,pady=6 )
      postno.grid(row=4, column=0,sticky=W)

      txtpno=ttk.Entry(LabelFrameleft,textvariable=self.var_post,width=29,font=("Arial",13,"bold"))
      txtpno.grid(row=4, column=1)

     #mobile no
      phno=Label(LabelFrameleft,text="Phone Number",font=("Arial",12,"bold"), padx=2,pady=6 )
      phno.grid(row=5, column=0,sticky=W)

      txtph_no=ttk.Entry(LabelFrameleft,textvariable=self.var_mobile,width=29,font=("Arial",13,"bold"))
      txtph_no.grid(row=5, column=1) 

     #email
      mail=Label(LabelFrameleft,text="Email : ",font=("Arial",12,"bold"), padx=2,pady=6 )
      mail.grid(row=6, column=0,sticky=W)

      txtmail=ttk.Entry(LabelFrameleft,textvariable=self.var_email,width=29,font=("Arial",13,"bold"))
      txtmail.grid(row=6, column=1)   

     #nationality
      nat=Label(LabelFrameleft,text="Nationality",font=("Arial",12,"bold"), padx=2,pady=6 )
      nat.grid(row=7, column=0,sticky=W)
      combo_nat=ttk.Combobox(LabelFrameleft,textvariable=self.var_nationality,font=("Arial",12,"bold"),width=27)
      combo_nat['state']='readonly'
      combo_nat["value"]=("Indian","Russian","Japanese","British","Others")
      combo_nat.current(0)
      combo_nat.grid(row=7, column=1) 

     #id proof type combobox
      lblidproof=Label(LabelFrameleft,text="ID Proof Type: ",font=("Arial",12,"bold"), padx=2,pady=6 )
      lblidproof.grid(row=8, column=0,sticky=W)

      combo_lblidproof=ttk.Combobox(LabelFrameleft,textvariable=self.var_id_proof,font=("Arial",12,"bold"),width=27)
      combo_lblidproof['state']='readonly'
      combo_lblidproof["value"]=("Aadhar Card","Driving License","PAN card","Others")
      combo_lblidproof.current(0)
      combo_lblidproof.grid(row=8, column=1) 

     #id number
      lblidno=Label(LabelFrameleft,text="ID Number",font=("Arial",12,"bold"), padx=2,pady=6 )
      lblidno.grid(row=9, column=0,sticky=W)

      lblidno_=ttk.Entry(LabelFrameleft,textvariable=self.var_id_number,width=29,font=("Arial",13,"bold"))
      lblidno_.grid(row=9, column=1)


      #===================btns================================
      btn_frame=Frame(LabelFrameleft,bd=2,relief=RIDGE)
      btn_frame.place(x=0,y=400,width=412,height=40)

      btnadd=Button(btn_frame,text="Add",command=self.add_data, font=("Arial",11,"bold"),bg="black",fg="gold",width=10)
      btnadd.grid(row=0,column=0,padx=1)

      btnupdate=Button(btn_frame,text="Update", font=("Arial",11,"bold"),bg="black",fg="gold",width=10)
      btnupdate.grid(row=0,column=1,padx=1)

      btndelete=Button(btn_frame,text="Delete", font=("Arial",11,"bold"),bg="black",fg="gold",width=10)
      btndelete.grid(row=0,column=2,padx=1)

      btnreset=Button(btn_frame,text="Reset", font=("Arial",11,"bold"),bg="black",fg="gold",width=10)
      btnreset.grid(row=0,column=3,padx=1)

      #==================table frame===============================
      Tabel_Frame=LabelFrame(self.root, bd=2,relief=RIDGE,text="View Details and Search System",font=("Arial",12,"bold"), padx=2)
      Tabel_Frame.place(x=437,y=50,width=860,height=490)

      lblsearchby=Label(Tabel_Frame,text="Search By: ",font=("Arial",12,"bold"), bg="red",fg="white")
      lblsearchby.grid(row=0, column=0,sticky=W,padx=2)

      combo_Search=ttk.Combobox(Tabel_Frame,font=("Arial",12,"bold"),width=24)
      combo_Search['state']='readonly'
      combo_Search["value"]=("Mobile Number","Reference")
      combo_Search.current(0)
      combo_Search.grid(row=0, column=1,padx=2) 

      textsearch=ttk.Entry(Tabel_Frame,font=("Arial",13,"bold"),width=24)
      textsearch.grid(row=0, column=2,padx=2)

      btnSearch=Button(Tabel_Frame,text="Search", font=("Arial",11,"bold"),bg="black",fg="gold",width=10)
      btnSearch.grid(row=0,column=3,padx=1)

      btnshowall=Button(Tabel_Frame,text="Update", font=("Arial",11,"bold"),bg="black",fg="gold",width=10)
      btnshowall.grid(row=0,column=4,padx=1)


      #=========================== show data table============================
      details_table=Frame(Tabel_Frame,bd=2,relief=RIDGE)
      details_table.place(x=0,y=50,width=860,height=350)

      scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
      scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)
      

      self.Customer_Details_table=ttk.Treeview(details_table,columns=("ref","name","mother","gender",
                                                                      "post","mobile","email","nationality","idproof","idnumber"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
      scroll_x.pack(side=BOTTOM,fill=X)
      scroll_y.pack(side=RIGHT,fill=Y)
      

      scroll_x.config(command=self.Customer_Details_table.xview)
      scroll_y.config(command=self.Customer_Details_table.yview)
      

      self.Customer_Details_table.heading("ref",text="Refer No")
      self.Customer_Details_table.heading("name",text="Name")
      self.Customer_Details_table.heading("mother",text="Mother's Name")
      self.Customer_Details_table.heading("gender",text="Gender")
      self.Customer_Details_table.heading("post",text="Postcode")
      self.Customer_Details_table.heading("mobile",text="Mobile No")
      self.Customer_Details_table.heading("email",text="Email")
      self.Customer_Details_table.heading("nationality",text="Nationality")
      self.Customer_Details_table.heading("idproof",text="ID proof")
      self.Customer_Details_table.heading("idnumber",text="ID Number")
      
      self.Customer_Details_table["show"]="headings"
      

      self.Customer_Details_table.column("ref",width=100)
      self.Customer_Details_table.column("name",width=100)
      self.Customer_Details_table.column("mother",width=100)
      self.Customer_Details_table.column("gender",width=100)
      self.Customer_Details_table.column("post",width=100)
      self.Customer_Details_table.column("mobile",width=100)
      self.Customer_Details_table.column("email",width=100)
      self.Customer_Details_table.column("nationality",width=100)
      self.Customer_Details_table.column("idproof",width=100)
      self.Customer_Details_table.column("idnumber",width=100)

      self.Customer_Details_table.pack(fill=BOTH,expand=1)
      self.fetch_data( )




   def add_data(self):
      if self.var_mobile.get()=="" or self.var_mother.get()=="":
         messagebox.showerror("Error","All Fields are Required")
      else:
         try:
            conn=mysql.connector.connect(host="localhost",username="root",password="Suraj@123",database="hotel")
            my_cursor=conn.cursor()
            my_cursor.execute("insert into customer_entry values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                              self.var_ref.get(),
                                                              self.var_custo_name.get(),
                                                              self.var_mother.get(),
                                                              self.var_gender.get(),
                                                              self.var_post.get(),
                                                              self.var_mobile.get(),
                                                              self.var_email.get(),
                                                              self.var_nationality.get(),
                                                              self.var_id_proof.get(),
                                                              self.var_id_number.get()
                                                              ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Success","Customer has been successfully added",parent=self.root)
         except Exception as es:
            messagebox.showwarning("Warning",f"Something went Wrong:{str(es)}",parent=self.root)


   def fetch_data(self):
      conn=mysql.connector.connect(host="localhost",username="root",password="Suraj@123",database="hotel")
      my_cursor=conn.cursor()
      my_cursor.execute("Select * from customer_entry")
      rows=my_cursor.fetchall()
      if len(rows)!=0:
         self.Customer_Details_table.delete(*self.Customer_Details_table.get_children())
         for i in rows:
            self.Customer_Details_table.insert("",END,values=i)
         conn.commit()
      conn.close()   

   def get_cursor(self,event=""):
      cursor_row=self.Customer_Details_table.focus()
      content=self.Customer_Details_table.item(cursor_row)
      row=content["values"]
      
         

   
          
                                                                                          


      



 



if __name__ =="__main__":
    root=Tk()
    obj=Customer_win(root)
    root.mainloop()























