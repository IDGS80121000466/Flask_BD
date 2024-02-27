from wtforms import Form
from flask_wtf import FlaskForm

from wtforms import StringField, TelField, IntegerField
from wtforms.validators import Length
from wtforms import EmailField

from wtforms import validators


class UserForm(Form):
    nombre=StringField('nombre',[validators.DataRequired(message='El campo Nombre es requerido'),
                                 validators.length(min=4,max=10,message='Ingresa nombre valido')])
    apaterno=StringField('apaterno',[validators.DataRequired(message='El campo Apellido Paternoes requerido'),
                                 validators.length(min=4,max=10,message='Ingresa Apellido Paterno valido')])
    amaterno=StringField('amaterno',[validators.DataRequired(message='El campo Apellido Materno requerido'),
                                 validators.length(min=4,max=10,message='Ingresa Apellido Materno valido')])
    email=EmailField('email',[validators.Email(message='Ingrese un correo valido')])
    edad = IntegerField('edad', [validators.DataRequired(message='El campo Edad es requerido')])

class UserForm2(Form):
    id = IntegerField('id', validators=[validators.Optional(), validators.NumberRange(min=1, max=20, message='Valor no válido')])
    nombre=StringField('nombre',[validators.DataRequired(message='El campo Nombre es requerido'),
                                 validators.Length(min=4,max=10,message='Ingresa nombre valido')])
    apaterno=StringField('apaterno',[validators.DataRequired(message='El campo Apellido Paternoes requerido'),
                                 validators.Length(min=4,max=10,message='Ingresa Apellido Paterno valido')])
    email=EmailField('email',[validators.Email(message='Ingrese un correo valido')])

class PuntosForm(FlaskForm):
    x1 = IntegerField('x1')
    x2 = IntegerField('x2')
    y1 = IntegerField('y1')
    y2 = IntegerField('y2')
    resultado = IntegerField('resultado')
