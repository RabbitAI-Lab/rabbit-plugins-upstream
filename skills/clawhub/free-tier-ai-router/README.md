# 🎛️ free-tier-ai-router

**Categories:** automation, agents, development  
**Public tags:** #automation, #llm-routing, #free-tier, #quota-management, #agents

## ✨ Functionalities

Quota-aware LLM router that squeezes maximum usable AI out of free-tier API keys across Gemini, Mistral, OpenRouter, Kilo and Cerebras. Probes model availability/quality, applies published rate limits, and routes requests to the cheapest capable model while preserving scarce daily quota.

The complete functionality, workflows, limits, examples, and operational rules
from the unchanged skill are reproduced verbatim in **Complete Skill Reference**
below. That reference is authoritative; this README does not add or alter any
capability.

## 🚀 Usage

Install the skill from ClawHub:

```bash
npx --yes clawhub@latest install @orionshaowswmw/free-tier-ai-router
```

Configure at least one supported provider key, run doctor/status, then invoke the router with general, fast, code, or best task mode as documented.

A representative command from the unchanged skill documentation is:

```bash
bash get-ai-router.sh <your-api-key>
ai "your question"
```

Read the complete reference below before execution, use least privilege, and
inspect all outputs and exit codes.

## 🔐 Permissions & Requirements

• Reads API keys from ~/.config/<provider>/credentials.json and the router keystore
• Sends prompts and system text to the selected third-party providers
• Writes persistent cache/cooldown/state under your home directory (e.g. ~/.cache/ai_router/)

All permissions above are capability requirements, not blanket authorization.
Grant only what the selected workflow needs, scope filesystem access to the
working directory, and do not elevate privileges unless SKILL.md explicitly
requires and explains it.

## 🔒 Security & Privacy

- Handles live provider API keys — keep the keystore permissions 600.
- Prompts and system text you send are forwarded to selected third-party AI providers.
- Persistent cache/cooldown/state is written under your home directory.
- Use --no-cache for sensitive work and clear local state when trust boundaries change.
- Review get-ai-router.sh and setup scripts before use, especially on shared systems.
- **Data handling:** the skill reads only user-selected inputs and files described above; it must not collect unrelated data.
- **Storage/logging:** inspect output and log locations before use. Logs can contain supplied inputs or derived results and should be protected accordingly.
- **Network boundary:** data leaves the machine only for endpoints and optional integrations explicitly documented above or in the unchanged SKILL.md; otherwise processing remains local.
- **Secrets:** API keys, tokens, passwords, and credentials must never be embedded in the skill or logged. Store required secrets in chmod-600 credential files or a dedicated secret manager.
- **Risks and mitigation:** review SKILL.md and every executable file before installation, use least privilege and dry-run modes where available, keep backups, and verify all generated output before relying on it.

## ✅ Verification Hash

This digest verifies every stable artifact file except `README.md`
(self-reference), generated `skill-card.md`, registry-generated `_meta.json`,
and `.clawhub/` bookkeeping.

**Artifact SHA-256 (TREE-SHA256-v1):** `3c0cf84a12f990ef69e0d89d9c73e1e324c812b71826d346a096d186785294af`

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

# 🎛️ free-tier-ai-router

**Get the most AI out of free keys, without hitting limits.**

Complements `model-fallback` (which reacts *after* failure) and `local-llm-router` (which routes
across local machines). This skill routes across **remote free tiers** and acts *before* failure,
using measured quota budgets.

## The measurements this is built on

Every number below came from probing **113 models across 5 provider keys** with live
completions on 2026-07-30 — not from docs, not from model names.

| Provider | Models answered a live prompt |
|---|---|
| Mistral | **40 / 42** |
| OpenRouter (free) | **12 / 14** |
| Kilo (free) | **11 / 13** |
| Gemini | **11 / 41** |
| Cerebras | **0 / 3** — account unfunded, every call 402 |
| **Total** | **74 / 113** |

### Three findings that drive the whole design

**1. Gemini's free tier is 20 requests per DAY, *per model*.**
The 429 body names it: `limit: 20, metric: generate_content_free_tier_requests`. Verified
per-model, not per-key: `gemini-3.6-flash` was exhausted while `gemini-3.5-flash` still returned
200 on the same key. → Gemini is treated as **scarce**, tried last, and budgeted per model.

**2. Mistral publishes exact limits in headers, and they vary 187×.**
Read from `x-ratelimit-limit-req-minute`:

| Model | req/min | | Model | req/min |
|---|---|---|---|---|
| `ministral-3b-latest` | **750** | | `mistral-large-latest` | **4** |
| `ministral-8b-latest` | 188 | | `magistral-medium-latest` | 5 |
| `codestral-latest` | 125 | | `mistral-small/medium` | 50 |

→ Routine work goes to 750/min models. The 4/min flagship is reserved, not squandered.

**3. A 429 is not a failure — it is a fact worth remembering, and its *scope* differs.**
Re-probing 21 Gemini 429s after a 45s cooldown recovered **0** — hard daily caps. Mistral 429s
clear in seconds. And OpenRouter meters **account-wide**: hitting
`Rate limit exceeded: free-models-per-day` kills *every* model on that key at once, so one 429
must sideline the whole provider rather than being retried model by model (observed live after
this skill's own probing exhausted the daily allowance). → Backoff is provider-specific, scoped
correctly (per-model vs per-account), and persisted so the next process inherits the knowledge.

### Measured quality (5 objective questions: 91-prime, bat-and-ball, strawberry r's, 9.11 vs 9.9, Canberra)

10 models scored a perfect 5/5. Fastest first:

| Model | Score | Latency |
|---|---|---|
| `mistral/mistral-medium-latest` | 5/5 | 0.43s |
| `gemini/gemini-3.1-flash-lite` | 5/5 | 0.63s |
| `gemini/gemini-3.5-flash-lite` | 5/5 | 0.66s |
| `openrouter/inclusionai/ling-3.0-flash:free` | 5/5 | 0.93s |
| `kilo/kilo-auto/free` | 5/5 | 1.46s |
| `kilo/nvidia/nemotron-3-ultra-550b-a55b:free` | 5/5 | 2.30s |

⚠️ Two Gemini models scored 0/5 — that was **quota exhaustion mid-test, not low quality**.
Verified separately. A benchmark that can't tell "wrong" from "rate-limited" produces a
poisoned ranking; this one re-checks every zero.

## Quick start (new users)

**Fastest — one self-contained script (recommended):**

```bash
bash get-ai-router.sh <your-api-key>
ai "your question"
```

`get-ai-router.sh` installs the package, upgrades it to the current router (payload
travels inside the script, checksum-verified), creates `~/ai`, and registers your key.
It works even though the registry entry is frozen — see the note below.

**Or, from a normal install:**

```bash
npx clawhub@latest install free-tier-ai-router
bash skills/free-tier-ai-router/install.sh <your-api-key>
ai "your question"
```

> ⚠️ **Registry note.** `clawhub publish` returns `OK. Published …` with an ID, but
> `/api/v1/skills/free-tier-ai-router/versions` has listed **1.6.1** as newest since —
> 1.7.0 through 2.1.0 were all accepted and none appeared. Versioned installs
> (`skill@1.6.1`) fail even for versions that exist. Because of this the package carries
> its own authoritative router (`router_fixed.json`) and `integrate.sh` repairs any stale
> download to current code automatically. A mirror is published at
> **`free-tier-ai-router-pro`**.

No key yet? Any one of these free tiers works — Mistral has the most generous limits:
[Mistral](https://console.mistral.ai/api-keys) ·
[Gemini](https://aistudio.google.com/apikey) ·
[OpenRouter](https://openrouter.ai/keys) ·
[Kilo](https://app.kilo.ai/profile)

`ai --doctor` diagnoses any setup problem.

## Usage

```bash
R=~/skill_inventions/free-tier-ai-router/router.py

python3 $R "explain X in one line"          # general: cheapest abundant model
python3 $R -t code "write a python retry decorator"
python3 $R -t fast "yes or no: is 17 prime"
python3 $R -t best -q 5 "audit this argument for logical errors"
python3 $R --status                         # live budget per route
python3 $R --plan -t code                   # show routing order, make no calls
python3 $R --reset                          # clear cooldowns
```

- `-q N` — only use models that **measured** ≥N/5.
- `--no-cache` — skip the SHA-256 response cache.
- Identical prompts return from cache in **~46 ms with zero API calls**.

## How it decides

```
task=general → cheap tier, highest req/min first   (spend abundance)
task=fast    → cheap tier, lowest measured latency
task=code    → code-tagged models first
task=best    → highest measured quality first
                     ↓
        skip anything in cooldown or over daily budget
                     ↓
        call → on success bank it; on 429 set provider-appropriate cooldown
               (gemini 1h + park for the day · others 60-300s · 402/404 24h)
                     ↓
        persist state atomically → next process inherits the knowledge
```

## Verified behaviour

| Test | Result |
|---|---|
| 25 distinct prompts back-to-back | **25/25 in 10s, zero 429s** |
| Gemini daily budget after that burst | **0/20 used on all 4 models** — scarce capacity untouched |
| Top 3 routes forced into cooldown | transparently fell through to route 4 |
| Repeat prompt | cache hit, 46 ms, no API call |
| `-q 5` gate | only 5/5-measured models offered |
| OpenRouter daily quota genuinely exhausted | whole provider parked in one step; **12/12 prompts still served** from remaining providers |

## v1.2.0 — bugs found by audit and fixed

Audited by feeding the entire source to a 1M-context model, then **independently verifying
every reported bug before fixing it** (one reported issue was a false positive; one real bug
the review missed was caught by a crash during concurrency testing).

| # | Bug | Concrete failure | Status |
|---|---|---|---|
| 1 | Comment promised a 20% daily reserve; code allowed 100% | scarce Gemini quota could be fully drained by routine traffic | fixed — real 80% guard, only `-q5`/`-t best` may spend the tail |
| 2 | Cache key omitted `max_tokens` and `quality` | a 50-token and a 4000-token request collided and served each other's answers | fixed — key is `v2\|task\|quality\|max_tokens\|system\|prompt` |
| 3 | `load_state`/`save_state` were a read-modify-write race | **measured: 10 concurrent increments landed as 1** — daily caps silently exceeded | fixed — `fcntl.flock` around the whole cycle |
| 4 | Account-wide 429 parked for only 1h | router rediscovered the same daily wall every hour until midnight | fixed — parks until local midnight |
| 5 | Gemini cooldown 1h but `day_count=9999` | `--status` reported "✅ ready" while the model was actually blocked all day | fixed — cooldown and budget now agree |
| 6 | Check-and-spend not atomic | two processes could both see 19/20 and both spend the last request | fixed — claim happens inside the lock |
| 7 | **Missed by the AI review**: shared `state.json.tmp` | concurrent `save_state` crashed with `FileNotFoundError`; first writer won, rest died | fixed — per-PID temp file |
| 8 | Missing credentials treated as per-model failure | one dead provider burned all 6 retries before healthy providers were reached | fixed — provider-wide park, doesn't consume the try budget |

Also fixed a double-count introduced by fix #6: `_claim()` and `note_result()` both incremented
`day_count`, so 20 calls recorded as 22. `note_result` no longer spends budget — the atomic
claim is the single source of truth.

### Post-fix verification

| Test | Before | After |
|---|---|---|
| 12 concurrent processes | crashed, 1/12 recorded | **12/12, 0 crashes, 0 leaked counters** |
| Accounting at N=5/12/20 | 20 calls → 22 recorded | **exact at every N** |
| Corrupt state file | silently wiped all state | recovers cleanly |
| Provider with no credentials | gave up entirely | falls through to a working provider |
| Cache hit | 46 ms | 40 ms |

## v1.3.0 — workspace integration + zero wasted API calls

**Install and wire up:**
```bash
npx clawhub@latest install free-tier-ai-router
bash skills/free-tier-ai-router/integrate.sh     # makes ZERO API calls
ai "your question"
```

`integrate.sh` creates the `~/ai` entry point, validates credential files on disk (no
network), restores from `cred_backup/` if a snapshot wipe removed them, and seeds the
cooldown state from shipped `health.json`. It is idempotent.

### Eliminated API calls

| Waste source | Before | After |
|---|---|---|
| Rediscovering permanently-dead routes on every fresh install / `--reset` | 1 wasted call per dead route (**17 routes**) | **0** — shipped in `health.json`, enforced before any network call |
| Cerebras (unfunded, always 402) | called, 402, cooldown, repeat next reset | never called |
| Repeat identical prompt | 1 call | **0** — cache checked first |
| One answer | 1 call | 1 call (no speculative parallel fan-out) |

Verified: `ai --plan`, `ai --status` and `integrate.sh` are **entirely offline** — they read
disk state only. Confirmed by asserting the success/failure counters stay at zero.

`health.json` records only *structural* failures (402/403/404/400, retired models, Labs-only
models). Transient 429s are deliberately excluded — those recover and must stay routable.

### ⚠️ Registry version pinning — read this if `fcntl` is absent from your copy

The ClawHub registry can keep serving an **older** release after a newer one publishes
successfully. Observed directly: 1.2.0 and 1.3.0 both returned
`OK. Published …`, yet `install` and `update` continued to deliver **1.1.0**, and a
`--dry-run --json` confirmed the server's `latestVersion` was still `1.1.0`. Versioned
installs (`skill@1.3.0`) return *"Skill not found"* for every version, including ones that
demonstrably exist. This is server-side and cannot be fixed from the client.

A stale 1.1.0 copy is genuinely dangerous: it lacks the concurrency lock (parallel use
**crashes** on a shared temp file and can exceed daily caps) and the dead-route table
(wastes ~17 API calls relearning what was already measured).

**`integrate.sh` therefore self-heals.** It inspects the code — not the version string — for
`fcntl` and `DEAD_ROUTES`, and if they are missing it patches `router.py` in place from a
known-good local source, or refuses to proceed with a clear warning. Verified end-to-end: an
installed 1.1.0 copy was auto-upgraded and then passed all 9 suite tests.

## v1.5.0 — final audit: 4 more bugs, found by changing perspective

The previous versions were tested **in this workspace**, which quietly hid failures. Testing
as a *clean machine with only some providers configured* exposed these:

| # | Bug | Why it hid | Fix |
|---|---|---|---|
| 9 | **One missing credentials file broke ALL providers.** `call()` built a dict literal that eagerly invoked `creds()` for every provider, so an absent `cerebras` key raised `FileNotFoundError` while routing to Mistral — every request returned "no credentials". | My workspace had all 5 keys, so the eager evaluation never raised. | build only the provider being called |
| 10 | Unwritable state dir **crashed** the router (`PermissionError`) | state dir is always writable here | degrade to in-memory + warn; routing is unaffected |
| 11 | `integrate.sh` patched code but left **stale v1.1.0 docs** — users read instructions that never mention `integrate.sh` | I read the source copy, not the installed one | sync `SKILL.md` too |
| 12 | Self-repair only worked if fixed source already existed locally → **dead on arrival for real users** | my workspace *is* the source | ship `router_fixed.b64` (checksum-verified) inside the package |

Also: a "credentials missing" park now clears the moment the file appears — previously
repairing your key appeared to do nothing for 15 minutes, and clearing only the provider-level
park left every per-model cooldown still set.

### Verified on a clean machine (2 of 5 providers configured)

```
🔧 repaired from bundled router_fixed.b64 (checksum verified)
✅ providers with valid credential files: 2/5
✅ seeded 17 known-dead routes — 0 API calls wasted
general → "Paris."   code → works   best → "No" (91 is not prime)
cache repeat → 0 API calls     8 parallel → 8/8 recorded, 0 leaks
```

All 16 blacklisted routes were **re-probed live** and confirmed still dead (no capacity
wrongly lost); all 21 configured routes confirmed reachable.

## v1.6.0 — security + waste + footgun

| # | Bug | Impact | Fix |
|---|---|---|---|
| 13 | **API key exposed in the process list.** Keys were passed as `curl -H "Authorization: Bearer …"`, readable by any local process via `ps -eo args` for the whole request. Confirmed live. | credential disclosure on shared/multi-user hosts | headers written to a `0600` temp file, passed as `-H @file`, deleted immediately |
| 14 | Invalid `--max-tokens` (e.g. `-5`) produced HTTP **422 on every route in turn** — real API calls spent to discover a client-side typo | wasted quota | validated locally before dispatch; `0` calls |
| 15 | `integrate.sh` run from **any** directory rewrote `~/ai` to point at that copy — running it on a scratch/test checkout silently repointed the user's main entry point at throwaway code (reproduced) | broken workspace | only writes `~/ai` when the skill lives under `$HOME`, or when no entry point exists yet |

| 16 | **Staleness detector could not see future fixes.** It grepped for `fcntl`/`DEAD_ROUTES` — markers of the *v1.2* fixes. A v1.5 copy contained both, passed the check, and silently kept the v1.6 key-in-`ps` vulnerability. | security fixes never reach existing installs | detector now compares the installed `router.py` against the **sha256 recorded in the shipped blob** — version-agnostic, catches any drift including future releases |

| 17 | **A corrupt or clock-skewed timestamp permanently bricked a route.** A `cooldown_until` written far in the future (state corruption, clock jump, bad edit) was honoured literally — one test produced a 10-year cooldown with no recovery short of `--reset`. | silent permanent capacity loss | cooldowns are clamped to a 24 h maximum; legitimate short cooldowns are unaffected |

| 18 | **The self-repair payload never shipped.** ClawHub's packager silently drops `.b64` files — local dir had 12 files, the published package had 11, and the missing one was `router_fixed.b64`. Every "self-healing" claim since v1.4.0 was therefore inert for real consumers. Caught only by diffing a fresh install against the source directory. | self-repair silently absent | payload moved to `router_fixed.json` (an extension the packager keeps); `integrate.sh` reads JSON first and falls back to `.b64` |

| 19 | **"Not stale" did not mean "current".** With no repair blob present the detector fell back to feature-grep for *old* markers, so a copy missing only the newest fix was silently declared fine. Reachable in normal use because the registry lags several releases behind. | users unknowingly run outdated code | `integrate.sh` now **always** audits the installed `router.py` and names each missing fix, separating ❌ critical (concurrency, key exposure, wasted calls) from ⚠️ advisory |

### v2.0.0 — consumer-experience audit (installed cold, in an isolated sandbox)

Tested as a brand-new user: empty `$HOME`, no credentials, no access to the author's tree.

| # | Bug | Consumer impact | Fix |
|---|---|---|---|
| 20 | `--status` reported **"provider quota spent"** when the real problem was *no API key at all* | sent new users chasing a rate-limit problem they did not have | credentials are checked before any quota logic; reports "no API key configured" |
| 21 | First run failed with **"all routes exhausted"** — no hint that keys were required | dead end on first contact | actionable setup help listing free-tier signup links, exit code **3** (distinct from 2 = genuinely rate-limited) |
| 22 | `integrate.sh` printed **"Ready"** and 5 green routes with **zero** keys installed | actively misleading | prints "NOT READY" plus exact next steps when no key is present |
| 23 | `--setup` wrote the new key **before** testing it — a typo destroyed a working credential | left users worse off than before | verifies first, restores the previous key on failure, removes the file if there was nothing to restore |
| 24 | Self-repair was gated on the old `.b64` filename after the payload moved to `.json`, and passed the wrong argv — staleness was detected but **repair never ran** | every consumer kept stale code | both fixed; verified repairing a real registry install |

New commands: **`ai --setup <key>`** (auto-detects the provider from the key format, then live-verifies it) and **`ai --doctor`** (shows which providers are configured, how many routes are usable, and runs a live test).

### v2.1.0 — final pre-release audit

| # | Issue | Fix |
|---|---|---|
| 25 | `router_fixed.b64` was left in the package and had gone **stale** (checksum `4828289a` vs current `207407a5`). `integrate.sh` falls back to `.b64` when `.json` is absent — so on any copy missing the JSON it would have "repaired" a user *backwards* to older code. | removed; JSON blob is now the single source of truth |

Also re-verified before release: a random sample of blacklisted routes is still genuinely
dead (5/5, no capacity wrongly lost); no credentials appear in any shipped file (the two
`sk-or-v1-`/`csk-` matches in `router.py` are key-*prefix* patterns for provider
auto-detection, not secrets); unknown provider response shapes fall through to the next
route instead of crashing; concurrent `--setup` calls leave a valid credentials file.

### Sealed-environment acceptance test (empty `$HOME`, no keys, no author files)

```
install → repaired from bundled blob → key saved + live-verified → answering
1 general ✅   2 code ✅   3 best -q5 ✅   4 cache 0 calls   5 1 answer = 1 call
6 bad args rejected   7 doctor 10/21 usable   8 dead provider 0 calls
9 key hidden from ps  10 12 parallel: 12/12, 0 leaks
11 bad key does not clobber a good one       12 Gemini 4/4 daily budgets unspent
```

### Additional verification this round

- **No credential leakage** into error messages, `state.json`, or cache files (scanned).
- **Hostile provider responses** — empty body, HTML 502, truncated JSON, `content: null`,
  missing `choices`, 100 KB payload — all handled without crashing (tested against a local
  server returning each shape).
- **Prompt injection into curl argv** (`-H evil: 1 --output /tmp/pwned`) does not escape: the
  prompt is JSON-encoded and piped via stdin, never interpolated into the command line.
- `tries=6` genuinely caps API calls at 6 (instrumented).
- `-q5` yields 11 routes with **0** below-threshold violations; scarce Gemini sits at
  position 18/21 in general mode — tried last, as designed.
- Corrupt `router_fixed.b64` is **rejected on checksum** rather than installed.
- `integrate.sh` is idempotent across repeated runs.
- **Midnight rollover** verified: a route parked "until midnight" yesterday frees correctly
  today, while a same-day exhausted budget stays blocked.
- `_until_midnight()` returns a sane next-midnight timestamp (verified mid-day: 20.5 h out).

## Limits and honesty

- **Cerebras is in the table but unusable** — the key authenticates (200 on `/v1/models`) yet
  every inference returns 402. It is deliberately excluded from routing until funded.
- **Kilo paid models are excluded**: balance is $0; only its 13 free models are routed.
- Quality scores come from 5 questions — enough to catch obvious reasoning failures, not a
  substitute for a full benchmark suite.
- Rate limits were read from live headers where published (Mistral) and from error text
  elsewhere (Gemini). Providers change these; re-run `probe.py` to refresh.
- The router does not stream. For interactive streaming, call a provider directly.

---
## Debugging

This skill includes debug enhancement framework for error handling, logging, and recovery.

### Enable Debug Mode
```bash
export DEBUG_LEVEL=debug
export DEBUG_LOG=/tmp/free-tier-ai-router-debug.log
```

### Run Diagnostics
```bash
python3 scripts/debugger.py diagnose free-tier-ai-router
```

### View Logs
```bash
tail -f /tmp/free-tier-ai-router-debug.log
```

### Run Tests
```bash
python3 -m pytest tests/ -v
```

---

*README-only documentation remediation. No functional artifact file was changed.*
