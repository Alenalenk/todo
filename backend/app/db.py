"""
db connection related stuff
"""
from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import create_engine, text
from sqlalchemy.schema import CreateSchema

from settings import get_settings

engine = create_async_engine(get_settings().DATABASE_URL)

engine_sync = create_engine(get_settings().DATABASE_URL_SYNC)

async_session_maker = async_sessionmaker(autocommit=False, autoflush=False, bind=engine, expire_on_commit=False)

async def create_schema():
    async with async_session_maker() as session:
        stmt = CreateSchema("todos", if_not_exists=True)
        await session.execute(stmt)
        await session.commit()

class Base(DeclarativeBase):
    pass


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session
