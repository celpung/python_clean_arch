from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.configs.db.mysql.mysql_config import Base, engine
from app.domain.admin.delivery.router import user_router

def create_tables():
    """
    Create all tables in the database based on SQLAlchemy Base metadata.
    This is only used at startup to ensure tables exist.
    """
    try:
        Base.metadata.create_all(bind=engine)
        print("✅ Database tables created successfully.")
    except Exception as e:
        print("❌ Error creating tables:", str(e))

def get_application() -> FastAPI:
    """
    Initialize the FastAPI app with all required routers and middleware.
    """
    app = FastAPI(
        title="Skoolar User Service",
        description="Service for managing users in Skoolar platform.",
        version="1.0.0"
    )

    # Middleware: CORS
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Register routers
    app.include_router(user_router.router)

    return app

# ----- Entrypoint -----
create_tables()
app = get_application()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
