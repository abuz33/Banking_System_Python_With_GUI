from random import randint


class Account:
    account_num = []

    def __init__(self, user_id, balance,  account_number):
        self.user_id = user_id
        self.balance = balance
        self.account_number = randint(self.range_start, self.range_end)

        for num in Account.account_nums:
            if self.account_number == num:
                self.account_number = randint(self.range_start, self.range_end)
        with open("accounts", "r+") as f:
            f.writelines(user_id+" " + balance+" "+account_number)

    def deposit_money(self, amount):
        with open("accounts", "r+") as f:
            all_lines = f.readlines()
            for line in all_lines:
                [user_ID, user_balance, account] = line
                if user_ID == self.user_id:
                    line.replace(user_balance, int(user_balance) + amount)

    def withdraw_money(self, amount):
        with open("accounts", "r+") as f:
            all_lines = f.readlines()
            for line in all_lines:
                [user_ID, user_balance, account] = line
                if user_ID == self.user_id:
                    line.replace(user_balance, int(user_balance) - amount)

    def account_overview(self, amount):
        with open("accounts", "r+") as f:
            all_lines = f.readlines()
            for line in all_lines:
                [user_ID, user_balance, account] = line
                if user_ID == self.user_id:
                    line.replace(user_balance, int(user_balance) - amount)
