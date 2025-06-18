from fastapi import Depends
from sqlalchemy.orm import Session

from app.configs.db.mysql.mysql_config import get_db
from app.domain.admin.repository.impl.user_repository_impl import UserRepositoryImpl
from app.domain.admin.usecase.impl.user_usecase_impl import UserUseCaseImpl


def get_user_usecase(db: Session = Depends(get_db)) -> UserUseCaseImpl:
    repo = UserRepositoryImpl(db)
    return UserUseCaseImpl(repo)