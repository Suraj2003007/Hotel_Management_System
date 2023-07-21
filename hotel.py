from tkinter import *
from PIL import Image,ImageTk
from customer import Customer_win



class HotelManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry('1550x800+0+0')
        self.root.minsize(width=600,height=300)



        #================1st image========================
        img1=Image.open(r"C:\Users\91790\Desktop\hotel\hotel images\hotel1.png")
        img1=img1.resize((1550,140),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
 
        lblimg=Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=1550,height=140)

        
        #================logo========================
        img2=Image.open(r"C:\Users\91790\Desktop\hotel\hotel images\logohotel.png")
        img2=img2.resize((230,140),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg=Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=230,height=140)

        #================title========================
        lbl_title=Label(self.root,text="HOTEL MANAGEMENT SYSTEM ", font=("Arial",40,"bold"),bg="black" ,fg="gold")
        lbl_title.place(x=0,y=140,width=1550,height=50)


        #================Main Frame========================
        main_frame=Frame(self.root,bd=4,relief=RIDGE)
        main_frame.place(x=0,y=190,width=1550,height=620)
        

        #================Menu========================
        lbl_menu=Label(main_frame,text="MENU ", font=("Arial",20,"bold"),bg="brown" ,fg="orange",bd=4,relief=RIDGE)
        lbl_menu.place(x=0,y=0,width=232)
    
        #================Btn frame========================
        btn_frame=Frame(main_frame,bd=4,relief=RIDGE)
        btn_frame.place(x=0,y=35,width=232,height=190)
     
     
        cust_btn=Button(btn_frame,text="CUSTOMER",command=self.cust_details, width=20,font=("Arial",14,"bold"),bg="black" ,fg="gold" , bd=0,cursor="hand2")
        cust_btn.grid(row=0,column=0,pady=1)
     
        room_btn=Button(btn_frame,text="ROOM",width=20,font=("Arial",14,"bold"),bg="black" ,fg="gold" , bd=0,cursor="hand2")
        room_btn.grid(row=1,column=0,pady=1)
     
        details_btn=Button(btn_frame,text="DETAILS",width=20,font=("Arial",14,"bold"),bg="black" ,fg="gold" , bd=0,cursor="hand2")
        details_btn.grid(row=2,column=0,pady=1)
     
        report_btn=Button(btn_frame,text="REPORT",width=20,font=("Arial",14,"bold"),bg="black" ,fg="gold" , bd=0,cursor="hand2")
        report_btn.grid(row=3,column=0,pady=1)
     
        logout_btn=Button(btn_frame,text="LOGOUT",width=20,font=("Arial",14,"bold"),bg="black" ,fg="gold" , bd=0,cursor="hand2")
        logout_btn.grid(row=4,column=0,pady=1)
     
        #================RIGHTSIDE IMAGE========================
        img3=Image.open(r"C:\Users\91790\Desktop\hotel\hotel images\slide3.jpg")
        img3=img3.resize((1310,590),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        lblimg1=Label(main_frame,image=self.photoimg3,bd=4,relief=RIDGE)
        lblimg1.place(x=225,y=0,width=1310,height=590)

        #================down IMAGE========================
        img4=Image.open(r"C:\Users\91790\Desktop\hotel\hotel images\myh.jpg")
        img4=img4.resize((230,210),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)
        lblimg1=Label(main_frame,image=self.photoimg4,bd=4,relief=RIDGE)
        lblimg1.place(x=0,y=225,width=230,height=210)
     
        img5=Image.open(r"C:\Users\91790\Desktop\hotel\hotel images\khana.jpg")
        img5=img5.resize((230,190),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)
        lblimg2=Label(main_frame,image=self.photoimg5,bd=4,relief=RIDGE)
        lblimg2.place(x=0,y=420,width=230,height=190)

    def cust_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Customer_win(self.new_window)





    
     






     















if __name__ =="__main__":
    root=Tk()
    obj=HotelManagementSystem(root)
    root.mainloop()


