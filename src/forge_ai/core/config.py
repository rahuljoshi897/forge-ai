from functools import lru_cache
from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict
from enum import StrEnum
from pydantic import Field
from functools import cached_property


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
    @property
    def is_production(self) -> bool:
        return self.app_env is Environment.PRODUCTION
    
    @property
    def is_development(self) -> bool:
        return self.app_env is Environment.DEVELOPMENT
    
    def is_staging(self) -> bool:
        return self.app_env is Environment.STAGING
    
    @property
    def is_test(self) -> bool:
        return self.app_env is Environment.TEST
    
    debug: bool = True
    host: str = "0.0.0.0"
    port: int = 8000
    # ------------------------------------------------------------------
    # Database
    # ------------------------------------------------------------------
    db_host: str = Field(
        default= "localhost",
        description="PostgreSQL host.",
    )
    db_port: int = Field(
        default=5432,
        description="PostgreSQL port.",
    )
    db_name: str = Field(
        default="forge_ai",
        description="Database name.",
    )
    db_user: str = Field(
        default="postgres",
        description="Database username.",
    )
    db_password: str = Field(
        default="postgres",
        description="Database password.",
    )
    model_config = SettingsConfigDict(
        env_file= BASE_DIR / ".env",
        case_sensitive=False,
        extra="ignore",
        env_file_encoding= "utf-8",
    )

    @cached_property
    def database_url(self)-> str:
         #SQLAlchemy async database URL.
         return (
                "postgresql+asyncpg://"
                f"{self.db_user}:{self.db_password}"
                f"@{self.db_host}:{self.db_port}"
                f"/{self.db_name}"
            )

@lru_cache

def get_settings()-> Settings:
    return Settings()
  