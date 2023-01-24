from sqlalchemy import create_engine
from sqlalchemy.sql import expression as sa_exp
from sqlalchemy import text
from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import (
    create_async_engine,
    AsyncSession,
)

engine = create_async_engine(
    "postgresql+asyncpg://practice:devpassword@localhost:35000/fastapi-practice"
)

def get_session() -> AsyncSession:
    with AsyncSession(engine) as session:
        yield session
