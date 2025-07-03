# app/api/v1/schemas.py
from pydantic import BaseModel, UUID4

class RoleResponse(BaseModel):
    """Esquema Pydantic para la respuesta de roles.
    Define cómo se serializarán los datos de rol al cliente."""
    
    id: UUID4  # ID del rol
    name: str  # Nombre del rol

    class Config:
        """Configuración especial para compatibilidad con ORMs"""
        from_attributes = True  # Anteriormente llamado 'orm_mode'