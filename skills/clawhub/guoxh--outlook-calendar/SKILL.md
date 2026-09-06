---
name: outlook-calendar
license: MIT
description: |
  Read and write the signed-in user's Microsoft 365 / Outlook.com personal calendar via Microsoft Graph.
  Calendar-only. No mail, no files, no contacts, no directory access.
  Use when the user wants to list today's events, look at next week, create / update / delete
  a single event by id, or check token status. Trigger keywords: "outlook calendar", "ms calendar",
  "graph calendar", "我的 outlook 日历", "微软日历".
metadata:
  openclaw:
    emoji: "📅"
    requires:
      bins: ["bash", "jq", "curl", "python3"]
    network:
      allow:
        - "https://login.microsoftonline.com"
        - "https://graph.microsoft.com"
    files:
      write:
        - "~/.outlook-calendar/"
---

# Outlook Calendar (Microsoft Graph, calendar-only)

A minimal, **calendar-only** Microsoft Graph skill. Reads and writes the signed-in user's
primary calendar through `/me/calendarView` and `/me/events`. **Does not request any mail,
contacts, files, or directory scope** — the only scopes this skill will ever ask for are:

| Scope | Why |
|---|---|
| `offline_access` | receive a `refresh_token` so the skill can run headlessly |
| `https://graph.microsoft.com/User.Read` | display the signed-in account UPN at sign-in and in `token status` |
| `https://graph.microsoft.com/Calendars.ReadWrite` | read & write the primary calendar |

If you need mail, files, contacts, or anything else, this is the wrong skill.

## ⚠️ Safety rules (read these before any write/delete)

1. **Every write is a two-step confirm.** `calendar-write.sh` defaults to **dry-run**: it
   prints the JSON payload it *would* send and exits 0. To actually call Graph you must
   pass **`--apply`**, and the script will then ask you to type `YES` at the terminal
   (or pass `--yes`). There is no implicit write.
2. **Delete is extra strict.** `delete` first fetches the event and prints subject / start /
   end / location / organizer so you can verify, then prompts for `YES`.
3. **No secrets in logs.** `access_token` and `refresh_token` are never echoed to stdout
   or stderr. Error responses are sanitized: any field whose name contains
   `token`, `refresh`, `access`, `secret`, or `password` is replaced with `[REDACTED]`.
4. **Token & config live under `~/.outlook-calendar/`** (chmod 700 dir, chmod 600 files).
   The `clear` subcommand of `token.sh` removes them — it requires `--yes-i-really-mean-it`.

## First-time setup

You need a **public client** application registration in Entra ID (Azure AD) with
"Allow public client flows" = **Yes** and "Mobile and desktop applications" → device-code
flow enabled. The skill uses the **device code flow** so it works on a headless host.

Azure app registration steps (bring your own — required once):

1. Portal → **Microsoft Entra ID** → **App registrations** → **New registration**.
2. Supported account types: **"Accounts in any organizational directory and personal Microsoft accounts"** (covers work/school and Outlook.com).
3. No redirect URI needed. In the app → **Authentication** → set **"Allow public client flows"** = **Yes**.
4. Copy the **Application (client) ID** — that is the `--client-id` below. No client secret is ever required (public client).

The setup script requests exactly these delegated Microsoft Graph scopes in one consent:
`offline_access`, `User.Read`, `Calendars.ReadWrite`, `Tasks.ReadWrite`, `Contacts.ReadWrite`
— so a single login covers calendar, To Do, and contacts (the other two skills in this family).

For personal Outlook.com accounts, manually adding Graph API permissions in Azure Portal is usually optional. The setup script requests delegated scopes during login, and Microsoft can grant them via dynamic user consent. For work/school tenants that disable user consent, an administrator may still need to preconfigure permissions and grant admin consent.

```bash
cd ~/.openclaw/skills/outlook-calendar
./scripts/setup-device-code.sh --client-id 12345678-1234-1234-1234-123456789012
# follow the printed URL, enter the code, finish the browser sign-in
```

The script writes:

| File | Mode | Content |
|---|---|---|
| `~/.outlook-graph/config.json` | 600 | client_id, tenant, authority, scopes, graph_base |
| `~/.outlook-graph/tokens.json` | 600 | access_token, refresh_token, expires_at, scope |

…and removes the temporary `device.json`.

> **Important:** never commit `~/.outlook-calendar/` to git. The `setup-device-code.sh`
> script refuses to overwrite existing files unless you pass `--force`.

## Reading events

```bash
# Today
./scripts/calendar-read.sh today

# Tomorrow
./scripts/calendar-read.sh tomorrow

# Current calendar week (Mon..Sun in --tz)
./scripts/calendar-read.sh week --tz Asia/Shanghai

# Next 7 days
./scripts/calendar-read.sh next-days 7 --format summary

# Search this week for "standup"
./scripts/calendar-read.sh week --query standup --format ids

# Different start date / timezone
./scripts/calendar-read.sh week --from 2026-06-22 --tz Europe/Berlin
```

`--format` options:

- `json`    (default) pretty Graph JSON
- `summary` tabular text
- `ids`     one event id per line (handy for piping into `update` / `delete`)
- `raw`     single-line JSON array

## Writing events

```bash
# 1. Dry-run: see the payload that *would* be sent
./scripts/calendar-write.sh create \
  --subject "Lunch with Mei" \
  --start   "2026-06-18 12:00" \
  --end     "2026-06-18 13:00" \
  --location "Din Tai Fung, Shanghai" \
  --body    "Discuss Q3 OKRs"

# 2. Real call (with confirmation prompt)
./scripts/calendar-write.sh create \
  --subject "Lunch with Mei" \
  --start   "2026-06-18 12:00" \
  --end     "2026-06-18 13:00" \
  --apply
#   ... prints summary, asks: "Type YES within 10s to proceed:" → user types YES

# 3. All-day event
./scripts/calendar-write.sh create \
  --subject "Travel to Tokyo" \
  --start   "2026-06-20" \
  --end     "2026-06-22" \
  --all-day --apply

# 4. Update (only changed fields need to be passed)
./scripts/calendar-write.sh update \
  --event-id AAMkAGI2... \
  --subject "Lunch (rescheduled)" \
  --start   "2026-06-18 12:30" \
  --end     "2026-06-18 13:30" \
  --apply

# 5. Delete (always shows the event first)
./scripts/calendar-write.sh delete --event-id AAMkAGI2... --apply
```

### Robust escaping

All user-supplied fields go through `jq -n --arg` / `--argjson` (see `scripts/_lib.sh`
and `build_event_body`). **No string interpolation** is used to build the JSON body,
so subjects like `She said "hi"\nwith a backslash \` and embedded nulls are safe.

## Token management

```bash
# Status (token presence, expiry, /me probe with User.Read only)
./scripts/token.sh status

# Force a refresh (no-op if still valid for >120s)
./scripts/token.sh refresh

# Show scopes the token was actually issued for
./scripts/token.sh scopes

# Nuke local config & tokens (irreversible)
./scripts/token.sh clear --yes-i-really-mean-it
```

The `token.sh` script never prints the access_token or refresh_token. The `/me` probe
uses `?$select=id,userPrincipalName` only.

## Files in this skill

| Path | Purpose |
|---|---|
| `SKILL.md` | this file |
| `scripts/setup-device-code.sh` | one-time device-code flow sign-in |
| `scripts/token.sh` | inspect / refresh / clear stored tokens |
| `scripts/calendar-read.sh` | `today` / `week` / `next-days N` over `/me/calendarView` |
| `scripts/calendar-write.sh` | `create` / `update` / `get` / `delete` over `/me/events` |
| `scripts/_lib.sh` | shared helpers (sourced; not for direct use) |
| `references/graph-calendar.md` | Microsoft Graph calendar endpoint reference |
| `tests/test-local.sh` | offline smoke + JSON escaping tests (no real Microsoft calls) |

## Troubleshooting

- **`AADSTS700016: Application with identifier ... was not found`** — your `client_id`
  is wrong or your app registration lives in a different tenant than the one you
  passed via `--tenant-id`.
- **`AADSTS65001: The user or administrator has not consented to ... Calendars.ReadWrite`** —
  the tenant likely blocks dynamic user consent. Ask an admin to preconfigure the delegated Graph permissions and grant consent; also verify "Allow public client flows" is enabled.
- **`401 Unauthorized` on every call** — the access token was likely revoked. Run
  `scripts/token.sh refresh --force`; if that fails, `scripts/setup-device-code.sh --force`.
- **Empty results in a known-busy week** — check `--tz`; the default is `Asia/Shanghai`,
  and a "week" in your local time may straddle a different set of events than the
  Graph server's UTC view.

## Tests (no real Microsoft credentials required)

```bash
cd ~/.openclaw/skills/outlook-calendar
./tests/test-local.sh
```

Covers: shell syntax (`bash -n`), `jq` payload validation for create/update/all-day,
JSON escaping (quotes, backslashes, newlines, control chars, emoji, CJK), dry-run
mode (no network), client-id / tenant-id / scope validation, all-day input
validation, and the `clear` safety interlock.
