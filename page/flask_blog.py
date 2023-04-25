from datetime import datetime
from flask import Flask, render_template, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from forms import forms_register, forms_login

app = Flask(__name__)
# REMEMBER TO MAKE AN ENVIRONMENT VARIABLE AT PRODUCTION!
app.config['SECRET_KEY'] = '1aa37a53492185cad4fdadd2793bef9b'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"


@app.route("/")
@app.route("/home/")
def routes_home():
    return render_template('pages/home.html', title='Home')

@app.route("/register/", methods=['GET', 'POST'])
def routes_register():
    form = forms_register()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('routes_home'))
    return render_template('pages/register.html', title='Register', form=form)

@app.route("/login/", methods=['GET', 'POST'])
def routes_login():
    form = forms_login()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('routes_dashboard'))
        else:
            flash('Wrong login data!', 'danger')
    return render_template('pages/login.html', title='Login', form=form)

@app.route("/dashboard/") # 
def routes_dashboard():
    return render_template('pages/dashboard.html')

if __name__ == "__main__":
    app.run(debug=True)

