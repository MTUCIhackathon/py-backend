import os

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    ADDR: str = "127.0.0.1"
    PORT: int = 8000
    TEST: bool = True

    LOG_LEVEL: str = "info"
    
    MODEL_TYPE: str = 'pro'
    LLM_TEMPERATYRE: float = 0.8
    LLM_MAX_TOKENS: int = 1000

    class Config:
        env_file = os.getenv("CONFIG_PATH")


settings = Settings()
