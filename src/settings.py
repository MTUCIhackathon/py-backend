import os

from dotenv import load_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict


load_dotenv()


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=os.getenv("CONFIG_PATH"),
        validate_default=True
    )

    ADDR: str = "127.0.0.1"
    PORT: int = 8083
    TEST: bool = True

    LOG_LEVEL: str = "info"

    MODEL_TYPE: str = 'pro'
    LLM_TEMPERATYRE: float = 0.8
    LLM_MAX_TOKENS: int = 1000

    FOLDER_ID: str = ""
    IAM_TOKEN: str = ""


settings = Settings()
