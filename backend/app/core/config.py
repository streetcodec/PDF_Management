import os

class Settings:
    PROJECT_NAME: str = "health Management API"
    DATABASE_URL: str = os.getenv(
        "DATABASE_URL",
        "postgresql+psycopg2://user:password@localhost:5432/dbname"
    )

    STORAGE_PATH: str = os.getenv("STORAGE_PATH", "storage")
    MAX_FILE_SIZE: int = os.getenv("MAX_FILE_SIZE", 10 * 1024 * 1024)

settings = Settings()

os.makedirs(settings.STORAGE_PATH, exist_ok=True)