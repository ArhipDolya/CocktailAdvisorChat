from pydantic_settings import BaseSettings
from pydantic import Field


class Config(BaseSettings):
    OPENAI_API_KEY: str = Field(None, env="OPENAI_API_KEY")
    WEAVIATE_URL: str = Field("http://weaviate:8080", env="WEAVIATE_URL")
    
    class Config:
        env_file = ".env"


def get_config() -> Config:
    return Config()
