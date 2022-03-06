from flask_wtf import FlaskForm
from flask_wtf.recaptcha import validators
from wtforms import StringField,PasswordField,BooleanField,SubmitField,ValidationError
from wtforms.validators import Email, Required,email,EqualTo
from ..models import User

class RegistrationForm(FlaskForm):
    email = StringField('your Email Address',validators=[Required(),Email()])
    author = StringField('Enter authors name',validators=[Required()])
    password = PasswordField('password',validators=[Required(),EqualTo('password_confirm',message= 'password must match')])
    password_confirm = PasswordField('confirm passwords',validators= [Required()])
    Submit = SubmitField('Sign up')

    def validate_email(self,data_field):
        if User.query.filter_by(email= data_field.data).first():
            raise ValidationError('there is an account with that email')
    def validate_author(self,data_field):
        if User.query.filter_by(author = data_field.data).first():
            raise ValidationError('that author name is already taken')
class LoginForm(FlaskForm):
    email = StringField('Enter your email address',validators=[Required(),Email()])
    password = PasswordField('Password',validators =[Required()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Sign In')