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

                    # print(lines)
                    if lines[0][:-1] == user_name and lines[1][:-1] == pin and lines[3] == acc_num:
                        self.balance = int(lines[2][:-1])

                        return True
                    else:
                        return "Informations entered doesn't match"

        return False

    def create_user(self, name, balance, pin):
        self.name = name
        self.balance = balance
        self.pin = pin

        self.save_file()

    def update_balance(self, operation_type, amount):
        print(str(self.balance) + 'User')

        if operation_type == 'deposit':
            self.balance += int(amount)
        elif operation_type == 'withdraw':
            self.balance -= int(amount)

        print('after ' + str(self.balance))

        with open(str(self.account_num)+'.txt', 'r+') as f:
            lines = f.readlines()
            lines[2] = str(self.balance) + '\n'

        with open(str(self.account_num) + '.txt', 'w') as f:
            f.writelines(lines)

        return True

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

    def gather_details(self):
        pass
