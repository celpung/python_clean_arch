from abc import ABC, abstractmethod
from fastapi import APIRouter

class UserDeliveryInterface(ABC):
    @abstractmethod
    def get_router(self) -> APIRouter:
        pass