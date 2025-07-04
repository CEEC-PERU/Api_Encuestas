from dataclasses import dataclass
from uuid import UUID
from typing import Optional

@dataclass
class Role:
    id: UUID
    name: str
    description: Optional[str] = None
    is_active: bool = True