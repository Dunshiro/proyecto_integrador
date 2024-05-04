from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from fastapi import HTTPException

# Configuración de la conexión a la base de datos
SQLALCHEMY_DATABASE_URL = "mysql://root:mysql@localhost/proyecto_integrador"

# Crear el motor de base de datos
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Crear una sesión de base de datos
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Declarar la base para las clases de modelo
Base = declarative_base()