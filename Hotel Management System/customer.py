from tkinter import*
from tkinter import font
from tkinter import ttk

import random
import mysql.connector
from tkinter import messagebox



class customer_window:
    def __init__(self,root):
        self.root=root
        self.root.title("customer") 
        self.root.geometry("1295x550+0+0")

        #Variables
        self.var_customer_id=StringVar()
        x=random.randint(1,99999)
        self.var_customer_id.set(str(x))

        self.var_name=StringVar()
        self.var_phone_number=StringVar()
        self.var_email_id=StringVar()
        self.var_id_proof=StringVar()
        self.var_id_number=StringVar()





        #label frame
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Customer Details",font=("times new roman",16,"bold"),fg="black")
        labelframeleft.place(x=5,y=0,width=425,height=310)

        #labels and entries
        lbl_customer_id=Label(labelframeleft,text="Customer ID",font=("time new roman",12,"bold"),padx=2,pady=6)
        lbl_customer_id.grid(row=0,column=0,sticky=W)

        enty_id=ttk.Entry(labelframeleft,textvariable=self.var_customer_id,font=("time new roman",12,"bold"),width=29,state="readonly")
        enty_id.grid(row=0,column=1)



        #customer name
        name=Label(labelframeleft,text="Name",font=("time new roman",12,"bold"),padx=2,pady=6)
        name.grid(row=1,column=0,sticky=W)

        txtname=ttk.Entry(labelframeleft,textvariable=self.var_name,font=("time new roman",12,"bold"),width=29)
        txtname.grid(row=1,column=1)
        

        #phone number
        phn=Label(labelframeleft,text="Phone Number",font=("time new roman",12,"bold"),padx=2,pady=6)
        phn.grid(row=2,column=0,sticky=W)
        
        txtphn=ttk.Entry(labelframeleft,textvariable=self.var_phone_number,font=("time new roman",12,"bold"),width=29)
        txtphn.grid(row=2,column=1)


        #email id
        email=Label(labelframeleft,text="Email Id",font=("time new roman",12,"bold"),padx=2,pady=6)
        email.grid(row=3,column=0,sticky=W)
        
        txtemail=ttk.Entry(labelframeleft,textvariable=self.var_email_id,font=("time new roman",12,"bold"),width=29)
        txtemail.grid(row=3,column=1)


        #id proof
        lbl_id_proof=Label(labelframeleft,text="ID Proof Type",font=("time new roman",12,"bold"),padx=2,pady=6)
        lbl_id_proof.grid(row=4,column=0,sticky=W)
        combo_id_proof=ttk.Combobox(labelframeleft,textvariable=self.var_id_proof,font=("time new roman",12,"bold"),width=27,state="readonly")
        combo_id_proof["value"]=("Adhar","Passport","Pan Card")
        combo_id_proof.current(0)
        combo_id_proof.grid(row=4,column=1)


        #id number
        lbl_id_number=Label(labelframeleft,text="ID number",font=("time new roman",12,"bold"),padx=2,pady=6)
        lbl_id_number.grid(row=5,column=0,sticky=W)
        
        
        txtid_number=ttk.Entry(labelframeleft,textvariable=self.var_id_number,font=("time new roman",12,"bold"),width=29)
        txtid_number.grid(row=5,column=1)


        #buttons
        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=240,width=345,height=40)

        btnadd=Button(btn_frame, text="Add",command=self.add_data,font=("times new roman",12,"bold"),bg="gold",fg="black",width=8)
        btnadd.grid(row=0,column=0,padx=1)

        btnupdate=Button(btn_frame, text="Update",command=self.update,font=("times new roman",12,"bold"),bg="gold",fg="black",width=8)
        btnupdate.grid(row=0,column=1,padx=1)

        btndelete=Button(btn_frame, text="Delete",command=self.delete,font=("times new roman",12,"bold"),bg="gold",fg="black",width=8)
        btndelete.grid(row=0,column=2,padx=1)
        
        btnreset=Button(btn_frame, text="Reset",command=self.reset,font=("times new roman",12,"bold"),bg="gold",fg="black",width=8)
        btnreset.grid(row=0,column=3,padx=1)


        #table frame
        table_frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="View and Search",font=("times new roman",16,"bold"),fg="black",padx=2)
        table_frame.place(x=435,y=0,width=860,height=490)

        lbl_searchby=Label(table_frame,text="Search by:",font=("time new roman",12,"bold"),padx=2,pady=6)
        lbl_searchby.grid(row=0,column=0,sticky=W,padx=2)
        self.search_var=StringVar()
        combo_search=ttk.Combobox(table_frame,textvariable=self.search_var,font=("time new roman",12,"bold"),width=27,state="readonly")
        combo_search["value"]=("customer_id","phone_no")
        combo_search.current(0)
        combo_search.grid(row=0,column=1,padx=2)

        self.text_search=StringVar()
        txtsearch=ttk.Entry(table_frame,textvariable=self.text_search,font=("time new roman",12,"bold"),width=24)
        txtsearch.grid(row=0,column=2,padx=2)

        btnsearch=Button(table_frame, text="Search",command=self.search,font=("times new roman",12,"bold"),bg="gold",fg="black",width=8)
        btnsearch.grid(row=0,column=3,padx=2)

        btnall=Button(table_frame, text="View all",command=self.fetch_data,font=("times new roman",12,"bold"),bg="gold",fg="black",width=8)
        btnall.grid(row=0,column=4,padx=2)


        #Show data table
        details_table=Frame(table_frame,bd=2,relief=RIDGE)
        details_table.place(x=0,y=50,width=840,height=400)

        scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)

        self.customer_details_table=ttk.Treeview(details_table,column = ("Customer ID","Name","Phone Number","Email ID","ID Proof","ID Number"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set )

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.customer_details_table.xview)
        scroll_y.config(command=self.customer_details_table.yview)

        self.customer_details_table.heading("Customer ID",text="Customer ID")
        self.customer_details_table.heading("Name",text="Name")
        self.customer_details_table.heading("Phone Number",text="Phone Number")
        self.customer_details_table.heading("Email ID",text="Email ID")
        self.customer_details_table.heading("ID Proof",text="ID Proof")
        self.customer_details_table.heading("ID Number",text="ID Number")

        self.customer_details_table["show"]="headings"
        self.customer_details_table.pack(fill=BOTH,expand=1)
        self.customer_details_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()



    def add_data(self):
        if self.var_phone_number.get()=="" or self.var_email_id.get()=="":
            messagebox.showerror("Error","All fields are compulsory",parent=self.root)
        else:
            try:

                conn=mysql.connector.connect(host="localhost",user="root",password="siddhanthsalian0605",database="hotel")
                my_cursor=conn.cursor()
                my_cursor.execute("Insert into customer values(%s,%s,%s,%s,%s,%s)",(
                self.var_customer_id.get(),
                self.var_name.get(),
                self.var_phone_number.get(),
                self.var_email_id.get(),
                self.var_id_proof.get(),
                self.var_id_number.get()
                ))
                conn.commit()
                self.fetch_data()

                conn.close()
                messagebox.showinfo("Success","Customer added successfully",parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning",f"Something went wrong:{str(es)}",parent=self.root)

    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="siddhanthsalian0605",database="hotel")
        my_cursor=conn.cursor()
        my_cursor.execute("select *from customer")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.customer_details_table.delete(*self.customer_details_table.get_children())
            for i in rows:
                self.customer_details_table.insert("",END,values=i)
            conn.commit()
        conn.close()


    def get_cursor(self,event=""):
        cursor_row=self.customer_details_table.focus()
        content=self.customer_details_table.item(cursor_row)
        row=content["values"]

        self.var_customer_id.set(row[0])
        self.var_name.set(row[1])
        self.var_phone_number.set(row[2])
        self.var_email_id.set(row[3])
        self.var_id_proof.set(row[4])
        self.var_id_number.set(row[5])

    
    def update(self):
        if self.var_phone_number.get()=="":
            messagebox.showerror("Error","Please enter phone number",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="siddhanthsalian0605",database="hotel")
            my_cursor=conn.cursor()
            my_cursor.execute("Update customer set name=%s,phone_no=%s,email_id=%s,id_proof=%s,id_number=%s where customer_id=%s",(
            self.var_name.get(),
            self.var_phone_number.get(),
            self.var_email_id.get(),
            self.var_id_proof.get(),
            self.var_id_number.get(), 
            self.var_customer_id.get()
            ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update","Customer details has been updated successfully",parent=self.root)


    def delete(self):
        delete=messagebox.askyesno("Hotel Management System","Do you want to delete this customer??",parent=self.root)
        if delete>0:
            conn=mysql.connector.connect(host="localhost",user="root",password="siddhanthsalian0605",database="hotel")
            my_cursor=conn.cursor()
            query="Delete from Customer where customer_id=%s"
            value=(self.var_customer_id.get(),)
            my_cursor.execute(query,value)
        else:
            if not delete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()


    def reset(self):
       
        self.var_name.set(""),
        self.var_phone_number.set(""),
        self.var_email_id.set(""),
        self.var_id_number.set("")

        x=random.randint(1,99999)
        self.var_customer_id.set(str(x))

        
    def search(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="siddhanthsalian0605",database="hotel")
        my_cursor=conn.cursor()

        my_cursor.execute("select * from customer where "+str(self.search_var.get())+" LIKE '%"+str(self.text_search.get())+"%'")
        rows=my_cursor.fetchall()
        if len (rows)!=0:
            self.customer_details_table.delete(*self.customer_details_table.get_children())
            for i in rows:
                self.customer_details_table.insert("",END,values=i)
            conn.commit()
        conn.close()




            
if __name__ == "__main__":
    root = Tk()
    obj = customer_window(root)
    root.mainloop() 

