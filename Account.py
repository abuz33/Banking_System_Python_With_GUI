
class Account:
    account_num = 544450

    def __init__(self, user_id, balance,  account_number):
        self.user_id = user_id
        self.balance = balance
        self.account_number = self.account_num
        Account.account_num += 1

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
