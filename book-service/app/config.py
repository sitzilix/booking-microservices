from pydantic_settings import BaseSettings
from pydantic import ConfigDict

class Settings(BaseSettings):
    app_name: str = "Auth-service"
    debug: bool = True
    database_url: str = "postgresql://user:password@localhost:5432/auth_db"
    secret_key: str = "super-secret-key-change-me"
    alghoritm: str = "HS256"
    access_token_expire_minutes: int = 30

    # Новый способ настройки Pydantic v2
    model_config = ConfigDict(env_file=".env")

settings = Settings()