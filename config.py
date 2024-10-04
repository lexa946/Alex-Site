from pydantic import model_validator
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DB_USERNAME: str
    DB_PASSWORD: str
    DB_NAME: str
    DB_HOST: str
    DB_PORT:str
    DATABASE_URL: str

    @model_validator(mode="before")
    def get_database_url(cls, values):
        values["DATABASE_URL"] = (f"postgresql+asyncpg://{values['DB_USERNAME']}:{values['DB_PASSWORD']}"
                                  f"@{values['DB_HOST']}:{values['DB_PORT']}/{values['DB_NAME']}")
        return values


    class Config:
        env_file = '.env'


settings = Settings()
