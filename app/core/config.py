from pydantic import BaseSettings, Field

class Settings(BaseSettings):

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'

    db_url: str = Field(..., env='DATABASE_URL')

settings = Settings()
