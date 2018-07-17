from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import ValidationError, DataRequired

class MatkulSave(FlaskForm):
    msg = 'Data tidak boleh Kosong'
    kode = StringField('Kode', validators=[DataRequired(message=msg)])
    nama = StringField('Nama', validators=[DataRequired(message=msg)])
    sks = StringField('SKS', validators=[DataRequired(message=msg)])
    semester = StringField('Semester', validators=[DataRequired(message=msg)])
    dosen = StringField('Dosen Pengampu', validators=[DataRequired(message=msg)])
    submit = SubmitField('Simpan')

class MatkulAmbil(FlaskForm):
    msg = 'Data tidak boleh Kosong'
    kode = StringField('Kode', validators=[DataRequired(message=msg)])
    nama = StringField('Nama', validators=[DataRequired(message=msg)])
    sks = StringField('SKS', validators=[DataRequired(message=msg)])
    semester = StringField('Semester', validators=[DataRequired(message=msg)])
    dosen = StringField('Dosen Pengampu', validators=[DataRequired(message=msg)])
    submit = SubmitField('Ambil')
