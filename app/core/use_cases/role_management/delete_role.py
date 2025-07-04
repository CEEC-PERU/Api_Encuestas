from app.core.entities.role import Role
from app.core.ports.role_repository import IRoleRepository
class DeleteRoleUseCase:
    def __init__(self,role_repository: IRoleRepository):
        self.role_repository = role_repository
    
    def execute(self, role_id):
        return self.role_repository.delete(role_id)