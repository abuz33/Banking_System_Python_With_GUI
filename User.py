class User:
    user_id = 0

    def __init__(self, name, birth_date, phone_number, email, password):
        self.name = name
        self.birth_date = birth_date
        self.phone_number = phone_number
        self.email = email
        self.password = password
        self.user_id = self.user_id
        User.user_id += 1

        with open("users", "r+") as f:
            f.write(name, birth_date, phone_number, email, password)
