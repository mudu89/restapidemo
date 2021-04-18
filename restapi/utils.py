from restapi import db
from restapi.models import User

class UserUtils():
    @staticmethod
    def check_user(user):
        return User.query.filter_by(username=user.username).first()

    @staticmethod
    def insert_user(user):
        db.session.add(user)
        db.session.commit()

    @staticmethod
    def delete_user(user):
        db.session.delete(user)
        db.session.commit()

    # def validate_user(self, user):
    #     password =
