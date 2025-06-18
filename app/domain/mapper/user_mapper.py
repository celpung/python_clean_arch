from datetime import datetime
from domain.delivery.dto.user_dto import UserResponse
from domain.entity.user_entity import UserEntity
from domain.repository.impl.user_model import UserModel

def to_entity(model: UserModel) -> UserEntity:
    return UserEntity(
        id=model.id,
        name=model.name,
        email=model.email,
        password=model.password,
        created_at=model.created_at,
        updated_at=model.updated_at,
    )

def to_model(entity: UserEntity) -> UserModel:
    return UserModel(
        id=entity.id,
        name=entity.name,
        email=entity.email,
        password=entity.password,
        created_at=entity.created_at or datetime.utcnow(),
        updated_at=entity.updated_at or datetime.utcnow(),
    )

def to_response(entity: UserEntity) -> UserResponse:
    return UserResponse(
        id=entity.id,
        name=entity.name,
        email=entity.email,
        created_at=entity.created_at,
        updated_at=entity.updated_at,
    )
