from tkinter import messagebox
import pymongo
import random


class User():

    uri = 'mongodb+srv://abuzer33:Asude1608.@cluster0.wqgsj.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'

    def __init__(self):
        self.name = ''
        self.pin = ''
        self.balance = ''
        self.account_num = ''

    def login(self, user_name, acc_num, pin):

        return False

    def check_user(self, acc_num):
        pass

    def send_money(self, to_acc_num, amount):
        pass

    def create_user(self, name, balance, pin):
        self.account_num = random.randint(1000000, 100000001)
        client = pymongo.MongoClient(self.uri)

        atm_db = client.atm_project
        accounts = atm_db.accounts

        result = accounts.insert_one(
            {"name": name, "balance": balance, "pin": pin, "account_number": self.account_num})

        if result.acknowledged:
            return True

    def update_balance(self, operation_type, acc_num, amount):
        return

    def update_info(self, name, pin):
        pass

    def fetch_accounts(self):
        client = pymongo.MongoClient(self.uri)

        atm_db = client.atm_project
        accounts = atm_db.accounts

        results = accounts.find()
        for result in results:
            print(account)

    def remove_account(self):
        pass
