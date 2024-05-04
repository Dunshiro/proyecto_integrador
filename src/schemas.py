from pydantic import BaseModel
from typing import Optional
from datetime import date

class UsuarioBase(BaseModel):
    dni: str
    nombres: str
    apellidos: str
    telefono: Optional[str] = None
    correo: str

class UsuarioCreate(UsuarioBase):
    password: str
    idRol: int
    idJefePrestamista: Optional[int] = None
    idGrupo: Optional[int] = None
    fechaRegistro: date

class Usuario(UsuarioBase):
    idUsuario: int
    idRol: int
    idJefePrestamista: Optional[int] = None
    idGrupo: Optional[int] = None
    fechaRegistro: date

    class Config:
        orm_mode = True

class RolBase(BaseModel):
    rol: str

class RolCreate(RolBase):
    pass

class Rol(RolBase):
    idRol: int

    class Config:
        orm_mode = True

class GrupoBase(BaseModel):
    nombreGrupo: str
    idJefePrestamista: int

class GrupoCreate(GrupoBase):
    pass

class Grupo(GrupoBase):
    idGrupo: int

    class Config:
        orm_mode = True

class PrestamoBase(BaseModel):
    monto: float
    fechaInicio: date
    fechaFin: date
    dias: int
    pagoDiario: float
    idPrestatario: int

class PrestamoCreate(PrestamoBase):
    pass

class Prestamo(PrestamoBase):
    idPrestamo: int
    fechaRegistro: date

    class Config:
        orm_mode = True
