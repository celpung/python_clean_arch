from abc import ABC, abstractmethod
from typing import Optional, List

from app.domain.admin.entity.user_entity import UserEntity


class UserRepositoryInterface(ABC):
    @abstractmethod
    def create(self, user: UserEntity) -> UserEntity:
        pass

    @abstractmethod
    def get_by_id(self, user_id: int) -> Optional[UserEntity]:
        pass

    @abstractmethod
    def get_by_email(self, email: str) -> Optional[UserEntity]:
        pass

    @abstractmethod
    def list_all(self) -> List[UserEntity]:
        pass

    @abstractmethod
    def update(self, user_id: int, updated_user: UserEntity) -> Optional[UserEntity]:
        pass

    @abstractmethod
    def delete(self, user_id: int) -> bool:
        pass
