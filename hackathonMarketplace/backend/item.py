import bcrypt
import sqlite3
import hackathonMarketplace.backend.user as User
import smtplib
from email.message import EmailMessage

conn = sqlite3.connect('riditDB.db')
cursor = conn.cursor()

class Item:
    # constructor from form
    def __init__(self, name, image, price, type, email, password, itemID):
        self.name = name
        self.image = image
        self.price = price
        self.type = type
        self.userID = User.from_db(username, password).get_userID()
        self.itemID = itemID

    # constructor from database
    # returns item
    @classmethod
    def create_from_db(cls, name, userID):
        cursor.execute(f"SELECT * FROM item WHERE name = {name} AND userID = {userID}")
        data = cursor.fetchone()
        listing = cls(data[5], data[1], data[2], data[3], data[4], data[0])
        return listing

    # functions

    # adds item to the database
    def add_to_db(cls):
        cursor.execute(f"INSERT INTO item (name, image, price, userID) VALUES (self.name, self.image, self.price, self.user.userID)")
        return True

    # removes item from database
    def remove_from_db(cls, itemID):
        if cursor.execute(f"DELETE FROM item WHERE itemID = {itemID}"):
            return True
        else:
            return False

    def purchase_request(self, purchaser, message):
        sellerEmail = self.get_email()
        purchaserEmail = purchaser.get_email()
        msg = EmailMessage()
        msg["subject"] = "Hackathon Marketplace Item Purchase Request"
        msg["from"] = "ridituvm@gmail.com"
        msg["to"] = sellerEmail, purchaserEmail
        msg.set_content(message)
        with smtplib.SMTP("smtp.gmail.com", 465) as smtp:
            smtp.login("ridituvm@gmail.com", "p4ssw0rd!41")
            smtp.send_message(msg)


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