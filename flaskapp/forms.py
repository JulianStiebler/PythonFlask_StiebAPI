# Created by: Julian Stiebler, 05.05.2023""" 
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, \
    ValidationError
from flaskapp.models import User
from flaskapp.localization.errors import errors

## FORMS_REGISTER
class forms_register(FlaskForm):
    username = StringField('Username', 
                        validators=[DataRequired(), Length(min=6, max=30)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', 
                        validators=[DataRequired(), EqualTo('password')])
    forname = StringField('Forname', validators=[DataRequired()])
    surname = StringField('Surname', validators=[DataRequired()])
    accepttos = BooleanField('', validators=[DataRequired()])
    submit = SubmitField('Sign up')

    """ Now we also need to implement Validation Checks and raise Errors,
    they will be displayed via ValidationError into the WTForms Inputs
    and are also styled. We just check if the user or email already
    exists in our database and also just check if the ToS box is checked """ 
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

## FORMS_LOGIN
class forms_login(FlaskForm):
    email = StringField('Email',  validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Login')

## FORMS_ACCOUNT_UPDATE
class forms_account_update(FlaskForm):
    username = StringField('Username', 
                        validators=[DataRequired(),  Length(min=4, max=30)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    picture = FileField('Update Profile Picture', 
                        validators=[FileAllowed(['jpg', 'png'])])
    forname = StringField('Forname', validators=[DataRequired()])
    surname = StringField('Surname', validators=[DataRequired()])
    job = StringField('Job Description')
    region = StringField('Region')
    city = StringField('City')

    """ Now we also need to implement Validation Checks and raise Errors,
    they will be displayed via ValidationError into the WTForms Inputs
    and are also styled. We just check if the data typed in is already
    in our databas """ 
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