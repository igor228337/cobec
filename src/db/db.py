from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine, AsyncSession
from src.enviroment import enviroment
from sqlmodel import SQLModel

__all__ = ["SQLModel"]

DATABASE_URL = enviroment.database_url

engine = create_async_engine(
    DATABASE_URL,
    pool_size=0,
    max_overflow=-1,
)
AsyncSessionLocal = async_sessionmaker(
    engine, expire_on_commit=False, class_=AsyncSession
)

async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async with AsyncSessionLocal() as session:
        yield session