# Audit history — 27 bugs found and fixed (v1.2 → v2.4)

Every fix below was independently verified before shipping (one AI-reported issue
was a false positive; one real bug the review missed was caught by a crash during
concurrency testing). This file is the deep record; SKILL.md carries only the rules.

## v2.5.4 — model-tags canonicalization (owner-supplied tag set) + distributed re-audit

No code changes. `references/model-tags.json` now carries the owner-supplied
canonical tag set: the redundant `llama-3.3-70b-versatile` alias entry was
merged into the single `llama-3.3-70b` "Groq · Cerebras" entry (25 → 24
primary entries; secondary + taxonomy unchanged). `references/model-tags.md`
synced to match (packaging note, row 3 cross-ref). Re-audit distributed
between the arena agent and the most capable models available via the stored
API keys (8 members, one per provider; 5 answered — OpenRouter 402 free-tier
wall, Mistral 4-rpm 429, Z.ai empty-completion bug are all known documented
issues; their 12-model buckets were web-verified by the arena agent instead).
Audit outcome: all 32 entries confirmed correct (1 live dissent rejected on
web evidence — Mistral Medium 3.5 is text+image in; 2 invalid 8B-voter
dissents documented); one advisory recorded (Mistral Small 4 119B-2603
architecture per HuggingFace card is MoE/256K vs the shipped "dense,
unverified" basis text — owner decision pending, tags shipped as-is per the
canonical spec). Validation: JSON parses, 24 primary + 8 secondary, all tags
∈ 15-tag taxonomy, model set cross-checked against ROUTES + BUILTIN_SPECS.

## v2.5.3 — ships the distributed per-model capability tags inside the package: references/model-tags.json (machine-readable; 25 primary routed models incl. the added groq tenant variant llama-3.3-70b-versatile + 8 secondary adjacent models, 15-tag taxonomy, per-entry evidence basis) and references/model-tags.md (human-readable; produced by a 6-model distributed job with web verification of every model). Validation: all 24 originally routed models covered, all primary tags ∈ taxonomy, all entries cross-checked against ROUTES + BUILTIN_SPECS. No code changes.

## v2.5.2 — no code changes. Note: skill-card.md is stripped from every publish by the ClawHub CLI (stripGeneratedSkillCards) and is now generated server-side by the registry; card.missing in verify resolves when the registry generates the record.

## v2.5.1 (= v2.5.0 content; version bumped because the registry held a stuck pending 2.5.0 record)

## v2.5.0 — grounding contract, reasoning-model compatibility, throughput, bootstrap fix

Found by: sandboxed 16-stage mock selftest + multi-model consensus review
(gpt-oss-120b, command-a-03-2025, nemotron-3-super-120b, gemini-3.1-flash-lite,
llm7, Llama-3.1-8B — 4 lenses: robustness / API-compatibility / machine-contract
/ token-efficiency) + live end-to-end bootstrap testing. Every fix verified.

1. **get-ai-router.sh was syntactically invalid bash** (truncated awk program,
   no `#__PAYLOAD__` marker): the advertised one-file bootstrap died with a
   syntax error before extracting anything. Rebuilt: real marker line,
   sha256-verified extraction, `[API_KEY]` now actually runs `--setup`.
   Verified end-to-end against the live registry + mock.
2. **Dead no-op `enable_local` loop** in `_load_specs` (referenced a key that
   never exists on the specs dict; body was `pass`) — removed.
3. **Credential-park clearing missed spec providers**: `available()` probed
   only `~/.config/<prov>/credentials.json`; providers configured with an
   inline `api_key`/`key_file` stayed parked for the full 900 s. Now uses
   `has_credentials()`.
4. **Reasoning-model compatibility**: `reasoning_content` honored when
   `content` is empty (DeepSeek-style); `<think>` blocks stripped from answers
   by default (`--no-strip-think` opt-out) so downstream agents never parse a
   leaked reasoning trace as answer content.
5. **Silent truncation hallucinations**: `finish_reason=length` was dropped on
   the floor — truncated answers looked complete. Now surfaced as
   `truncated` in the answer contract (cache entries carry it too).
6. **Cache never expired**: entries lived forever → stale answers served
   indefinitely. Entries now timestamped; `--cache-ttl` (default 7 days).
   Legacy entries without `ts` stay valid (back-compat).
7. **SSE usage-only chunks mis-parsed**: `choices: []` raised IndexError and
   the valid JSON was filed as an incomplete carry buffer (latent bug — only
   reachable once `stream_options.include_usage` was requested). Guarded.
8. **Strict servers could break streaming**: `stream_options` is now requested
   for the tok/s metric, with a single silent retry without it on HTTP 400.
9. **Learning overlay poisoning**: one >8×-median outlier (provider hiccup,
   cold start) could bury a fast route in the EWMA. 16-sample latency ring +
   median-based outlier guard; p50/p95, tok/s EWMA and a 2×-probe drift flag
   in `--learn`.
10. **Schema honesty**: `answer.v1` gained optional confidence/degraded/
    truncated/attempts/latency_s/tps; `learn.v1` gained lats/ewma_tps/outliers
    (both `additionalProperties: false` schemas updated in lockstep).
11. **--race N** (opt-in, ≤3 lanes, cheap tier only, never reserve/stream):
    parallel first-token race with per-lane claim rollback — measured TTFT
    wins without silently multiplying quota spend.

## v1.2.0 — concurrency & accounting (found by whole-source AI audit + verification)

1. Comment promised a 20% daily reserve; code allowed 100% → real 80% guard (only `-q5`/`-t best` spend the tail).
2. Cache key omitted `max_tokens` and `quality` → 50- and 4000-token requests collided → key is `v2|task|quality|max_tokens|system|prompt`.
3. `load_state`/`save_state` read-modify-write race (10 concurrent increments landed as 1) → `fcntl.flock` around the whole cycle.
4. Account-wide 429 parked only 1h (rediscovered the wall hourly) → parks until local midnight.
5. Gemini cooldown 1h but `day_count=9999` — status lied "ready" → cooldown and budget now agree.
6. Check-and-spend not atomic (two processes both spend the last slot) → claim inside the lock. Also fixed the double-count this introduced.
7. **Missed by the AI review**: shared `state.json.tmp` crashed concurrent writers → per-PID temp file.
8. Missing credentials treated as per-model failure (burned all retries) → provider-wide park, no try consumed.

## v1.3.0 — workspace integration + zero wasted API calls

`integrate.sh` (idempotent, zero API calls) creates `~/ai`, validates credentials
offline, restores from `cred_backup/`, seeds dead routes from shipped `health.json`
(17 known-dead routes = 17 wasted calls saved per fresh install). `--plan`,
`--status`, `integrate.sh` verified entirely offline.

## v1.5.0 — clean-machine perspective (2 of 5 providers configured)

9. One missing credentials file broke ALL providers (eager dict literal) → build only the provider being called.
10. Unwritable state dir crashed the router → in-memory fallback + warn.
11. Self-repair patched code but left stale docs → SKILL.md synced too.
12. Self-repair dead on arrival for real users → ship the payload inside the package.

## v1.6.0 — security + waste + footguns

13. **API key exposed in `ps`** (curl -H in argv) → headers via 0600 temp file, `-H @file`, deleted immediately.
14. Invalid `--max-tokens` spent real API calls to discover a typo → validated locally, 0 calls.
15. `integrate.sh` from any directory repointed `~/ai` at scratch checkouts → only writes when installed under `$HOME` or no entry exists.
16. Staleness detector could not see future fixes → sha256 comparison against the shipped blob.
17. Far-future corrupt cooldown bricked a route forever → cooldowns clamped to 24h max.
18. **Self-repair payload never shipped** (packager dropped `.b64`) → payload moved to `router_fixed.json`.
19. "Not stale" ≠ "current" → `integrate.sh` always audits and names each missing fix (❌ critical vs ⚠️ advisory).

## v2.0.0 — consumer-experience audit (empty `$HOME`, no keys)

20. `--status` said "quota spent" when the problem was *no key at all* → credentials checked first.
21. First run "all routes exhausted" with no hint → actionable setup help, exit code **3** (≠ 2 = rate-limited).
22. `integrate.sh` printed "Ready" with zero keys → prints NOT READY + next steps.
23. `--setup` wrote the key before testing (a typo destroyed a working credential) → verify first, restore on failure.
24. Self-repair gated on the old `.b64` name + wrong argv → repair actually runs (verified on a real registry install).

## v2.1.0 — final pre-release audit

25. Stale `router_fixed.b64` left in-package could "repair" users **backwards** → removed; the JSON blob is the single source of truth. Also re-verified: blacklisted routes still dead (5/5 sample), no credentials in shipped files, hostile response shapes handled, prompt injection into curl argv impossible, `tries=6` caps calls, midnight rollover correct.

Sealed-environment acceptance (empty HOME, no keys, no author files): install → repair
from bundled blob → key saved + live-verified → 12/12 checks passing.

## v2.4.0 — this release

26. `--discover --apply` "hot-reload" assigned `ROUTES`/`PROVIDER_SPECS` without `global` — the current process kept a stale routing table → fixed.
27. Spec-only setups (e.g. a local Ollama gateway) exited **3** ("no keys") on route exhaustion instead of **2** → spec providers count as configured.

New in v2.4.0: `--stream` (SSE live passthrough on the same security path),
`--learn` self-improvement overlay (bounded reordering, see SKILL.md), shipped
JSON Schemas (`schema/`), sandboxed 9-stage selftest (`scripts/selftest.sh`,
zero API cost), progressive-disclosure docs (this file + measurements/providers).

## Registry incident record (historical)

During v1.x–v2.1 the ClawHub registry kept serving 1.6.1 after later publishes
returned OK (versioned installs failed too — server-side). The package therefore
carries its own authoritative `router_fixed.json` and `integrate.sh` self-heals any
stale download (sha256-audited, version-agnostic). **The freeze resolved by
2026-09: installs deliver current code.** The self-heal remains as belt-and-braces.
A mirror slug `free-tier-ai-router-pro` exists from that period.
