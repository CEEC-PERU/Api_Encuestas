from app.core.entities.role import Role
from app.core.ports.role_repository import IRoleRepository
class UpdateRoleUseCase:
    def __init__(self,role_repository: IRoleRepository):
        self.role_repository = role_repository
    
    def execute(self, role_id, name):
        return self.role_repository.update(role_id, name)