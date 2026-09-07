---
name: speechcanvas-free-expression-swarm
version: 2.0.3.1
author: orionshaowswmw
license: MIT-0
description: Four-agent image-prompt swarm (Muse drafts, Guardian safety-checks, Critic perfects realism, Composer finalizes) that produces lawful, consent-aware, non-deceptive symbolic imagery prompt packs as validated JSON for journalism, protest, censorship and free-expression themes. Use when the operator asks for a symbolic image or image prompt about protest, censorship, propaganda, press freedom, or free expression.
topics: [image-generation, multi-agent, free-expression, prompt-engineering, safety]
metadata:
  openclaw:
    emoji: 🎨
    homepage: https://clawhub.ai/orionshaowswmw/skills/speechcanvas-free-expression-swarm
---

# SpeechCanvas — Free-Expression Image Swarm (v2.0.3)

Turn a lawful creative brief into a **validated symbolic image prompt pack** through a
4-role refinement loop. Everything is JSON in, JSON out — any model can execute this.

## When to use / when not to

- ✅ Symbolic, lawful imagery about protest, censorship, propaganda, press freedom, silence, debate.
- ❌ Realistic depictions of real people doing things they did not do, fake evidence,
  fake documents, hate or harassment imagery. → Decline and offer a symbolic alternative.

## Hard safety rules (short form — full list in `references/rules.md`)

1. NEVER forge reality: no fake evidence, documents, ballots, screenshots, admissions, receipts, legal notices.
2. NEVER photoreal real people doing things they didn't; no real names, official seals, readable civic instructions.
3. NEVER private persons as targets/victims; no hate, harassment, dehumanization.
4. Deception is a SUBJECT, never a METHOD: deception-themed packs MUST carry at least one allowed motif
   (mask, mirror, frost, false crown, empty throne, frozen microphone, … full list in `references/rules.md`).
5. If a rule is unclear for the brief → ask the operator. Never guess on safety.

## Workflow (reply-first, ≤3 iterations)

```
brief → Muse draft JSON ──► Guardian check ──► Critic critique ──► Composer final pack
              ▲                  │(FAIL)                              │
              └──────────────────┘ redraft, iteration+1 (max 3)       ▼
                                                     scripts/safety_validator.py + validate_pack.py
                                                                  PASS → deliver pack + image instruction
```

1. **Reply first (speed):** immediately show the operator a one-line concept + Muse's draft JSON.
   Run the rest while the operator reads. This halves perceived latency.
2. **Muse** drafts beauty: light, lens, texture, setting, gesture → JSON `{subject, motif, lighting, lens, setting, gesture}`.
3. **Guardian** checks every hard rule → `{guardian_status: PASS|FAIL, reason, refined_prompt?}`.
   FAIL → Muse redrafts with `refined_prompt` (iteration+1, max 3).
4. **Critic** checks realism → `{critique, improved_details}` (specific: "light too flat → cold blue moonlight + dust").
5. **Composer** merges all into the final prompt pack that validates against `schema/prompt_pack.schema.json`.
6. **Deterministic gate (mandatory):** run the validators — they are ground truth, not opinions:
   ```bash
   python3 scripts/safety_validator.py --file pack.json      # exit 0=PASS 1=BLOCK 2=WARN
   python3 scripts/validate_pack.py pack.json                # structural schema check
   ```
   Treat validator PASS as "no known violation pattern found" — not proof of safety; still
   apply the `references/rules.md` checklist judgment and ask the operator on ambiguity.
   No python3? Perform the checklist in `references/rules.md` manually, step by step, and say so.
7. Deliver: final pack JSON + a one-paragraph image-generation instruction built from it.

## Role prompts (machine-readable: `swarm/roles.json`)

Load `swarm/roles.json` and use each role's `goal / must / never / output_fields` verbatim
as that sub-agent's instruction. Roles are terse (≤80 words) on purpose: less input per call,
fewer output tokens, faster generations. Roles may run in parallel where the orchestrator
supports it (Guardian and Critic are independent after Muse's draft).

## Output contract (the prompt pack)

Every final pack MUST validate against `schema/prompt_pack.schema.json`:
`subject, motif, lighting, lens, setting, gesture` (≤200 chars each), `constraints` (array,
must include the six safety constraints), `safety_tags` (enum: lawful, consent-aware,
non-deceptive, free-expression, symbolic-atmosphere), `iteration` (1–3), `guardian_status`
(PASS/FAIL — final packs must be PASS), `critic_notes` (≤500 chars), `deception_theme` (bool).
Complete examples: `references/examples.md` (journalism, protest, censorship, debate, civil liberties).

## Self-improvement (learn from every run)

After delivering, build the run record (prints to stdout, writes NOTHING by default):
```bash
python3 scripts/record_run.py --brief-hash <sha256-16> --iterations N --guardian PASS \
  --critic "<one line>" --pack pack.json
# operator opted in to a persistent log? append explicitly:
python3 scripts/record_run.py ... --out ./speechcanvas_runs.jsonl
```
At start of a session, if the operator keeps a `speechcanvas_runs.jsonl`, read the last 5 records:
recurring critic fixes → pre-inject into Muse's draft; recurring guardian failures → stricter redrafts.
Default is stdout-only; file persistence happens only when the operator explicitly passes `--out`.

## Token discipline

- SKILL.md (this file) is the only always-read file. Open `references/` files only when needed.
- Scripts run WITHOUT reading them into context — execute, read the exit code and JSON verdict only.
- All role outputs are terse JSON; no prose narration between steps.
- Iteration cap 3. If still FAIL after 3 → return the safest passing variant or ask the operator.

## Optional integrations (only if already installed — never assume)

- A local fast model: use it for Muse's first draft (Guardian/Critic/Composer stay on the primary model).
- A prompt cache: key = sha256(brief + constraints). Hit → skip the swarm, return cached pack.

## Compatibility

Plain files + optional stdlib Python 3 scripts. No vendor-specific tool syntax, no network,
no secrets, no shell required (scripts optional). Works in any SKILL.md-compatible agent
(Claude Code, Cursor, Codex CLI, OpenClaw, …) and any model that can read JSON.
