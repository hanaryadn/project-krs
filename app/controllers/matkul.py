from flask import url_for, redirect, render_template
from app.forms.matkul import MatkulSave, MatkulAmbil
from app.models.models import Matkul, Mahasiswa, Krs
from app import db

class MatkulController:
    # View    
    def index(self):
        matkulsave = MatkulSave()            
        matkul = Matkul().getAll()
        return render_template('matkul/index.html', form = matkulsave, title='Input Mata Kuliah', matkul=matkul)

    # Input
    def input(self):
        matkulsave = MatkulSave()
        if matkulsave.validate_on_submit():
            matkul = Matkul(kode=matkulsave.kode.data, nama=matkulsave.nama.data, sks= matkulsave.sks.data, semester= matkulsave.semester.data, dosen=matkulsave.dosen.data)
            matkul.save()
            return redirect(url_for('index_matkul'))        
        return render_template('matkul/input.html', form = matkulsave, title='Input Mata Kuliah')

    # Edit
    def edit(self, id):
        matkulsave = MatkulSave()
        matkul = Matkul().getOne(id)
        if matkulsave.validate_on_submit():
            matkul.nama = matkulsave.nama.data
            matkul.sks = matkulsave.sks.data
            matkul.semester = matkulsave.semester.data
            matkul.dosen = matkulsave.dosen.data
            db.session.commit()
            return redirect(url_for('index_matkul'))
        return render_template('matkul/edit.html', form=matkulsave, title='Edit Mata Kuliah',matkul=matkul)
    
    # AMbil
    def ambil(self, id):
        matkulambil = MatkulAmbil()
        mahasiswa = Mahasiswa().getOne(id)
        if matkulambil.validate_on_submit():
            krs = Krs(kode=matkulambil.kode.data, nama=matkulambil.nama.data, sks= matkulambil.sks.data, semester= matkulambil.semester.data, dosen=matkulambil.dosen.data)
            krs.save()
            return redirect(url_for('lihat_krs'))
        matkul = Matkul().getOne(id)
        krs = Krs().getAll()
        return render_template('krs/info.html', form=matkulambil, title='KRS', matkul=matkul, krs=krs)

    def lihat(self, id):
        krs = Krs().getAll()
        return render_template('krs/lihat.html', title='Lihat KRS', krs=krs)
    
    def hapus_matkul(self, id):
        krs = Krs().getOne(id)
        krs.delete()
        return redirect(url_for('lihat_krs'))
        
    # Delete
    def delete(self, id):
        matkul = Matkul().getOne(id)
        matkul.delete()
        return redirect(url_for('index_matkul'))
