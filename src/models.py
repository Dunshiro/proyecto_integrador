from sqlalchemy import Column, ForeignKey, Integer, String, Date, DECIMAL
from sqlalchemy.orm import relationship

from .database import Base

class Usuario(Base):
    __tablename__ = "usuario"

    idUsuario = Column(Integer, primary_key=True, index=True)
    dni = Column(String(20), unique=True, index=True)
    nombres = Column(String(100))
    apellidos = Column(String(100))
    telefono = Column(String(20))
    correo = Column(String(100), unique=True, index=True)
    password = Column(String(255))
    idRol = Column(Integer, ForeignKey("rol.idRol"))
    idJefePrestamista = Column(Integer, ForeignKey("usuario.idUsuario"))
    idGrupo = Column(Integer, ForeignKey("grupo.idGrupo"))
    fechaRegistro = Column(Date)

    # Definir la relación con el rol
    rol = relationship("Rol", back_populates="usuarios")

    # Definir la relación con el jefe prestamista
    jefe_prestamista = relationship("Usuario", back_populates="empleados", remote_side=[idUsuario])
    
    # Definir la relación con los empleados (solo para jefes prestamistas)
    empleados = relationship("Usuario", back_populates="jefe_prestamista", cascade="all, delete")

    # Definir la relación con el grupo
    grupo = relationship("Grupo", back_populates="usuarios")

class Rol(Base):
    __tablename__ = "rol"

    idRol = Column(Integer, primary_key=True, index=True)
    rol = Column(String(50), unique=True, index=True)

    # Definir la relación con los usuarios
    usuarios = relationship("Usuario", back_populates="rol")

class Grupo(Base):
    __tablename__ = "grupo"

    idGrupo = Column(Integer, primary_key=True, index=True)
    nombreGrupo = Column(String(100))
    idJefePrestamista = Column(Integer, ForeignKey("usuario.idUsuario"))

    # Definir la relación con los usuarios
    usuarios = relationship("Usuario", back_populates="grupo")

    # Definir la relación con el jefe prestamista
    jefe_prestamista = relationship("Usuario", back_populates="grupos")

class Prestamo(Base):
    __tablename__ = "prestamo"

    idPrestamo = Column(Integer, primary_key=True, index=True)
    monto = Column(DECIMAL(10, 2))
    fechaInicio = Column(Date)
    fechaFin = Column(Date)
    dias = Column(Integer)
    pagoDiario = Column(DECIMAL(10, 2))
    idPrestatario = Column(Integer, ForeignKey("usuario.idUsuario"))
    fechaRegistro = Column(Date)

    # Definir la relación con el prestatario
    prestatario = relationship("Usuario", back_populates="prestamos")