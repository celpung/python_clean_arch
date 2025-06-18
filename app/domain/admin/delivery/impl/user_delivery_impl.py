from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.domain.admin.delivery.dependency.user_dependency import get_user_usecase
from app.domain.admin.delivery.dto.user_dto import UserResponse, CreateUserRequest, UpdateUserRequest, LoginRequest
from app.domain.admin.delivery.interface.user_delivery import UserDeliveryInterface
from app.domain.admin.entity.user_entity import UserEntity
from app.domain.admin.mapper.user_mapper import to_response
from app.domain.admin.usecase.impl.user_usecase_impl import UserUseCaseImpl


class UserDeliveryImplementation(UserDeliveryInterface):
    def __init__(self):
        self.router = APIRouter(prefix="/users", tags=["User"])
        self.router.add_api_route("/", self.create_user, methods=["POST"], response_model=UserResponse)
        self.router.add_api_route("/", self.get_all_users, methods=["GET"], response_model=List[UserResponse])
        self.router.add_api_route("/{user_id}", self.get_user_by_id, methods=["GET"], response_model=UserResponse)
        self.router.add_api_route("/{user_id}", self.update_user, methods=["PUT"], response_model=UserResponse)
        self.router.add_api_route("/{user_id}", self.delete_user, methods=["DELETE"])
        self.router.add_api_route("/login", self.login, methods=["POST"])

    def get_router(self) -> APIRouter:
        return self.router

    def create_user(self, request: CreateUserRequest, usecase: UserUseCaseImpl = Depends(get_user_usecase)):
        entity = UserEntity(
            id=None,
            name=request.name,
            email=request.email,
            password=request.password
        )
        created = usecase.create_user(entity)
        return to_response(created)

    def get_all_users(self, usecase: UserUseCaseImpl = Depends(get_user_usecase)):
        users = usecase.get_all_users()
        return [to_response(u) for u in users]

    def get_user_by_id(self, user_id: int, usecase: UserUseCaseImpl = Depends(get_user_usecase)):
        user = usecase.get_user_by_id(user_id)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return to_response(user)

    def update_user(self, user_id: int, request: UpdateUserRequest, usecase: UserUseCaseImpl = Depends(get_user_usecase)):
        existing = usecase.get_user_by_id(user_id)
        if not existing:
            raise HTTPException(status_code=404, detail="User not found")

        updated = UserEntity(
            id=user_id,
            name=request.name or existing.name,
            email=request.email or existing.email,
            password=request.password or existing.password,
            created_at=existing.created_at,
            updated_at=existing.updated_at
        )
        result = usecase.update_user(user_id, updated)
        return to_response(result)

    def delete_user(self, user_id: int, usecase: UserUseCaseImpl = Depends(get_user_usecase)):
        if not usecase.delete_user(user_id):
            raise HTTPException(status_code=404, detail="User not found")
        return {"message": "User deleted successfully"}
    
    def login(self, request: LoginRequest, usecase: UserUseCaseImpl = Depends(get_user_usecase)):
        token = usecase.login(request.email, request.password)
        if not token:
            raise HTTPException(status_code=401, detail="Invalid email or password")
        return {"token": token, "type": "bearer"}
