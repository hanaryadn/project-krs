from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, PasswordField, SelectField
from wtforms.validators import ValidationError, DataRequired

class MahasiswaSave(FlaskForm):
    msg = 'Data tidak boleh Kosong'
    npm = StringField('NPM', validators=[DataRequired(message=msg)])
    password = StringField('Password', validators=[DataRequired(message=msg)])
    nama = StringField('Nama', validators=[DataRequired(message=msg)])
    ttl = StringField('TTL', validators=[DataRequired(message=msg)])
    kelamin = SelectField('Jenis Kelamin', choices=[('','-- Jenis Kelamin --'),('Laki-laki','Laki-laki'), ('Perempuan', 'Perempuan')], validators=[DataRequired(message=msg)])
    alamat = StringField('Alamat', validators=[DataRequired(message=msg)])
    jurusan = SelectField('Jurusan', choices=[('','-- Pilih Jurusan --'),('TI','TI'), ('SI', 'SI')], validators=[DataRequired(message=msg)])
    pa = StringField('Dosen PA', validators=[DataRequired(message=msg)])
    submit = SubmitField('Simpan')