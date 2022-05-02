from functools import lru_cache

from pydantic import BaseSettings


class Settings(BaseSettings):
    database_url: str

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'


@lru_cache
def settings() -> Settings:
    return Settings()
