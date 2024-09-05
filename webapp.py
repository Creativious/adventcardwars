import argparse
import os.path
import string
from datetime import datetime
import random

from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

import constants

parser = argparse.ArgumentParser()
parser.add_argument('--port', type=int, default=5000)
parser.add_argument('--debug', action='store_true')

args, _ = parser.parse_args()
app = Flask(__name__)


def log(category: str, message: str):
    os.makedirs("data/persist/logs", exist_ok=True)
    date = datetime.now().strftime("%Y-%m-%d")
    time = datetime.now().strftime("%H:%M:%S")
    with open("data/persist/logs/" + date + ".txt", "a") as f:
        log = f"{time} - [{category.upper()}] - {message} \n"
        f.write(log)


if not os.path.exists("flaskkey"):
    log("server", "Creating a new Flask secret key")
    with open("flaskkey", "w") as f:
        f.write(''.join(random.choice(string.ascii_letters + string.digits) for _ in range(50)))
app.secret_key = open("flaskkey", "r").read()
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = '/'


