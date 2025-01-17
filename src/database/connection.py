import os

from sqlalchemy import MetaData
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from dotenv import load_dotenv
from src.config import DATABASE_URL

load_dotenv()

engine = create_async_engine(DATABASE_URL)
async_session_maker = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
metadata = MetaData()

class Base(DeclarativeBase):
    pass