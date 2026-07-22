from functools import lru_cache
from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict
from enum import StrEnum

BASE_DIR = Path(__file__).resolve().parents[3]

class Environment(StrEnum):
    DEVELOPMENT = "development"
    TEST = "test"
    STAGING = "staging"
    PRODUCTION = "production"

class Settings(BaseSettings):
    app_name: str = "ForgeAI"
    app_version: str = "0.1.0"
    app_description: str="ForgeAI is AI Software Engineering Platform1"

    app_env:Environment = Environment.DEVELOPMENT
    debug: bool = True
    host: str = "0.0.0.0"
    port: int = 8000
    model_config = SettingsConfigDict(
        env_file= BASE_DIR / ".env",
        case_sensitive=False,
        extra="ignore",
    )

@lru_cache

def get_settings()-> Settings:
    return Settings()
  