# app/core/use_cases/role_management/create_role.py
from app.core.entities.role import Role
from app.core.ports.role_repository import IRoleRepository

class CreateRoleUseCase:
    """Caso de uso para la creación de nuevos roles.
    Contiene la lógica de negocio específica para esta operación."""
    
    def __init__(self, repository: IRoleRepository):
        """Inicializa el caso de uso con un repositorio inyectado"""
        self.repository = repository

    def execute(self, name: str) -> Role:
        """Ejecuta la creación del rol con validaciones de negocio"""
        # 1. Validación de negocio
        if not name:
            raise ValueError("El nombre es requerido")
            
        # 2. Delega la persistencia al repositorio
        return self.repository.create(name)