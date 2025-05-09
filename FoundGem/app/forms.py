from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, TextAreaField, DecimalField, DateField, FileField
from wtforms.validators import DataRequired, Email, EqualTo, Length, Optional


class LoginForm(FlaskForm):
    username = StringField('Usuario', validators=[DataRequired()])
    password = PasswordField('Contraseña', validators=[DataRequired()])
    submit = SubmitField('Iniciar Sesión')

class RegistroForm(FlaskForm):
    username = StringField('Nombre de usuario', 
                         validators=[DataRequired(), Length(min=4, max=64)])
    email = StringField('Email', 
                      validators=[DataRequired(), Email()])
    password = PasswordField('Contraseña', 
                           validators=[DataRequired()])
    confirm_password = PasswordField('Confirmar Contraseña', 
                                   validators=[DataRequired(), EqualTo('password')])
    universidad = StringField('Universidad', 
                            validators=[DataRequired(), Length(max=100)])
    facultad = StringField('Facultad', 
                         validators=[DataRequired(), Length(max=100)])
    rol = SelectField('Rol', 
                    choices=[
                        ('estudiante', 'Estudiante'),
                        ('docente', 'Docente'),
                        ('administrador', 'Administrador')
                    ], 
                    validators=[DataRequired()])
    submit = SubmitField('Registrarse')

class ProyectoForm(FlaskForm):
    titulo = StringField('Título', validators=[DataRequired()])
    descripcion = TextAreaField('Descripción', validators=[DataRequired()])
    categoria = SelectField('Categoría', choices=[
        ('', 'Selecciona una categoría'),
        ('Tecnología', 'Tecnología'),
        ('Educación', 'Educación'),
        ('Salud', 'Salud'),
        ('Medio Ambiente', 'Medio Ambiente'),
        ('Otro', 'Otro')
    ], validators=[DataRequired()])
    tecnologias = StringField('Tecnologías')
    meta_financiamiento = DecimalField('Meta de financiamiento', places=2, validators=[Optional()])
    fecha_limite = DateField('Fecha límite', format='%Y-%m-%d', validators=[Optional()])
    imagen = FileField('Imagen del proyecto')