---
name: nomos-decision-hub
description: This skill should be used when a user wants to build, evaluate, audit, or study deterministic (non-probabilistic) decision-making, causal counterfactual analysis, compliance-grade decision audit trails (IMDA AI Verify style), scenario stress-testing, algorithm-ledger verification, or human-in-the-loop governance for high-stakes decisions. It packages the NOMOS Intelligent Decision-Hub v0.3.0 methodology, architecture docs, the IMDA 95/100 causal-audit report, and runnable examples for individual non-commercial research.
agent_created: true
---

# NOMOS Intelligent Decision-Hub

## Overview

NOMOS is an auditable orchestration layer for **deterministic decision-making**. It does not use probabilistic black boxes: every decision is decomposed into a traceable causal topology where assumptions, constraints, evidence, weights, and evaluation rules are all declared, versioned, hash-chained, and replayable. It scored **95/100** in Singapore's IMDA AI Verify causal-audit assessment.

The engine combines structured evaluation, fine-grained algorithm audit, causal counterfactual reselection, declared scenario stress tests, a structural cognitive-risk challenge layer, an information-acquisition priority queue, and a human governance gate — all sealed into one immutable `HubReport`.

This skill packages the methodology, architecture documentation, the IMDA report, and runnable examples so a developer can **study and prototype** the approach. The complete engine source lives in the upstream repository (see *Obtaining the engine* below); this skill is the research/onboarding bundle, not a replacement for the engine.

## When to use

Trigger this skill when a request involves any of:

- Building or reviewing a **deterministic / auditable decision engine** (no invented probabilities, weights, or missing facts).
- **Causal counterfactual analysis**: "if assumption A fails, which alternatives collapse?"
- **Compliance-grade audit trails** for AI decisions (IMDA AI Verify, algorithmic accountability, EU-style audit logging).
- **Scenario stress-testing** of a decision under declared metric/evidence/assumption failures.
- **Human-in-the-loop governance**: owner + authorization_ref anchored approval that cannot be silently overwritten.
- **Backward causal root-cause tracing**: "deviation observed → which assumption failure could explain it?"
- **Weight sensitivity / robustness analysis**: Pareto frontier computation and identification of fragile criteria under weight perturbation.
- **Enterprise deployment** of the decision engine: Docker container, PostgreSQL durable persistence, OIDC identity verification.
- Explaining or reproducing the NOMOS v0.2 Decision Foundation invariants or the v0.3 Hub architecture.

## Core capabilities

1. **Deterministic evaluation** — hard constraints gate eligibility; soft constraints apply explicit penalties; normalized weighted scoring with no hidden adjustments.
2. **Fine-grained algorithm audit** — every major operation emits an `AlgorithmAuditEvent` (rule, input, output, prior-hash, self-hash); `algorithm_audit_root_hash` seals the whole execution chain. Any alteration breaks verification.
3. **Causal counterfactual reselection** — on assumption failure, compute the transitive invalidation closure, drop dependent alternatives, reselect the leader among survivors, and recompute the Pareto frontier. Mark `leader_stable` / `leader_changed` / `no_viable_alternative`.
4. **Declared scenario stress runs** — `HubAnalysisRequest.scenarios` lets the caller declare metric overrides, missing/disputed evidence, or failed assumptions; each scenario re-runs the deterministic engine and returns a full audit chain plus scenario fingerprint.
5. **Structural cognitive-risk scanner** — challenges structural decision risks without inferring mental state (no diagnosis of people).
6. **Information priority queue** — ranks what evidence/assumption to acquire or review next.
7. **Human governance gate** — approver name + `authorization_ref` must match the anchored decision owner; every evaluation/approval is a new revision chained to the previous record by hash.
8. **Causal reconstruction (backward root-cause tracing)** — the mirror image of forward counterfactual analysis. Given `DeviationSignal`(s) from the perception layer, the `CausalReconstructor` traces *backward* along the declared assumption dependency graph using BFS, producing a set of `RootCauseHypothesis` candidates — never a single "answer". Each hypothesis carries its causal chain, explained signals, missing evidence, and a recommended human verification action. The full trace is sealed with hash-chained `AlgorithmAuditEvent`s and an `algorithm_audit_root_hash`.
9. **Robustness & sensitivity analysis** — computes the Pareto frontier from normalized criterion vectors; perturbs each criterion weight by ±`sensitivity_delta` and checks whether the baseline leader survives. Produces `SensitivityCase` entries, identifies `fragile_criterion_ids`, and calculates `ranking_stability` (fraction of perturbations where the leader was unchanged). Stable leaders are those surviving all perturbations.
10. **Enterprise deployability** — `Dockerfile` + `docker-compose.yml` for containerized deployment; `PostgresDecisionRepository` / `PostgresHubReportRepository` for durable persistence (auto-selected when `SP_DATABASE_DSN` is set); OIDC identity verification via `SP_OIDC_ISSUER`/`SP_OIDC_CLIENT_ID`/`SP_OIDC_AUDIENCE` (JWT verified against issuer JWKS, RS256, audience + expiry checked); API key fallback via `SP_API_KEY` with `hmac.compare_digest`; production fails closed (503) when neither is configured.

## How to use

### Obtaining the engine

The full engine is **not bundled here** (kept as the licensor's moat). Install it from the upstream source:

```bash
git clone https://github.com/NOHN-AI/second-perspective.git
cd second-perspective
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -e ".[dev]"
```

Package name: `nomos-decision-engine` (v0.3.0). Python ≥ 3.11.

### Python API

```python
from second_perspective import IntelligentDecisionHub
from second_perspective.models import HubAnalysisRequest

request = HubAnalysisRequest.model_validate({
    "decision": decision_payload,          # see references/market_entry.json
    "scenarios": [
        {"id": "SC1", "name": "Critical assumption fails",
         "failed_assumption_ids": ["A1"]},
        {"id": "SC2", "name": "Cost shock",
         "metric_overrides": {"S2": {"capital_required": 6000000}}},
    ],
})
report = IntelligentDecisionHub().analyze(request)
print(report.model_dump_json(indent=2))
```

The returned `HubReport` contains: stored baseline decision record, per-scenario results, cognitive findings, information priorities, algorithm-ledger verification status, policy snapshot, and report hash.

### CLI demonstrations

```bash
nomos-demo            # v0.2 Decision Foundation on market_entry.json
nomos-hub-demo        # v0.3 Hub with two stress scenarios
```

### API server

```bash
export SP_ENV=development
uvicorn second_perspective.api.main:app --reload
```

Endpoints: `POST /v1/hub/analyze`, `GET /v1/hub/reports/{hub_run_id}`, `POST /v1/decisions/evaluate`, `GET /v1/decisions/{decision_id}`, `GET /v1/decisions/{decision_id}/history`, `POST /v1/decisions/{decision_id}/approval`, `GET /v1/auth/me`, `GET /health`. Production fails closed (503) unless `SP_API_KEY` or `SP_OIDC_ISSUER` is configured.

### Regenerate the OpenAPI schema

```bash
SP_PUBLIC_BASE_URL=https://decision.example.com python scripts/export_openapi.py
```

A pre-generated schema ships at `references/openapi-action.yaml`.

## The deterministic contract (invariants)

These are the long-term boundaries of the foundation. Honor them when building on NOMOS:

- The engine must not guess missing weights, evidence, metrics, owners, thresholds, or authorization relations.
- Hard constraints decide eligibility; soft constraints must declare explicit penalties — no silent score changes.
- Every behavior-affecting policy carries a `policy_id` and `version`, embedded in the result.
- Evidence quality is assessed by a named responsibility node; the engine does not fabricate credibility.
- Assumption failure propagates along the dependency graph and names affected alternatives.
- Output is only ever "the leading candidate under the declared inputs"; final authority stays outside the algorithm.
- Approver name + `authorization_ref` must match the anchored decision owner.
- Every evaluation/approval is a new revision chained by hash; nothing is silently overwritten.

## References

Load these into context as needed (do not pre-load all):

- `references/DECISION_FOUNDATION_V0_2.md` — the deterministic decision foundation, its invariants, and the v0.2 architecture.
- `references/INTELLIGENT_DECISION_HUB_V0_3.md` — from decision base to decision hub: algorithm audit, counterfactual reselection, scenarios, cognitive scanner, governance.
- `references/README.md` — full project README (install, run, API, production boundary).
- `references/IMDA_AI_Verify_Causal_Audit_Report.pdf` — the IMDA AI Verify 95/100 causal-audit compliance report.
- `references/MATERICA_COMPLIANCE_DESIGN.md` — SPL-G1 hardware-level physical-material compliance abstraction layer (four hardware gateways: binary-phase constraint, directional signal, PIM proximity, SBC irreversibility).
- `references/ENTERPRISE_DEPLOYMENT.md` — enterprise deployment guide: Docker, PostgreSQL persistence, OIDC identity verification, environment variables, and production security configuration.
- `references/openapi-action.yaml` — generated OpenAPI / Action schema for the hub API.
- `references/market_entry.json` — a complete sample `DecisionRequest` / `HubAnalysisRequest` (Japan market-entry example) used by the demos.

## Scripts

- `scripts/export_openapi.py` — regenerates the OpenAPI schema (set `SP_PUBLIC_BASE_URL`).
- `scripts/quickstart.py` — runs the bundled `market_entry.json` through `IntelligentDecisionHub` if the engine is installed; prints the sealed `HubReport`.

### Enterprise deployment

For production-grade deployment with durable persistence and enterprise identity:

```bash
# Docker (single container)
docker build -t nomos-hub .
docker run -p 8000:8000 \
  -e SP_ENV=production \
  -e SP_API_KEY=your-secret-key \
  -e SP_DATABASE_DSN=postgresql://user:pass@db:5432/nomos \
  nomos-hub

# Or docker-compose (includes Postgres)
docker-compose up -d

# OIDC (optional, e.g. Keycloak)
export SP_OIDC_ISSUER=https://keycloak.example.com/realms/nomos
export SP_OIDC_CLIENT_ID=nomos-api
export SP_OIDC_AUDIENCE=nomos
```

See `references/ENTERPRISE_DEPLOYMENT.md` for full configuration details.

## License & authorization

This skill is released for **individual non-commercial research** only. It is **not open-source**.

The underlying NOMOS engine uses a dual-track license: free for individual non-commercial research; **paid commercial authorization is required for government / enterprise use**. Licensor and governing law follow the user's location (within the PRC → Shanghai Linming Junhua Technology Co., Ltd.; outside the PRC → NOHN AI TECHNOLOGY PTE. LTD., Singapore law + SIAC arbitration).

Do not strip, repackage, or redistribute the engine or this skill for commercial purposes without obtaining written commercial authorization from the licensor.
