from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from configs.db.mysql.mysql_config import Base

class UserModel(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, index=True, nullable=False)
    password = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

def __init__(self, id=None, name=None, email=None, password=None, created_at=None, updated_at=None):
    self.id = id
    self.name = name
    self.email = email
    self.password = password
    self.created_at = created_at or datetime.utcnow()
    self.updated_at = updated_at or datetime.utcnow()
