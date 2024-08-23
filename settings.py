from pydantic import BaseSettings


class Settings(BaseSettings):
    aws_access_key_id: str
    aws_secret_access_key: str
    aws_region: str
    endpoint_url: str

    class Config:
        env_file = ".env"


settings = Settings()