# ADR-0001: Own users table and FastAPI JWT auth
Status: Accepted | Date: 2026-11-24
Context: Draft schema referenced Supabase auth.users while the API is FastAPI.
Options: Supabase Auth; own auth in FastAPI.
Decision: Own `users` table, FastAPI-issued JWT, Argon2id hashing.
Rationale: One auth path, no external dependency, full control of tenancy.
Trade-offs: We own password handling and its security review (gate G8).
Consequences: Auth is implemented and threat-modeled in its own step.
