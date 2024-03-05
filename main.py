from flask import Flask, render_template, request, send_from_directory, redirect,url_for
from forms import UserForm, PuntosForm
from flask import flash
from flask_wtf.csrf import CSRFProtect
from config import DevelopmentConfig
from flask import g

from models import db
from models import Alumnos

import os
import forms

app = Flask(__name__)
app.secret_key = 'esta es mi clave secreta'
app.config.from_object(DevelopmentConfig)
csrf=CSRFProtect()

@app.errorhandler(404)
def page_not_fouund(e):
    return render_template('404.html'),404

@app.route("/")
def indexx():
    return render_template("index.html")

@app.route("/alumnos2", methods=['GET', 'POST'])
def alumnos():
    print("before 2")
    nom=''
    apa=''
    ama=''
    email=''
    edad=''
    alumno_clase=forms.UserForm(request.form)
    if request.method=='POST' and alumno_clase.validate():
        nom=alumno_clase.nombre.data
        apa=alumno_clase.apaterno.data
        ama=alumno_clase.amaterno.data
        email=alumno_clase.email.data
        edad=alumno_clase.edad.data
        print('Nombre: {}'.format(nom))
        print('Apaterno: {}'.format(apa))
        print('Amaterno: {}'.format(ama))
        print('Email: {}'.format(email))
        print('Edad: {}'.format(edad))

        mensaje='Bienvenido {}'.format(nom)
        flash(mensaje)
    return render_template("alumnos2.html",form=alumno_clase,nom=nom,apa=apa,ama=ama,email=email,edad=edad)

@app.route('/index', methods=['POST', 'GET'])
def index():
    create_form = forms.UserForm2(request.form)
    if request.method == 'POST' and create_form.validate():
        alum = Alumnos(
            nombre=create_form.nombre.data,
            apaterno=create_form.apaterno.data,
            email=create_form.email.data
        )
        db.session.add(alum)
        db.session.commit()
        flash('Alumno registrado exitosamente')
    return render_template('index.html', form=create_form)

@app.route('/ABC_Completo', methods=['POST', 'GET'])
def ABCompleto():
    alum_form = forms.UserForm2(request.form)
    alumno=Alumnos.query.all()
    
    return render_template('ABC_Completo.html', alumno = alumno)

@app.route('/eliminar', methods=['POST', 'GET'])
def eliminar():
    create_form = forms.UserForm2(request.form)
    if request.method=='GET':
        id= request.args.get('id')
        # SELECT * FROM alumnos WHERE id = id
        alum1 = db.session.query(Alumnos).filter(Alumnos.id == id).first()
        create_form.id.data = request.args.get('id')
        create_form.nombre.data= alum1.nombre
        create_form.apaterno.data= alum1.apaterno
        create_form.email.data= alum1.email
    if request.method=='POST':
        id=create_form.id.data
        alum =Alumnos.query.get(id)
        #DELETE from alumnos WHERE id = id
        db.session.delete(alum)
        db.session.commit()
        return redirect(url_for('ABCompleto'))
    return render_template('eliminar.html',form=create_form)

@app.route('/modificar', methods=['POST', 'GET'])
def modificar():
    create_form = forms.UserForm2(request.form)
    if request.method=='GET':
        id= request.args.get('id')
        # SELECT * FROM alumnos WHERE id = id
        alum1 = db.session.query(Alumnos).filter(Alumnos.id == id).first()
        create_form.id.data = request.args.get('id')
        create_form.nombre.data= alum1.nombre
        create_form.apaterno.data= alum1.apaterno
        create_form.email.data= alum1.email
    if request.method=='POST':
        id=create_form.id.data
        alum1 = db.session.query(Alumnos).filter(Alumnos.id == id).first()
        alum1.nombre = create_form.nombre.data
        alum1.apaterno = create_form.apaterno.data
        alum1.email = create_form.email.data
        db.session.add(alum1)
        db.session.commit()
        return redirect(url_for('ABCompleto'))
    return render_template('modificar.html',form=create_form)




@app.route("/static/bootstrap/css/<path:filename>")
def send_css(filename):
    return send_from_directory(os.path.join(app.root_path, 'static', 'bootstrap', 'css'), filename, mimetype='text/css')


if __name__ == "__main__":
    csrf.init_app(app)
    db.init_app(app)

with app.app_context():
    db.create_all()
app.run()




