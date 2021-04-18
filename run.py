from restapi import create_app
from restapi.config import Config

app=create_app(Config)

if __name__ == "__main__":
    app.run()