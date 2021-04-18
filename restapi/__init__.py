from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from restapi.config import Config

db = SQLAlchemy()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    db.init_app(app)

    with app.app_context():
        from restapi.adduser.routes import adduser
        from restapi.delete.routes import Delete
        from restapi.login.route import login_user
        from restapi.listuser.routes import listusers
        from restapi.updateuser.routes import updateusers

        app.register_blueprint(adduser)
        app.register_blueprint(Delete)
        app.register_blueprint(login_user)
        app.register_blueprint(listusers)
        app.register_blueprint(updateusers)

        return app

