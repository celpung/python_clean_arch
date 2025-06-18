from configs.db.mysql.mysql_config import SessionLocal
from domain.repository.impl.user_repository_impl import UserRepositoryImpl
from domain.usecase.impl.user_usecase_impl import UserUseCaseImpl
from domain.entity.user_entity import UserEntity

def test_create_user():
    db = SessionLocal()

    user_repo = UserRepositoryImpl(db)
    user_usecase = UserUseCaseImpl(user_repo)

    test_user = UserEntity(
        name="Nadiem Makarim",
        email="nadiem@makarim.com",
        password="killer123"
    )

    try:
        created_user = user_usecase.create_user(test_user)
        print("✅ User berhasil dibuat:", created_user.id, created_user.name, created_user.email)
    except :
        print("Gagal menambahkan user")
    
    db.close()

if __name__ == "__main__":
    test_create_user()