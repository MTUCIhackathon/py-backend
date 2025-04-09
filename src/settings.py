import os

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    ADDR: str = "0.0.0.0"
    PORT: int = 8001
    TEST: bool = True

    LOG_LEVEL: str = "info"

    class Config:
        env_file = os.getenv("CONFIG_PATH")


settings = Settings()
