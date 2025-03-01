import bcrypt
import sqlite3
conn = sqlite3.connect('riditDB.db')
cursor = conn.cursor()

class User:

    def __init__(self, userID, password, email, role= "notStudent"):
        self.userID = userID
        self.password = self.hash(password)
        self.email = email
        self.role = role

    @classmethod
    def from_db(cls, email, password):
        hash_pass = cls.hash(password)
        hash_user = cls.hash(username)
        cursor.execute("SELECT userID, password_hash, email, role FROM users WHERE email = ?", (email,))
        data = cursor.fetchone()
        if data and bcrypt.checkpw(password.encode('utf-8'), data[1].encode('utf-8')):  
            return cls(data[0], data[1], data[2], data[3])  # Return matching user
        else:
            return None
    
    @staticmethod
    def hash(password):
        byte_password = password.encode('UTF-8')
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(byte_password, salt)
        return hashed_password.decode('UTF-8')

    def retrieve_userID(cls):
        id = cursor.execute(f"SELECT userID FROM user WHERE username_hash = {cls.username}")
        
    def add_user(self):
        cursor.execute("INSERT INTO users (password_hash, email, role) VALUES (?, ?, ?)", 
                       (self.password, self.email, self.role))
        
        conn.commit()
        conn.close()
