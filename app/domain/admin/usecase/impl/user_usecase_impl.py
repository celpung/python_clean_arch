from abc import ABC
from typing import List, Optional

from app.domain.admin.entity.user_entity import UserEntity
from app.domain.admin.repository.interface.user_repository import UserRepositoryInterface
from app.domain.admin.usecase.interface.user_usecase import UserUseCaseInterface
from app.utils.jwt.jwt import create_access_token
from app.utils.password.hash_password import hash_password
from app.utils.password.verify_password import verify_password

class UserUseCaseImpl(UserUseCaseInterface):
    def __init__(self, user_repository: UserRepositoryInterface):
        self.user_repository = user_repository

    def create_user(self, user: UserEntity) -> UserEntity:
        user.password = hash_password(user.password)
        return self.user_repository.create(user)

    def get_user_by_id(self, user_id: int) -> Optional[UserEntity]:
        return self.user_repository.get_by_id(user_id)

    def get_user_by_email(self, email: str) -> Optional[UserEntity]:
        return self.user_repository.get_by_email(email)

    def get_all_users(self) -> List[UserEntity]:
        return self.user_repository.list_all()

    def update_user(self, user_id: int, user: UserEntity) -> Optional[UserEntity]:
        return self.user_repository.update(user_id, user)

    def delete_user(self, user_id: int) -> bool:
        return self.user_repository.delete(user_id)

    def login(self, email: str, password: str) -> Optional[str]:
        usr = self.get_user_by_email(email)
        if not usr:
            return None
        if not verify_password(password, usr.password):
            return None
        
        token = create_access_token({"sub": usr.id, "email": usr.email})
        return token

