from pydantic_settings import BaseSettings

class Settings(BaseSettings):

    DB_CONNECTION: str
    DB_HOST: str
    DB_PORT: str
    DB_DATABASE: str
    DB_USERNAME: str
    DB_PASSWORD: str

    class Config:

        enf_file="api/.env"
        enf_file_encoding="utf-8"