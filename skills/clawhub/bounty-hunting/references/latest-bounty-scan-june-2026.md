# Latest Bounty Scan Results — June 13, 2026

Most recent scan. See also `scans/2026-06-13.md` for the full session log.

## Summary
- High-value bounties ($50+) in target languages: **0 actionable**
- Only real $5k bounty (tenstorrent/tt-metal) is C++ hardware kernels — outside wheelhouse
- openai-python: null-output crash cluster is best opportunity (no bounty, but high visibility)

## New Bounties (Last 48h)

### tenstorrent/tt-metal #46862 — $5,000 (C++)
- Optimize atanh/asinh/acosh with log1p-based SFPU implementations
- Competition: 1 competing PR already (#46908 by Tne-max, submitted ~5h after issue)
- Verdict: Skip — C++ hardware kernels, fast-mover advantage lost

### Dipraise1/Engram — 3 bounties (unspecified amounts)
- #24 benchmarks, #23 OpenAPI docs, #22 TypeScript SDK
- All saturated with competing PRs
- Verdict: Skip

### $10 Opire Fork Farms (ignore)
- victorjones6awpg/Casbin, davontepowlowsk1i/*, rodrickparker11/TiKV, juanitahagenes/ClickHouse
- All $10 on major-repo forks, confirmed fake

## openai-python Issues Worth Tackling

### 🔴 HIGH PRIORITY: Stream null output crash (5+ duplicate reports)
Real user pain — `responses.stream()` crashes with `TypeError: 'NoneType' not iterable` when `response.completed` has `output=null`. Likely simple null-check fix.

| Issue | URL |
|-------|-----|
| #3325 | https://github.com/openai/openai-python/issues/3325 |
| #3321 | https://github.com/openai/openai-python/issues/3321 |
| #3314 | https://github.com/openai/openai-python/issues/3314 |
| #3313 | https://github.com/openai/openai-python/issues/3313 |
| #3312 | https://github.com/openai/openai-python/issues/3312 |

### 🟡 Other Bugs
- #3341 — `construct_type()` ValueError on bare dict annotation
- #3338 — IndexError in `_transform_recursive` with bare dict TypedDict
- #3303 — InvalidURL when NO_PROXY has newlines
- #3294 — websocket_base_url corrupts URLs with http:// in query params
- #3282 — AzureOpenAI AAD bearer token 401 regression in 2.34.0
- #3269 — Non-streaming calls hang behind NAT (no TCP keepalive)
- #3263 — Streaming structured output parses incomplete JSON early
- #3256 — `client.images.edit()` fails to pass image_url
- #3231 — `summary="auto"` no reasoning summary on gpt-5.3-codex

### 🔵 Enhancements
- #3375 — Consider migrating from httpx to httpx2
- #3277 — RFC: Proactive Server-Side Cancellation via Request-Timeout-Ms
- #3273 — Use Trusted Publishing to upload to PyPI
- #3271 — AzureOpenAI: promote x-ms-served-model into Response.model
- #3264 — README "Nested params" example calls non-existent method

## Tracked PR Status
- **#3194** (shell completion): CLOSED (merged or rejected)
- **#3180**: NOT FOUND — likely deleted or never created
