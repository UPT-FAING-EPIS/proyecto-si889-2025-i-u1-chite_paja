from app import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class Usuario(db.Model, UserMixin):
    __tablename__ = 'usuarios'
    
    id = db.Column(db.Integer, primary_key=True)
    nombre_usuario = db.Column(db.String(64), unique=True, nullable=False)
    correo = db.Column(db.String(120), unique=True, nullable=False)
    contrasena = db.Column(db.String(128), nullable=False)
    universidad = db.Column(db.String(100), nullable=False)
    facultad = db.Column(db.String(100), nullable=False)
    rol = db.Column(db.String(50), nullable=False)
    fecha_creacion = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relaciones (mantén las que ya tienes)
    proyectos = db.relationship('Proyecto', backref='creador', lazy=True)
    aportes = db.relationship('Aporte', backref='usuario', lazy=True)
    
    def set_password(self, password):
        self.contrasena = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.contrasena, password)
    
    # Para compatibilidad con Flask-Login
    @property
    def is_active(self):
        return True
    
    def get_id(self):
        return str(self.id)
    
    def __repr__(self):
        return f'<Usuario {self.nombre_usuario}>'

class Proyecto(db.Model):
    __tablename__ = 'proyectos'
    
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(140), nullable=False)
    descripcion = db.Column(db.Text, nullable=False)
    url_imagen = db.Column(db.String(200), nullable=False)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)
    universidad = db.Column(db.String(100), nullable=False)
    departamento = db.Column(db.String(100), nullable=False)
    categoria = db.Column(db.String(50), nullable=False)
    objetivo_financiamiento = db.Column(db.Numeric(12, 2), nullable=False)
    financiamiento_actual = db.Column(db.Numeric(12, 2), default=0.00)
    fecha_limite = db.Column(db.DateTime, nullable=False)
    fecha_creacion = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relación con aportes
    aportes = db.relationship('Aporte', backref='proyecto', lazy=True,
                            cascade='all, delete-orphan')
    
    @property
    def progreso_financiamiento(self):
        """Calcula el porcentaje de financiamiento alcanzado"""
        if self.objetivo_financiamiento > 0:
            return (self.financiamiento_actual / self.objetivo_financiamiento) * 100
        return 0
    
    def __repr__(self):
        return f'<Proyecto {self.titulo}>'

class Aporte(db.Model):
    """
    Modelo de aportes a proyectos
    """
    __tablename__ = 'aportes'
    
    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)
    proyecto_id = db.Column(db.Integer, db.ForeignKey('proyectos.id'), nullable=False)
    monto = db.Column(db.Numeric(10, 2), nullable=False)
    mensaje = db.Column(db.Text)
    fecha_aporte = db.Column(db.DateTime, default=datetime.utcnow)
    anonimo = db.Column(db.Boolean, default=False)
    
    def __repr__(self):
        return f'<Aporte {self.id} - ${self.monto}>'