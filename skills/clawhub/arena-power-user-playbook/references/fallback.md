# Fallback and weak-response playbook

## Cloud-only fallback (no local models)

Standing rule for this skill: **no local GGUF/llama.cpp fallbacks**. When
arena.ai is throttled, degraded, or down, route the *same model families*
through alternative cloud providers you already have API keys for.

| Situation | Do | Verify first |
|---|---|---|
| 429 / rate limit on arena.ai | wait out the window; if work is blocked, continue via an equivalent cloud model family (e.g. GPT-5.x via OpenAI, Claude x.x via Anthropic, Gemini x.x via Google, DeepSeek/GLM/Kimi/Qwen/Grok via their native or aggregator APIs) | the model actually exists at the provider (check its live model list — names rotate) |
| arena.ai down | same: pick the family closest to what you would have used (see the dated snapshot for which family was leading at your snapshot date) | provider status page |
| one provider degraded mid-task | switch providers for the *remaining* steps; do not re-run completed steps | keep the SESSION-STATE.md summary so the new chat/provider resumes without redoing work |

Cloud equivalence is *approximate*: different providers run different
weights/harnesses for "the same" model name. Say so in any artifact that
relies on the result.

**Never** do this (removed from v1.x for cause): installing llama.cpp or
downloading GGUF models as a fallback, or citing local tok/s numbers for
0.5B–1.5B models as equivalent to frontier cloud models. They are not
equivalent, and it violates the cloud-only standing rule.

## Weak-response escalation (3-strike, measurable version)

v1.x's "Pineapple" detector (regex "As an AI", <20 tokens, apology count)
was not runnable and not testable. The executable replacement:

`python3 scripts/arena_playbook.py weak --response "..." [--expect-short]`

Flags (each weighted; bands: weak>=50, medium>=25, strong<25):
refusal_pattern(30), too_short(20), apology_density(15), vagueness(10),
repetition(15), truncated_ending(10). Code blocks are stripped before
word counting. **The tool reports screening flags only — it never claims
the response is bad.** A legitimate short answer is "weak" by word count;
`--expect-short` exists for exactly that.

Known false-positive paths (screening, by design):
- "I can't ..." in the opening of a short-but-legitimate answer (use
  `--expect-short` when brevity is the point of the answer).
- Self-identification like "I'm an AI enthusiast" reads as the refusal
  self-identification pattern; it scores 30 (medium band alone) — treat a
  lone refusal_pattern flag on a substantive answer as noise.
- A single hedge phrase in a very short answer trips `vagueness` (threshold
  is one filler per ~50 words; longer answers are not flagged for one hedge).

Escalation when a weak band appears on a real task:

1. **Strike 1** — new chat, same task, same mode; log it:
   `python3 scripts/arena_playbook.py stats log --event weak_response
   --model <name> --mode <mode> --note "strike1: band=weak"`
2. **Strike 2** — rephrase: add one concrete constraint or example, keep
   the mode; if Agent mode, start a fresh chat (a new chat re-rolls the
   agent's plan) and carry state via `state next`.
3. **Strike 3** — change the variable: switch tier (higher compute tier
   for the same model) or switch to a different family from the live
   leaderboard's top rows; log `--event model_note`.
4. **Persistent** (>=3 weak on the same task) — switch provider per the
   cloud fallback table above, or split the task (the task may be
   ill-posed, not the model).

## Chunking long Agent tasks (state carry)

Long multi-chat work loses context between chats. The pattern:

```
python3 scripts/arena_playbook.py state --file SESSION-STATE.md --action init --goal "Ship X"
# ... do chunk 1 in chat 1 ...
python3 scripts/arena_playbook.py state --file SESSION-STATE.md --action add \
  --phase research --done "collected A" --done "verified B" --next "write C"
python3 scripts/arena_playbook.py state --file SESSION-STATE.md --action next
# paste the printed block as the first message of a NEW chat
```

`next` prints a carry block that states goal, completed items, next items,
and the "do not redo completed items" constraint. The state file is
markdown with YAML frontmatter — human-readable and machine-parseable,
safe to commit.

Notes:
- "Start a fresh chat each chunk" is a context-management heuristic for
  long work, not a claim that Agent Mode has a hard message limit (v1.x's
  "5-message soft limit" was an unverified community observation and is
  not documented by arena.ai — treat chunking as best practice, not a
  workaround for a documented limit).
- `init` refuses to overwrite without `--force`; `add` de-duplicates
  items; `validate` checks the file's integrity.

## Self-improvement loop (local, no telemetry)

`stats` keeps a local JSONL log (default `./playbook_log.jsonl`) of what
happened: weak_response, mode_pick, rotation_check, chunk_start,
chunk_end, model_note. Periodically:

```
python3 scripts/arena_playbook.py stats report --log ./playbook_log.jsonl
```

Read your own data before blaming a model: if weak_response events cluster
on one mode (e.g. Agent with files), the task shape is the variable, not
the model.
