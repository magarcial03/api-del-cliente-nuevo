from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
from .models import Clausula

class ClausulaSchema(SQLAlchemySchema):
    class Meta:
        model = Clausula
        load_instance = True
    
    id = auto_field
    descripcion = auto_field
    contenido = auto_field