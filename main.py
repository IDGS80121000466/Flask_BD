from flask import Flask, render_template, request, send_from_directory
from forms import UserForm, PuntosForm
from flask import flash
from flask_wtf.csrf import CSRFProtect
from config import DevelopmentCongig
from flask import g

import os
import forms


app = Flask(__name__)
app.secret_key = 'esta es mi clave secreta'
app.config.from_object(DeprecationWarning)
csrf=CSRFProtect()

@app.errorhandler(404)
def page_not_fouund(e):
    return render_template('404.html'),404

@app.route("/")
def index():
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


@app.route("/static/bootstrap/css/<path:filename>")
def send_css(filename):
    return send_from_directory(os.path.join(app.root_path, 'static', 'bootstrap', 'css'), filename, mimetype='text/css')


if __name__ == "__main__":
    csrf.init_app(app)
    app.run()
