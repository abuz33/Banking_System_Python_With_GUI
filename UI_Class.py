from tkinter import *
from tkinter import messagebox
from random import randint
import os
import glob

from Account import Account
from User import User


class UI_Class(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master

        self.user = User()
        self.account = Account()

        self.master.geometry("500x500")
        self.master.title("Most Secure banking")
        self.master.geometry("500x500")
        # pages
        self.entry_page = Frame(self.master)
        self.user_create_page = Frame(self.master)
        self.user_logged_page = Frame(self.master)
        self.user_login_page = Frame(self.master)

        self.user_deposit_page = Frame(self.master)
        self.user_withdraw_page = Frame(self.master)
        self.user_edit_page = Frame(self.master)
        self.user_delete_page = Frame(self.master)
        self.user_send_page = Frame(self.master)

        self.UI_elements()
        self.create_entry_page()
        self.open_windows = []
    # Pages

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

    def withdraw_page(self):
        self.user_logged_page.grid_remove()
        self.user_withdraw_page.grid(row=0)
        self.withdraw_label_1.grid(row=0, column=0)
        self.withdraw_entry_1.grid(row=0, column=1)

        self.withdraw_submit_button.grid(row=1)
        self.withdraw_home_button.grid(row=2)

    def deposit_page(self):
        self.user_logged_page.grid_remove()
        self.user_deposit_page.grid(row=0)
        self.deposit_label_1.grid(row=0, column=0)
        self.deposit_entry_1.grid(row=0, column=1)

        self.deposit_submit_button.grid(row=1)
        self.deposit_home_button.grid(row=2)

    def edit_personal_page(self):
        self.user_logged_page.grid_forget()
        self.user_edit_page.grid(row=0)
        self.edit_label_1.grid(row=0, column=0)
        self.edit_entry_1.grid(row=0, column=1)

        self.edit_label_2.grid(row=1, column=0)
        self.edit_entry_2.grid(row=1, column=1)

        self.edit_submit_button.grid(row=2)
        self.edit_home_button.grid(row=3)

    def delete_page(self):
        self.user_logged_page.grid_remove()
        self.user_delete_page.grid(row=0)

        self.delete_entry_1.grid(row=0)
        self.delete_yes_button.grid(row=1, column=0)
        self.delete_no_button.grid(row=1, column=1)

    def send_page(self):
        self.user_logged_page.grid_remove()
        self.user_send_page.grid(row=0)

        self.send_label_1.grid(row=0, column=0)
        self.send_entry_1.grid(row=0, column=1)

        self.send_label_2.grid(row=1, column=0)
        self.send_entry_2.grid(row=1, column=1)

        self.send_submit_button.grid(row=2)
        self.send_home_button.grid(row=3)

    def login(self):
        user_name = self.login_entry_1.get()
        user_account = self.login_entry_2.get()
        user_pin = self.login_entry_3.get()
        return_result = self.user.login(user_name, user_account, user_pin)
        if return_result:
            self.user.account_num = user_account
            self.user.pin = user_pin
            self.user.name = user_name
            print(str(self.user.balance) + "UI")
            self.account.login(
                self.user.name, self.user.balance, self.user.account_num)
            self.logged_page()
        elif return_result == False:
            messagebox.showwarning(
                "Operation is not successful", 'Cannot find user')
        elif type(return_result) == str:
            messagebox.showwarning(
                'Not valid data', 'Your informations are not correct')

    def check_create_user(self):
        user_name = self.create_entry_1.get()
        user_balance = int(self.create_entry_2.get())
        user_pin = self.create_entry_3.get()
        if user_pin == '' or user_name == '' or user_balance == '':
            messagebox.showwarning(
                "Try Again", "You have to enter all of the information!!!")
        else:
            self.user.create_user(user_name, user_balance, user_pin)
            self.account.init_account(
                user_name, user_balance, self.user.account_num)
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
        self.logged_logout_button.grid(row=5)

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

    def edit_info(self):
        name = self.edit_entry_1.get()
        pin = self.edit_entry_2.get()
        self.user.update_info(name, pin)
    ###Submit buttons ####

    def deposit(self):
        amount = int(self.deposit_entry_1.get())
        result_user = self.user.update_balance('deposit', amount)
        if result_user:
            result_account = self.account.deposit_money(amount)

        if result_account:
            messagebox.showinfo("Success", 'Operation is succesfully done.')

    def widthdraw(self):
        amount = int(self.withdraw_entry_1.get())
        self.user.update_balance('withdraw', amount)
        self.account.withdraw_money(amount)

    def send_money(self):
        self.send_entry_1.get()
        self.send_entry_2.get()

    def delete(self):
        self.open_windows.append(self.user_delete_page)

    def send_submit(self):
        acc_num = self.send_entry_1.get()
        amount = self.send_entry_2.get()
        self.account.send_money(acc_num, amount)

    def delete_account(self):
        pass
    #### Cancel Buttons #####

    def return_logged_menu(self, page):
        page.grid_remove()
        self.logged_page()

    def exit_pages(self):
        self.master.destroy()
    #### UI ELEMENTS #####

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
        self.login_entry_3 = Entry(self.user_login_page, show='*')

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
        self.logged_delete_button = Button(self.user_logged_page,
                                           text="Delete account", command=self.delete_page)

        self.logged_send_money_button = Button(self.user_logged_page,
                                               text="Send money", command=self.send_page)

        self.logged_logout_button = Button(self.user_logged_page,
                                           text="Logout", command=self.return_home)

        ###### DEPOSIT  PAGE ######
        # Lables
        self.deposit_label_1 = Label(self.user_deposit_page,
                                     text='Enter your name: ')

        # Entry
        self.deposit_entry_1 = Entry(
            self.user_deposit_page, text=self.user.name)

        # Buttons
        self.deposit_submit_button = Button(
            self.user_deposit_page, text="Submit", command=self.deposit)

        self.deposit_home_button = Button(self.user_deposit_page,
                                          text="Cancel", command=lambda: self.return_logged_menu(self.user_deposit_page))

        ###### Withdraw  PAGE ######
        # Lables
        self.withdraw_label_1 = Label(self.user_withdraw_page,
                                      text='Enter your name: ')

        # Entry
        self.withdraw_entry_1 = Entry(
            self.user_withdraw_page, text=self.user.name)

        # Buttons
        self.withdraw_submit_button = Button(
            self.user_withdraw_page, text="Submit", command=self.widthdraw)

        self.withdraw_home_button = Button(self.user_withdraw_page,
                                           text="Cancel", command=lambda: self.return_logged_menu(self.user_withdraw_page))

        ###### SEND MONEY PAGE ######
        # Lables
        self.send_label_1 = Label(self.user_send_page,
                                  text='Enter your name: ')
        self.send_label_2 = Label(self.user_send_page,
                                  text='Enter your PIN: ')

        # Entry
        self.send_entry_1 = Entry(self.user_send_page)
        self.send_entry_2 = Entry(self.user_send_page, show='*')

        # Buttons
        self.send_submit_button = Button(
            self.user_send_page, text="Submit", command=self.send_submit)

        self.send_home_button = Button(self.user_send_page,
                                       text="Cancel", command=lambda: self.return_logged_menu(self.user_send_page))

        ###### EDIT PERSONAL DETAIL PAGE ######
        # Lables
        self.edit_label_1 = Label(self.user_edit_page,
                                  text='Enter your name: ')
        self.edit_label_2 = Label(self.user_edit_page,
                                  text='Enter your PIN: ')

        # Entry
        self.edit_entry_1 = Entry(self.user_edit_page, text=self.user.name)
        self.edit_entry_2 = Entry(self.user_edit_page, show='*')

        # Buttons
        self.edit_submit_button = Button(
            self.user_edit_page, text="Submit", command=self.edit_info)

        self.edit_home_button = Button(self.user_edit_page,
                                       text="Cancel", command=lambda: self.return_logged_menu(self.user_edit_page))

        ###### DELETE PAGE ######
        # Labels
        self.delete_entry_1 = Label(
            self.user_delete_page, text='Woudl you like to delete your account? \nThink about it again!!!!')

        # Buttons
        self.delete_yes_button = Button(
            self.user_delete_page, text='YES', command=self.delete_account)
        self.delete_no_button = Button(
            self.user_delete_page, text="No", command=lambda: self.return_logged_menu(self.user_delete_page))


root = Tk()
app = UI_Class(root)
app.mainloop()
