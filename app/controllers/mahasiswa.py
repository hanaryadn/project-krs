from flask import url_for, redirect, render_template, flash
from app.forms.mahasiswa import MahasiswaSave
from app.forms.login import LoginMhs
from app.forms.matkul import MatkulAmbil
from app.models.models import Mahasiswa, Matkul, Krs
from flask_login import current_user, login_user, logout_user, login_required
from flask import request
from werkzeug.urls import url_parse
from app import db

class MahasiswaController:
    # Index
    def index(self):
        mahasiswasave = MahasiswaSave
        mahasiswa = Mahasiswa().getAll()
        return render_template('mahasiswa/index.html', title='Info Mahasiswa', form=mahasiswasave, mahasiswa=mahasiswa)
    
    # Input
    def input(self):
        mahasiswasave = MahasiswaSave()
        if mahasiswasave.validate_on_submit():
            mahasiswa = Mahasiswa(npm=mahasiswasave.npm.data, nama=mahasiswasave.nama.data, ttl= mahasiswasave.ttl.data, kelamin= mahasiswasave.kelamin.data, alamat=mahasiswasave.alamat.data, jurusan=mahasiswasave.jurusan.data, pa=mahasiswasave.pa.data)
            mahasiswa.set_password(mahasiswasave.password.data)
            mahasiswa.save()
            return redirect(url_for('lihat_mahasiswa'))
        return render_template('mahasiswa/input.html', form = mahasiswasave, title='Input Mahasiswa')
   
    # Lihat
    def lihat_mahasiswa(self):  
        mahasiswasave = MahasiswaSave()      
        mahasiswa = Mahasiswa().getAll()
        return render_template('mahasiswa/lihat.html', form = mahasiswasave, title='Lihat Mahasiswa' , mahasiswa=mahasiswa)


    # Edit
    def edit(self, id):
        mahasiswasave = MahasiswaSave()
        mahasiswa = Mahasiswa().getOne(id)
        if mahasiswasave.validate_on_submit():
            mahasiswa.nama = mahasiswasave.nama.data
            mahasiswa.ttl = mahasiswasave.ttl.data
            mahasiswa.kelamin = mahasiswasave.kelamin.data
            mahasiswa.alamat = mahasiswasave.alamat.data
            mahasiswa.jurusan = mahasiswasave.jurusan.data
            mahasiswa.pa = mahasiswasave.pa.data
            db.session.commit()
            return redirect(url_for('lihat_mahasiswa'))
        return render_template('mahasiswa/edit.html', title='Edit Mahasiswa', form=mahasiswasave, mahasiswa=mahasiswa)

    # Abmil
    def ambil(self, id):
        matkul = Matkul().getAll()
        return render_template('krs/index.html', title='KRS', matkul=matkul)
    
    def lihat(self):
        krs = Krs().getAll()
        return render_template('krs/lihat.html', title='Lihat KRS', krs=krs)

    # Delete
    def delete(self, id):
        mahasiswa = Mahasiswa().getOne(id)
        mahasiswa.delete()
        return redirect(url_for('lihat_mahasiswa'))
    
    def login(self):
        if current_user.is_authenticated:
            return redirect(url_for('index_mahasiswa'))
        form = LoginMhs()
        if form.validate_on_submit():
            mahasiswa = Mahasiswa.query.filter_by(npm=form.npm.data).first()
            if mahasiswa is None or not mahasiswa.check_password(form.password.data):
                flash('Username atau Password Salah')
                return redirect(url_for('login'))
            login_user(mahasiswa, remember=form.remember_me.data)
            next_page = request.args.get('next')
            if not next_page or url_parse(next_page).netloc != '':
                next_page = url_for('index_mahasiswa')
            return redirect(next_page) 
            return redirect(url_for('index_mahasiswa'))
        return render_template('login.html', title='Log In', form=form)
