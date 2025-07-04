from abc import ABC, abstractmethod
from uuid import UUID
from app.core.entities.role import Role

class RoleRepository(ABC):
    @abstractmethod
    def create(self, role: Role) -> Role:
        pass
    
    @abstractmethod
    def get_by_id(self, role_id: UUID) -> Role:
        pass
    
    @abstractmethod
    def update(self, role: Role) -> Role:
        pass
    
    @abstractmethod
    def delete(self, role_id: UUID) -> bool:
        pass


        