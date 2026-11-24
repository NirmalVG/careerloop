# Database schema

Source of truth: apps/api/app/db/models.py and apps/api/migrations/.
Update this file in the same change as any migration.

| Table | Purpose |
|---|---|
| users | Accounts (own auth, see ADR-0001) |
| resumes | Uploaded resume files and ingestion status |
| resume_chunks | Section-aware text chunks, scoped by user_id |
| chunk_embeddings | Vectors keyed by (chunk_id, model), see ADR-0002 |

Planned (added with their features): job_descriptions,
generated_artifacts, eval_records.
