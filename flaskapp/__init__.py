from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
# REMEMBER TO MAKE AN ENVIRONMENT VARIABLE AT PRODUCTION!
app.config['SECRET_KEY'] = '1aa37a53492185cad4fdadd2793bef9b'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'routes_login'
login_manager.login_message_category = 'info'

from flaskapp import routes  # noqa: E402, F401