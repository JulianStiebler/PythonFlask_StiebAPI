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
    image_file = url_for('static', filename='profile_pics/' + current_user.image_file)
    return render_template('pages/user/account.html', 
                           title='Profile', image_file=image_file, posts=posts)


def save_picture(form_picture):
    """ 
        Create a random filename, split it by extension, store random generated 
        filename + the extension in picture_fn and join it with app.root_path/static
    """
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/profile_pics', picture_fn)

    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_fn


@app.route("/user/settings", methods=['GET', 'POST'])
@login_required
def routes_account_settings():
    form = forms_account_update()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Account information succesfully updated.', 'success')
        return redirect(url_for('routes_account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    image_file = url_for('static', filename='profile_pics/' + current_user.image_file)
    return render_template('pages/user/settings.html', 
                           title='Settings', 
                           image_file=image_file, posts=posts, form=form)

@app.route("/dashboard/") 
@login_required
def routes_dashboard():
    return render_template('pages/dashboard.html', title='Dashboard')