import bcrypt
import sqlite3
import user as User

conn = sqlite3.connect('riditDB.db')
cursor = conn.cursor()

class Item:
    # constructor from form
    def __init__(self, name, image, price, type, username, password):
        self.name = name
        self.image = image
        self.price = price
        self.type = type
        self.user = User.from_db(username, password)

    # constructor from database
    @classmethod
    def item_from_db(cls, name):
        return True

    # functions

    # adds item to the database
    def add_item_to_db(cls):
        cursor.execute(f"INSERT INTO item (name, image, price, userID) VALUES (self.name, self.image, self.price, self.user.userID)")
        return True

    # getters
    def get_name(self):
        return self.name

    def get_image(self):
        return self.image

    def get_price(self):
        return self.price

    def get_quality(self):
        return self.quality

    def get_description(self):
        return self.description

    def get_user(self):
        return self.user