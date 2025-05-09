from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.utils import secure_filename
from app import db
from app.models import Usuario, Proyecto  # <-- Importa Proyecto aquí
from app.forms import LoginForm, RegistroForm, ProyectoForm
import os  # <-- Necesario para crear carpetas y guardar archivos
from datetime import datetime, timedelta

# Crear Blueprint con nombre 'main'
main = Blueprint('main', __name__)

# Configuración para subir imágenes
UPLOAD_FOLDER = 'app/static/proyectos'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    
    form = LoginForm()
    if form.validate_on_submit():
        user = Usuario.query.filter_by(nombre_usuario=form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('main.index'))
        flash('Usuario o contraseña incorrectos', 'danger')
    return render_template('autenticacion.html', form=form)

@main.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))

@main.route('/registro', methods=['GET', 'POST'])
def registro():
    form = RegistroForm()
    if form.validate_on_submit():
        user = Usuario(
            nombre_usuario=form.username.data,
            correo=form.email.data,
            universidad=form.universidad.data,
            facultad=form.facultad.data,
            rol=form.rol.data
        )
        user.set_password(form.password.data)
        try:
            db.session.add(user)
            db.session.commit()
            flash('¡Registro exitoso! Por favor inicia sesión.', 'success')
            return redirect(url_for('main.login'))
        except Exception as e:
            db.session.rollback()
            flash('Error al registrar el usuario. Por favor intenta nuevamente.', 'danger')
    
    return render_template('autenticacion.html', form=form)

@main.route('/tecnologia')
def tecnologia():
    return render_template('tecnologia.html')

@main.route('/educacion')
def educacion():
    return render_template('educacion_chat.html')

@main.route('/juegos')
def juegos():
    return render_template('juegos.html')

@main.route('/turismo')
def turismo():
    return render_template('turismo.html')

@main.route('/descubrir')
def descubrir():
    return render_template('descubrir.html')

@main.route('/innovadores', methods=['GET', 'POST'])
@login_required
def innovadores():
    if request.method == 'POST':
        try:
            # Obtener datos del formulario
            titulo = request.form.get('titulo')
            descripcion = request.form.get('descripcion')
            url_imagen = request.form.get('url_imagen')
            universidad = request.form.get('universidad')
            departamento = request.form.get('departamento')
            categoria = request.form.get('categoria')
            objetivo_financiamiento = float(request.form.get('objetivo_financiamiento'))
            
            # Establecer fecha límite automática (30 días desde hoy)
            fecha_limite = datetime.utcnow() + timedelta(days=30)
            
            # Crear nuevo proyecto
            proyecto = Proyecto(
                titulo=titulo,
                descripcion=descripcion,
                url_imagen=url_imagen,
                usuario_id=current_user.id,
                universidad=universidad,
                departamento=departamento,
                categoria=categoria,
                objetivo_financiamiento=objetivo_financiamiento,
                financiamiento_actual=0.00,  # Inicializar en 0
                fecha_limite=datetime.utcnow() + timedelta(days=30),
                fecha_creacion=datetime.utcnow()
            )
            
            # Guardar en la base de datos
            db.session.add(proyecto)
            db.session.commit()
            
            flash('¡Proyecto creado exitosamente!', 'success')
            return redirect(url_for('main.innovadores'))
            
        except Exception as e:
            db.session.rollback()
            flash(f'Error al crear el proyecto: {str(e)}', 'error')
    
    # Obtener proyectos del usuario actual
    proyectos = Proyecto.query.filter_by(usuario_id=current_user.id).all()
    return render_template('innovadores.html', proyectos=proyectos)

@main.route('/proyectos')
def proyectos():
    return render_template('proyectos.html')

@main.route('/proyecto2')
def proyecto2():
    return render_template('proyecto2.html')

@main.route('/proyecto3')
def proyecto3():
    return render_template('proyecto3.html')

@main.route('/index1')
def index1():
    return render_template('index1.html')

@main.route('/perfil')
def perfil():
    return render_template('perfil.html')

@main.route('/detalles1')
def detalles1():
    return render_template('detalles1.html')

@main.route('/detalles2')
def detalles2():
    return render_template('detalles2.html')

@main.route('/recomendacion1')
def recomendacion1():
    return render_template('recomendacion1.html')

@main.route('/recomendacion2')
def recomendacion2():
    return render_template('recomendacion2.html')

@main.route('/recomendacion3')
def recomendacion3():
    return render_template('recomendacion3.html')

@main.route('/grafico')
def grafico():
    return render_template('grafico.html')

@main.route('/notificaciones')
def notificaciones():
    return render_template('notificaciones.html')

@main.route('/usuario1')
def usuario1():
    return render_template('usuario1.html')

@main.route('/proyecto/<int:proyecto_id>')
def proyecto_detalle(proyecto_id):
    # Obtener el proyecto con el id proporcionado
    proyecto = Proyecto.query.get_or_404(proyecto_id)  # Si el proyecto no existe, lanzará un 404
    
    # Renderizar la plantilla con la información del proyecto
    return render_template('proyecto_detalle.html', proyecto=proyecto)