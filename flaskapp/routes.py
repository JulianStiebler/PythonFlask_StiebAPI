from flask import render_template, flash, redirect, url_for, request
from flaskapp import app, db, bcrypt
from flaskapp.forms import forms_register, forms_login
from flaskapp.models import User
from flask_login import login_user, current_user, logout_user, login_required

posts = [
    {
        'author': 'Max Mustermann',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 4, 2069'
    },
    {
        'author': 'Maxine Musterfrau',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 4, 2069'
    }
]

@app.route("/")
@app.route("/home/")
def routes_home():
    return render_template('pages/home.html', title='Home', posts=posts)

@app.route("/register/", methods=['GET', 'POST'])
def routes_register():
    if current_user.is_authenticated:
        return redirect(url_for('routes_dashboard'))
    form = forms_register()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data)\
            .decode('utf-8')
        user = User(username=form.username.data, 
                    email = form.email.data, 
                    password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Account created for {form.email.data}!', 'success')
        return redirect(url_for('routes_login'))
    return render_template('pages/register.html', title='Register', form=form)

@app.route("/login/", methods=['GET', 'POST'])
def routes_login():
    if current_user.is_authenticated:
        return redirect(url_for('routes_dashboard'))
    form = forms_login()
    if form.validate_on_submit():
        # Get first matching user and if theres none, return None
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) \
                if next_page else redirect(url_for('routes_dashboard'))
        else:
            flash('Wrong login data! Please check your user input.', 'danger')
    return render_template('pages/login.html', title='Login', form=form)

@app.route("/logout/")
def routes_logout():
    logout_user()
    return redirect(url_for('routes_home'))


@app.route("/account/")
@login_required
def routes_account():
    return render_template('pages/user/account.html', title='Account')

@app.route("/dashboard/") 
@login_required
def routes_dashboard():
    return render_template('pages/dashboard.html', title='Dashboard')