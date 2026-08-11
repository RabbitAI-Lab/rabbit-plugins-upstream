# 🏆 arena-power-user-playbook

**Categories:** productivity, research  
**Public tags:** #productivity, #arena-ai, #prompting, #model-selection, #research

## ✨ Functionalities

Power-user guide to always getting top-tier frontier models on Arena.ai: Max router, Direct vs Agent vs Code selection, rotation caveats, Pineapple mitigation, message chunking, and a local fallback matrix when Arena is unavailable.

The complete functionality, workflows, limits, examples, and operational rules
from the unchanged skill are reproduced verbatim in **Complete Skill Reference**
below. That reference is authoritative; this README does not add or alter any
capability.

## 🚀 Usage

Install the skill from ClawHub:

```bash
npx --yes clawhub@latest install @orionshaowswmw/arena-power-user-playbook
```

Invoke this reference when choosing an Arena mode/model or diagnosing routing quality; apply the decision tables and fallback sequence in SKILL.md.

A representative command from the unchanged skill documentation is:

```bash
# Pre-flight self-heal (from sandbox-selfheal-guard)
source ~/skills/@orionshaowswmw/sandbox-selfheal-guard/scripts/selfheal_runner.sh

# Arena first
# (use arena.ai web UI Max)

# Fallback local if needed
export PATH="$HOME/.shim:$PATH"
./run_max_speed.sh q3 "fallback question" 128   # 34 t/s
./run_max_speed.sh r1 "deep verify" 256        # 14 t/s CoT

# Cache Arena responses for offline
python3 ~/prompt_cache_layer.py set arena_max "question" 128 /tmp/arena_response.txt
python3 ~/prompt_cache_layer.py get arena_max "question" 128  # 0.06s hit
```

Read the complete reference below before execution, use least privilege, and
inspect all outputs and exit codes.

## 🔐 Permissions & Requirements

• Read-only: it is a reference/guide skill
• Optionally invokes local fallback tools (edge-cpu-gguf-tuner, sandbox-selfheal-guard) if configured

All permissions above are capability requirements, not blanket authorization.
Grant only what the selected workflow needs, scope filesystem access to the
working directory, and do not elevate privileges unless SKILL.md explicitly
requires and explains it.

## 🔒 Security & Privacy

- Read-only reference; no data collection.
- Only uses Arena.ai as you direct.
- No secrets are read or transmitted.
- **Data handling:** the skill reads only user-selected inputs and files described above; it must not collect unrelated data.
- **Storage/logging:** inspect output and log locations before use. Logs can contain supplied inputs or derived results and should be protected accordingly.
- **Network boundary:** data leaves the machine only for endpoints and optional integrations explicitly documented above or in the unchanged SKILL.md; otherwise processing remains local.
- **Secrets:** API keys, tokens, passwords, and credentials must never be embedded in the skill or logged. Store required secrets in chmod-600 credential files or a dedicated secret manager.
- **Risks and mitigation:** review SKILL.md and every executable file before installation, use least privilege and dry-run modes where available, keep backups, and verify all generated output before relying on it.

## ✅ Verification Hash

This digest verifies every stable artifact file except `README.md`
(self-reference), generated `skill-card.md`, registry-generated `_meta.json`,
and `.clawhub/` bookkeeping.

**Artifact SHA-256 (TREE-SHA256-v1):** `a48a11f3b939738c5a44bd6e5df7786c4f3f0d7ad0590878a53818a64532d2c0`

Run from the installed skill directory:

```bash
python3 - <<'PY'
from pathlib import Path
import hashlib
root = Path('.')
excluded_parts = {'.git', '.clawhub', '__pycache__', '.pytest_cache'}
excluded_names = {'readme.md', 'skill-card.md', '_meta.json', '.published', '.ds_store'}
files = sorted(
    (p for p in root.rglob('*') if p.is_file()
     and not any(part in excluded_parts for part in p.relative_to(root).parts)
     and p.name.lower() not in excluded_names),
    key=lambda p: p.relative_to(root).as_posix(),
)
h = hashlib.sha256()
h.update(b'TREE-SHA256-v1\0')
for p in files:
    rel = p.relative_to(root).as_posix().encode('utf-8')
    data = p.read_bytes()
    h.update(rel); h.update(b'\0')
    h.update(str(len(data)).encode('ascii')); h.update(b'\0')
    h.update(data); h.update(b'\0')
print(h.hexdigest())
PY
```

The printed digest must exactly match the value above. A mismatch means a
functional file, script, configuration, or metadata file differs from the
published artifact; review before use.


## 📚 Complete Skill Reference (Unchanged)

The text below is copied from the installed `SKILL.md` body so every
functionality and usage instruction remains available without rewriting or
changing the skill itself.

---

# arena-power-user-playbook 🏆 v1.3.0 — MAX SPEED + FALLBACK MATRIX

**Always get GPT-5 / Claude Opus / Gemini Pro tier responses on Arena.ai without paying — now with local fallback when Arena throttles.**

## What's New in v1.3.0 — Debug Fixes & Features

**Debug fixes (from user "not responding and stuck" reports):**
- Added Pineapple weak-model 3-strike mitigation: detect vague/short/over-apologetic → new chat + Max re-route + prompt rephrase (was just "new chat")
- Added Agent Mode 5-message soft limit chunking strategy: split big tasks into 4-message chunks, fresh chat per chunk, carry summary via SESSION-STATE.md
- Added rotation caveat: GPT-5.4-High removed April 2026 manual picker but Max still routes — document shows how to verify via Max trace
- Fixed frontier list outdated mid-2026 → updated late July 2026 (GPT-5.6-Sol, Claude Opus 4.8, Gemini 3.1 Pro, Kimi K3, DeepSeek V4)
- Fixed missing local fallback → now integrates edge-cpu-gguf-tuner (34 t/s local) + sandbox-selfheal-guard when Arena down/throttles

**New features:**
- **Router vs Local Fallback Matrix**: when to use Arena Max vs local Qwen3-0.6B 34 t/s vs R1 14 t/s deep
- **arena_mode_detector.sh** helper: auto-detect Direct/Agent/Code mode from prompt complexity
- **Pineapple detector regex**: patterns like "As an AI", overly short <20 tokens, repeated apology
- **Integration with prompt-cache**: cache Arena Max responses locally → 0.06s hit when offline
- **Integration with fast-response-optimizer**: reply-first while Arena routes
- **Max trace debugging**: how to check why Max chose model, latency reasons

## One-Sentence Playbook (updated)

Use **Direct → Max** for most, **Code Arena → Max** for coding, **Agent Mode fresh chat each chunk** for multi-step, **local Qwen3-0.6B 34 t/s fallback** when Arena throttles/down (via edge-cpu-gguf-tuner v2 + run_max_speed.sh).

## Decision Tree v1.3.0

1. Simple quick → Direct Chat → **Max** (multimodal router 5M+ votes, +3 Elo vision, +12 Elo text)
2. Multi-step/research/build → **Agent Mode** `/agent` fresh chat per 4-message chunk; carry summary; T1 orchestrators; `run_swarm_optimized.sh` local assist
3. Coding → **Code Arena → Max** (Claude-Opus heavy routing; Kimi K3 frontend)
4. Vision/image → Direct → Max
5. Compare 2 models → Side-by-Side
6. Blind test → Battle Mode vote honestly
7. **Arena throttles / Pineapple / down → Local Fallback**: `./run_max_speed.sh q3 "question" 128` (34 t/s) or `r1` for deep

## Router vs Local Fallback Matrix (NEW)

| Condition | Use | Why | Speed | Cost |
|---|---|---|---|---|
| Online, simple | Arena Max | Best quality, free, 12 Elo over single | ~20-40 t/s cloud | Free |
| Online, coding | Code Arena Max | Claude Opus routing | ~25 t/s | Free |
| Online, complex multi-step | Agent Mode + Max | T1 orchestrator + Max | Variable | Free |
| Arena slow / 429 / throttled | Local Qwen3-0.6B Q4_K_M | 34 t/s local, instant, no rate limit | 34 t/s local | Free CPU |
| Arena down / offline needed | Local Qwen3 + prompt-cache | 0.06s cache hit = ∞ t/s | 0.06s hit | Free |
| Need deep verification | Local DeepSeek-R1 1.5B | CoT reasoning | 14 t/s | Free |
| Need coding specialist | Local Qwen2.5-Coder | 31 t/s + pp145 | 31 t/s | Free |

## Why Max Wins (unchanged but verified July 2026)

Max router trained 5M+ pairwise votes, latency-controlled:
- Vision +3 Elo over best single, 20+s faster
- Frontend code heavy claude-opus-4.5
- Text routes 62% gpt-5.2-chat-latest 38% diversified +12 Elo

## Critical Caveats Updated Late July 2026

- GPT-5.4-High removed manual picker April 2026 but Max still routes — check via `/max` trace if needed
- Agent Mode ~5-message soft limit community observed — **use chunking**: messages 1-4 task, message 5 summary, new chat next chunk
- Rotation: models in/out weekly; don't hardcode names; let Max decide
- Pineapple weak model still appears — 3-strike mitigation below
- Battle Mode for eval not work

## Pineapple Mitigation 3-Strike (NEW v1.3.0)

Detection regex:
```js
/(As an AI|I am an AI|I'm sorry.*can't|I cannot.*as an AI)/i
response.length < 20 tokens
/(apologize){2,}/
```

Mitigation:
1. Strike 1: New chat + same prompt → Max re-routes
2. Strike 2: Rephrase prompt more specific + add context + use Max
3. Strike 3: Switch to local fallback `./run_max_speed.sh q3 "rephrased question" 128` (34 t/s) and report Pineapple

## Agent Mode Chunking Strategy (NEW)

Old: one long thread hits 5-message limit → weak/confused
New:
- Chunk 1 (msgs 1-4): research phase, msg 4 = summary.md
- New chat Chunk 2: "Continue from summary: [summary] — next do X"
- Carry via `SESSION-STATE.md` cache (fast-response-optimizer)
- Use local swarm `run_swarm_optimized.sh` to assist between chunks

## If Weak/Bad Response

- Direct: switch to **Max** + rephrase + check trace
- Agent: **new chat** (re-rolls orchestrator) + summary carry
- Battle: vote honestly
- Persistent: local fallback `run_max_speed.sh q3` 34 t/s + prompt-cache

## Integration with Self-Heal & Max-Speed

```bash
# Pre-flight self-heal (from sandbox-selfheal-guard)
source ~/skills/@orionshaowswmw/sandbox-selfheal-guard/scripts/selfheal_runner.sh

# Arena first
# (use arena.ai web UI Max)

# Fallback local if needed
export PATH="$HOME/.shim:$PATH"
./run_max_speed.sh q3 "fallback question" 128   # 34 t/s
./run_max_speed.sh r1 "deep verify" 256        # 14 t/s CoT

# Cache Arena responses for offline
python3 ~/prompt_cache_layer.py set arena_max "question" 128 /tmp/arena_response.txt
python3 ~/prompt_cache_layer.py get arena_max "question" 128  # 0.06s hit
```

## Frontier Tier Late July 2026 Updated

- **GPT-5.6-Sol / 5.5 / 5.4** — general flagship multimodal, best latency/quality
- **Claude Opus 4.8 / 4.7 / Fable 5** — deep reasoning coding (Fable 5 suspended June 2026 export control, returns soon)
- **Gemini 3.1 Pro** — long context 2M vision price-efficiency
- **Claude Sonnet 4.6/5** — 80% tasks quality-per-dollar
- **Kimi K3** — #1 Frontend Code Arena July 2026
- **DeepSeek V4 Pro / R1** — math/reasoning ultra-cheap open-weight fallback
- **Local Qwen3-0.6B Q4_K_M** — 34 t/s 151 pp fastest edge, fallback when Arena down

Max still beats any single — let Max decide.

## Scripts Added v1.3.0

- `arena_mode_detector.sh` — complexity → Direct/Agent/Code recommendation
- `pineapple_detector.py` — regex + length heuristic
- `chunk_manager.py` — manages 4-msg chunks + summary carry

## URLs

- Direct: https://arena.ai/ (Direct)
- Agent: https://arena.ai/agent
- Leaderboard: https://arena.ai/leaderboard/agent
- Max: https://arena.ai/max
- Blog Agent Mode: https://arena.ai/blog/agent-mode/

Arena 10M+ users 700M+ convos 82M+ votes, $250M+ funding, mission free — verified late July 2026.

---

*README-only documentation remediation. No functional artifact file was changed.*
