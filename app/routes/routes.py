from app import app
from flask import url_for, redirect, render_template, flash
from app.controllers.mahasiswa import MahasiswaController
from app.controllers.matkul import MatkulController
from app.controllers.krs import KrsController
from app.controllers.user import UserController
# Login
from flask_login import current_user, login_user, logout_user, login_required
from app.models.models import User, Mahasiswa
from app.forms.login import LoginForm, LoginMhs
from flask import request
from werkzeug.urls import url_parse

# Login sbg Index
@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def login():
    return MahasiswaController().login()
# Logout
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))
#----------------------------------------------------------------------------#
@app.route('/mahasiswa', methods=['GET', 'POST'])

# Mahasiswa
def index_mahasiswa():
    return MahasiswaController().index()

# Input Mhs
@app.route('/mahasiswa/input', methods=['GET','POST'])

def input_mahasiswa():
    return MahasiswaController().input()

# Lihat Mhs
@app.route('/mahasiswa/lihat', methods=['GET','POST'])

def lihat_mahasiswa():
    return MahasiswaController().lihat_mahasiswa()

# Edit
@app.route('/mahasiswa/<id>/edit', methods=['POST', 'GET'])

def edit_mahasiswa(id):
    return MahasiswaController().edit(id)

# Ambil------------------------------------------------------#
@app.route('/krs/<id>/index', methods=['POST', 'GET'])

def krs_mahasiswa(id):
    return MahasiswaController().ambil(id)
#--------------------------------------------------------#
# Delete
@app.route('/mahasiswa/<id>/delete')
def delete_mahasiswa(id):
    return MahasiswaController().delete(id)

#-----------------------------------------------------------#
@app.route('/matkul', methods=['GET', 'POST'])

# View Matkul
def index_matkul():
    return MatkulController().index()

# Edit
@app.route('/matkul/<id>/edit', methods=['POST', 'GET'])

def edit_matkul(id):
    return MatkulController().edit(id)

# Input
@app.route('/matkul/input', methods=['POST', 'GET'])

def input_matkul():
    return MatkulController().input()

#Ambil MK
@app.route('/krs/<id>/info', methods=['POST', 'GET'])

def ambil_matkul(id):
    return MatkulController().ambil(id)

#Lihat KRS
@app.route('/krs/lihat', methods=['POST', 'GET'])

def lihat_krs():
    return MatkulController().lihat(id)

#Hapus Krs
@app.route('/krs/<id>/delete')
def hapus_matkul(id):
    return MatkulController().hapus_matkul(id)

# Delete
@app.route('/matkul/<id>/delete')
def delete_matkul(id):
    return MatkulController().delete(id)

#--------------------------------------------------------------#
# Admin
@app.route('/admin/login', methods=['GET', 'POST'])
def login_admin():
   return UserController().login_admin()
# Logout
@app.route('/logout_admin')
def logout_admin():
    logout_user()
    return redirect(url_for('login_admin'))
#------------------------------------
@app.route('/admin', methods=['GET', 'POST'])
@login_required
def index_admin():
    return render_template('admin/index.html', title='Admin Panel')
#Input
@app.route('/admin/input', methods=['GET', 'POST'])

def input_admin():
    return UserController().input()
# Delete
@app.route('/matkul/<id>/delete')
def delete_admin(id):
    return UserController().delete(id)