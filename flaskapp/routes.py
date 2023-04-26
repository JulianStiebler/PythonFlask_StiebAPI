from flask import render_template, flash, redirect, url_for
from flaskapp import app
from flaskapp.forms import forms_register, forms_login
from flaskapp.models import User, Post

posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
]

@app.route("/")
@app.route("/home/")
def routes_home():
    return render_template('pages/home.html', title='Home', posts=posts)

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
            flash(f'Succesfully logged in with {form.email.data}!', 'success')
            return redirect(url_for('routes_dashboard'))
        else:
            flash(f'Wrong login data!', 'danger')
    return render_template('pages/login.html', title='Login', form=form)

@app.route("/dashboard/") # 
def routes_dashboard():
    return render_template('pages/dashboard.html')