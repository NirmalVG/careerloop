# ADR-0003: No ANN vector index in MVP; exact search scoped by user
Status: Accepted | Date: 2026-11-24 | Amends PRD sections 0 and 10
Context: PRD proposed HNSW. A user has roughly 15 to 40 chunks.
Options: HNSW; IVFFlat; exact scan with user_id index.
Decision: Exact search, filtered by user_id, no ANN index yet.
Rationale: Exact scan over dozens of vectors is sub-millisecond with
100% recall. ANN plus a WHERE filter can return fewer than k rows.
Trade-offs: Must re-evaluate if per-query candidate sets grow large.
Consequences: Revisit only if the benchmark shows a latency problem.
