from pathlib import Path
from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict
from sqlalchemy.engine import URL

BASE_DIR = Path(__file__).resolve().parent


class Settings(BaseSettings):
    ORIGINS: list[str] = Field(default_factory=list)

    POSTGRES_USER: str = "postgres"
    POSTGRES_PASSWORD: str = "postgres"
    POSTGRES_DB: str
    POSTGRES_SERVER: str = "localhost"
    POSTGRES_PORT: int = Field(default=5432, ge=1, le=65535)

    model_config = SettingsConfigDict(
        env_file=BASE_DIR / ".env",
        env_file_encoding="utf-8",
        extra="ignore",
        case_sensitive=False,
    )

    def build_database_url(self, driver: str) -> str:
        return URL.create(
            drivername=driver,
            username=self.POSTGRES_USER,
            password=self.POSTGRES_PASSWORD,
            host=self.POSTGRES_SERVER,
            port=self.POSTGRES_PORT,
            database=self.POSTGRES_DB,
        ).render_as_string(hide_password=False)

    @property
    def DATABASE_URL(self) -> str:
        return self.build_database_url("postgresql+asyncpg")

    @property
    def DATABASE_URL_SYNC(self) -> str:
        return self.build_database_url("postgresql+psycopg")


@lru_cache
def get_settings() -> Settings:
    return Settings()