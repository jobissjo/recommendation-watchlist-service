from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    SECRET_KEY: str
    ALGORITHM: str
    DATABASE_URL: str = "sqlite://db.sqlite3"
    DEBUG: bool = False

    class Config:
        env_file = ".env"

settings = Settings()
