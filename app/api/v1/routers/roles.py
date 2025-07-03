# app/api/v1/routers/roles.py
from fastapi import APIRouter, Depends, HTTPException
from core.use_cases.role_management import CreateRoleUseCase
from api.v1.schemas import RoleCreate, RoleResponse
from infrastructure.adapters.db.postgres.role_repository_impl import PostgresRoleRepository
from infrastructure.db.database import get_db

router = APIRouter(prefix="/roles", tags=["roles"])

@router.post("/", response_model=RoleResponse)
async def create_role(
    role_data: RoleCreate,
    db: Session = Depends(get_db)
):
    """Endpoint para crear un nuevo rol.
    
    Flujo:
    1. Valida los datos de entrada con el esquema Pydantic
    2. Crea el repositorio con la sesión de base de datos
    3. Ejecuta el caso de uso
    4. Maneja posibles errores de negocio
    5. Retorna la respuesta formateada"""
    
    # 1. Inicializa el repositorio concreto (adaptador PostgreSQL)
    repo = PostgresRoleRepository(db)
    
    # 2. Inicializa el caso de uso con el repositorio
    use_case = CreateRoleUseCase(repo)
    
    try:
        # 3. Ejecuta el caso de uso
        role = use_case.execute(role_data.name)
        
        # 4. Retorna la respuesta convertida a esquema Pydantic
        return role
    except ValueError as e:
        # 5. Maneja errores de negocio
        raise HTTPException(status_code=400, detail=str(e))