from tkinter import*
from tkinter import ttk
from tkinter import font
from PIL import Image, ImageTk
from tkinter import messagebox
from hotelmanagement import hotelmanagement


class login_window:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("1295x550+0+0")

        # PHOTO
        img1 = Image.open(
            "C:/Users/lenovo/Desktop/python programming/python projects/login.jpg")
        img1 = img1.resize((1500, 800), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        lblimg = Label(self.root, image=self.photoimg1, bd=4, relief=RIDGE)
        lblimg.place(x=0, y=0, width=1400, height=800)

        frame = Frame(self.root, bg="blue")
        frame.place(x=560, y=120, width=350, height=450)

        get_str = Label(frame, text="Manager Login", font=(
            "times new roman", 20, "bold"), fg="gold", bg="blue")
        get_str.place(x=50, y=40)

        # Label
        username = Label(frame, text="Username", font=(
            "times new roman", 15, "bold"), fg="gold", bg="blue")
        username.place(x=70, y=100)

        self.txtuser = ttk.Entry(frame, font=("times new roman", 15, "bold"))
        self.txtuser.place(x=40, y=125, width=270)

        password = Label(frame, text="Password", font=(
            "times new roman", 15, "bold"), fg="gold", bg="blue")
        password.place(x=70, y=160)

        self.txtpass = ttk.Entry(
            frame, show="*", font=("times new roman", 15, "bold"))
        self.txtpass.place(x=40, y=185, width=270)

        # login button
        loginbtn = Button(frame, text="Login", command=self.login, font=("times new roman", 15, "bold"),
                          bd=3, relief=RIDGE, fg="gold", bg="red", activeforeground="white", activebackground="red")
        loginbtn.place(x=110, y=220, width=120, height=35)

    def login(self):
        if self.txtuser.get() == "" or self.txtuser.get() == "":
            messagebox.showerror("Error", "All fields are required")
        elif self.txtuser.get() == "manager" and self.txtpass.get() == "12345":
            messagebox.showinfo(
                "Success", "Welcome to Hotel Management System")
            self.new_window = self.root
            self.app = hotelmanagement(self.new_window)
        else:
            messagebox.showerror("Invalid", "Invalid username and password")


if __name__ == "__main__":
    root = Tk()
    obj = login_window(root)
    root.mainloop()
