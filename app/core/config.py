from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict



@lru_cache
def get_settings():
    return DevelopmentSettings()


class Settings(BaseSettings):
    # General
    PROJECT_NAME: str = "face-identification-service"
    PROJECT_VERSION: str = "0.0.1"
    ENVIRONMENT: str = "production"
    API_PREFIX: str = "/api/v1"
    DEBUG: bool = False
    LOG_LEVEL: str = "INFO"

    # Server
    HOST: str = "127.0.0.1"
    PORT: int = 8000

    # Image Processing
    IMAGE_WIDTH: int = 720
    IMAGE_HEIGHT: int = 720
    ALLOWED_IMAGE_TYPES: list[str] = ["jpg", "jpeg", "png", "webp"]

    model_config = SettingsConfigDict (
        env_file=".env",
        env_file_encoding = "utf-8",
        case_sensitive = True,
    )

class DevelopmentSettings(Settings):
    ENVIRONMENT: str = "development"
    DEBUG: bool = True
    LOG_LEVEL: str = "DEBUG"