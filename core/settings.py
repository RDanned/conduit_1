from pydantic import BaseModel, BaseSettings


# class MongoSettings(BaseModel):
#     mongo_url: str


class Settings(BaseSettings):
    mongo_url: str
    salt: str = 'salt123'

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'


settings: Settings = Settings()
