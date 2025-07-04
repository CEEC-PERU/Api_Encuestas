from app.infrastructure.adapters.db.models import RoleModel
from app.core.entities.role import Role
from app.core.ports.role_repository import RoleRepository

class PostgresRoleRepository(RoleRepository):
    def __init__(self, db_session):
        self.db = db_session
    
    def create(self, name):
        db_role = RoleModel(name=name)
        self.db.add(db_role)
        self.db.commit()
        self.db.refresh(db_role)
        return Role(id=db_role.id, name=db_role.name)
    
    def get_by_id(self, role_id):
        db_role = self.db.query(RoleModel).filter(RoleModel.id == role_id).first()
        if db_role:
            return Role(id=db_role.id, name=db_role.name)
        return None
    
    def get_all(self, skip=0, limit=100):
        db_roles = self.db.query(RoleModel).offset(skip).limit(limit).all()
        return [Role(id=role.id, name=role.name) for role in db_roles]
    
    def update(self, role_id, name):
        db_role = self.db.query(RoleModel).filter(RoleModel.id == role_id).first()
        if db_role:
            db_role.name = name
            self.db.commit()
            self.db.refresh(db_role)
            return Role(id=db_role.id, name=db_role.name)
        return None
    
    def delete(self, role_id):
        db_role = self.db.query(RoleModel).filter(RoleModel.id == role_id).first()
        if db_role:
            self.db.delete(db_role)
            self.db.commit()
            return True
        return False