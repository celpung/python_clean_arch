from datetime import datetime

from app.domain.admin.delivery.dto.user_dto import UserResponse
from app.domain.admin.entity.user_entity import UserEntity
from app.domain.admin.repository.impl.user_model import UserModel


def to_entity(model: UserModel) -> UserEntity:
    return UserEntity(
        id=model.id,
        name=model.name,
        email=model.email,
        password=model.password,
        role=model.role,
        active=model.active,
        created_at=model.created_at,
        updated_at=model.updated_at,
    )


def to_model(entity: UserEntity) -> UserModel:
    return UserModel(
        id=entity.id,
        name=entity.name,
        email=entity.email,
        password=entity.password,
        role=entity.role if entity.role is not None else 1,  # fallback
        active=entity.active,
        created_at=entity.created_at or datetime.utcnow(),
        updated_at=entity.updated_at or datetime.utcnow(),
    )


def to_response(entity: UserEntity) -> UserResponse:
    return UserResponse(
        id=entity.id,
        name=entity.name,
        email=entity.email,
        role=entity.role,
        active=entity.active,
        created_at=entity.created_at,
        updated_at=entity.updated_at,
    )
