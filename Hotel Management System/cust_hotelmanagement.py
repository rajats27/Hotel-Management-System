from tkinter import*
from tkinter import font
from PIL import Image, ImageTk
from cust_customer import customer_window
from cust_room import hotel_room_window
from cust_booking import booking



class hotelmanagement:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1550x800+0+0")

        # PHOTO
        img1 = Image.open("C:/Users/lenovo/Desktop/python programming/python projects/hotelmanagement.jpg")
        img1 = img1.resize((1500, 800), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        lblimg = Label(self.root, image=self.photoimg1, bd=4, relief=RIDGE)
        lblimg.place(x=0, y=0, width=1400, height=800)

        #Main frame
       # main_frame=Frame(self.root,bd=4,relief=RIDGE)
        #main_frame.place(x=0,y=190,width=1400,height=800)

        #Menu
        lbl_menu=Label(text="Menu",font=("times new roman",20,"bold"),bg="gold",fg="black",bd=4,relief=RIDGE)
        lbl_menu.place(x=50,y=50,width=228)

        #Btn
        btn_frame=Frame(bd=4,relief=RIDGE)
        btn_frame.place(x=50,y=85,width=228,height=157)

        customer_btn=Button(btn_frame,text="1.Customer",command=self.customer_details,width=20,font=("times new roman",14,"bold"),bg="gold",fg="black",bd=0)
        customer_btn.grid(row=0,column=0,pady=1)


        hotelroom_btn=Button(btn_frame,text="2.Hotel Room",command=self.hotelroom_details,width=20,font=("times new roman",14,"bold"),bg="gold",fg="black",bd=0)
        hotelroom_btn.grid(row=1,column=0,pady=1)

        booking_btn=Button(btn_frame,text="3.Booking",command=self.booking_details,width=20,font=("times new roman",14,"bold"),bg="gold",fg="black",bd=0)
        booking_btn.grid(row=2,column=0,pady=1)

        exit_btn=Button(btn_frame,text="4.Exit",command=self.exit,width=20,font=("times new roman",14,"bold"),bg="gold",fg="black",bd=0)
        exit_btn.grid(row=4,column=0,pady=1)

    
    def customer_details(self):
        self.new_window=Toplevel(self.root)
        self.app=customer_window(self.new_window)

    def hotelroom_details(self):
        self.new_window=Toplevel(self.root)
        self.app=hotel_room_window(self.new_window)

    def booking_details(self):
        self.new_window=Toplevel(self.root)
        self.app=booking(self.new_window)

    def exit(self):
        self.root.destroy()



if __name__ == "__main__":
    root = Tk()
    obj = hotelmanagement(root)
    root.mainloop()
