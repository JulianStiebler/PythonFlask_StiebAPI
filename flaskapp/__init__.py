# Created by: Julian Stiebler, 05.05.2023"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_minify import Minify

"""
Initiliaze the app and append some config, pass it to DB and start Flask-Migrate,
add BCrypt and LoginManager and then add Limiter and minify.
"""
app = Flask(__name__)
app.config['SECRET_KEY'] = '1aa37a53492185cad4fdadd2793bef9b'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'routes_login'
login_manager.login_message_category = 'info'
Minify(app=app, html=True, js=True, cssless=True, static=True)


"""
Since we need to avoid circular imports we are forced to import
routes after we created App, and we are not going to do anything
more here, so we need to ignore two Ruff-errors.
(Import not at Header-Level & import routes not used)
"""
from flaskapp import routes  # noqa: E402, F401