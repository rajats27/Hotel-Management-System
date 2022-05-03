from tkinter import*
from tkinter import font
from tkinter import ttk
import random
import mysql.connector
from tkinter import messagebox
from time import strftime
from datetime import datetime


class booking:
    def __init__(self, root):
        self.root = root
        self.root.title("Booking")
        self.root.geometry("1550x800+0+0")

        #Variables
        self.var_customer_id=StringVar()
        self.var_roomno=StringVar()
        self.var_start_date=StringVar()
        self.var_end_date=StringVar()
        self.var_days=StringVar()
        self.var_price=StringVar()
        self.var_total_price=StringVar()

     #label frame
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Booking Details",font=("times new roman",16,"bold"),fg="black")
        labelframeleft.place(x=5,y=0,width=425,height=355)


        #labels and entries
        lbl_customer_id=Label(labelframeleft,text="Customer ID",font=("time new roman",12,"bold"),padx=2,pady=6)
        lbl_customer_id.grid(row=0,column=0,sticky=W)

        enty_id=ttk.Entry(labelframeleft,textvariable=self.var_customer_id,font=("time new roman",12,"bold"),width=29)
        enty_id.grid(row=0,column=1)


        #room no
        roomno=Label(labelframeleft,text="Room Number",font=("time new roman",12,"bold"),padx=2,pady=6)
        roomno.grid(row=1,column=0,sticky=W)

        nroomno=ttk.Entry(labelframeleft,textvariable=self.var_roomno,font=("time new roman",12,"bold"),width=29)
        nroomno.grid(row=1,column=1)

        #start date
        startdate=Label(labelframeleft,text="Check In",font=("time new roman",12,"bold"),padx=2,pady=6)
        startdate.grid(row=2,column=0,sticky=W)

        nstartdate=ttk.Entry(labelframeleft,textvariable=self.var_start_date,font=("time new roman",12,"bold"),width=29)
        nstartdate.grid(row=2,column=1)

        #end date
        enddate=Label(labelframeleft,text="Check Out",font=("time new roman",12,"bold"),padx=2,pady=6)
        enddate.grid(row=3,column=0,sticky=W)

        nenddate=ttk.Entry(labelframeleft,textvariable=self.var_end_date,font=("time new roman",12,"bold"),width=29)
        nenddate.grid(row=3,column=1)

        #no of days
        days=Label(labelframeleft,text="No of days",font=("time new roman",12,"bold"),padx=2,pady=6)
        days.grid(row=4,column=0,sticky=W)

        ndays=ttk.Entry(labelframeleft,textvariable=self.var_days,font=("time new roman",12,"bold"),width=29)
        ndays.grid(row=4,column=1)


        #price
        price=Label(labelframeleft,text="Price",font=("time new roman",12,"bold"),padx=2,pady=6)
        price.grid(row=5,column=0,sticky=W)
        combo_price=ttk.Combobox(labelframeleft,textvariable=self.var_price,font=("time new roman",12,"bold"),width=27,state="readonly")
        combo_price["value"]=("Normal=2000","Deluxe=5000","Adjoint=7000","Luxury=10000")
        combo_price.current(0)
        combo_price.grid(row=5,column=1)

        #nprice=ttk.Entry(labelframeleft,textvariable=self.var_price,font=("time new roman",12,"bold"),width=29)
        #nprice.grid(row=5,column=1)

        #totalprice
        price=Label(labelframeleft,text="Total Price",font=("time new roman",12,"bold"),padx=2,pady=6)
        price.grid(row=6,column=0,sticky=W)

        tprice=ttk.Entry(labelframeleft,textvariable=self.var_total_price,font=("time new roman",12,"bold"),width=29)
        tprice.grid(row=6,column=1)

       


        #buttons
        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=250,width=170,height=75)

        btnadd=Button(btn_frame,command=self.add_data ,text="Add",font=("times new roman",12,"bold"),bg="gold",fg="black",width=8)
        btnadd.grid(row=2,column=0,padx=1)

        #btndelete=Button(btn_frame,command=self.delete ,text="Delete",font=("times new roman",12,"bold"),bg="gold",fg="black",width=8)
        #btndelete.grid(row=2,column=2,padx=1)

        btnbill=Button(btn_frame,text="Bill",command=self.total,font=("times new roman",12,"bold"),bg="gold",fg="black",width=8)
        btnbill.grid(row=1,column=0,padx=1)



        #table frame
        #table_frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="View and Search",font=("times new roman",16,"bold"),fg="black",padx=2)
        #table_frame.place(x=435,y=0,width=860,height=490)

        #lbl_searchby=Label(table_frame,text="Search by:",font=("time new roman",12,"bold"),padx=2,pady=6)
        #lbl_searchby.grid(row=0,column=0,sticky=W,padx=2)
        #self.search_var=StringVar()
        #combo_search=ttk.Combobox(table_frame,textvariable=self.search_var,font=("time new roman",12,"bold"),width=27,state="readonly")
        #combo_search["value"]=("customer_id","room_no")
        #combo_search.current(0)
        #combo_search.grid(row=0,column=1,padx=2)

        #self.text_search=StringVar()
        #txtsearch=ttk.Entry(table_frame,textvariable=self.text_search,font=("time new roman",12,"bold"),width=24)
        #txtsearch.grid(row=0,column=2,padx=2)

        #btnsearch=Button(table_frame, text="Search",command=self.search,font=("times new roman",12,"bold"),bg="gold",fg="black",width=8)
        #btnsearch.grid(row=0,column=3,padx=2)

        #btnall=Button(table_frame, text="View all",command=self.fetch_data,font=("times new roman",12,"bold"),bg="gold",fg="black",width=8)
        #btnall.grid(row=0,column=4,padx=2)


        #Show data table
        #details_table=Frame(table_frame,bd=2,relief=RIDGE)
        #details_table.place(x=0,y=50,width=840,height=400)

        #scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        #scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)

        #self.booking_details_table=ttk.Treeview(details_table,column = ("Customer ID","Room Number","Check In","Check Out","No of days","Price","Total Price"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set )

        #scroll_x.pack(side=BOTTOM,fill=X)
        #scroll_y.pack(side=RIGHT,fill=Y)

        #scroll_x.config(command=self.booking_details_table.xview)
        #scroll_y.config(command=self.booking_details_table.yview)

        #self.booking_details_table.heading("Customer ID",text="Customer ID")
        #self.booking_details_table.heading("Room Number",text="Room Number")
        #self.booking_details_table.heading("Check In",text="Check In")
        #self.booking_details_table.heading("Check Out",text="Check Out")
        #self.booking_details_table.heading("No of days",text="No of days")
        #self.booking_details_table.heading("Price",text="Price")
        #self.booking_details_table.heading("Total Price",text="Total Price")
        
       

        #self.booking_details_table["show"]="headings"
        #self.booking_details_table.pack(fill=BOTH,expand=1)
        #self.booking_details_table.bind("<ButtonRelease-1>",self.get_cursor)
        #self.fetch_data()



    def add_data(self):
        if self.var_customer_id.get()=="" or self.var_roomno.get()=="":
            messagebox.showerror("Error","All fields are compulsory",parent=self.root)
        else:
            try:

                conn=mysql.connector.connect(host="localhost",user="root",password="siddhanthsalian0605",database="hotel")
                my_cursor=conn.cursor()
                my_cursor.execute("Insert into booking values(%s,%s,%s,%s,%s,%s,%s)",(
                self.var_customer_id.get(),
                self.var_roomno.get(),
                self.var_start_date.get(),
                self.var_end_date.get(),
                self.var_days.get(),
                self.var_price.get(),
                self.var_total_price.get()
                ))
                conn.commit()
                self.fetch_data()

                conn.close()
                messagebox.showinfo("Success","Booking done successfully",parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning",f"Something went wrong:{str(es)}",parent=self.root)

    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="siddhanthsalian0605",database="hotel")
        my_cursor=conn.cursor()
        my_cursor.execute("select *from booking")
        rows=my_cursor.fetchall()
        #if len(rows)!=0:
         #   self.booking_details_table.delete(*self.booking_details_table.get_children())
          #  for i in rows:
           #     self.booking_details_table.insert("",END,values=i)
            #conn.commit()
        conn.close()


    def get_cursor(self,event=""):
        cursor_row=self.booking_details_table.focus()
        content=self.booking_details_table.item(cursor_row)
        row=content["values"]

        self.var_customer_id.set(row[0])  
        self.var_roomno.set(row[1])  
        self.var_start_date.set(row[2])
        self.var_end_date.set(row[3])
        self.var_days.set(row[4])
        self.var_price.set(row[5])
        self.var_total_price.set(row[6])

    #def search(self):
     #   conn=mysql.connector.connect(host="localhost",user="root",password="siddhanthsalian0605",database="hotel")
      #  my_cursor=conn.cursor()

        #my_cursor.execute("select * from booking where "+str(self.search_var.get())+" LIKE '%"+str(self.text_search.get())+"%'")
        #rows=my_cursor.fetchall()
        #if len (rows)!=0:
         ##   self.booking_details_table.delete(*self.booking_details_table.get_children())
           # for i in rows:
            #    self.booking_details_table.insert("",END,values=i)
            #conn.commit()
        #conn.close()
        


    #def delete(self):
      #  delete=messagebox.askyesno("Hotel Management System","Do you want to delete this booking??",parent=self.root)
       # if delete>0:
        #    conn=mysql.connector.connect(host="localhost",user="root",password="siddhanthsalian0605",database="hotel")
         #   my_cursor=conn.cursor()
          #  query="Delete from booking where customer_id=%s"
           # value=(self.var_customer_id.get(),)
           # my_cursor.execute(query,value)
        #else:
         #   if not delete:
          #      return
        #conn.commit()
        #self.fetch_data()
        #conn.close()


    
    #Tottal price
    def total(self):
        startdate=self.var_start_date.get()
        enddate=self.var_end_date.get()
        startdate=datetime.strptime(startdate,"%Y-%m-%d")
        enddate=datetime.strptime(enddate,"%Y-%m-%d")
        self.var_days.set(abs(enddate-startdate).days)
        days=int(self.var_days.get())
      
      
       
        if(self.var_price.get()=="Normal=2000"):
            totalprice=(days)*2000
        elif (self.var_price.get()=="Deluxe=5000"):
            totalprice=(days)*5000
        elif (self.var_price.get()=="Adjoint=7000"):
            totalprice=(days)*7000
        else:
            totalprice=(days)*10000
        self.var_total_price.set(totalprice)

        



    
        













if __name__ == "__main__":
    root = Tk()
    obj = booking(root)
    root.mainloop()