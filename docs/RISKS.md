# Risk register
Owner for all: Nirmal VG. Next review: 2026-12-24.

| ID | Category | Description | Prob | Impact | Mitigation | Status |
|---|---|---|---|---|---|---|
| R1 | AI quality | Letter claims skills not in resume | Med | High | Evidence-only prompt, citations, hallucination probes in evals | Open |
| R2 | Data quality | Multi-column or scanned PDFs parse badly | High | Med | User review step before embedding, clear scanned-PDF error | Open |
| R3 | Operational | Groq rate limits or outage | Med | Med | Timeouts, bounded retries, JD-hash caching | Open |
| R4 | Privacy | Resume text sent to a third-party provider | Med | High | Minimal context, disclosure to users, provider terms review | Open |
| R5 | Financial | Uncontrolled model spend | Med | Med | Per-user daily caps, token ceilings | Open |
