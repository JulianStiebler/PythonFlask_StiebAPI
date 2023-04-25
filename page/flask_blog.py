from flask import Flask, render_template, flash, redirect, url_for
from forms import forms_register, forms_login
app = Flask(__name__)

# REMEMBER TO MAKE AN ENVIRONMENT VARIABLE AT PRODUCTION!
app.config['SECRET_KEY'] = '1aa37a53492185cad4fdadd2793bef9b'

posts = [
    {
        'author': 'Max Mustermann',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'Yesterday'
    },
    {
        'author': 'Max Mustermann',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'Today'
    }
]
title = 'Main'

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

