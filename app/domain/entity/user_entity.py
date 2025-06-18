from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional

@dataclass
class UserEntity:
    id: Optional[int] = None
    name: str = ""
    email: str = ""
    password: str = ""
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime = field(default_factory=datetime.utcnow)
