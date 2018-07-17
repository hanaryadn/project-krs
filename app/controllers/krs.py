from flask import url_for, redirect, render_template
from app.models.models import Matkul
from app import db

class KrsController:
    def index(self):
        matkul = Matkul().getAll()
        return render_template('mahasiswa/krs.html', title='KRS', matkul=matkul)