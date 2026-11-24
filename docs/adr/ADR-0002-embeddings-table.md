# ADR-0002: Embeddings in a separate table keyed by (chunk_id, model)
Status: Accepted | Date: 2026-11-24 | Amends PRD section 10
Context: PRD put the vector on resume_chunks.
Options: column on chunk; separate table with model name.
Decision: chunk_embeddings(chunk_id, model, embedding vector(384)).
Rationale: Embedding model is a hypothesis; we must compare models in
the eval harness and always know which model produced a vector.
Trade-offs: One extra join. A model with a different dimension needs
its own table or migration.
Consequences: Re-embedding never touches source text.
