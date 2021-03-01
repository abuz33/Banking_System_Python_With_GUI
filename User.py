class User():
    user_id = 10000

    def __init__(self):
        self.user = {
            'name': '',
            'pin': '',
            'balance': '',
            'account_num': ''
        }

    def login(self, user_name, password, email):
        self.user['user_ame'] = user_name
        self.user['password'] = password
        self.user['email'] = email

    def create_user(self, user_name, phone, email, password):
        self.user['user_name'] = user_name
        self.user['phone'] = phone
        self.user["email"]

    def save_file(self):
        pass

    def gather_details(self):
        pass
