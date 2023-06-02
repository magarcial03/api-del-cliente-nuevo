from flask import Blueprint, render_template, request
from .models import Clausula
from flask_wtf import FlaskForm
from wtforms import  SelectMultipleField, SubmitField, validators, widgets


docs = Blueprint('documentos', __name__)

@docs.get("/clausulas")
def consulta_clausulas():
    return render_template('clausulas.html', 
        clausulas=Clausula.query.all())

@docs.get('/formulario')
def presenta_formulario():
    elementos = [(item.id, item.descripcion) for item in Clausula.query.all()]
    print(elementos)
    class FormularioOpciones(FlaskForm):
        choices = SelectMultipleField(
            widget = widgets.ListWidget(prefix_label=False),
            option_widget = widgets.CheckboxInput(),
            choices = elementos)
        submit = SubmitField()
    formulario = FormularioOpciones()
    return render_template('opciones.html', form=formulario)

@docs.post('/clausulas')
def presenta_clausulas():
    clausulas = ([Clausula.query.filter_by(id=int(item)).first() for item in request.form.getlist("choices")])
    return render_template('clausulas.html', 
        clausulas=clausulas)