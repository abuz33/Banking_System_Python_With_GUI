
class Account:
    account_num = 544450

    def __init__(self, user_id, balance,  account_number):
        self.user_id = user_id
        self.balance = balance
<<<<<<< HEAD
        self.account_number = self.account_num
        Account.account_num += 1
=======
        self.account_number = randint(self.range_start, self.range_end)

        for num in Account.account_nums:
            if self.account_number == num:
                self.account_number = randint(self.range_start, self.range_end)

>>>>>>> 43b53da0065f34ca635319f9956862177950b849

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

    def create_account(self):
        with open("accounts", "r+") as f:
            f.writelines(self.user_id+" " + self.balance+" "+self.account_number)
