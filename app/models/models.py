from app import db
from app import la
# Import Login
from app import login
from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class Mahasiswa(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    npm = db.Column(db.String(15), nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    nama = db.Column(db.String(50), nullable=False)
    ttl = db.Column(db.String(75), nullable=False)
    kelamin = db.Column(db.String(20), nullable=False)
    alamat = db.Column(db.String(50), nullable=False)
    jurusan = db.Column(db.String(20), nullable=False)
    pa = db.Column(db.String(50), nullable=False)
    created_at = db.Column(db.DATETIME, default=datetime.now())
    updated_at = db.Column(db.DATETIME, default=datetime.now())

    def save(self):
        db.session.add(self)
        db.session.commit()
    
    #View
    def getAll(self):
        return Mahasiswa.query.all()

    # Edit
    def getOne(self, id):
        return Mahasiswa.query.filter_by(id=id).first()

    # Delete
    def delete(self):
        db.session.delete(self)
        db.session.commit()
        
    # Login
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    @login.user_loader
    def load_user(id):
        return Mahasiswa.query.get(int(id))

    def __repr__(self):
        return '<id:{}>'.format(self.id)

class Matkul(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    kode = db.Column(db.String(10), nullable=False)
    nama = db.Column(db.String(25), nullable=False)
    sks = db.Column(db.Integer, nullable=False)
    semester = db.Column(db.Integer, nullable=False)
    dosen = db.Column(db.String(50), nullable=False)
    created_at = db.Column(db.DATETIME, default=datetime.now())
    updated_at = db.Column(db.DATETIME, default=datetime.now())

    def save(self):
        db.session.add(self)
        db.session.commit()

    # View
    def getAll(self):
        return Matkul.query.all()

    # Edit
    def getOne(self, id):
        return Matkul.query.filter_by(id=id).first()

    # Delete
    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return '<id:{}>'.format(self.id)

class Krs(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    kode = db.Column(db.String(10), nullable=False)
    nama = db.Column(db.String(25), nullable=False)
    sks = db.Column(db.Integer, nullable=False)
    semester = db.Column(db.Integer, nullable=False)
    dosen = db.Column(db.String(50), nullable=False)
    created_at = db.Column(db.DATETIME, default=datetime.now())
    updated_at = db.Column(db.DATETIME, default=datetime.now())

    def save(self):
        db.session.add(self)
        db.session.commit()

    # View
    def getAll(self):
        return Krs.query.all()

    # Edit
    def getOne(self, id):
        return Krs.query.filter_by(id=id).first()

    # Delete
    def delete(self):
        db.session.delete(self)
        db.session.commit()

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    nama = db.Column(db.String(50), nullable=False)
    username = db.Column(db.String(20), nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DATETIME, default=datetime.now())
    updated_at = db.Column(db.DATETIME, default=datetime.now())

    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def getAll(self):
        return User.query.all()

    def getOne(self, id):
        return User.query.filter_by(id=id).first()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    @la.user_loader
    def load_user(id):
        return User.query.get(int(id))

    def __repr__(self):
        return '<User {}>'.format(self.user)