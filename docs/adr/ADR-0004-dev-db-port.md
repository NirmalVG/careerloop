# ADR-0004: Dev database exposed on host port 55432
Status: Accepted | Date: 2026-11-24
Context: Port 5432 collided with another service on the dev machine,
causing misleading authentication failures.
Decision: Map container 5432 to host 55432 and use 127.0.0.1 in URLs.
Consequences: Documented in README, .env.example and config defaults.
