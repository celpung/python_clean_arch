from sqlalchemy.orm import Session
from typing import Optional, List

from app.domain.admin.entity.user_entity import UserEntity
from app.domain.admin.mapper.user_mapper import to_model, to_entity
from app.domain.admin.repository.impl.user_model import UserModel
from app.domain.admin.repository.interface.user_repository import UserRepositoryInterface


class UserRepositoryImpl(UserRepositoryInterface):
    def __init__(self, db: Session):
        self.db = db

    def create(self, user: UserEntity) -> UserEntity:
        model = to_model(user)
        self.db.add(model)
        self.db.commit()
        self.db.refresh(model)
        return to_entity(model)

    def get_by_id(self, user_id: int) -> Optional[UserEntity]:
        user = self.db.query(UserModel).filter(UserModel.id == user_id).first()
        return to_entity(user) if user else None

    def get_by_email(self, email: str) -> Optional[UserEntity]:
        user = self.db.query(UserModel).filter(UserModel.email == email).first()
        return to_entity(user) if user else None

    def list_all(self) -> List[UserEntity]:
        users = self.db.query(UserModel).all()
        return [to_entity(user) for user in users]

    def update(self, user_id: int, updated_user: UserEntity) -> Optional[UserEntity]:
        user = self.db.query(UserModel).filter(UserModel.id == user_id).first()
        if not user:
            return None

        user.name = updated_user.name
        user.email = updated_user.email
        user.password = updated_user.password
        user.updated_at = updated_user.updated_at

        self.db.commit()
        self.db.refresh(user)
        return to_entity(user)

    def delete(self, user_id: int) -> bool:
        user = self.db.query(UserModel).filter(UserModel.id == user_id).first()
        if not user:
            return False

        self.db.delete(user)
        self.db.commit()
        return True
