from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# REMEMBER TO MAKE AN ENVIRONMENT VARIABLE AT PRODUCTION!
app.config['SECRET_KEY'] = '1aa37a53492185cad4fdadd2793bef9b'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

from flaskapp import routes