import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# Inicializar extensiones
db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    # Configurar rutas absolutas para los templates y recursos
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    template_dir = os.path.join(base_dir, 'vista')
    static_dir = os.path.join(base_dir, 'recursos')
    
    app = Flask(__name__,
               template_folder=template_dir,
               static_folder=static_dir)
    
    # Configuración
    from app.config import Config
    app.config.from_object(Config)
    
    # Inicializar extensiones con la app
    db.init_app(app)
    login_manager.init_app(app)
    
    # Configurar LoginManager
    login_manager.login_view = 'main.login'  # Usando el nombre del blueprint
    login_manager.login_message = "Por favor inicia sesión para acceder a esta página."
    login_manager.login_message_category = 'info'
    
    # Registrar blueprints (importar aquí para evitar importaciones circulares)
    from app.routes import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    # Crear tablas de la base de datos
    with app.app_context():
        # Importar modelos dentro del contexto para evitar problemas
        from app.models import Usuario, Proyecto, Aporte
        
        @login_manager.user_loader
        def load_user(user_id):
            return Usuario.query.get(int(user_id))
            
        try:
            db.create_all()
            print("¡Tablas de la base de datos creadas correctamente!")
        except Exception as e:
            print(f"Error al crear tablas: {str(e)}")
    
    return app