---
name: nomos-decision-hub
slug: nomos-decision-hub
version: 1.2.0
displayName: NOMOS Decision Hub
description: Every decision leaves a trail. NOMOS traces each choice to its causal roots, stress-tests assumptions until they break, and rebuilds rankings from the survivors — a deterministic decision engine where nothing is hidden and everything is auditable. Validated by Singapore IMDA AI Verify at 95/100.
required_commands:
  - python3
metadata:
  openclaw:
    required_binaries:
      - python3
    emoji: "⚖️"
    homepage: "https://github.com/NOHN-AI/second-perspective"
---
# NOMOS Decision Hub
A deterministic, auditable decision orchestration layer built on causal reasoning — no probabilistic black boxes. Every decision decomposes into traceable causal topologies, supporting compliance-grade audit trails, scenario stress testing, and human-in-the-loop governance.
## Trigger Scenarios
Automatically activates when users ask about:
- Deterministic or auditable decision engine design
- Causal counterfactual analysis and root cause tracing
- AI decision compliance auditing (IMDA/EU standards)
- Decision scenario stress testing and robustness analysis
- Human-in-the-loop governance for high-stakes decisions
- Enterprise decision system deployment
## Core Capabilities
- **Deterministic Evaluation**: Hard-constraint thresholds plus explicit soft-constraint penalties — no hidden score adjustments
- **Granular Algorithm Auditing**: Every operation generates hash-chained audit events; any modification breaks verification
- **Causal Counterfactual Re-selection**: When assumptions fail, automatically computes transitive failure closure and re-selects surviving candidates
- **Scenario Stress Testing**: Supports declarative metric overrides, evidence gaps, and assumption failure simulation
- **Reverse Root Cause Tracing**: Traces observed deviations back to failed assumption points, outputting root cause hypotheses with causal chains
- **Sensitivity & Robustness Analysis**: Computes Pareto frontier, identifies fragile criteria, outputs ranking stability scores
- **Enterprise Deployment**: Docker containerization, PostgreSQL persistence, OIDC authentication
## Usage
### Basic Decision Analysis
```python
from second_perspective import IntelligentDecisionHub
from second_perspective.models import HubAnalysisRequest
request = HubAnalysisRequest.model_validate({
    "decision": decision_payload,  # See examples/market_entry.json
    "scenarios": [
        {"id": "SC1", "name": "Key assumption failure",
         "failed_assumption_ids": ["A1"]},
        {"id": "SC2", "name": "Cost shock",
         "metric_overrides": {"S2": {"capital_required": 6000000}}},
    ],
})
report = IntelligentDecisionHub().analyze(request)
print(report.model_dump_json(indent=2))
```
### Enterprise Deployment
```bash
docker build -t nomos-hub .
docker run -p 8000:8000 \
  -e SP_ENV=production \
  -e SP_API_KEY=your-secret-key \
  -e SP_DATABASE_DSN=postgresql://user:pass@db:5432/nomos \
  nomos-hub
```
## Deterministic Contract (Invariants)
- The engine never guesses missing weights, evidence, thresholds, or authorization relationships
- Hard constraints gate eligibility; soft constraints must declare explicit penalties — no silent score changes
- All behavioral policies carry `policy_id` and `version`, embedded in results
- Evidence quality is assessed by designated responsible nodes — the engine never fabricates credibility
- Assumption failures propagate along dependency graphs, explicitly naming affected alternatives
- Output is always "the leading candidate under declared inputs" — final authority rests outside the algorithm
- Approver name and `authorization_ref` must match the anchored decision owner
- All evaluations and approvals are hash-linked new revisions — no silent overrides
## License
Personal non-commercial research use only. Government/enterprise commercial use requires written authorization.
