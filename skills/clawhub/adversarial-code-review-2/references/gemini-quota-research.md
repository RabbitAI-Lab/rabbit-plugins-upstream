# Gemini / agy Quota Research

**Status: NO public API for real-time quota checking.** Discovered 2026-06-12 during an
adversarial review of the quota-checking tooling (Codex Architect + agy Inspector).

## The problem

Google Gemini API (used by agy, the Antigravity CLI) has quota limits per project:
- Free tier: ~1500 req/day, ~60 req/min
- Pay-as-you-go (Tier 1+): higher but based on billing tier
- Resets at midnight Pacific time

But there is **no public API endpoint** to query remaining quota programmatically.
Confirmed by Google collaborator (ryanjsalva) in GitHub discussion #3096.

## What does NOT work

- `models.list` only validates the key, doesn't return quota info
- `/stats` in Gemini CLI is session-level only
- No HTTP headers carry remaining quota (unlike some other APIs)
- No `generativelanguage.googleapis.com` endpoint returns usage stats

## What COULD work (options, ordered by feasibility)

### Option A — Probe-based (recommended, low effort)
Send a minimal `generateContent` request to a cheap model (`gemini-2.5-flash` with
`{"contents":[{"parts":[{"text":"ok"}]}]}`). If the response is 200 → quota available.
If 429 → quota exceeded. Track 429 rate over time for a rough estimate.

```python
import urllib.request, json
req = urllib.request.Request(
    "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent",
    data=json.dumps({"contents": [{"parts": [{"text": "ok"}]}]}).encode(),
    headers={"Content-Type": "application/json", "x-goog-api-key": API_KEY}
)
try:
    urllib.request.urlopen(req, timeout=10)
    print("Quota available")
except urllib.error.HTTPError as e:
    if e.code == 429:
        print("Quota exceeded")
```

### Option B — Reactive counter (medium effort)
Log every 429 error from agy (or direct Gemini API calls) into a persistent counter
file. Display "X 429s in last 24h" as a quota-health proxy. Works for any CLI that
wraps Gemini (agy, google-gemini CLI, etc.).

```python
# In a file like ~/.hermes/data/quota-429-log.jsonl
{"ts": 1718200000, "provider": "gemini", "model": "gemini-2.5-flash", "code": 429}
```

### Option C — Google Cloud Monitoring (high effort, accurate)
Requires:
1. A GCP project with billing enabled AND the Gemini API linked
2. `gcloud` CLI installed and authenticated
3. Query `cloudaicompanion.googleapis.com/usage/response_count` metric

This gives real numbers but is overkill for most use cases. Only worth it if the
user already has GCP billing set up.

## How to integrate (for check-ai-quota.py)

Add a `gemini_quota()` function that:
1. Reads `GOOGLE_API_KEY` from env (check `os.environ.get()` first, then ~/.hermes/.env)
2. Validates key via `models.list` (returns model availability)
3. Sends probe to `gemini-2.5-flash:generateContent` (checks if 429)
4. Optionally reads the reactive 429 counter

JSON output shape:
```json
{
  "provider": "gemini",
  "key_valid": true,
  "models_available": ["gemini-2.5-flash", "gemini-3.1-pro-preview", ...],
  "probe_status": "ok",  // "ok" | "rate_limited" | "error"
  "recent_429s": 0       // from counter file
}
```

## Related files

- `scripts/check-ai-quota.py` — the script that should get this function
- `references/ai-quota-apis.md` — shared API reference doc
- `~/.hermes/plugins/hermes-quota-status/__init__.py` — statusbar plugin (also needs Gemini)
