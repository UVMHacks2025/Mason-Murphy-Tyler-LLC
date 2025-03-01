import bcrypt
import sqlite3
conn = sqlite3.connect('riditDB.db')
cursor = conn.cursor()

class User:

    def __init__(self, userID, password, name, email):
        self.userID = userID
        self.password = password
        self.name = name
        self.email = email

    @classmethod
    def from_db(cls, username, password):
        hash_pass = cls.hash(password)
        hash_user = cls.hash(username)
        cursor.execute(f"SELECT * FROM users WHERE password_hash = {hash_pass}")
        data = cursor.fetchone()
        if data:
            return cls(data[0], data[1], data[2], f"{data[3]}  {data[4]}", data[5])
        else:
            return None


    def hash(cls, input):
        byteWord = input.encode('UTF-8')
        salt = bcrypt.gensalt()
        hashWord = bcrypt.hashpw(byteWord, salt)
        return hashWord

    def retrieve_userID(cls):
        id = cursor.execute(f"SELECT userID FROM user WHERE username_hash = {cls.username}")
        
    def add_user(cls):
        cursor.execute(f"INSERT INTO user (password_hash, email, role) VALUES ({cls.password}, {cls.email}) ")

    # getters

    def get_userID(cls):
        return cls.userID

    def get_name(cls):
        return cls.name

    def get_email(cls):
        return cls.email
