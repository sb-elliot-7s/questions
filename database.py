from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from settings import settings

engine = create_async_engine(settings().database_url)
LocalAsyncSession = sessionmaker(bind=engine, expire_on_commit=False, class_=AsyncSession)
Base = declarative_base()


async def get_session():
    async with LocalAsyncSession() as session:
        yield session
