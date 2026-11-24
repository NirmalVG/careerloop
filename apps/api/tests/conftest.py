import uuid

import pytest_asyncio
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine

from app.core.config import get_settings
from app.db.models import Resume, User


@pytest_asyncio.fixture(scope="session")
async def engine():
    eng = create_async_engine(get_settings().database_url)
    yield eng
    await eng.dispose()


@pytest_asyncio.fixture
async def session(engine):
    """A session inside a transaction that is always rolled back."""
    async with engine.connect() as conn:
        trans = await conn.begin()
        sess = AsyncSession(bind=conn, expire_on_commit=False)
        yield sess
        await sess.close()
        await trans.rollback()


@pytest_asyncio.fixture
async def seeded(session):
    """A user and a resume, for tests that need parent rows."""
    user = User(email=f"{uuid.uuid4()}@example.com", password_hash="not-a-real-hash")
    session.add(user)
    await session.flush()
    resume = Resume(user_id=user.id, file_key="resumes/test.pdf")
    session.add(resume)
    await session.flush()
    return user, resume
