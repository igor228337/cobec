from pathlib import Path
import sys

from pydantic_settings import BaseSettings, SettingsConfigDict
from loguru import logger


logger.add(sys.stderr, format="{time} {level} {message}", backtrace=True, diagnose=True, enqueue=True)

ENV_PATH = Path(__file__).resolve().parent.parent / ".env"

class Environment(BaseSettings):
    # Database.
    DB_NAME: str
    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASSWORD: str
    
    @property
    def database_url(self):
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    # Admin
    LOGIN_ADMIN: str
    PASSWORD_ADMIN: str
    ADMIN_KEY: str

    model_config = SettingsConfigDict(env_file=ENV_PATH, env_file_encoding="utf-8")


enviroment = Environment()
