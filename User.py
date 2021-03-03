from tkinter import messagebox
import glob
import os


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

        file_name = acc_num+'.txt'

        all_accounnts = os.listdir()
        for file in all_accounnts:
            if file_name == file:
                with open(file, 'r') as f:
                    lines = f.readlines()

                    if user_name == lines[0][:-1]:
                        if lines[1][:-1] == pin:
                            if lines[3] == acc_num:
                                self.balance = int(lines[2][:-1])
                                return True
                    else:
                        return "Informations entered doesn't match"

        return False

    def check_user(self, acc_num):
        file_name = acc_num+'.txt'

        all_accounnts = os.listdir()
        for file in all_accounnts:
            if file_name == file:
                return True
        else:
            return False

    def send_money(self, to_acc_num, amount):
        if self.check_user(to_acc_num):
            balance = self.update_balance('deposit', to_acc_num, amount)
            self.update_balance('withdraw', self.account_num, amount)
            return balance
        else:
            messagebox.showinfo("Operation is not Successfully done",
                                'User you tried to send is not in our system')
            return False

    def create_user(self, name, balance, pin):
        self.name = name
        self.balance = balance
        self.pin = pin

        self.save_file()

    def update_balance(self, operation_type, acc_num, amount):

        with open(str(acc_num)+'.txt', 'r+') as f:
            lines = f.readlines()

            if operation_type == 'deposit':
                balance = int(lines[2][:-1]) + int(amount)
            elif operation_type == 'withdraw':
                balance = int(lines[2][:-1]) - int(amount)

            lines[2] = str(balance) + '\n'

        with open(str(acc_num) + '.txt', 'w') as f:
            f.writelines(lines)

        return balance

    def update_info(self, name, pin):
        with open(str(self.account_num)+'.txt', 'w') as f:
            f.write(name + '\n')
            f.write(pin+'\n')
            f.write(str(self.balance)+'\n')
            f.write(str(self.account_num))

    def save_file(self):
        with open('Account_rec.txt', 'r+') as f:
            accnt_n = int(f.readlines()[-1])
            new_accnt_n = accnt_n + 1
            self.account_num = new_accnt_n
            f.write('\n'+str(new_accnt_n))

        with open(str(self.account_num)+'.txt', 'w') as f:
            f.write(self.name + '\n')
            f.write(self.pin+'\n')
            f.write(self.balance+'\n')
            f.write(str(self.account_num))

    def remove_account(self):
        os.remove(self.account_num+'.txt')
