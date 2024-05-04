from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from proyecto_integrador import schemas, models, crud
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/register", response_model=schemas.Usuario)
def create_user(user: schemas.UsuarioCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)

@app.post("/login")
def login(user: schemas.UsuarioCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user is None or not db_user.verify_password(user.password):
        raise HTTPException(status_code=400, detail="Incorrect email or password")
    return {"message": f"Welcome {db_user.nombres} {db_user.apellidos}, {db_user.rol}"}

@app.post("/grupos", response_model=schemas.Grupo)
def create_grupo(grupo: schemas.GrupoCreate, db: Session = Depends(get_db)):
    return crud.create_grupo(db=db, grupo=grupo)

@app.post("/locales", response_model=schemas.Local)
def create_local(local: schemas.LocalCreate, db: Session = Depends(get_db)):
    return crud.create_local(db=db, local=local)

@app.post("/prestamos", response_model=schemas.Prestamo)
def create_prestamo(prestamo: schemas.PrestamoCreate, db: Session = Depends(get_db)):
    return crud.create_prestamo(db=db, prestamo=prestamo)

##
@app.get("/usuarios/{usuario_id}", response_model=schemas.Usuario)
def read_usuario(usuario_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_usuario(db, usuario_id=usuario_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return db_user

@app.get("/grupos/{grupo_id}", response_model=schemas.Grupo)
def read_grupo(grupo_id: int, db: Session = Depends(get_db)):
    db_grupo = crud.get_grupo(db, grupo_id=grupo_id)
    if db_grupo is None:
        raise HTTPException(status_code=404, detail="Grupo no encontrado")
    return db_grupo

@app.get("/locales/{local_id}", response_model=schemas.Local)
def read_local(local_id: int, db: Session = Depends(get_db)):
    db_local = crud.get_local(db, local_id=local_id)
    if db_local is None:
        raise HTTPException(status_code=404, detail="Local no encontrado")
    return db_local

@app.get("/prestamos/{prestamo_id}", response_model=schemas.Prestamo)
def read_prestamo(prestamo_id: int, db: Session = Depends(get_db)):
    db_prestamo = crud.get_prestamo(db, prestamo_id=prestamo_id)
    if db_prestamo is None:
        raise HTTPException(status_code=404, detail="Prestamo no encontrado")
    return db_prestamo

@app.put("/usuarios/{usuario_id}", response_model=schemas.Usuario)
def update_usuario(usuario_id: int, usuario: schemas.UsuarioCreate, db: Session = Depends(get_db)):
    db_user = crud.update_usuario(db, usuario_id=usuario_id, usuario=usuario)
    if db_user is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return db_user

@app.put("/grupos/{grupo_id}", response_model=schemas.Grupo)
def update_grupo(grupo_id: int, grupo: schemas.GrupoCreate, db: Session = Depends(get_db)):
    db_grupo = crud.update_grupo(db, grupo_id=grupo_id, grupo=grupo)
    if db_grupo is None:
        raise HTTPException(status_code=404, detail="Grupo no encontrado")
    return db_grupo

##
@app.put("/locales/{local_id}", response_model=schemas.Local)
def update_local(local_id: int, local: schemas.LocalCreate, db: Session = Depends(get_db)):
    db_local = crud.update_local(db, local_id=local_id, local=local)
    if db_local is None:
        raise HTTPException(status_code=404, detail="Local no encontrado")
    return db_local

@app.put("/prestamos/{prestamo_id}", response_model=schemas.Prestamo)
def update_prestamo(prestamo_id: int, prestamo: schemas.PrestamoCreate, db: Session = Depends(get_db)):
    db_prestamo = crud.update_prestamo(db, prestamo_id=prestamo_id, prestamo=prestamo)
    if db_prestamo is None:
        raise HTTPException(status_code=404, detail="Prestamo no encontrado")
    return db_prestamo

##
@app.delete("/usuarios/{usuario_id}", response_model=schemas.Usuario)
def delete_usuario(usuario_id: int, db: Session = Depends(get_db)):
    db_user = crud.delete_usuario(db, usuario_id=usuario_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return db_user

@app.delete("/grupos/{grupo_id}", response_model=schemas.Grupo)
def delete_grupo(grupo_id: int, db: Session = Depends(get_db)):
    db_grupo = crud.delete_grupo(db, grupo_id=grupo_id)
    if db_grupo is None:
        raise HTTPException(status_code=404, detail="Grupo no encontrado")
    return db_grupo

@app.delete("/locales/{local_id}", response_model=schemas.Local)
def delete_local(local_id: int, db: Session = Depends(get_db)):
    db_local = crud.delete_local(db, local_id=local_id)
    if db_local is None:
        raise HTTPException(status_code=404, detail="Local no encontrado")
    return db_local

@app.delete("/prestamos/{prestamo_id}", response_model=schemas.Prestamo)
def delete_prestamo(prestamo_id: int, db: Session = Depends(get_db)):
    db_prestamo = crud.delete_prestamo(db, prestamo_id=prestamo_id)
    if db_prestamo is None:
        raise HTTPException(status_code=404, detail="Prestamo no encontrado")
    return db_prestamo

##
@app.get("/usuarios", response_model=List[schemas.Usuario])
def read_usuarios(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    usuarios = crud.get_usuarios(db, skip=skip, limit=limit)
    return usuarios

@app.get("/grupos", response_model=List[schemas.Grupo])
def read_grupos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    grupos = crud.get_grupos(db, skip=skip, limit=limit)
    return grupos

@app.get("/locales", response_model=List[schemas.Local])
def read_locales(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    locales = crud.get_locales(db, skip=skip, limit=limit)
    return locales

@app.get("/prestamos", response_model=List[schemas.Prestamo])
def read_prestamos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    prestamos = crud.get_prestamos(db, skip=skip, limit=limit)
    return prestamos

##
@app.get("/usuarios/{rol}", response_model=List[schemas.Usuario])
def read_usuarios_by_rol(rol: str, db: Session = Depends(get_db)):
    usuarios = crud.get_usuarios_by_rol(db, rol=rol)
    return usuarios
