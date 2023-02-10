from pydantic import BaseSettings, Field

import os
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
        
    #PGHOST: str = os.getenv('PGHOST')
    #PGPORT: str = os.getenv('PGPORT', 5432)
    #PGDATABASE: str = os.getenv('PGDATABASE')
    #PGUSER: str = os.getenv('PGUSER')
    #PGPASSWORD: str = os.getenv('PGPASSWORD')
    #DATABASE_URL: str = f"postgresql://{PGUSER}:{PGPASSWORD}@{PGHOST}:{PGPORT}/{PGDATABASE}"

    class Config:
        env_file = ".env"
        
    db_url: str = Field(..., env='DATABASE_URL')

settings = Settings()

#print(settings.DATABASE_URL)