from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from sqlalchemy.orm import Session

# Schemas
from app.api.v1.schemas.s_role import RoleCreate, RoleResponse, RoleUpdate

# Use Cases
from app.core.use_cases.role_management.get_roles import GetRolesUseCase

# Repository
from app.infrastructure.adapters.db.postgres.role_repository_impl import PostgresRoleRepository

# Database
from app.infrastructure.database import get_db

router = APIRouter(prefix="/roles", tags=["roles"])

@router.get("/", response_model=List[RoleResponse])
async def get_all_roles(
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 100
):
    repo = PostgresRoleRepository(db)
    use_case = GetRolesUseCase(repo)
    try:
        return use_case.execute(skip=skip, limit=limit)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
