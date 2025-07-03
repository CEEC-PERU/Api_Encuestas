# app/core/use_cases/role_management/get_role.py
from app.core.entities.role import Role
from app.core.ports.role_repository import IRoleRepository
from typing import Optional

class GetRoleUseCase:
    def __init__(self, repository: IRoleRepository):
        self.repository = repository

    def execute(self, role_id: str) -> Optional[Role]:
        return self.repository.get_by_id(role_id)