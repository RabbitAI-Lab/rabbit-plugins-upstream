# AI CLI Quota APIs — Direct programmatic access

**Updated 2026-07-31** — Standalone CLI startup and explicit endpoint inventory.
All five providers share the optional external adapter
`~/.hermes/plugins/hermes-quota-status/quota_api.py`.

## Architecture

```
quota_api.py  ←  shared module (token reading + API calls)
   ├── check-ai-quota.py  ←  CLI script (human + JSON output)
   └── hermes-quota-status/__init__.py  ←  Hermes TUI statusbar plugin
```

The CLI imports the adapter lazily. Importing `check-ai-quota.py` and running
`--help` therefore require only the Python standard library. A quota check still
requires the `hermes-quota-status` plugin; if it is absent, the CLI reports a
per-provider error in its normal human or JSON output without a traceback.

No tmux scraping or URL-embedded API keys are used. Each direct request reveals
the caller's IP address, request timing, and association with the authenticated
account to the target provider. Credentials are sent in headers and are never
intentionally printed. The provider-specific caveats below are additional to
that baseline disclosure.

## Claude Code (Pro subscription)

- **Token**: `~/.claude/.credentials.json` → `claudeAiOauth.accessToken`
- **Endpoint**: `https://api.anthropic.com/api/oauth/usage`
- **Status**: First-party Anthropic endpoint, but undocumented and
  community-discovered; it is not a supported public API contract and may change.
- **Auth**: `Authorization: Bearer <token>`
- **Privacy**: Sends the Claude OAuth credential to Anthropic and requests
  subscription utilization and reset times.
- **Response**:
  ```json
  {
    "five_hour": {"utilization": 27.0, "resets_at": "2026-06-12T18:30:00Z"},
    "seven_day": {"utilization": 10.0, "resets_at": "2026-06-19T09:00:00Z"}
  }
  ```
- **Note**: Claude returns utilization as percentages (0-100). The old code had a
  scale="fraction" bug that inflated sub-1% values to 80%. Fixed 2026-06-12.

## Codex (ChatGPT Plus subscription)

- **Token**: `~/.codex/auth.json` → `tokens.access_token`
- **Endpoint**: `https://chatgpt.com/backend-api/wham/usage`
- **Status**: First-party/official ChatGPT service endpoint used for Codex
  account usage, but not a documented public developer API contract.
- **Auth**: `Authorization: Bearer <token>`
- **Privacy**: Sends the ChatGPT OAuth credential to OpenAI and requests account
  rate-limit utilization and reset times.
- **Response**:
  ```json
  {
    "rate_limit": {
      "primary_window": {"used_percent": 11, "reset_at": 1779762941},
      "secondary_window": {"used_percent": 4, "reset_at": 1780313088}
    }
  }
  ```

## Gemini / agy (Google AI Studio)

- **Key**: `GOOGLE_API_KEY` env var or `~/.hermes/.env` → `GOOGLE_API_KEY=...`
- **Endpoints**:
  - `https://generativelanguage.googleapis.com/v1beta/models`
  - `https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent`
- **Status**: Both are official Google Generative Language API endpoints. They
  are not quota-reporting endpoints; `models.list` validates the key and
  `generateContent` is used only as a live availability probe.
- **Auth**: `x-goog-api-key: <key>` (header, NOT URL query string)
- **Privacy**: Sends the API key and a minimal prompt (`ok`) to Google. The probe
  processes content and consumes a small amount of model quota and may incur cost.
- **Quota**: Google does NOT expose a public quota API. We work around this with:
  1. `models.list` to validate the key (step 1)
  2. Minimal `generateContent("ok")` probe to HTTP 200 vs 429 (step 2)
- **Rate limits** (free tier, published):
  - ~1500 requests/day per project
  - ~60 requests/minute per project
  - Resets at midnight Pacific time
  - Applied per project, not per API key
- **Probe response**:
  ```json
  {
    "key_valid": true,
    "available_models": ["gemini-2.5-flash", ...],
    "model_count": 28,
    "probe": {"status": 200, "rate_limit_remaining": null}
  }
  ```

## GLM / Z.AI coding plan

- **Key**: `GLM_API_KEY` env var, falling back to `ZHIPU_API_KEY`
- **Endpoints** (tried in order):
  - `https://api.z.ai/api/monitor/usage/quota/limit`
  - `https://open.bigmodel.cn/api/monitor/usage/quota/limit`
- **Status**: Undocumented, community-derived coding-plan monitoring endpoints;
  neither is a supported public quota API contract.
- **Auth**: `Authorization: <key>`
- **Privacy**: Sends the API key and requests account quota data. If the primary
  host fails, the same credential is sent to the Zhipu fallback host, so one
  check can contact both domains.

## DeepSeek (pay-as-you-go)

- **Key**: `DEEPSEEK_API_KEY` env var
- **Endpoint**: `https://api.deepseek.com/user/balance`
- **Status**: Official, documented DeepSeek user-balance API.
- **Auth**: `Authorization: Bearer <key>`
- **Privacy**: Sends the API key to DeepSeek and requests all account balance
  entries; the CLI selects and displays the USD balance.

## Script

`scripts/check-ai-quota.py` — CLI checker, human-readable + JSON output.
Usage: `python3 scripts/check-ai-quota.py [--claude] [--codex] [--gemini] [--glm] [--deepseek] [--all] [--json]`

## When to check

Before launching an expensive adversarial pipeline (REVIEW A + CROSS A→B + SYNTHESIS
= 4+ LLM calls), always run the quota checker. If Claude 5h utilization ≥ 80%,
consider swapping roles: use Codex for the review phases and Claude Sonnet for
cross-review.

## Pitfalls

- Claude token expires after ~7h of inactivity. HTTP 401 → start a `claude` session
  then `/exit` to refresh, then retry.
- Gemini has NO real-time quota API. The probe detects if you're rate-limited now
  (HTTP 429), but can't tell remaining capacity.
- Codex endpoint is official but tied to ChatGPT OAuth lifecycle.
- Claude, Codex, and GLM endpoints are not documented public API contracts and
  can change without notice.
- GLM fallback behavior may disclose the configured credential to both listed
  hosts.
