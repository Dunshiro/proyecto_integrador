from fastapi import FastAPI, Request, Depends, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session
from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

#app=FastAPI()
#app.mount("/static",StaticFiles(directory="static"),name="static")


#templates=Jinja2Templates(directory="templates")

#@app.get("/")
#async def index(request:Request):
#    return templates.TemplateResponse("base.html",{"request":request})

app = FastAPI()

# Dependencia para obtener la sesión de base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/usuarios/", response_model=schemas.Usuario)
def create_usuario(usuario: schemas.UsuarioCreate, db: Session = Depends(get_db)):
    return crud.create_usuario(db=db, usuario=usuario)

@app.get("/usuarios/", response_model=list[schemas.Usuario])
def read_usuarios(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_usuarios(db, skip=skip, limit=limit)

@app.get("/usuarios/{usuario_id}", response_model=schemas.Usuario)
def read_usuario(usuario_id: int, db: Session = Depends(get_db)):
    db_usuario = crud.get_usuario(db, usuario_id=usuario_id)
    if db_usuario is None:
        raise HTTPException(status_code=404, detail="Usuario not found")
    return db_usuario

# Operaciones CRUD para la clase Rol
@app.post("/roles/", response_model=schemas.Rol)
def create_rol(rol: schemas.RolCreate, db: Session = Depends(get_db)):
    return crud.create_rol(db=db, rol=rol)

@app.get("/roles/", response_model=list[schemas.Rol])
def read_roles(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_roles(db, skip=skip, limit=limit)

@app.get("/roles/{rol_id}", response_model=schemas.Rol)
def read_rol(rol_id: int, db: Session = Depends(get_db)):
    db_rol = crud.get_rol(db, rol_id=rol_id)
    if db_rol is None:
        raise HTTPException(status_code=404, detail="Rol not found")
    return db_rol

# Operaciones CRUD para la clase Grupo
@app.post("/grupos/", response_model=schemas.Grupo)
def create_grupo(grupo: schemas.GrupoCreate, db: Session = Depends(get_db)):
    return crud.create_grupo(db=db, grupo=grupo)

@app.get("/grupos/", response_model=list[schemas.Grupo])
def read_grupos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_grupos(db, skip=skip, limit=limit)

@app.get("/grupos/{grupo_id}", response_model=schemas.Grupo)
def read_grupo(grupo_id: int, db: Session = Depends(get_db)):
    db_grupo = crud.get_grupo(db, grupo_id=grupo_id)
    if db_grupo is None:
        raise HTTPException(status_code=404, detail="Grupo not found")
    return db_grupo

# Operaciones CRUD para la clase Prestamo
@app.post("/prestamos/", response_model=schemas.Prestamo)
def create_prestamo(prestamo: schemas.PrestamoCreate, db: Session = Depends(get_db)):
    return crud.create_prestamo(db=db, prestamo=prestamo)

@app.get("/prestamos/", response_model=list[schemas.Prestamo])
def read_prestamos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_prestamos(db, skip=skip, limit=limit)

@app.get("/prestamos/{prestamo_id}", response_model=schemas.Prestamo)
def read_prestamo(prestamo_id: int, db: Session = Depends(get_db)):
    db_prestamo = crud.get_prestamo(db, prestamo_id=prestamo_id)
    if db_prestamo is None:
        raise HTTPException(status_code=404, detail="Prestamo not found")
    return db_prestamo