from tkinter import*
from tkinter import font
from PIL import Image, ImageTk
from tkinter import messagebox
from login import login_window
from cust_hotelmanagement import hotelmanagement




class choice:
    def __init__(self,root):
        self.root = root
        self.root.title("Choice")
        self.root.geometry("1295x550+0+0")


        img1 = Image.open("C:/Users/lenovo/Desktop/python programming/python projects/choice.jpg")
        img1 = img1.resize((1500, 800), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        lblimg = Label(self.root, image=self.photoimg1, bd=4, relief=RIDGE)
        lblimg.place(x=0, y=0, width=1400, height=800)



  

        #buttons
        manager = Button(text="Manager",command=self.manager,font=("times new roman", 15, "bold"), bd=3,relief=RIDGE, fg="gold", bg="red", activeforeground="white", activebackground="red")
        manager.place(x=400, y=150, width=120, height=35)

        customer = Button( text="Customer",command=self.customer, font=("times new roman", 15, "bold"), bd=3,relief=RIDGE, fg="gold", bg="red", activeforeground="white", activebackground="red")
        customer.place(x=600, y=150, width=120, height=35)

    def manager(self):
        self.new_window=(self.root)
        self.app=login_window(self.new_window)


    def customer(self):
        self.new_window=(self.root)
        self.app=hotelmanagement(self.new_window)










if __name__ == "__main__":
    root = Tk()
    obj = choice(root)
    root.mainloop()

