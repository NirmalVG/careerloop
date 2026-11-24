from fastapi import Depends, FastAPI
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.config import get_settings
from app.db.session import get_session

settings = get_settings()

app = FastAPI(title="CareerLoop API", version="0.1.0")


@app.get("/health")
async def health(session: AsyncSession = Depends(get_session)) -> dict:
    await session.execute(text("SELECT 1"))
    result = await session.execute(
        text("SELECT extversion FROM pg_extension WHERE extname = 'vector'")
    )
    pgvector_version = result.scalar_one_or_none()
    return {
        "status": "ok" if pgvector_version else "degraded",
        "environment": settings.environment,
        "database": "up",
        "pgvector": pgvector_version,
        "model": settings.groq_model,
    }
