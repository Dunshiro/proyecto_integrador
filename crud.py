from sqlalchemy.orm import Session
from . import models, schemas

def get_user_by_email(db: Session, email: str):
    return db.query(models.Usuario).filter(models.Usuario.email == email).first()

def create_user(db: Session, user: schemas.UsuarioCreate):
    hashed_password = pwd_context.hash(user.password)
    db_user = models.Usuario(password=hashed_password, **user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def create_grupo(db: Session, grupo: schemas.GrupoCreate):
    db_grupo = models.Grupo(**grupo.dict())
    db.add(db_grupo)
    db.commit()
    db.refresh(db_grupo)
    return db_grupo

def create_local(db: Session, local: schemas.LocalCreate):
    db_local = models.Local(**local.dict())
    db.add(db_local)
    db.commit()
    db.refresh(db_local)
    return db_local

def create_prestamo(db: Session, prestamo: schemas.PrestamoCreate):
    db_prestamo = models.Prestamo(**prestamo.dict())
    db.add(db_prestamo)
    db.commit()
    db.refresh(db_prestamo)
    return db_prestamo

##
def get_usuario(db: Session, usuario_id: int):
    return db.query(models.Usuario).filter(models.Usuario.id == usuario_id).first()

def get_grupo(db: Session, grupo_id: int):
    return db.query(models.Grupo).filter(models.Grupo.id == grupo_id).first()

def get_local(db: Session, local_id: int):
    return db.query(models.Local).filter(models.Local.id == local_id).first()

def get_prestamo(db: Session, prestamo_id: int):
    return db.query(models.Prestamo).filter(models.Prestamo.id == prestamo_id).first()

##
def update_usuario(db: Session, usuario_id: int, usuario: schemas.UsuarioCreate):
    db_user = db.query(models.Usuario).filter(models.Usuario.id == usuario_id).first()
    if db_user is None:
        return None
    for key, value in usuario.dict().items():
        setattr(db_user, key, value)
    db.commit()
    db.refresh(db_user)
    return db_user

def update_grupo(db: Session, grupo_id: int, grupo: schemas.GrupoCreate):
    db_grupo = db.query(models.Grupo).filter(models.Grupo.id == grupo_id).first()
    if db_grupo is None:
        return None
    for key, value in grupo.dict().items():
        setattr(db_grupo, key, value)
    db.commit()
    db.refresh(db_grupo)
    return db_grupo

def update_local(db: Session, local_id: int, local: schemas.LocalCreate):
    db_local = db.query(models.Local).filter(models.Local.id == local_id).first()
    if db_local is None:
        return None
    for key, value in local.dict().items():
        setattr(db_local, key, value)
    db.commit()
    db.refresh(db_local)
    return db_local

def update_prestamo(db: Session, prestamo_id: int, prestamo: schemas.PrestamoCreate):
    db_prestamo = db.query(models.Prestamo).filter(models.Prestamo.id == prestamo_id).first()
    if db_prestamo is None:
        return None
    for key, value in prestamo.dict().items():
        setattr(db_prestamo, key, value)
    db.commit()
    db.refresh(db_prestamo)
    return db_prestamo

##
def delete_usuario(db: Session, usuario_id: int):
    db_user = db.query(models.Usuario).filter(models.Usuario.id == usuario_id).first()
    if db_user is None:
        return None
    db.delete(db_user)
    db.commit()
    return db_user

def delete_grupo(db: Session, grupo_id: int):
    db_grupo = db.query(models.Grupo).filter(models.Grupo.id == grupo_id).first()
    if db_grupo is None:
        return None
    db.delete(db_grupo)
    db.commit()
    return db_grupo

def delete_local(db: Session, local_id: int):
    db_local = db.query(models.Local).filter(models.Local.id == local_id).first()
    if db_local is None:
        return None
    db.delete(db_local)
    db.commit()
    return db_local

def delete_prestamo(db: Session, prestamo_id: int):
    db_prestamo = db.query(models.Prestamo).filter(models.Prestamo.id == prestamo_id).first()
    if db_prestamo is None:
        return None
    db.delete(db_prestamo)
    db.commit()
    return db_prestamo

##
def get_usuarios(db: Session):
    return db.query(models.Usuario).all()

def get_grupos(db: Session):
    return db.query(models.Grupo).all()

def get_locales(db: Session):
    return db.query(models.Local).all()

def get_prestamos(db: Session):
    return db.query(models.Prestamo).all()

##
def get_usuarios_by_rol(db: Session, rol: str):
    return db.query(models.Usuario).filter(models.Usuario.rol == rol).all()
