from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, \
    ValidationError
from flaskapp.models import User

from flaskapp.localization.errors import errors
from flaskapp.localization.english import form_labels as labels

class forms_register(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), 
                                                   Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), 
                                                                     EqualTo('password')])
    accepttos = BooleanField('', validators=[DataRequired()])
    submit = SubmitField(labels.account_register)

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError(errors.register_username_taken)
            
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError(errors.register_email_taken)
    
    def validate_tos(self, accepttos):
        if accepttos.data is False:
            raise ValidationError(errors.register_tos)

class forms_login(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField(labels.remember_password)
    submit = SubmitField('Login')

class forms_account_update(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), 
                                                   Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField(labels.account_update)

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError(errors.register_username_taken)

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError(errors.register_email_taken)