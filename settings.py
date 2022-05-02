from functools import lru_cache

from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    postgres_user: str
    postgres_password: str
    postgres_db_name: str
    postgres_port: int
    database_url: str

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'


@lru_cache
def settings() -> Settings:
    return Settings()
