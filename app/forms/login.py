from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import ValidationError, DataRequired


class LoginForm(FlaskForm):
    msg = 'Data tidak boleh Kosong'
    username = StringField('Username', validators=[DataRequired(message=msg)])
    password = PasswordField('Password', validators=[DataRequired(message=msg)])
    remember_me = BooleanField('Ingat Saya!')
    submit = SubmitField('Login')

class LoginMhs(FlaskForm):
    msg = 'Data tidak boleh Kosong'
    npm = StringField('NPM', validators=[DataRequired(message=msg)])
    password = PasswordField('Password', validators=[DataRequired(message=msg)])
    remember_me = BooleanField('Ingat Saya!')
    submit = SubmitField('Login')