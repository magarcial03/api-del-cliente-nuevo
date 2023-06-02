from flask import Flask
from .main.blueprints import docs
from .main.models import db, Clausula
from sqlalchemy import inspect
from json import load

def create_app():
    '''Función principal de la aplicación'''
    # Crear el objeto app
    app = Flask(__name__)
    
    # Obtener la configuración de la aplicación a partir de settings.py
    app.config.from_pyfile("settings.py")
    

    # Se incializa la conexión entre SQLALchemy y la base de datos
    db.init_app(app) 
    
    @app.before_first_request
    def crea_bases():
        # Verifica que exista la tabla alumno en la base de datos
        inspector = inspect(db.engine)
        if not inspector.has_table('clausula'):
            # Crea y llena la base de alumno.
            db.create_all()
            with open(app.config['PATH'] + "/../data/clausulas.json", "rt") as f:
                clausulas = load(f)
                for clausula in clausulas:
                    print(clausula)
                    if Clausula.query.filter_by(id=clausula["id"]).first():
                        continue
                    else:
                        db.session.add(Clausula(**clausula))
                db.session.commit()
                
    # Registra los blueprints con los endpoints
    app.register_blueprint(docs, url_prefix='/')
    
    #Regresa la aplicación
    return app
