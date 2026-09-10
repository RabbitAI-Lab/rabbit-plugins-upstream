---
name: owntracks-location
description: >
  Your phone's location, on your own machine, behind a token. An OwnTracks HTTP
  receiver that stores the trail in a local SQLite/JSON store you own, with named
  places and distance queries. Binds to 127.0.0.1 by default and refuses to start
  without a token, so there is no unauthenticated path to your location — reads and
  writes both need it. Retention is capped by default (7 days / 500 points) and
  `--purge-data` erases the trail on demand. Use when: (1) "where am I?", (2) storing
  named locations (home, gym, work), (3) querying nearby places by distance, (4)
  checking location history. Requires: OwnTracks app, Node.js 22+, better-sqlite3.
  Built for the TinkerClaw fork — github.com/globalcaos/tinkerclaw. See Permissions,
  Data Flow & Consent.
version: 1.0.2
metadata:
  openclaw:
    emoji: "🛰️"
    os: ["linux", "darwin"]
    requires:
      bins: ["node"]
    notes:
      security: "A self-hosted location receiver. Your position history is the most sensitive thing an agent can hold, so the listener binds to 127.0.0.1 unless you deliberately change OWNTRACKS_BIND, and it REFUSES TO START without a token — every endpoint that can return or accept location data requires it (only /health, which carries none, is open). The token lives in the OS keychain when one exists and in a 0600 file otherwise, with a printed warning. Data is stored under the skill's own data directory at 0700/0600, pruned to 7 days and 500 points by default, and erasable with --purge-data. Wi-Fi SSID is dropped unless OWNTRACKS_STORE_SSID=1 and coordinates stay out of the logs unless OWNTRACKS_LOG_COORDS=1. No cloud service is contacted: the only network traffic is your phone talking to your own machine. See the Permissions, Data Flow & Consent section."
    permissions:
      network:
        required: true
        scope: "Listens on 127.0.0.1:18793 by default. It makes NO outbound connections of any kind — no vendor API, no telemetry, no geocoding. Binding to a non-loopback address is your explicit choice via OWNTRACKS_BIND and prints a warning, because plain HTTP puts the token and your coordinates on the wire in clear text."
      shell:
        required: false
        scope: "Only the keychain helper: `secret-tool` (libsecret) on Linux or `security` on macOS, for storing/reading/clearing the receiver token. Nothing else is executed."
      credentials:
        required: true
        scope: "One secret you generate: the receiver token. Preferred home is the OS keychain (service owntracks-location, account receiver-token); the fallback is a 0600 file in the data directory, and the fallback prints a warning. `--revoke` clears both."
      file_read:
        required: true
        scope: "Its own data directory only: latest.json, history.json, places.sqlite and the token fallback file."
      file_write:
        required: true
        scope: "The same data directory (0700), files created 0600: latest.json, history.json, places.sqlite. Nothing is written anywhere else."
      file_delete:
        required: false
        scope: "Only on explicit command: `--purge-data` deletes latest.json and history.json; `--revoke` deletes the token file. Named places are never touched by either."
repository: https://github.com/globalcaos/tinkerclaw
homepage: https://github.com/globalcaos/tinkerclaw
---

# OwnTracks Location

> One of dozens of skills and plugins in **[TinkerClaw](https://github.com/globalcaos/tinkerclaw)** — a self-improving OpenClaw fork that's been running 24/7 for months.

Ask your agent "where am I?" — and get a real answer, not a shrug.

No Google Timeline. No app phoning home to a stranger's servers. Just your phone, your box, your data.

Your phone already knows where you are. This skill catches those location pings on your own machine: a tiny webhook receiver that logs each one into a local store. Name the spots that matter — home, gym, work — and your agent can tell you where you are, what's nearby, and how far you've wandered, all without a cloud middleman ever touching the trail.

And because a location history is the single most sensitive thing an agent can be handed: the receiver **binds to localhost**, **refuses to start without a token**, **forgets by default**, and hands you one command that erases the lot.

**Part of [TinkerClaw](https://github.com/globalcaos/tinkerclaw)** — real-time token tracking, self-improving crons, persistent cognitive memory. This is one piece of that stack; the repo has dozens more.

👉 **https://github.com/globalcaos/tinkerclaw**

_Clone it. Fork it. Break it. Make it yours._

<scope>
Real-time location awareness via OwnTracks → authenticated HTTP → local store. Use this skill when the user wants to know "where am I?", record a named place, or query nearby places by distance.
</scope>

## Architecture

```
Phone (OwnTracks) --HTTP Basic, token--> server.mjs (127.0.0.1:18793) --> latest.json + history.json (0600)
Agent queries     --Bearer token------->  GET /latest, GET /history
Agent queries     --local file---------->  places.mjs CLI (reads latest.json directly)
```

## Setup

### 1. Create a token — the receiver will not start without one

```bash
# Generates a token, stores it in your OS keychain, and prints it once:
node scripts/server.mjs --set-token

# Or supply your own on stdin (never on argv, where `ps` can read it):
printf %s "$MY_TOKEN" | node scripts/server.mjs --set-token
```

If no OS keychain is available (`secret-tool` on Linux, `security` on macOS) the token is
written to a 0600 file in the data directory instead, and the command says so loudly.

Retrieve it later with `node scripts/server.mjs --show-token`.

### 2. Start the receiver

```bash
node scripts/server.mjs
# Binds 127.0.0.1:18793. Port: OWNTRACKS_PORT. Data dir: OWNTRACKS_DATA.
```

It prints its bind address, retention window and SSID setting on startup, and exits with an
error if no token is configured.

**Reaching it from your phone.** The default bind is loopback, which your phone cannot reach.
The right answer is a private network, not a wider bind: put the host on **Tailscale** (or
WireGuard) and point OwnTracks at the host's Tailscale IP with `OWNTRACKS_BIND` set to that
interface. Binding to `0.0.0.0` over plain HTTP puts your token and your coordinates on the
wire in clear text; the server warns when you do it. If you must expose it beyond a private
tunnel, terminate TLS in a reverse proxy in front of it.

### 3. Install as a user service (optional)

```bash
mkdir -p ~/.config/systemd/user
cat << 'EOF' > ~/.config/systemd/user/owntracks-receiver.service
[Unit]
Description=OwnTracks Location Receiver
After=network.target

[Service]
Type=simple
Environment=OWNTRACKS_PORT=18793
Environment=OWNTRACKS_DATA=%h/.openclaw/skills/owntracks-location/scripts/data
ExecStart=/usr/bin/env node %h/.openclaw/skills/owntracks-location/scripts/server.mjs
Restart=always
RestartSec=5

[Install]
WantedBy=default.target
EOF
systemctl --user daemon-reload
systemctl --user enable --now owntracks-receiver
```

Adjust the two `%h/...` paths to wherever you installed the skill. This is a **user** unit —
it runs as you, with your keychain, never as root. Do not install it into
`/etc/systemd/system`: system-wide, `%h` resolves to `/root` and the service would run
privileged, reading a keychain that is not yours.

Do **not** put the token in an `Environment=` line if you can avoid it — the keychain entry
is read automatically and a unit file is world-readable on most systems.

### 4. Configure OwnTracks on the phone

1. Install OwnTracks from F-Droid or the App Store
2. Menu → Preferences → **Mode → HTTP**
3. **URL**: `http://<host-tailscale-ip>:18793/owntracks`
4. **Preferences → Connection → Authentication**: set *any* username, and paste the token as the **password**
5. Tap the share icon on the map to send a test ping

The receiver accepts HTTP Basic (what the phone sends, token as the password) and Bearer
(what curl and the agent send).

### 5. Verify

```bash
TOKEN=$(node scripts/server.mjs --show-token)
curl -s -H "Authorization: Bearer $TOKEN" http://localhost:18793/latest
# => {"lat":...,"lon":...,"acc":...,"batt":...,"tst":...}
```

## Server Endpoints

| Method | Path | Auth | Description |
|--------|------|------|-------------|
| POST | `/owntracks` (or `/`) | **required** | OwnTracks webhook (expects `_type: "location"`) |
| GET | `/latest` | **required** | Last known location |
| GET | `/history?limit=50` | **required** | Location history |
| GET | `/health` | open | Liveness only — carries no location data |

Everything that can read or write the trail needs the token. `/health` is the single
exception and returns the string `ok` and nothing else.

## Retention and erasure

The trail is pruned on every write and again at startup:

| Setting | Default | Meaning |
|---|---|---|
| `OWNTRACKS_RETENTION_DAYS` | `7` | Drop points older than this. `0` = keep forever. |
| `OWNTRACKS_MAX_POINTS` | `500` | Hard cap on stored points. `0` = unlimited. |
| `OWNTRACKS_STORE_SSID` | off | Store the Wi-Fi network name. Off, because it is not needed to answer "where am I?" and it identifies places by itself. |
| `OWNTRACKS_LOG_COORDS` | off | Print coordinates to the log. Off, because logs are a second copy of the trail that nothing prunes. |

```bash
node scripts/server.mjs --purge-data   # delete latest.json + history.json
node scripts/server.mjs --revoke       # clear the token from keychain AND file
```

`--purge-data` leaves your named places alone (remove those with `places.mjs remove`).
`--revoke` does not delete the trail, and does not stop the phone — it prints the phone-side
steps, because only clearing the URL and password in OwnTracks stops the device sending.

## Places CLI

Named locations with haversine distance queries. Reads `latest.json` from the data directory
directly, so it works whether or not the receiver is running.

```bash
# Add a place
node scripts/places.mjs add "Home" 41.3200 1.8900 home "Olivella"
node scripts/places.mjs add "Gym" 41.2229 1.7385 gym "Aqua Sport, Vilanova"

# Where am I? (nearest named place; --precise adds exact coordinates)
node scripts/places.mjs where
node scripts/places.mjs where --precise

# Find nearby places from arbitrary coordinates
node scripts/places.mjs nearest 41.22 1.74 5 500

# Search / list / remove
node scripts/places.mjs search "gym"
node scripts/places.mjs list [category]
node scripts/places.mjs remove "Old Place"
```

By default `where` prints the nearest named place plus coordinates rounded to ~1 km — enough
to orient, not enough to pinpoint a doorway in a transcript. Pass `--precise` for the exact
fix, accuracy and battery level.

<agent_usage>
When the user asks "where am I?", prefer the CLI — it reads the local file and needs no token:

```bash
node scripts/places.mjs where
```

If you need the raw fix over HTTP, the token is required:

```bash
TOKEN=$(node scripts/server.mjs --show-token)
curl -s -H "Authorization: Bearer $TOKEN" http://localhost:18793/latest
```

When the user says "this is my X" at a location:

1. Get current coords from `places.mjs where --precise`
2. Reverse geocode via Nominatim or a web search for the business name
3. `node scripts/places.mjs add "<name>" <lat> <lon> <category>`

Treat coordinates as private: report the named place in chat where you can, and do not paste
a lat/lon into any outbound message, file or third-party service without being asked.
</agent_usage>

## Permissions, Data Flow & Consent

Short version: your location goes from your phone to your machine and stops there. Longer
version, because you should not have to take that on trust:

**What data it touches.** Latitude, longitude, accuracy, altitude, velocity, battery level
and a timestamp per ping — plus the named places you create. Wi-Fi SSID only if you turn it
on. Nothing else from the phone is stored, even when OwnTracks sends it.

**Where it goes.** Nowhere. The receiver makes **no outbound connections at all** — no vendor
API, no telemetry, no geocoding service. The only traffic is your phone → your machine. If
your agent reverse-geocodes a place name, that is a separate tool you invoke deliberately.

**What it writes to disk.** `latest.json`, `history.json` and `places.sqlite`, all mode 0600
inside a 0700 directory, under `OWNTRACKS_DATA` (default: `scripts/data`). Nothing outside it.

**What credentials it reads.** One: the receiver token you generate. OS keychain first, 0600
file otherwise (with a warning). It reads no other application's credential store.

| Capability | Why | Scope |
| --- | --- | --- |
| Listen on a port | Receive pings from the phone | `127.0.0.1:18793` by default; a wider bind is your explicit choice and warns |
| Auth on every data endpoint | A location trail must not be readable by anything that can reach the port | Token required for POST `/owntracks`, GET `/latest`, GET `/history` |
| Credential read | The receiver token | OS keychain, else a 0600 file |
| File write | Store the trail and your named places | The data directory only, 0700/0600 |
| File delete | `--purge-data`, `--revoke` | Exactly those files, only on explicit command |
| Outbound network | **None.** It never calls out | — |

**The refusals, and what each protects you from:**

```bash
node scripts/server.mjs                 # exits if no token — no accidental open listener
OWNTRACKS_BIND=0.0.0.0 node ...         # starts, but warns: cleartext token + coordinates
node scripts/server.mjs --purge-data    # the trail is gone; the phone keeps sending until you stop it
node scripts/server.mjs --revoke        # the token is gone; tells you the phone-side step too
```

**Read it before you run it.** `scripts/server.mjs` is about 330 lines of dependency-free
Node and `scripts/places.mjs` about 160. `tests/test-server.sh` starts a real receiver in a
throwaway directory and asserts each of the claims above — the 401s, the loopback bind, the
retention prune, the purge — so you can check them rather than believe them.

## Dependencies

- Node.js 22+ (the receiver has **no** npm dependencies)
- `better-sqlite3` — only for `places.mjs`
- OwnTracks app (Android/iOS)
- A private network path from phone to receiver (Tailscale recommended)

## Pairs Well With

- [torrent-scout](https://clawhub.ai/globalcaos/torrent-scout) — same "verify before you act" philosophy, different domain

https://github.com/globalcaos/tinkerclaw

_Clone it. Fork it. Break it. Make it yours._

---

## Credits

Created by Oscar Serra with the help of Claude (Anthropic).
