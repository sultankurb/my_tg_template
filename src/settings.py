from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Optional
from pathlib import Path


BASE_DIR = Path(__name__).parent.parent


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=f"{BASE_DIR}/.env")
    ADMIN_ID: Optional[int] = None
    DATABASE_URL: str
    BOT_TOKEN: Optional[str] = None


settings = Settings()
async_engine = create_async_engine(url=settings.DATABASE_URL)
async_session_maker = async_sessionmaker(bind=async_engine)
