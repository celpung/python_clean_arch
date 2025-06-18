from abc import ABC, abstractmethod
from typing import List, Optional
from domain.entity.user_entity import UserEntity

class UserUseCaseInterface(ABC):
    @abstractmethod
    def create_user(self, user: UserEntity) -> UserEntity:
        pass

    @abstractmethod
    def get_user_by_id(self, user_id: int) -> Optional[UserEntity]:
        pass

    @abstractmethod
    def get_user_by_email(self, email: str) -> Optional[UserEntity]:
        pass

    @abstractmethod
    def get_all_users(self) -> List[UserEntity]:
        pass

    @abstractmethod
    def update_user(self, user_id: int, user: UserEntity) -> Optional[UserEntity]:
        pass

    @abstractmethod
    def delete_user(self, user_id: int) -> bool:
        pass

    @abstractmethod
    def login(self, email: str, password: str) -> Optional[str]:
        pass
