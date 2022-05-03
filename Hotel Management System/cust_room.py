from tkinter import*
from tkinter import font
from tkinter import ttk
import random
import mysql.connector
from tkinter import messagebox



class hotel_room_window:
    def __init__(self,root):
        self.root=root
        self.root.title("hotel room") 
        self.root.geometry("1295x550+0+0")

        #Variables
        self.var_room_no=StringVar()
        self.var_room_type=StringVar()
        self.var_status=StringVar()
        

        #label frame
        #labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Hotel Room Details ",font=("times new roman",16,"bold"),fg="black")
        #labelframeleft.place(x=5,y=0,width=425,height=190)


         #labels and entries
        #lbl_room_no=Label(labelframeleft,text="Room Number:",font=("time new roman",12,"bold"),padx=2,pady=6)
        #lbl_room_no.grid(row=0,column=0,sticky=W)

        #enty_room_no=ttk.Entry(labelframeleft,textvariable=self.var_room_no,font=("time new roman",12,"bold"),width=29)
        #enty_room_no.grid(row=0,column=1)

        #label_room_type=Label(labelframeleft,font=("time new roman",12,"bold"),text="Room Type:",padx=2,pady=6)
        #label_room_type.grid(row=1,column=0,sticky=W)

        #combo_room_type=ttk.Combobox(labelframeleft,textvariable=self.var_room_type,font=("time new roman",12,"bold"),width=29,state="readonly")
        #combo_room_type["value"]=("Normal","Deluxe","Adjoint","Luxury")
        #combo_room_type.current(0)
        #combo_room_type.grid(row=1,column=1)

        #label_status=Label(labelframeleft,font=("time new roman",13,"bold"),text="Status:",padx=2,pady=6)
        #label_status.grid(row=2,column=0,sticky=W)
        #combo_status=ttk.Combobox(labelframeleft,textvariable=self.var_status,font=("time new roman",12,"bold"),width=29,state="readonly")
        #combo_status["value"]=("Available","Unavailable")
        #combo_status.current(0)
        #combo_status.grid(row=2,column=1)


        #table frame
        table_frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="Room Details",font=("times new roman",16,"bold"),fg="black",padx=2)
        table_frame.place(x=200,y=0,width=860,height=490)

        lbl_searchby=Label(table_frame,text="Search by:",font=("time new roman",12,"bold"),padx=2,pady=6)
        lbl_searchby.grid(row=0,column=0,sticky=W,padx=2)
        self.search_var=StringVar()
        combo_search=ttk.Combobox(table_frame,textvariable=self.search_var,font=("time new roman",12,"bold"),width=27,state="readonly")
        combo_search["value"]=("room_type")
        combo_search.current(0)
        combo_search.grid(row=0,column=1,padx=2)

        self.text_search=StringVar()
        txtsearch=ttk.Entry(table_frame,textvariable=self.text_search,font=("time new roman",12,"bold"),width=24)
        txtsearch.grid(row=0,column=2,padx=2)

        btnsearch=Button(table_frame, text="Search",command=self.search,font=("times new roman",12,"bold"),bg="gold",fg="black",width=8)
        btnsearch.grid(row=0,column=3,padx=2)

        btnall=Button(table_frame, text="View all",command=self.fetch_data,font=("times new roman",12,"bold"),bg="gold",fg="black",width=8)
        btnall.grid(row=0,column=4,padx=2)


         #buttons
        #btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        #btn_frame.place(x=0,y=120,width=260,height=40)

        #btnadd=Button(btn_frame, text="Add",command=self.add_data,font=("times new roman",12,"bold"),bg="gold",fg="black",width=8)
        #btnadd.grid(row=3,column=0,padx=1)

        #btnupdate=Button(btn_frame, text="Update",command=self.update,font=("times new roman",12,"bold"),bg="gold",fg="black",width=8)
        #btnupdate.grid(row=3,column=1,padx=1)

        #btndelete=Button(btn_frame, text="Delete",command=self.delete,font=("times new roman",12,"bold"),bg="gold",fg="black",width=8)
        #btndelete.grid(row=3,column=2,padx=1)

        

        #Show data table
        details_table=Frame(table_frame,bd=2,relief=RIDGE)
        details_table.place(x=0,y=50,width=840,height=400)

        scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)

        self.room_details_table=ttk.Treeview(details_table,column = ("Room Number","Room Type","Status"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set )

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.room_details_table.xview)
        scroll_y.config(command=self.room_details_table.yview)

        self.room_details_table.heading("Room Type",text="Room Type")
        self.room_details_table.heading("Room Number",text="Room Number")
        self.room_details_table.heading("Status",text="Status")
       

        self.room_details_table["show"]="headings"
        self.room_details_table.pack(fill=BOTH,expand=1)
        self.room_details_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()



        



        

    #def add_data(self):
     #   if self.var_room_no.get()=="":
          # messagebox.showerror("Error","All fields are compulsory",parent=self.root)
      #  else:
       #     try:

        #        conn=mysql.connector.connect(host="localhost",user="root",password="siddhanthsalian0605",database="hotel")
         ##       my_cursor=conn.cursor()
           #     my_cursor.execute("Insert into hotel_room values(%s,%s,%s)",(
            #    self.var_room_no.get(),
             #   self.var_room_type.get(),
            #    self.var_status.get()
            #    ))
            #    conn.commit()
             #   self.fetch_data()

              #  conn.close()
               # messagebox.showinfo("Success","Room details added successfully",parent=self.root)
            #except Exception as es:
             #   messagebox.showwarning("Warning",f"Something went wrong:{str(es)}",parent=self.root)






    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="siddhanthsalian0605",database="hotel")
        my_cursor=conn.cursor()
        my_cursor.execute("select *from hotel_room")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.room_details_table.delete(*self.room_details_table.get_children())
            for i in rows:
                self.room_details_table.insert("",END,values=i)
            conn.commit()
        conn.close()


    def get_cursor(self,event=""):
        cursor_row=self.room_details_table.focus()
        content=self.room_details_table.item(cursor_row)
        row=content["values"]

        self.var_room_no.set(row[0])
        self.var_room_type.set(row[1])
        self.var_status.set(row[2])


    
   # def update(self):
    ##    if self.var_room_no.get()=="":
      #      messagebox.showerror("Error","Please enter room number",parent=self.root)
       # else:
        #    conn=mysql.connector.connect(host="localhost",user="root",password="siddhanthsalian0605",database="hotel")
         #   my_cursor=conn.cursor()
          #  my_cursor.execute("Update hotel_room set room_type=%s,status=%s where room_no=%s ",(
            
           # self.var_room_type.get(),
            #self.var_status.get(),
            #self.var_room_no.get()
       
            #))
            #conn.commit()
            #self.fetch_data()
            #conn.close()
            #messagebox.showinfo("Update","Room details has been updated successfully",parent=self.root)


    #def delete(self):
     #   delete=messagebox.askyesno("Hotel Management System","Do you want to delete this room details??",parent=self.root)
      #  if delete>0:
       #     conn=mysql.connector.connect(host="localhost",user="root",password="siddhanthsalian0605",database="hotel")
        #    my_cursor=conn.cursor()
         #   query="Delete from hotel_room where room_no=%s"
          #  value=(self.var_room_no.get(),)
           # my_cursor.execute(query,value)
        #else:
         #   if not delete:
          #      return
        #conn.commit()
        #self.fetch_data()
        #conn.close()




    def search(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="siddhanthsalian0605",database="hotel")
        my_cursor=conn.cursor()

        my_cursor.execute("select * from hotel_room where "+str(self.search_var.get())+" LIKE '%"+str(self.text_search.get())+"%'")
        rows=my_cursor.fetchall()
        if len (rows)!=0:
            self.room_details_table.delete(*self.room_details_table.get_children())
            for i in rows:
                self.room_details_table.insert("",END,values=i)
            conn.commit()
        conn.close()
      

    
    




       
if __name__ == "__main__":
    root = Tk()
    obj = hotel_room_window(root)
    root.mainloop() 