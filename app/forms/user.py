from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import ValidationError, DataRequired


class UserForm(FlaskForm):
    msg = 'Data tidak boleh Kosong'
    nama = StringField('Nama', validators=[DataRequired(message=msg)])
    username = StringField('Username', validators=[DataRequired(message=msg)])
    password = PasswordField('Password', validators=[DataRequired(message=msg)])
    remember_me = BooleanField('Ingat Saya!')
    submit = SubmitField('Login')