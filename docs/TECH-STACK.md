# Tech stack and rationale

| Layer | Choice | Why |
|---|---|---|
| Frontend | Next.js 16, TypeScript, Tailwind, Shadcn UI | Streaming UI, accessible primitives |
| Server state | TanStack Query v5 | Caching, optimistic updates |
| API | FastAPI, Pydantic v2 | Typed contracts, async, SSE |
| Data | PostgreSQL 17 + pgvector, SQLAlchemy 2.0 async, Alembic | One store for relational data and vectors |
| LLM | Groq, openai/gpt-oss-120b | Low-latency streaming |
| Embeddings | To be decided in Step 3 (ADR-0005) | Must be evaluated, not assumed |
| Tooling | uv, ruff, pytest | Fast, reproducible |

Deviations from the standard's reference stack: none material.
