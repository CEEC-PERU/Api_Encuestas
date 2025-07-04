from pydantic import BaseModel
from typing import Optional
from uuid import UUID

class RoleBase(BaseModel):
    name: str
    description: Optional[str] = None

class RoleCreate(RoleBase):
    pass

class RoleUpdate(RoleBase):
    pass

class RoleResponse(RoleBase):
    id: UUID
    is_active: Optional[bool] = True

    class Config:
        from_attributes = True