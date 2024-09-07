from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase


engine = create_async_engine('sqlite+aiosqlite:///main.db', echo=True)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)

class Base(DeclarativeBase):
    pass

async def get_db() -> AsyncSession:
    async with async_session_maker() as session:
        yield session