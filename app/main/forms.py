from flask_wtf import FlaskForm
from flask_wtf.recaptcha import validators
from wtforms import StringField,TextAreaField,SubmitField,SelectField
from wtforms.validators import Required



class PitchForm(FlaskForm):
    title = StringField('Pitch Title',validators=[Required()])
    category = SelectField(u'Pitch Category', choices = [('', 'life'), ('coding', 'coding'), ('fun', 'fun')])
    pitch = TextAreaField('pitch')
    submit = SubmitField('Submit')


class CommentForm(FlaskForm):
    comment = TextAreaField('Comment')
    Submit = SubmitField('Submit')

class Updateprofile(FlaskForm):
    bio = TextAreaField('Tell us more about you',validators=[Required])
    submit = SubmitField('Submit')
