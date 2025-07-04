from app.core.entities.role import Role
from app.core.ports.role_repository import RoleRepository
class GetRolesUseCase:
    def __init__(self, role_repository: RoleRepository):
        self.role_repository = role_repository
    
    def execute(self, skip=0, limit=100):
        return self.role_repository.get_all(skip=skip, limit=limit)