from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Clausula(db.Model):
    __tablename__ = 'clausula'
    id = db.Column(db.Integer, primary_key=True)
    descripcion = db.Column(db.String(20), unique=True, nullable=False)
    contenido = db.Column(db.String, nullable=False)