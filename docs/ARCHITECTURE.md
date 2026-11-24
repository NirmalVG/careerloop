# Architecture (current state)

Browser (Next.js) -> Next.js route handlers (same-origin proxy)
  -> FastAPI -> PostgreSQL+pgvector, Groq API, embedding model

Implemented: API skeleton with deep /health, schema v1 (see
DATABASE-SCHEMA.md). Full target design: docs/PRD.md section 9.
Trust boundary: all user data is scoped by user_id at the data layer.
Decisions: docs/adr/.
