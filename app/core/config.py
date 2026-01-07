from pathlib import Path
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """
    Основные настройки приложения.

    Атрибуты:
        POSTGRES_DB: имя базы данных
        POSTGRES_USER: пользователь базы данных
        POSTGRES_PASSWORD: пароль пользователя базы данных
        POSTGRES_HOST: хост базы данных
        POSTGRES_PORT: порт базы данных
        APP_HOST: хост API
        APP_PORT: порт API
    """

    POSTGRES_DB: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_HOST: str
    POSTGRES_PORT: int
    APP_HOST: str
    APP_PORT: int

    class Config:
        env_file = Path(__file__).parent.parent / ".env"
        env_file_encoding = "utf-8"
        extra = "forbid"  # запрещаем лишние переменные


settings = Settings()
