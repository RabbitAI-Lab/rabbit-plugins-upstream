---
name: linkedin-hack
version: 1.1.0
description: "Your agent crawls LinkedIn through the browser session you already have — profiles, search, connections, inbox, feed. No official API, no app review. Session cookies + Voyager. The session cookie is sealed in your OS keychain, sending a message needs an explicit flag, and `session logout` erases everything. Built for the TinkerClaw fork — github.com/globalcaos/tinkerclaw. See Permissions, Data Flow & Consent."
metadata:
  openclaw:
    emoji: "🔗"
    os: ["linux", "darwin"]
    requires:
      capabilities: ["browser", "network", "file_write"]
      bins: ["node"]
    notes:
      security: "Handles a LinkedIn session cookie (li_at + JSESSIONID, optional bcookie/bscookie). That cookie is password-equivalent: whoever holds it is signed in as you. It is stored in the OS keychain (secret-tool on Linux, security on macOS) under openclaw-linkedin-hack/linkedin-session; if no keychain is present the CLI falls back to ~/.openclaw/credentials/linkedin-session.json at mode 0600 and prints a warning every time it writes. Off switch: `linkedin session logout` clears BOTH stores and prints LinkedIn's server-side revoke URL (https://www.linkedin.com/psettings/sessions); add --purge-data to also delete the cached profiles and the activity counters. The only endpoint that writes to LinkedIn is message-send, refused without --i-mean-it. Crawled third-party profiles are cached at ~/.openclaw/workspace/memory/linkedin-cache.json (0600, 60h TTL) — LINKEDIN_CACHE=0 disables it. Soft daily ceilings live in ~/.openclaw/workspace/memory/linkedin-activity.json (0600). See the Permissions, Data Flow & Consent section."
    env:
      - name: LINKEDIN_TRANSPORT
        description: "browser (default, cookies stay in the shared tab) or external (offline cookie replay; fragile and burns li_at)."
        required: false
        sensitive: false
      - name: LINKEDIN_CACHE
        description: "Set to 0 to stop caching other people's crawled profile data on disk."
        required: false
        sensitive: false
      - name: LINKEDIN_NO_KEYCHAIN
        description: "Set to 1 to skip the OS keychain and use the warned 0600 file store instead."
        required: false
        sensitive: false
      - name: LINKEDIN_PACE_MS
        description: "Base pacing between Voyager calls in ms (default 1200); jitter is added on top."
        required: false
        sensitive: false
      - name: LINKEDIN_PACE_STRICT
        description: "Set to 0 to disable the random 15-45s distraction pauses."
        required: false
        sensitive: false
      - name: LINKEDIN_CACHE_TTL_H
        description: "Profile/company cache lifetime in hours (default 60)."
        required: false
        sensitive: false
      - name: LINKEDIN_CDP_URL
        description: "OpenClaw browser relay CDP websocket (default ws://127.0.0.1:18792/cdp)."
        required: false
        sensitive: false
      - name: LINKEDIN_RELAY_HTTP
        description: "OpenClaw browser relay HTTP endpoint (default http://127.0.0.1:18792)."
        required: false
        sensitive: false
    # Declared capabilities. Each is used for exactly the reason given; anything
    # not listed here, the skill does not do.
    permissions:
      browser:
        required: true
        scope: "Drives one linkedin.com tab that YOU explicitly shared with the OpenClaw relay, and reads its cookies via CDP. It cannot see or open any tab you have not shared. This is the default transport, and on it the cookies never leave the browser."
      network:
        required: true
        scope: "Outbound HTTPS to www.linkedin.com only (the /voyager/api endpoints), plus the loopback OpenClaw relay at 127.0.0.1:18792. No third party, no telemetry, no analytics endpoint is ever contacted."
      credentials:
        required: true
        scope: "Your LinkedIn session cookies (li_at, JSESSIONID, optional bcookie/bscookie/li_a/lidc). Read from the tab you shared, sealed in the OS keychain, replayed only against www.linkedin.com. Never printed: `session extract-cdp` reports cookie NAMES and LENGTHS, never values."
      shell:
        required: true
        scope: "Runs exactly two binaries, with a fixed argument list and no shell: secret-tool (Linux) or security (macOS), to seal, read and erase the keychain entry. No other command is executed."
      file_read:
        required: true
        scope: "The keychain entry or ~/.openclaw/credentials/linkedin-session.json, plus its own cache and activity counters under ~/.openclaw/workspace/memory/. It reads nothing else on your disk."
      file_write:
        required: true
        scope: "Three files, all mode 0600: the credentials fallback (only when no keychain exists, and it warns), linkedin-activity.json (rate-guard counters), linkedin-cache.json (crawled profiles, LINKEDIN_CACHE=0 to disable). Nothing is written outside ~/.openclaw."
      file_delete:
        required: true
        scope: "`session logout` deletes the credentials file and clears the keychain entry. `session logout --purge-data` additionally deletes linkedin-cache.json and linkedin-activity.json. The cache also self-prunes entries older than 7 days. No other deletion path exists, and nothing outside those three files is ever removed."
      env_read:
        required: true
        scope: "The LINKEDIN_* variables listed above. No secret is read from the environment; the session comes from the browser or the keychain."
repository: https://github.com/globalcaos/tinkerclaw
homepage: https://github.com/globalcaos/tinkerclaw
---

> One of dozens of skills and plugins in **[TinkerClaw](https://github.com/globalcaos/tinkerclaw)** — a self-improving OpenClaw fork that's been running 24/7 for months.

No official LinkedIn API. No app review. No OAuth dance that dies in 60 days.

LinkedIn's product surface is a private REST API called **Voyager**. The website already talks to it with cookies from your signed-in browser. This skill does the same thing: share a `linkedin.com` tab, extract the session once, then crawl profiles / people search / companies / connections / inbox / feed from a zero-dep Node CLI.

**Part of [TinkerClaw](https://github.com/globalcaos/tinkerclaw)** — real-time token tracking, self-improving crons, persistent cognitive memory.

👉 **https://github.com/globalcaos/tinkerclaw**

_Clone it. Fork it. Break it. Make it yours._

# LinkedIn Hack

<why_this_matters>
LinkedIn bans automation that looks like a bot farm. This skill is deliberately boring: soft daily ceilings, send gated behind an explicit flag, the session cookie sealed in your OS keychain, and the same "borrow the browser session" pattern as teams-hack / factorial-hack. Useful for research and inbox triage — not for spray-and-pray outreach.
</why_this_matters>

<capabilities>
- Crawl through a **shared LinkedIn tab** (browser transport — default). Cookies stay in-browser.
- Identity: `me`, `profile <vanity>` via Voyager in-tab fetch
- People search via search-results page DOM scrape (LinkedIn SDUI broke classic Voyager search)
- Company/profile/connections/inbox/feed: Voyager in-tab (best-effort where endpoints still live)
- Optional external cookie-jar transport (`LINKEDIN_TRANSPORT=external`) — fragile; often burns `li_at`
- Optional message send (hard-gated: requires `--i-mean-it`)
- Daily activity counters with soft rate limits + request pacing
- Session sealed in the OS keychain (`secret-tool` / `security`), with a warned 0600 file fallback
- One-command off switch: `session logout [--purge-data]`
</capabilities>

## Quick Start

### 0. Relay Preflight — DO THIS FIRST

Extraction runs **through the OpenClaw browser relay**, which only exposes tabs the user actively clicked **Share** on. Empty tab list ≠ broken code.

1. Confirm relay is up: `GET http://127.0.0.1:<relayPort>/extension/status` → `connected:true`, `count>=1`
   (`<relayPort>` = `browser.profiles.chrome-relay.cdpUrl` in `~/.openclaw/openclaw.json`, usually `18792`)
2. List tabs (`GET /tabs` or `browser action=tabs`) and confirm a `linkedin.com` tab is shared. Grab its `targetId`.

If count is 0 or LinkedIn isn't listed: reload the OpenClaw extension (`chrome://extensions`) in the browser holding LinkedIn, click **Share** on the tab, re-check.

### 1. Session Extraction (one-time, ~30 seconds)

Open `https://www.linkedin.com/feed/` while signed in. Share the tab via the OpenClaw extension.

**Default transport is in-tab** (`LINKEDIN_TRANSPORT=browser`). No cookie extract required for crawl — share a feed tab and call commands, and the cookies never leave the browser.

Persisting the session is **opt-in**: without `--store`, `extract-cdp` only reports which cookies it can see (names and lengths, never values). Pass `--store` and the session is sealed in your OS keychain — or, if you have no keychain, written to a 0600 file with a warning:

```bash
node {baseDir}/scripts/linkedin.mjs session extract-cdp --store
node {baseDir}/scripts/linkedin.mjs session status    # says where it landed
node {baseDir}/scripts/linkedin.mjs session logout    # erases it from both stores
```

**Do not use external cookie replay as the main path.** Live 2026-07-29: external `/me` after extract worked once, then every further external call 302'd and the browser lost `li_at` (login wall). In-tab fetch does not burn the session the same way.

**Do not burst.** Pace is built in (`LINKEDIN_PACE_MS`, default 1200). One command at a time after login.

**B. Fallback — evaluate in page** (usually misses httpOnly `li_at`):

```javascript
(() => {
  const want = ['li_at', 'JSESSIONID', 'bcookie', 'bscookie', 'li_a', 'lidc', 'liap'];
  const cookies = {};
  for (const part of document.cookie.split(';').map(s => s.trim()).filter(Boolean)) {
    const eq = part.indexOf('=');
    if (eq < 0) continue;
    const k = part.slice(0, eq);
    if (want.includes(k)) cookies[k] = part.slice(eq + 1);
  }
  return {
    cookies,
    csrf: cookies.JSESSIONID?.replace(/^"|"$/g, '') || null,
    has_li_at: Boolean(cookies.li_at),
    note: cookies.li_at ? 'ok' : 'li_at httpOnly — use browser cookies action',
  };
})();
```

Store (never echo `li_at` into chat history if you can avoid it):

```bash
node {baseDir}/scripts/linkedin.mjs session store \
  --li-at '<value>' \
  --jsessionid '<ajax:… or "ajax:…">' \
  --bcookie '<optional>' \
  --bscookie '<optional>'
```

`csrf-token` defaults to the unquoted JSESSIONID (Voyager's usual rule).

### 2. Verify

```bash
node {baseDir}/scripts/linkedin.mjs session test
node {baseDir}/scripts/linkedin.mjs me
```

### 3. Crawl

```bash
node {baseDir}/scripts/linkedin.mjs search people "warehouse director spain" --top 10
node {baseDir}/scripts/linkedin.mjs profile some-vanity-slug
node {baseDir}/scripts/linkedin.mjs company microsoft
node {baseDir}/scripts/linkedin.mjs connections --top 40
node {baseDir}/scripts/linkedin.mjs conversations --top 15
node {baseDir}/scripts/linkedin.mjs messages 'urn:li:msg_conversation:(…)' --top 30
node {baseDir}/scripts/linkedin.mjs feed --top 10
node {baseDir}/scripts/linkedin.mjs activity show
```

## How It Works

1. LinkedIn web uses cookies (`li_at` session + `JSESSIONID` / CSRF) for Voyager.
2. The skill seals those cookies in your **OS keychain** (`secret-tool` on Linux, `security` on macOS, entry `openclaw-linkedin-hack/linkedin-session`). With no keychain present it falls back to `~/.openclaw/credentials/linkedin-session.json` at mode `0600` **and prints a warning every time it writes**. Only one copy is ever kept: a successful keychain write deletes the file.
3. CLI replays them against `https://www.linkedin.com/voyager/api/*` with:
   - `csrf-token: <unquoted JSESSIONID>`
   - `Cookie: li_at=…; JSESSIONID="…"; …`
   - `x-restli-protocol-version: 2.0.0`
   - desktop Chrome UA + linkedin.com Origin/Referer
4. Responses are Rest.li "normalized" JSON (`data` + `included`). The CLI flattens the useful bits.

Same family as:

| Skill | Auth model | Stores secrets? |
| ----- | ---------- | --------------- |
| teams-hack / outlook-hack | MSAL refresh token from Teams localStorage | yes (`outlook-msal.json`) |
| factorial-hack | live page `fetch` (httpOnly cookies never leave browser) | no |
| **linkedin-hack** | in-tab fetch by default; cookie jar optional | yes — OS keychain, warned 0600 file fallback |

LinkedIn needs the offline jar because Voyager is same-site cookie auth and we want CLI use without a live tab on every call. Re-extract when you get 401/403.

## Rate Guard (do not skip)

LinkedIn will challenge or ban aggressive automation. Soft daily ceilings live in:

```
~/.openclaw/workspace/memory/linkedin-activity.json
```

Stealth design (2026-08-05): pacing is **jittered**, not metronomic — each wait is base ±random(−300..+1400ms), with an 8% chance of a 15–45s "distraction" pause (`LINKEDIN_PACE_STRICT=0` disables). Speed comes from **fat payloads + local cache**, never from parallelism:

- Local cache at `~/.openclaw/workspace/memory/linkedin-cache.json` — `profile` and `company` results cached 60h (`LINKEDIN_CACHE_TTL_H`, prune >7d). Cache hits cost zero requests and zero rate-guard counters. `--no-cache` forces live.
- `connections` defaults to `--top 100` in one request (Voyager happily serves fat pages).

Defaults (override by editing `limits` in that file):

| counter | default / day |
| ------- | ------------- |
| profile_views | 40 |
| messages_read | 200 |
| messages_sent | 25 |
| connections_sent | 15 |
| likes | 40 |
| sessions | 15 |
| total_minutes | 90 |

Commands that would exceed a counter throw instead of calling Voyager.

`message-send` additionally requires `--i-mean-it`. No flag → exit 2, no request.

Human pacing heuristics the agent should follow even under the ceilings:

- Burst ≤ ~10 profile views, then pause minutes not seconds
- Prefer search → shortlist → deep profile, not full-graph walks
- Never auto-connect or auto-message from a cron without an explicit, per-run human brief

## Permissions, Data Flow & Consent

Read this before you install. It is the honest version.

### What it touches

- **One browser tab that you shared.** The default transport runs `fetch` inside a `linkedin.com` tab you explicitly clicked **Share** on in the OpenClaw extension. The skill cannot reach a tab you did not share, and it opens nothing on its own.
- **Your LinkedIn session cookies** — `li_at`, `JSESSIONID`, and optionally `bcookie` / `bscookie` / `li_a` / `lidc`. Treat `li_at` as a password: it is a full sign-in as you, with no second factor. The skill never prints cookie values; `session extract-cdp` reports names and lengths only.
- **Three files, all mode 0600, all under `~/.openclaw`** — the credentials fallback, the rate-guard counters (`linkedin-activity.json`), and the crawl cache (`linkedin-cache.json`). It reads nothing else on your disk.
- **Two binaries, run with a fixed argument list and no shell** — `secret-tool` (Linux) or `security` (macOS), for the keychain only.

### Where the secret lives

1. **OS keychain, by default** — `secret-tool` on Linux, `security` on macOS, entry `openclaw-linkedin-hack` / `linkedin-session`. On Linux the value is passed over stdin, so it never appears in `ps`. On macOS `security` takes it as an argument, so it is briefly visible to your own processes.
2. **A 0600 file, only if there is no keychain** — `~/.openclaw/credentials/linkedin-session.json`. This path **prints a warning every single time it writes**, because a session cookie sitting in a plain file is a materially different risk. Force it with `LINKEDIN_NO_KEYCHAIN=1` if you prefer.

A successful keychain write **deletes** the file, so the secret never exists in two places.

### What leaves your machine

- **To `www.linkedin.com` only:** the Voyager API calls you asked for, carrying your own cookies — exactly what your browser sends when you use the site normally.
- **To `127.0.0.1:18792`:** the local OpenClaw browser relay. That is loopback, not the network.
- **To anyone else: nothing.** No telemetry, no analytics, no third-party host, no phone-home. The skill has zero dependencies, so there is no transitive package doing it either.
- **Outbound writes to LinkedIn:** exactly one endpoint, `message-send`, and it is refused without `--i-mean-it`. Everything else is a read.

### Third-party data, and the cost of it

Crawling LinkedIn means putting **other people's** personal data on your disk. Profiles and companies you fetch are cached at `~/.openclaw/workspace/memory/linkedin-cache.json` (0600, 60h TTL, pruned after 7 days). The cache is on by default because a cache hit costs zero requests, which is a large part of what keeps this skill under LinkedIn's rate radar — but you may not want it:

```bash
LINKEDIN_CACHE=0 node {baseDir}/scripts/linkedin.mjs profile some-vanity-slug
```

You are responsible for what you do with that data. In the EU, scraped profile data is personal data under GDPR, and a lawful basis is your problem, not the tool's.

### What it costs

- **No API key, no subscription, no per-call fee.** LinkedIn has no official API here; this rides your own session.
- **The real cost is account risk.** LinkedIn restricts and bans accounts for automation. That is why the pacing is jittered, the ceilings are low, and there is no parallelism anywhere in the code. A ban is not reversible by this skill.
- **Session lifetime.** Bursts burn `li_at` — observed 2026-07-29: an external-transport burst dropped the session to a login wall. Slow is the feature.

### How to turn it off

```bash
node {baseDir}/scripts/linkedin.mjs session logout                # keychain + file
node {baseDir}/scripts/linkedin.mjs session logout --purge-data   # + cache + counters
```

`logout` clears **both** stores and prints LinkedIn's own revoke page:

**https://www.linkedin.com/psettings/sessions**

Use it. Deleting the local copy does not invalidate the cookie — until you sign that session out at LinkedIn, it stays valid. Uninstalling the skill also does not revoke anything.

### What it will not do

There is no endpoint in this skill for connecting, following, liking, posting, endorsing, or deleting. `message-send` is the only write, and it is flag-gated. The `likes` and `connections_sent` counters exist so those actions stay accounted for if they are ever added — today nothing increments them.

## CLI Reference

| Command | Description |
| ------- | ----------- |
| `session extract-cdp [--store]` | Pull httpOnly `li_at` via OpenClaw CDP relay (preferred) |
| `session extract-browser` | Print in-page extract snippet (often misses `li_at`) |
| `session store --li-at … --jsessionid …` | Save cookies (0600) + auto-test |
| `session test` | `GET /voyager/api/me` |
| `session status` | Where the session is stored + today's counters |
| `session logout [--purge-data]` | Erase the session from keychain **and** file; print LinkedIn's revoke URL. `--purge-data` also deletes the cached profiles and counters |
| `me` | Mini-profile |
| `profile <vanity>` | Profile + positions (+ education) |
| `search people "q" [--top N] [--network F\|S\|O]` | People search |
| `search companies "q" [--top N]` | Company search |
| `connections [--top N] [--start N]` | 1st-degree connections |
| `company <vanity>` | Company page summary |
| `posts <vanity> [--top N]` | Member share feed (best-effort) |
| `conversations [--top N]` | Inbox list |
| `messages <urn> [--top N]` | Thread events |
| `message-send <urn> --message "…" --i-mean-it` | Send (gated) |
| `feed [--top N]` | Home feed (best-effort) |
| `notifications [--top N]` | Notifications (best-effort) |
| `activity show` | Counters + limits |
| `activity bump <counter> [--by N]` | Manual counter bump |

## Extraction: httpOnly `li_at`

`li_at` is frequently **httpOnly**, so `document.cookie` will not see it. Prefer:

1. `browser(action=cookies, domain="linkedin.com")` when the tool path is available
2. Or CDP `Network.getCookies` on the shared LinkedIn target through the relay

`JSESSIONID` is usually readable and doubles as the CSRF token (strip surrounding quotes).

Never paste full `li_at` values into chat transcripts, git commits, or clawhub packages. Store → test → discard from the message.

## Failure Modes

| Symptom | Likely cause | Fix |
| ------- | ------------ | --- |
| `401` / `403` | Session expired, challenge, or missing csrf | Re-login in browser, `session extract-cdp --store` |
| `302 redirect` / redirect loop | Dead/rotated `li_at` (CLI uses `redirect:manual`) | Same: re-login + extract-cdp |
| `429` | LinkedIn rate limit | Stop for minutes; do not retry in a loop |
| `Rate guard: daily …` | Soft ceiling hit | Wait for next day or edit limits deliberately |
| Empty search results | Voyager decorationId drift | CLI already falls back to `/search/hits`; re-check with `--raw` on profile if needed |
| `li_at` missing from evaluate | httpOnly cookie | Use `session extract-cdp`, not document.cookie |
| Tab on `/login` | Session burned (often after a request burst) | Human re-login, open feed, re-share, extract once |
| Send refused | Missing `--i-mean-it` | Intentional; only pass when a human has explicitly approved that exact message |

## Architecture

```
linkedin-hack/
├── SKILL.md
└── scripts/
    └── linkedin.mjs    # zero-dep CLI (session + voyager + rate guard)
```

- **Zero external deps** — pure Node 22+ (`fetch` built-in)
- **Credentials** — OS keychain `openclaw-linkedin-hack/linkedin-session`; fallback `~/.openclaw/credentials/linkedin-session.json` (0600, warned)
- **Activity** — `~/.openclaw/workspace/memory/linkedin-activity.json` (0600)
- **Cache** — `~/.openclaw/workspace/memory/linkedin-cache.json` (0600, 60h TTL, `LINKEDIN_CACHE=0` to disable)
- **API** — LinkedIn Voyager (`/voyager/api`), Rest.li normalized JSON
- **Off switch** — `node scripts/linkedin.mjs session logout --purge-data`

## Sibling Skills

| Skill | What it does |
| ----- | ------------ |
| [teams-hack](https://clawhub.ai/globalcaos/teams-hack) | Teams chat via Graph + MSAL refresh |
| [outlook-hack](https://clawhub.ai/globalcaos/outlook-hack) | Outlook read/draft (send code-disabled) |
| [factorial-hack](https://clawhub.ai/globalcaos/factorial-hack) | Factorial HR GraphQL in-page |

## The Full Stack

Pair with [outlook-hack](https://clawhub.ai/globalcaos/outlook-hack) for email, [whatsapp-ultimate](https://clawhub.ai/globalcaos/whatsapp-ultimate) for messaging, and [teams-hack](https://clawhub.ai/globalcaos/teams-hack) for org chat.

[Clone it. Fork it. Break it. Make it yours.](https://github.com/globalcaos/tinkerclaw)
