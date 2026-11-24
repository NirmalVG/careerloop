# CareerLoop

RAG-powered job search agent: upload a resume once, paste any job
description, get a match score, skill gaps, a citation-backed cover letter
and interview prep. Built under AI-SDLC-STD-001.

## Stack
Next.js 16, Tailwind, Shadcn UI, TanStack Query, FastAPI, PostgreSQL +
pgvector, Groq GPT-OSS 120B. See docs/TECH-STACK.md.

## Local setup
1. `docker compose up -d`            (Postgres on host port 55432)
2. `cd apps/api && cp .env.example .env`
3. `uv sync && uv run alembic upgrade head`
4. `uv run uvicorn app.main:app --reload`
5. `curl localhost:8000/health`      (expect status "ok")

## Docs
PRD, architecture, schema, ADRs and quality gates are in docs/.
