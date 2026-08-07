---
name: space-duck-kimi-relay
description: Optional add-on for Space Duck — local "Sign in with Kimi" device flow so a Remote-Hosted (Lane A / BYOB) duck can run Kimi models on the owner's flat-rate Kimi membership. Token is stored on the owner's own box and never sent to Spaceduckling. Hosted (Lane B) ducks do NOT need this skill — they use the "Sign in with Kimi" card in Mission Control instead. Triggers on phrases like "sign in with kimi", "kimi membership login", "clawhub space-duck kimi", "kimi relay login".
---

# Space Duck Kimi Relay (optional add-on, Lane A)

Lets a duck that runs on **your own infrastructure** use your **Kimi
membership** (flat-rate subscription quota) for inference instead of
pay-per-token API keys.

## Trust model — the whole point

- The device-code sign-in runs **locally on your box**.
- Tokens are stored at `~/.kimi-code/credentials/kimi.json` (0600), on
  **your machine only**.
- The only host this skill contacts is Kimi itself (`auth.kimi.com` and
  `api.kimi.com`). **Spaceduckling never sees or holds the token.**
- This is the Lane A mirror of Mission Control's hosted "Sign in with
  Kimi" card: same protocol capability, different custody. (Cross-lane
  parity doctrine — capability exists in both lanes, credentials follow
  the lane's trust model.)

## Commands

```
kimi_login.py login         # interactive device sign-in
kimi_login.py token         # print fresh access token (auto-refresh, file-locked)
kimi_login.py probe         # inference smoke on membership quota
kimi_login.py serve [port]  # local proxy for your runtime (default 8471)
kimi_login.py install-service [port]   # run proxy as a service (systemd user / launchd)
kimi_login.py uninstall-service        # remove the service
kimi_login.py status [port] # creds + proxy + fallback-meter health check
kimi_login.py logout        # delete local credentials
```

`login` shows a kimi.com URL + user code; approve it in your browser and
the script stores the tokens. `token` transparently refreshes — Kimi
access tokens live ~15 minutes and **refresh tokens rotate on every
grant**, so always let this script (not ad-hoc curl) do the refreshing;
a stale refresh token is dead after one rotation.

## Wiring the duck's brain — use the proxy

Kimi access tokens live ~15 minutes, so a static key in your runtime's
config will not survive. Run the local proxy instead:

```
kimi_login.py serve            # http://127.0.0.1:8471/v1/chat/completions
```

Point your runtime's OpenAI-compatible provider at
`http://127.0.0.1:8471/v1` with any placeholder api key. The proxy
injects a fresh membership token per request (refreshes under a file
lock — safe when several ducks on one box share the login).

- Models: `k3` (full), `kimi-for-coding` (budget)
- k3 emits `reasoning_content` and spends completion budget on it —
  give it roomy `max_tokens` (512+) or replies can arrive empty.

Streaming (`"stream": true`) is passed through as SSE, so chat UIs get
token-by-token output on the membership lane.

**Automatic fallback:** export `OPENROUTER_API_KEY` before `serve` and
any failed membership call (quota/auth/outage) is retried once on
OpenRouter's kimi lane (`moonshotai/*`, pay-per-token) — same
degradation the hosted lane performs. Fallback is metered: capped at
`KIMI_RELAY_FALLBACK_DAILY_CAP` calls/day (default 200) so a broken
membership can't silently run up a pay-per-token bill; past the cap the
proxy returns 429. If the client asked for `stream: true`, the fallback
reply is wrapped as a single SSE chunk + `[DONE]` so streaming clients
still get valid SSE. Without the env var, failures return the error so
your runtime's own ladder takes over.

For a proxy that survives reboots, `install-service` writes a systemd
user unit (Linux — enable lingering with
`loginctl enable-linger $USER` so it runs while logged out) or a
launchd agent (macOS). Any `OPENROUTER_API_KEY` / `KIMI_*` env vars set
when you run `install-service` are captured into the unit (0600), so
the fallback survives reboots too. `status` shows creds, proxy health,
and the fallback meter.

Env overrides: `KIMI_CLIENT_ID` (if Moonshot rotates the public
client), `KIMI_AUTH_HOST`, `KIMI_CODING_BASE`,
`KIMI_RELAY_FALLBACK_DAILY_CAP`.

## Data residency

Kimi inference is processed by Moonshot AI on infrastructure in China.
Don't route conversations through this lane if you require Western data
residency.

## Scripts

| Script | Purpose |
|--------|---------|
| `scripts/kimi_login.py` | Device sign-in, token refresh, probe, logout |

## Important

- Opt-in add-on; the core `space-duck` skill works without it.
- Updates arrive via ClawHub with owner consent (Mission Control shows
  "update available") — never force-pushed to your box.
