__author__='akishan'


class User(object):
    def __init__(self, email, password):
        self.email= email
        self.password = password

    def get_by_email(self):
        data=Database.find_one("users", {"email": self.email})
        if data is not None:
            return cls(**data)
