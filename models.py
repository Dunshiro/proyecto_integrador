from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date, Enum
from sqlalchemy.orm import relationship

from .database import Base
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    dni = Column(String, unique=True, index=True)
    nombres = Column(String)
    apellidos = Column(String)
    correo = Column(String, unique=True, index=True)
    password = Column(String)
    fechaNacimiento = Column(Date)
    fecha_registro = Column(Date)
    rol = Column(Enum('Inversionista', 'JefePrestamista', 'Prestamista', 'Prestatario'))
    jefe_id = Column(Integer, ForeignKey("usuarios.id"))
    
    def verify_password(self, plain_password):
        return pwd_context.verify(plain_password, self.password)
