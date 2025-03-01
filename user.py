import bcrypt

class User:
    def __init__(self, username, password, name, email, phoneNumber):
        self.username = username
        self.password = self.hash_password(password)
        self.name = name
        self.email = email
        self.phoneNumber = phoneNumber

    @classmethod
    def from_db(cls, username, password):


    def hash_password(self, password):
        byteWord = password.encode('UTF-8')
        salt = bcrypt.gensalt()
        hashWord = bcrypt.hashpw(byteWord, salt)
        return hashWord

    def add_user_to_db(self):
