from pydantic import BaseModel
from typing import Optional

class UsuarioBase(BaseModel):
    dni: str
    nombres: str
    apellidos: str
    correo: str
    password: str
    fechaNacimiento: date
    rol: str
    jefe_id: Optional[int] = None
    

class UsuarioCreate(UsuarioBase):
    pass

class Usuario(UsuarioBase):
    id: int
    class Config:
        orm_mode = True

class GrupoBase(BaseModel):
    nombre: str
    jefe_id: int

class GrupoCreate(GrupoBase):
    pass

class Grupo(GrupoBase):
    id: int
    class Config:
        orm_mode = True

class LocalBase(BaseModel):
    nombre: str
    grupo_id: int
    prestamista_id: int

class LocalCreate(LocalBase):
    pass

class Local(LocalBase):
    id: int
    class Config:
        orm_mode = True

class PrestamoBase(BaseModel):
    monto: float
    fecha_inicio: date
    fecha_fin: date
    dias: int
    pago_diario: float
    prestatario_id: int

class PrestamoCreate(PrestamoBase):
    pass

class Prestamo(PrestamoBase):
    id: int
    class Config:
        orm_mode = True
