-- Crear la base de datos
CREATE DATABASE IF NOT EXISTS FoundGem;
USE FoundGem;

-- Crear tablas

CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre_usuario VARCHAR(64) NOT NULL UNIQUE,
    correo VARCHAR(120) NOT NULL UNIQUE,
    contrasena VARCHAR(128) NOT NULL,
    universidad VARCHAR(100) NOT NULL, 
    facultad VARCHAR(100) NOT NULL, 
    rol VARCHAR(50) NOT NULL, -- Rol (estudiante, docente, administrador)
    fecha_creacion DATETIME NOT NULL DEFAULT NOW()
);

CREATE TABLE proyectos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(140) NOT NULL,
    descripcion TEXT NOT NULL,
    url_imagen VARCHAR(200) NOT NULL,
    usuario_id INT NOT NULL,
    universidad VARCHAR(100) NOT NULL,
    departamento VARCHAR(100) NOT NULL,
    categoria VARCHAR(50) NOT NULL,
    objetivo_financiamiento DECIMAL(12, 2) NOT NULL,
    financiamiento_actual DECIMAL(12, 2) NOT NULL DEFAULT 0.00,
    fecha_limite DATETIME NOT NULL,
    fecha_creacion DATETIME NOT NULL DEFAULT NOW(),
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
);

CREATE TABLE recompensas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    proyecto_id INT NOT NULL,
    monto DECIMAL(10, 2) NOT NULL,
    descripcion TEXT NOT NULL,
    fecha_entrega DATETIME NOT NULL,
    FOREIGN KEY (proyecto_id) REFERENCES proyectos(id)
);

CREATE TABLE aportes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario_id INT NOT NULL,
    proyecto_id INT NOT NULL,
    monto DECIMAL(10, 2) NOT NULL,
    recompensa_id INT,
    fecha_creacion DATETIME NOT NULL DEFAULT NOW(),
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id),
    FOREIGN KEY (proyecto_id) REFERENCES proyectos(id),
    FOREIGN KEY (recompensa_id) REFERENCES recompensas(id)
);

CREATE TABLE actualizaciones (
    id INT AUTO_INCREMENT PRIMARY KEY,
    proyecto_id INT NOT NULL,
    titulo VARCHAR(140) NOT NULL,
    contenido TEXT NOT NULL,
    fecha_creacion DATETIME NOT NULL DEFAULT NOW(),
    FOREIGN KEY (proyecto_id) REFERENCES proyectos(id)
);
