import pytest
from sqlalchemy import delete, func, select, text
from sqlalchemy.exc import IntegrityError

from app.db.models import EMBEDDING_DIM, ChunkEmbedding, ResumeChunk, User

EXPECTED_TABLES = {"users", "resumes", "resume_chunks", "chunk_embeddings"}


async def test_expected_tables_exist(session):
    result = await session.execute(
        text("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'")
    )
    assert EXPECTED_TABLES <= {row[0] for row in result}


async def test_embedding_column_is_vector_with_configured_dimension(session):
    result = await session.execute(
        text(
            "SELECT format_type(atttypid, atttypmod) FROM pg_attribute "
            "WHERE attrelid = 'chunk_embeddings'::regclass AND attname = 'embedding'"
        )
    )
    assert result.scalar_one() == f"vector({EMBEDDING_DIM})"


async def test_database_rejects_unknown_section(session, seeded):
    user, resume = seeded
    session.add(
        ResumeChunk(
            resume_id=resume.id,
            user_id=user.id,
            section="hobbies",  # not an allowed section
            content="Chess",
            chunk_index=0,
        )
    )
    with pytest.raises(IntegrityError):
        await session.flush()


async def test_deleting_user_cascades_to_all_their_data(session, seeded):
    user, resume = seeded
    chunk = ResumeChunk(
        resume_id=resume.id,
        user_id=user.id,
        section="skills",
        content="Python, FastAPI",
        chunk_index=0,
    )
    session.add(chunk)
    await session.flush()
    session.add(
        ChunkEmbedding(chunk_id=chunk.id, model="test-model", embedding=[0.0] * EMBEDDING_DIM)
    )
    await session.flush()

    await session.execute(delete(User).where(User.id == user.id))

    chunks = await session.scalar(
        select(func.count()).select_from(ResumeChunk).where(ResumeChunk.user_id == user.id)
    )
    embeddings = await session.scalar(
        select(func.count()).select_from(ChunkEmbedding).where(ChunkEmbedding.chunk_id == chunk.id)
    )
    assert chunks == 0
    assert embeddings == 0
