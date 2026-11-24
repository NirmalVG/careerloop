# Testing

| Layer | Tooling | Location |
|---|---|---|
| Unit | pytest | apps/api/tests/test_config.py |
| Integration (real Postgres, rolled-back transactions) | pytest, pytest-asyncio, httpx | apps/api/tests/ |
| Lint and format | ruff | apps/api/pyproject.toml |
| Types | mypy | apps/api/pyproject.toml |

Run from apps/api (database must be up and migrated):

    uv run pytest -v
    uv run ruff check . && uv run ruff format --check .
    uv run mypy app

Principles
- Integration tests hit a real PostgreSQL with pgvector, never a mock.
- Each test runs in a transaction that is rolled back (savepoint mode).
- A test must be seen failing once before it is trusted (AI-SDLC 9.4).
- Coverage is not proof of effectiveness; critical logic is tested by behavior.
AI evaluation (retrieval and generation quality) is documented separately
in AI-EVALUATION.md once the golden set exists.
