# Agent integration guide

This guide is intentionally model-agnostic. A caller may be a small local model, a hosted model, or a human using shell commands. Treat every model-generated interpretation as a hypothesis and let the CLI's JSON records remain the source of truth.

## Token-efficient protocol

1. `init --json` once. Supply a focused topic and PICOS when known.
2. `search --json` with a bounded `--limit`, explicit `--years`, and only the engines needed for coverage. Save the JSON result and inspect `failed_engines` before interpreting counts.
3. `extract`, `classify`, and `validate --json`. Use `validate --check-web` when a network check is permitted.
4. Use `rank --json --min-confidence medium` to pass only selected candidates to a model. Do not paste the entire evidence matrix when the ranked JSON plus provenance is sufficient.
5. Read `report.md` for human review. The durable records are `evidence.json` and `gaps.json`; their schemas are in `schemas/`.

## Required interpretation rules

- `statement` is a source-linked candidate cue, not a proof that the literature has an absence.
- `sources` are recognized identifiers. `verification=identifier-present` means syntax/provenance only; `verification=web-validated` means the requested resolver check passed.
- `confidence=High` is permitted only when every listed identifier resolves and at least two independent source labels are recorded. `Medium` is not proof; `Low` is exploratory.
- `importance.estimated=true` means the five scores are transparent baselines, not an expert judgment. Do not convert the total into a probability or a claim of novelty.
- A missing record, empty result, or failed API is search uncertainty. Never paraphrase it as “no studies exist.”
- Preserve `query`, exact key-free `request_urls`, `engines`, `years`, `limit`, `outcomes`, `provenance`, and `cache_warnings` when handing results between agents.

## Safe machine hand-off

Pass structured JSON between agents rather than prose when possible. Keep the following fields:

```json
{
  "schema_version": "2.1",
  "id": "gap-...",
  "statement": "...",
  "sources": ["10...."],
  "verified_sources": [],
  "verification": "identifier-present",
  "confidence": "Medium",
  "exploratory": false,
  "importance": {"total": 9, "estimated": true},
  "source_provenance": [{"source": "openalex", "identifier": "10...."}]
}
```

Unknown fields should be preserved, not guessed. If a field is missing or malformed, ask for a new CLI result or label the conclusion uncertain. Do not invent citations, query counts, confidence, or API coverage.
