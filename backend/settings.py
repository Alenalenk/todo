from pydantic_settings import BaseSettings, SettingsConfigDict, SettingsError, NoDecode
from pydantic import Field, field_validator, ValidationError
from typing import Annotated

import sys

class Settings(BaseSettings):
    DEBUG: bool = Field(default=False, alias="DEBUG")

    ORIGINS: Annotated[list[str], NoDecode]

    POSTGRES_USER: str = Field(default="postgres", alias="POSTGRES_USER")
    POSTGRES_PASSWORD: str = Field(default="postgres", alias="POSTGRES_PASSWORD")
    POSTGRES_DB: str = Field(alias="POSTGRES_DB")
    POSTGRES_SERVER: str = Field(alias="POSTGRES_SERVER")
    POSTGRES_PORT: int = Field(default=5432, alias="POSTGRES_PORT")

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    @property
    def DATABASE_URL(self):
        return "postgresql+asyncpg://{}:{}@{}:{}/{}".format(
            self.POSTGRES_USER, self.POSTGRES_PASSWORD, self.POSTGRES_SERVER, self.POSTGRES_PORT, self.POSTGRES_DB)

    
    @property
    def DATABASE_URL_SYNC(self):
        return "postgresql+psycopg://{}:{}@{}:{}/{}".format(
            self.POSTGRES_USER, self.POSTGRES_PASSWORD, self.POSTGRES_SERVER, self.POSTGRES_PORT, self.POSTGRES_DB)

    @field_validator("ORIGINS", mode="before")
    @classmethod
    def split_origins(cls, v):
        if isinstance(v, str):
            return v.split(sep=';')
        else:
            raise SettingsError("ORIGINS must be a list")


try:
    settings = Settings()
except (ValidationError, SettingsError) as e:
    sys.exit(1)
