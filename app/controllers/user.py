from flask import url_for, redirect, render_template, flash
from app.forms.user import UserForm
from app.forms.login import LoginForm
from app.models.models import User
from flask_login import current_user, login_user, logout_user, login_required
from flask import request
from werkzeug.urls import url_parse
from app import db

class UserController:
    def input(self):
        form = UserForm()
        if form.validate_on_submit():
            user = User(nama=form.nama.data, username=form.username.data)
            user.set_password(form.password.data)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('input_admin'))    
        user = User().getAll()
        return render_template('admin/input.html', form = form, title='Input Admin', user=user)

    def delete(self, id):
        user = User().getOne(id)
        user.delete()
        return redirect(url_for('input_admin'))        
    
    def login_admin(self):
        if current_user.is_authenticated:
            return redirect(url_for('index_admin'))
        form = LoginForm()
        if form.validate_on_submit():
            user = User.query.filter_by(username=form.username.data).first()
            if user is None or not user.check_password(form.password.data):
                flash('Username atau Password Salah')
                return redirect(url_for('login_admin'))
            login_user(user, remember=form.remember_me.data)
            next_page = request.args.get('next')
            if not next_page or url_parse(next_page).netloc != '':
                next_page = url_for('index_admin')
            return redirect(next_page) 
            return redirect(url_for('index_admin'))
        return render_template('admin/login.html', title='Log In Admin', form=form)
