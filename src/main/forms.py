from flask_wtf import FlaskForm
from wtforms import  SelectMultipleField, widgets, SubmitField, validators

class MultiCheckboxField(SelectMultipleField):
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()

class FormularioOpciones(FlaskForm):
    opciones = SelectMultipleField(validators=[validators.DataRequired()])
    submit = SubmitField
    