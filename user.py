import bcrypt
import sqlite3
conn = sqlite3.connect('riditDB.db')
cursor = conn.cursor()

class User:

    def __init__(self, username, password, name, email, phoneNumber):
        self.username = hash(username)
        self.password = self.hash(password)
        self.name = name
        self.email = email
        self.phoneNumber = phoneNumber

    @classmethod
    def from_db(cls, username, password):
        hash_pass = cls.hash(password)
        hash_user = cls.hash(username)
        userData = cursor.execute(f"SELECT * FROM users WHERE username = {hash_user}, password = {hash_pass}")
        return True


    def hash(self, input):
        byteWord = input.encode('UTF-8')
        salt = bcrypt.gensalt()
        hashWord = bcrypt.hashpw(byteWord, salt)
        return hashWord

    def add_user_to_db(self):
