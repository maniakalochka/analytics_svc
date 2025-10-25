from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.pool import QueuePool
from core.config import settings

DB_URL = settings.get_database_url()
DATABASE_PARAMS = {
    "poolclass": QueuePool,
}

engine = create_async_engine(url=DB_URL, echo=True, **DATABASE_PARAMS)

SessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
)


async def get_async_session() -> AsyncGenerator[AsyncSession]:
    async with SessionLocal() as session:
        try:
            yield session
        except Exception as e:
            await session.rollback()
            raise e