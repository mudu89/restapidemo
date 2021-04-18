from restapi import db
from base64 import decode

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)
    lastlogin = db.Column(db.DateTime, nullable=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.lastlogin}')"
