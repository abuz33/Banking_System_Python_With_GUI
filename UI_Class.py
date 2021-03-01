from tkinter import *
from tkinter import messagebox
from random import randint
import os
import glob

import Account


class User():

    def __init__(self):
        self.name = ''
        self.pin = ''
        self.balance = ''
        self.account_num = ''

    def login(self, user_name, acc_num, pin):
        if user_name == '' or acc_num == '' or pin == '':
            messagebox.showwarning(
                'Invalid way of Entering', 'You need to enter all of the information')
            return

        all_accounnts = glob.glob('./*.txt')

        for file in all_accounnts:
            if acc_num in file:
                with open(file, 'r') as f:
                    lines = f.readlines()

                    if lines[0][:-1] == user_name and lines[1][:-1] == pin and lines[3] == acc_num:
                        return True
                    else:
                        return "Informations entered doesn't match"

        return False

    def create_user(self, name, balance, pin):
        self.name = name
        self.balance = balance
        self.pin = pin

        self.save_file()

    def save_file(self):
        with open('Account_rec.txt', 'r+') as f:
            accnt_n = int(f.readlines()[-1])
            new_accnt_n = accnt_n + 1
            print(accnt_n)
            print(new_accnt_n)
            self.account_num = new_accnt_n
            f.write('\n'+str(new_accnt_n))

        with open(str(self.account_num)+'.txt', 'w') as f:
            f.write(self.name + '\n')
            f.write(self.pin+'\n')
            f.write(self.balance+'\n')
            f.write(str(self.account_num))

    def gather_details(self):
        pass


class UI_Class(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master

        self.user = User()

        self.master.geometry("500x500")
        self.master.title("Most Secure banking")
        self.master.geometry("500x500")
        # pages
        self.entry_page = Frame(self.master)
        self.user_create_page = Frame(self.master)
        self.user_logged_page = Frame(self.master)
        self.user_login_page = Frame(self.master)

        self.UI_elements()
        self.create_entry_page()

    def withdraw_page(self):
        pass

    def deposit_page(self):
        pass

    def edit_personal_page(self):
        pass

    def user_delete_page(self):
        pass

    def login(self):
        user_name = self.login_entry_1.get()
        user_account = self.login_entry_2.get()
        user_pin = self.login_entry_3.get()
        return_result = self.user.login(user_name, user_account, user_pin)
        if return_result:
            self.logged_page()
        elif return_result == False:
            messagebox.showwarning(
                "Operation is not successful", 'Cannot find user')
        elif type(return_result) == str:
            messagebox.showwarning(
                'Not valid data', 'You informations is not correct')

    def check_create_user(self):
        user_name = self.create_entry_1.get()
        user_balance = self.create_entry_2.get()
        user_pin = self.create_entry_3.get()
        if user_pin == '' or user_name == '' or user_balance == '':
            messagebox.showwarning("Try Again", "You have to enter all of the information!!!")
        else:
            self.user.create_user(user_name, user_balance, user_pin)
            messagebox.showinfo('Operation is successful!',
                                'Successfully created an account, \n Your account number is ' + str(self.user.account_num)+' please login to the system')
            self.login_page()

    def logged_page(self):
        self.user_login_page.grid_remove()
        self.user_create_page.grid_remove()
        self.user_logged_page.grid(row=0)
        self.logged_deposit_button.grid(row=0)
        self.logged_withdraw_button.grid(row=1)
        self.logged_send_money_button.grid(row=2)
        self.logged_edit_personal_detail.grid(row=3)
        self.logged_delete_button.grid(row=4)
        self.logged_logout_button.grid(5)

    def return_home(self):
        self.user_logged_page.grid_remove()
        self.user_login_page.grid_remove()
        self.user_create_page.grid_remove()
        self.create_entry_page()

    def create_entry_page(self):
        self.entry_page.grid(row=0)
        self.entry_create_button.grid(row=0, pady=10)
        self.entry_login_button.grid(row=1)
        self.entry_exit_button.grid(row=2)

    def create_page(self):
        self.entry_page.grid_remove()
        self.user_create_page.grid(row=0)
        self.create_label_1.grid(row=0, column=0)
        self.create_entry_1.grid(row=0, column=1)

        self.create_label_2.grid(row=1, column=0)
        self.create_entry_2.grid(row=1, column=1)

        self.create_label_3.grid(row=2, column=0)
        self.create_entry_3.grid(row=2, column=1)

        self.create_submit_button.grid(row=3, sticky=W)
        self.create_home_button.grid(row=4, sticky=W)

    def exit_pages(self):
        self.master.destroy()

    def UI_elements(self):
        # Entry Pages
        self.entry_create_button = Button(
            self.entry_page, text="Create an Account", command=self.create_page)
        self.entry_login_button = Button(
            self.entry_page, text='Login to your account', command=self.login_page)
        self.entry_exit_button = Button(
            self.entry_page, text='Exit', command=self.exit_pages)

        ###### CREATE PAGE ######
        # Labels
        self.create_label_1 = Label(
            self.user_create_page, text='Enter Name: ')
        self.create_label_2 = Label(
            self.user_create_page, text='Enter deposit amount: ')
        self.create_label_3 = Label(
            self.user_create_page, text='Enter desired PIN: ')

        # Entry
        self.create_entry_1 = Entry(self.user_create_page)
        self.create_entry_2 = Entry(self.user_create_page)
        self.create_entry_3 = Entry(self.user_create_page, show='*')

        # Buttons
        self.create_submit_button = Button(
            self.user_create_page, text="Submit", command=self.check_create_user)

        self.create_home_button = Button(self.user_create_page,
                                         text="Cancel", command=self.return_home)

        ###### LOGIN PAGE ######
        # Lables
        self.login_label_1 = Label(self.user_login_page,
                                   text='Enter your name: ')
        self.login_label_2 = Label(self.user_login_page,
                                   text='Enter account number: ')
        self.login_label_3 = Label(self.user_login_page,
                                   text='Enter your PIN: ')

        # Entry
        self.login_entry_1 = Entry(self.user_login_page)
        self.login_entry_2 = Entry(self.user_login_page)
        self.login_entry_3 = Entry(self.user_login_page)

        # Buttons
        self.login_submit_button = Button(
            self.user_login_page, text="Submit", command=self.login)

        self.login_home_button = Button(self.user_login_page,
                                        text="Cancel", command=self.return_home)

        ###### LOGGED PAGE ######
        # Buttons
        self.logged_withdraw_button = Button(self.user_logged_page,
                                             text="Withdraw Money", command=self.withdraw_page)
        self.logged_deposit_button = Button(self.user_logged_page,
                                            text="Deposit Money", command=self.deposit_page)
        self.logged_edit_personal_detail = Button(self.user_logged_page,
                                                  text="Edit Personal Detail", command=self.edit_personal_page)
        self.logged_delete_button = Button(self.user_login_page,
                                           text="Delete account", command=self.user_delete_page)

        self.logged_send_money_button = Button(self.user_login_page,
                                               text="Send money", command=self.user_delete_page)

        self.logged_logout_button = Button(self.user_logged_page,
                                           text="Logout", command=self.return_home)

    def login_page(self):
        self.entry_page.grid_remove()
        self.user_login_page.grid(row=0)

        self.login_label_1.grid(row=0, column=0)
        self.login_entry_1.grid(row=0, column=1)

        self.login_label_2.grid(row=1, column=0)
        self.login_entry_2.grid(row=1, column=1)

        self.login_label_3.grid(row=2, column=0)
        self.login_entry_3.grid(row=2, column=1)

        self.login_submit_button.grid(row=3)
        self.login_home_button.grid(row=4)


root = Tk()
app = UI_Class(root)
app.mainloop()
