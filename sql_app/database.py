from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv
from ..config import settings

load_dotenv()

PGHOST=os.getenv('PGHOST')
PGPORT=os.getenv('PGPORT')
PGDATABASE=os.getenv('PGDATABASE')
PGUSER=os.getenv('PGUSER')
PGPASSWORD=os.getenv('PGPASSWORD')


SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()