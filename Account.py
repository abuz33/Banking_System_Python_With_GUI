from time import gmtime, strftime
import os


class Account:

    def __init__(self):
        self.name = ''
        self.balance = ''
        self.account_number = ''

    def init_account(self, name, balance, acc_num):
        self.name = name
        self.balance = balance
        self.account_number = acc_num
        with open(str(acc_num)+'-rec.txt', "w") as frec:
            frec.write(
                "Date               \t\t\t\t\tDeposit         withdraw                Balance\n")
            frec.write(str(strftime("[%Y-%m-%d] [%H-%M-%S]", gmtime())
                           )+"\t\t\t\t"+balance+'\t\t\t\t\t\t\t\t\t\t'+balance)

    def deposit_money(self, amount):
        self.balance = int(self.balance) + amount
        self.add_line_to_file(amount, 'deposit', self.account_number)
        return True

    def withdraw_money(self, amount):
        pass

    def account_overview(self, amount):

        # with open("accounts", "r+") as f:
        #     all_lines = f.readlines()
        #     for line in all_lines:
        #         [user_ID, user_balance, account] = line
        #         if user_ID == self.user_id:
        #             line.replace(user_balance, int(user_balance) - amount)
        pass

    def send_money(self, acc_num, amount):
        all_accounts = os.listdir()
        filename = acc_num + '-rec'
        for file in all_accounts:
            if filename in file:
                with open(file, 'r+') as f:
                    lines = f.readlines()
                    lines[2] = str(int(f.readlines[2]) + int(amount))
                    f.writelines(lines)

    # def save_transcations(self, acc_num, type, amount):
    #     all_accounts = os.listdir()
    #     filename = acc_num + '-rec'
    #     for file in all_accounts:
    #         if filename in file:
    #             with open(file, 'r+') as f:
    #                 lines = f.readlines()
    #                 lines[2] = str(int(f.readlines[2]) + int(amount))

    def add_line_to_file(self, amount, operation_type, acc_num):
        if operation_type == ' deposit':
            line = '\n'+str(strftime("[%Y-%m-%d] [%H-%M-%S]", gmtime())
                            )+"\t\t\t\t"+amount+'\t\t\t\t\t\t\t\t\t\t'+self.balance
        elif operation_type == 'withdraw':
            line = '\n'+str(strftime("[%Y-%m-%d] [%H-%M-%S]", gmtime())
                            )+"\t\t\t\t\t\t\t\t"+amount + "\t\t\t\t\t\t" + str(self.balance)

        all_accounts = os.listdir()
        filename = acc_num + '-rec'
        for file in all_accounts:
            if filename in file:
                with open(file, 'r+') as f:
                    f.write(line)

    def save_file(self):
        pass
