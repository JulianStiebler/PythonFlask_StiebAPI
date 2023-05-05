from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, \
    ValidationError
from flaskapp.models import User
from flaskapp.localization.errors import errors
from flaskapp.localization.english import form_labels as labels

"""We create a form for registration, derived from FlaskForm (Flask-WTF),
assign it some different Type of Fields and also implement Validation checks."""
class forms_register(FlaskForm):
    """Input field for username, 
    Validators: DataRequired(), Length Min 6 Max 30"""
    username = StringField(
        'Username', 
        validators=[
            DataRequired(),
            Length(min=6, max=30)
        ]
    )

    """Input field for email,
    Validators: DataRequired, Email()"""
    email = StringField(
        'Email',
        validators=[
            DataRequired(),
            Email()
        ]
    )
    
    """Input field for password, auto converts to ***
    Validators: DataRequired - we also need confirm password"""
    password = PasswordField(
        'Password',
        validators=[DataRequired()]
    )
    confirm_password = PasswordField(
        'Confirm Password',
        validators=[
            DataRequired(),
            EqualTo('password')
        ]
    )

    """Input field (Checkbox) for checking if ToS were accepted
    Validators: DataRequired"""
    accepttos = BooleanField(
        '', 
        validators=[DataRequired()
        ]
    )

    # Submit Button
    submit = SubmitField(labels.account_register)

    """Now we also need to implement Validation Checks and raise Errors,
    they will be displayed via ValidationError into the WTForms Inputs
    and are also styled. We just check if the user or email already
    exists in our database and also just check if the ToS box is checked"""
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

"""We create a form for logging in, derived from FlaskForm (Flask-WTF),
assign it some different Type of Fields and also implement Validation checks."""
class forms_login(FlaskForm):
    """Input field for email,
    Validators: DataRequired, Email()"""
    email = StringField(
        'Email', 
        validators=[
            DataRequired(), 
            Email()
        ]
    )

    """Input field for password,
    Validators: DataRequired"""
    password = PasswordField(
        'Password', 
        validators=[DataRequired()])
    
    """Input field (Checkbox) for checking if remember me is checked"""
    remember = BooleanField(labels.remember_password)
    
    # Submit Button
    submit = SubmitField('Login')

"""We create a form for updating the account, derived from FlaskForm (Flask-WTF),
assign it some different Type of Fields and also implement Validation checks."""
class forms_account_update(FlaskForm):
    """Input field for username,
    Validators: DataRequired, Email()"""
    username = StringField(
        'Username', 
        validators=[
            DataRequired(), 
            Length(min=6, max=30)
        ]
    )

    """Input field for email,
    Validators: DataRequired, Email()"""
    email = StringField(
        'Email', 
        validators=[DataRequired(), Email()])
    
    """File field for profile picture,
    Validators: FileAllowed - jpg png"""
    picture = FileField(
        'Update Profile Picture', 
        validators=[
            FileAllowed(['jpg', 'png'])
        ]
    )

    # Submit button
    submit = SubmitField(labels.account_update)

    """Now we also need to implement Validation Checks and raise Errors,
    they will be displayed via ValidationError into the WTForms Inputs
    and are also styled. We just check if the data typed in is already
    in our database"""
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