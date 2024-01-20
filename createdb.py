from flaskapp import db, app
from flaskapp.models import User, Post

with app.app_context():
    db.create_all()