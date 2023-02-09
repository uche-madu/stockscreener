from pydantic import BaseSettings
import os
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):

    class Config:
        env_file = ".env"
        
    PGHOST: str = os.getenv('PGHOST')
    PGPORT: str = os.getenv('PGPORT', 5432)
    PGDATABASE: str = os.getenv('PGDATABASE')
    PGUSER: str = os.getenv('PGUSER')
    PGPASSWORD: str = os.getenv('PGPASSWORD')
    DATABASE_URL: str = f"postgresql://{PGUSER}:{PGPASSWORD}@{PGHOST}:{PGPORT}/{PGDATABASE}"


settings = Settings()