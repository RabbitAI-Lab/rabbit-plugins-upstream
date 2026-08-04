# Enterprise Deployment Guide

NOMOS Intelligent Decision-Hub v0.3.0 supports production-grade deployment with Docker containerization, PostgreSQL durable persistence, and OIDC enterprise identity verification.

## 1. Quick start: Docker

### Build and run (single container)

```bash
docker build -t nomos-hub .
docker run -p 8000:8000 \
  -e SP_ENV=production \
  -e SP_API_KEY=your-secret-api-key \
  nomos-hub
```

The container runs as a non-root user (`app`), with a health check on `/health` (30s interval, 3 retries).

### Docker Compose (with PostgreSQL)

```yaml
# docker-compose.yml (provided in the upstream repository)
# Starts the NOMOS API + a PostgreSQL database
docker-compose up -d
```

## 2. Environment variables

| Variable | Required | Description |
|---|---|---|
| `SP_ENV` | Yes | `development` (default) or `production`. Production fails closed (503) when no auth is configured. |
| `SP_API_KEY` | Conditional | Static API key for bearer-token auth. Required in production unless OIDC is configured. |
| `SP_DATABASE_DSN` | No | PostgreSQL connection string (e.g. `postgresql://user:pass@host:5432/dbname`). When empty, in-memory repositories are used. |
| `SP_OIDC_ISSUER` | No | OIDC issuer URL (e.g. `https://keycloak.example.com/realms/nomos`). When set, JWT bearer tokens are verified against the issuer's JWKS. |
| `SP_OIDC_CLIENT_ID` | No | OIDC client ID (used as the expected audience claim). |
| `SP_OIDC_AUDIENCE` | No | Explicit audience to validate. If empty, audience verification is skipped. |

### Example `.env`

```bash
SP_ENV=production
SP_API_KEY=

# PostgreSQL — set to enable durable persistence (leave empty for in-memory)
SP_DATABASE_DSN=

# OIDC — set to enable enterprise identity verification (leave empty for API key only)
# SP_OIDC_ISSUER=https://keycloak.company.example/realms/nomos
# SP_OIDC_CLIENT_ID=nomos-api
# SP_OIDC_AUDIENCE=nomos
SP_OIDC_ISSUER=
SP_OIDC_CLIENT_ID=
SP_OIDC_AUDIENCE=
```

## 3. Authentication flow

The API supports two authentication modes, evaluated in this order:

### OIDC (enterprise)

When `SP_OIDC_ISSUER` is set, incoming `Authorization: Bearer <JWT>` tokens are verified:

1. Fetch the issuer's `.well-known/openid-configuration` to discover `jwks_uri`.
2. Fetch JWKS keys from the discovered endpoint.
3. Verify the JWT signature (RS256), expiry, issuer, and audience (if configured).
4. If verification succeeds, the request is authenticated. Claims are available at `GET /v1/auth/me`.

If OIDC verification fails and `SP_API_KEY` is also set, the system falls through to API-key mode.

### API key (simple)

When `SP_API_KEY` is set, incoming bearer tokens are compared using `hmac.compare_digest` (constant-time comparison) against the configured key.

### Production fail-closed

When `SP_ENV=production` and neither `SP_API_KEY` nor `SP_OIDC_ISSUER` is configured, the API returns `503 Service Unavailable` on all protected endpoints.

## 4. Persistence

### In-memory (default)

When `SP_DATABASE_DSN` is empty, the engine uses `InMemoryDecisionRepository` and `InMemoryHubReportRepository`. Data is lost on restart. Suitable for development and testing.

### PostgreSQL (production)

When `SP_DATABASE_DSN` is set, the engine automatically uses `PostgresDecisionRepository` and `PostgresHubReportRepository` for durable, multi-tenant persistence. The connection is established on application startup.

## 5. API endpoints

| Method | Path | Auth | Description |
|---|---|---|---|
| `GET` | `/health` | None | Health check + version |
| `GET` | `/v1/auth/me` | Bearer | Identity snapshot (OIDC claims or API-key subject) |
| `POST` | `/v1/hub/analyze` | Bearer | Run a full Hub analysis with scenarios |
| `GET` | `/v1/hub/reports/{hub_run_id}` | Bearer | Retrieve a stored Hub report |
| `POST` | `/v1/decisions/evaluate` | Bearer | Evaluate a decision request |
| `GET` | `/v1/decisions/{decision_id}` | Bearer | Retrieve a decision record |
| `GET` | `/v1/decisions/{decision_id}/history` | Bearer | Retrieve the full revision history |
| `POST` | `/v1/decisions/{decision_id}/approval` | Bearer | Record a human approval |

## 6. Dependencies

Runtime dependencies (from `pyproject.toml`):

- `fastapi >=0.110, <1.0`
- `pydantic >=2.6, <3.0`
- `pyyaml >=6, <7`
- `uvicorn[standard] >=0.29, <1.0`
- `asyncpg >=0.29, <1.0` (PostgreSQL async driver)
- `python-dotenv >=1.0, <2.0`
- `python-jose[cryptography] >=3.3, <4.0` (JWT/OIDC verification)

Python >= 3.11 required.

## 7. Causal reconstruction (v0.3+)

When the Hub receives `DeviationSignal`(s) — observable metric deviations from the perception layer — the `CausalReconstructor` engine traces *backward* along the declared assumption dependency graph:

1. **Signal-to-assumption mapping** — match each deviation signal's metric name against assumption falsification conditions.
2. **Backward BFS** — from matched seeds, traverse the reverse dependency graph toward root causes, stopping at assumptions verified by supplied, non-expired evidence.
3. **Hypothesis construction** — each root candidate becomes a `RootCauseHypothesis` with: causal chain, explained signals, missing evidence IDs, recommended verification action, and severity (ERROR/WARNING/INFO based on criticality and blast radius).
4. **Audit trail** — each phase emits hash-chained `AlgorithmAuditEvent`s, sealed with an `algorithm_audit_root_hash`.

The output is a `CausalReconstructionReport` — a structured diagnostic input for human decision-makers. The engine never declares a single root cause as "the answer."

## 8. Robustness analysis (v0.3+)

The `analyze_robustness` function evaluates decision stability under weight perturbation:

1. **Pareto frontier** — from normalized criterion vectors of eligible alternatives, identify non-dominated candidates.
2. **Sensitivity sweep** — for each criterion, perturb its weight by ±`sensitivity_delta` (from `DecisionPolicy`), renormalize remaining weights, and re-evaluate leaders.
3. **Fragility identification** — criteria whose perturbation changes the leader are marked as `fragile_criterion_ids`.
4. **Stability score** — `ranking_stability` = fraction of perturbation cases where the baseline leader was unchanged.

Output: `RobustnessReport` with frontier, sensitivity cases, fragile criteria, and stable leaders.

## 9. Materica compliance (hardware-level)

NOMOS integrates with SPL-G1's Materica specification through a hardware-level compliance abstraction layer. See `references/MATERICA_COMPLIANCE_DESIGN.md` for the full design document.

Four hardware gateways encode the Materica physical constraints:

1. **Binary-phase constraint** — spontaneous state-flip monitoring (16-bit sliding window).
2. **Directional signal** — multi-target broadcast detection + reverse CONFIG transaction counting.
3. **PIM proximity** — compute-address == store-address identity check.
4. **SBC irreversibility** — physical destruction latch (temperature/voltage/radiation sensors, OR-gated, software-unrecoverable).

Any gateway failure triggers chip lockdown — independently of logical audit failures.
