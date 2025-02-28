from fastapi import APIRouter, Depends, HTTPException, status
from db.database import get_db
from db.models.usuario_model import UsuarioDB
from sqlalchemy.orm import Session
from pydantic import BaseModel
from auth.manejador_auth import verificar_password, crear_token_acceso


auth_router = APIRouter(prefix="/auth", tags=["Autenticación"])


class DatosLogin(BaseModel):
    codigo_usuario: str
    password: str

@auth_router.post(path="/login")
async def login(datos: DatosLogin, db: Session = Depends(dependency=get_db)):
    
    # Buscar al usuario por codigo de usuario
    usuario_db = db.query(UsuarioDB).filter(UsuarioDB.codigo_usuario == datos.codigo_usuario).first()
    if not usuario_db:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Credenciales invalidas")
    
    # Verificar la contraseña
    if not verificar_password(password=datos.password, hashed_password=usuario_db.password):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Credenciales invalidas")
    
    # Crear el token de acceso
    token_acceso = crear_token_acceso(datos={"sub": str(usuario_db.id)})
    return {"access_token": token_acceso, "token_type": "bearer"}