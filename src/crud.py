from sqlalchemy.orm import Session
from . import models, schemas

# Operaciones CRUD para la clase Usuario
def get_usuario(db: Session, usuario_id: int):
    return db.query(models.Usuario).filter(models.Usuario.idUsuario == usuario_id).first()

def get_usuarios(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Usuario).offset(skip).limit(limit).all()

def create_usuario(db: Session, usuario: schemas.UsuarioCreate):
    db_usuario = models.Usuario(**usuario.dict())
    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)
    return db_usuario

# Operaciones CRUD para la clase Rol
def get_rol(db: Session, rol_id: int):
    return db.query(models.Rol).filter(models.Rol.idRol == rol_id).first()

def get_roles(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Rol).offset(skip).limit(limit).all()

def create_rol(db: Session, rol: schemas.RolCreate):
    db_rol = models.Rol(**rol.dict())
    db.add(db_rol)
    db.commit()
    db.refresh(db_rol)
    return db_rol

# Operaciones CRUD para la clase Grupo
def get_grupo(db: Session, grupo_id: int):
    return db.query(models.Grupo).filter(models.Grupo.idGrupo == grupo_id).first()

def get_grupos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Grupo).offset(skip).limit(limit).all()

def create_grupo(db: Session, grupo: schemas.GrupoCreate):
    db_grupo = models.Grupo(**grupo.dict())
    db.add(db_grupo)
    db.commit()
    db.refresh(db_grupo)
    return db_grupo

# Operaciones CRUD para la clase Prestamo
def get_prestamo(db: Session, prestamo_id: int):
    return db.query(models.Prestamo).filter(models.Prestamo.idPrestamo == prestamo_id).first()

def get_prestamos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Prestamo).offset(skip).limit(limit).all()

def create_prestamo(db: Session, prestamo: schemas.PrestamoCreate):
    db_prestamo = models.Prestamo(**prestamo.dict())
    db.add(db_prestamo)
    db.commit()
    db.refresh(db_prestamo)
    return db_prestamo
