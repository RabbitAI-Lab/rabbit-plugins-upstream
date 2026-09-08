# Audit history — 27 bugs found and fixed (v1.2 → v2.4)

Every fix below was independently verified before shipping (one AI-reported issue
was a false positive; one real bug the review missed was caught by a crash during
concurrency testing). This file is the deep record; SKILL.md carries only the rules.

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
