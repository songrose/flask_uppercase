from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import TextAreaField

from wtforms.validators import DataRequired, SubmitField

class RegistrationForm(FlaskForm):
    textInput = TextAreaField('TextInput', validators=[DataRequired()])
    submit = SubmitField('Enter')