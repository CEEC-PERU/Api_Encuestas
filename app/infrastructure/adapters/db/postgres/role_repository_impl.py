from uuid import UUID
from sqlalchemy.orm import Session
from app.core.entities.role import Role
from app.core.ports.role_repository import RoleRepository
from app.infrastructure.adapters.db.models import RoleModel

class RoleRepositoryImpl(RoleRepository):
    def __init__(self, db: Session):
        self.db = db
    
    def create(self, role: Role) -> Role:
        db_role = RoleModel(
            id=role.id,
            name=role.name,
            description=role.description,
            is_active=role.is_active
        )
        self.db.add(db_role)
        self.db.commit()
        self.db.refresh(db_role)
        return Role(
            id=db_role.id,
            name=db_role.name,
            description=db_role.description,
            is_active=db_role.is_active
        )
    
    def get_by_id(self, role_id: UUID) -> Role:
        db_role = self.db.query(RoleModel).filter(RoleModel.id == role_id).first()
        if db_role:
            return Role(
                id=db_role.id,
                name=db_role.name,
                description=db_role.description,
                is_active=db_role.is_active
            )
        return None
    
    def update(self, role: Role) -> Role:
        db_role = self.db.query(RoleModel).filter(RoleModel.id == role.id).first()
        if db_role:
            db_role.name = role.name
            db_role.description = role.description
            db_role.is_active = role.is_active
            self.db.commit()
            self.db.refresh(db_role)
            return Role(
                id=db_role.id,
                name=db_role.name,
                description=db_role.description,
                is_active=db_role.is_active
            )
        return None
    
    def delete(self, role_id: UUID) -> bool:
        db_role = self.db.query(RoleModel).filter(RoleModel.id == role_id).first()
        if db_role:
            self.db.delete(db_role)
            self.db.commit()
            return True
        return False