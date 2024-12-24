from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file='.env', env_file_encoding='utf-8'
    )
    DB_NAME: str
    DB_PORT: str
    DB_HOST: str
    DB_PASSWORD: str
    DB_USER: str