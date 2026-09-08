# Sealed Report Specification (P0 upgrade, v2.0)

Every decision from the hub can be emitted as a **sealed report** — tamper-evident,
verifiable, and machine-readable. This is the artifact auditors consume.

## Report structure (JSON)

```json
{
  "report_id": "rep-<uuid>",
  "schema_version": 1,
  "engine": "SPL NOMOS Decision Hub",
  "engine_version": "2.0.0",
  "generated_at": "2026-08-08T12:00:00Z",
  "decision": {
    "question": "approve vendor X?",
    "verdict": "reject",
    "confidence": "high",
    "chain": [
      {"op": "narrative-strip", "input_hash": "sha256:...", "output": "..."},
      {"op": "assumption-probe", "input_hash": "sha256:...", "output": "..."},
      {"op": "fragility-hedge", "input_hash": "sha256:...", "output": "..."},
      {"op": "responsibility-anchor", "input_hash": "sha256:...", "output": "..."},
      {"op": "causal-reconstruction", "input_hash": "sha256:...", "output": "..."}
    ]
  },
  "evidence": {
    "scenarios": ["stress-case-01", "adversarial-02"],
    "sources": ["policy-v3.md", "vendor-contract.pdf"]
  }
}
```

## Sealing mechanism

1. Hash each operator's output → `input_hash` chain (each step references the
   previous hash — a Merkle-style causal chain).
2. Canonicalize the full report (deterministic JSON serialization).
3. Seal: `seal = sha256(canonical_report + sealed_at + nonce)`.
4. Publish: report JSON + `seal` + a signed envelope (HMAC with the hub's key).

## Verification (for auditors)

```bash
# recompute the seal from the published report
python verify_seal.py report.json --expect <seal>
```

Output: `SEAL VALID` or `TAMPERED` with the mismatched segment.

## Rules

- Every P0/P1 decision MUST produce a sealed report; P2 optional.
- `confidence` ∈ {low, medium, high} — derived from scenario coverage, never
  subjective.
- Audit trail is append-only; corrections create a new report linking the old
  `report_id` as `supersedes`.

## Integration

- Online demo mirrors this format: nohnlins.com/audit/ (SPL Cognitive Audit
  Engine). Skill and website share the same five-operator chain semantics.
- Multi-language export: the report body carries a `lang` field (zh/en); export
  renders the same causal chain in the target language without re-running the
  engine.
