from tkinter import *


class User(Frame):
    user_id = 10000

    def __init__(self, master):
        self.master = master
        super().__init__(master)
        # self.master.geometry("500x500")
        self.master.title("Most Secure banking")
        self.master.geometry("500x500")
        self.user = {}
        self.page = Frame(self.master)

        self.UI_elements()
        self.create_entry_page()

    def create_entry_page(self):
        self.label1.grid(row=0, sticky=N, pady=10)
        self.login_button.grid(row=1, sticky=N, pady=10)
        self.create_button.grid(row=2, sticky=N, pady=10)

    def create_page(self):
        # self.page.grid_remove()
        self.label1.grid(row=0)

    def UI_elements(self):
        # Entry Pages
        self.create_button = Button(
            self.page, text="Create an Account", command=self.create_page)
        self.login_button = Button(
            self.page, text='Login to your account', command=self.login_page)

        # Labels
        self.label1 = Label(self.page,
                            text='Please Enter your details below',
                            font="Calibri 12")

    def login_page(self):
        print("Login Page")

    def login(self, user_name, password, email):
        self.user['user_ame'] = user_name
        self.user['password'] = password
        self.user['email'] = email

    def create_user(self, user_name, phone, email, password):
        self.user['user_name'] = user_name
        self.user['phone'] = phone
        self.user["email"]

    def gatherdata(self):
        with open("user", "r+") as f:
            for line in f:
                if self.user["user_name"] in line:
                    List = line.split('\t')


root = Tk()
app = User(master=root)
app.mainloop()
