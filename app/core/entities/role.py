from dataclasses import dataclass
from uuid import UUID


@dataclass
class Role:
    id: UUID
    name: str
    description: str
    is_active: bool = True