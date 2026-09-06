# References: Model resilience & weak-model fallback (load in model_resilience mode)

Single source of truth: templates/quality_floor_matrix.yaml (flat,
machine-readable). Gate every model change:

    bash scripts/quality_floor_check.sh --task "<task>" --proposed-model "<model>"

## Tiers (grounded in the operator's live cloud fleet)
- tier1 (frontier): claude-opus-5, claude-opus-4-8, claude-sonnet-5,
  claude-sonnet-4-6, gpt-5.6-sol, gpt-5.5, gpt-5.4, grok-4.6
- tier2 (strong-fast): claude-haiku-4-5, gpt-5.4-mini, gpt-oss-120b,
  deepseek-v4-flash, gemini-3-flash, gemini-3.5-flash-low,
  gemini-3.1-flash-lite, grok-4.5, kimi-k3, glm-4.7, codestral-latest,
  gemma4:31b
- tier3: everything else (unknown names resolve to tier3)

## Policy (hard)
- cloud_only: local/offline models (gguf, ollama, llama.cpp, onnx) are
  rejected by the script. Never route a ShieldSwarm task to a local model.
- Never use weak-model fallback for security-critical review, incident
  command, production changes, or ROE work (floor = tier1).
- Unknown model name = tier3. When uncertain about a model, treat it as weak.

## Fallback sequences (per task type)
| task | floor | fallback sequence |
|---|---|---|
| security review / red-team analysis | tier1 | tier1 list order; below floor => block |
| incident command / prod change | tier1 | tier1 list order; below floor => block |
| code review, rollback plans, postmortems | tier2 | tier2 → tier1 |
| status/stakeholder updates | tier2 | tier2 → tier1 |
| triage, general chat | tier3 | any tier2+ preferred for speed |

## Degraded mode (required UX)
If the best available model is below the floor:
1. Do not silently downgrade.
2. Tell the user: quality is reduced for this task; suggest retrying when a
   floor-compliant model is reachable.
3. Log the event: python3 tools/self_improve.py log \
      --event "below_floor" --area floor \
      --context "task=... model=... floor=..."

## Speed guidance (tokens/second)
- Use the fastest model that passes the floor: tier2 models give higher
  throughput for tier2-floor tasks; reserve tier1 for floor-gated work.
- Prefer short prompts + this skill's machine-readable outputs
  (key=value) over long prose — smaller payloads = faster TTFT and
  completion.
