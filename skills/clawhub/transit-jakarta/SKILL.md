---
name: transit-jakarta
description: Query real-time TransJakarta bus arrivals, schedules, and route info via CLI. Trigger when asking about bus ETAs, halte (stops) locations, route details, or any TransJakarta live data. Usage: tj search <halte>, tj halte <id> --rute <route> --arah <destination>, tj stats, tj route <id>, tj nearest <lat> <lng>, tj bus <bus_id>. API: transit.oyenza.com (public, no auth). Supports all TransJakarta routes including BRT, Mikrotrans, Transjabodetabek, Royaltrans.
---

# Transit Jakarta Skill — SKILL.md

## Deskripsi
Skill ini memungkinkan query real-time bus TransJakarta via command line menggunakan API publik transit.oyenza.com. Tidak perlu browser — langsung curl ke API.

## Trigger
- User bertanya tentang jadwal bus, ETA, atau posisi bus TransJakarta
- Query seperti: "bus P11 Cibubur Junction kapan?", "ETA bus ke Blok M", "halte terdekat"
- Keywords: `bus`, `halte`, `ETA`, `kapan`, `datang`, `rute`, `TransJakarta`, nama halte

## Alur Kerja

### Setup (one-time)
```bash
# Buat file config jika belum ada
mkdir -p ~/.qclaw-oversea/skills/transit-jakarta
# Config auto-generated on first run
```

### CLI Usage

```bash
# Alias praktis (tambahkan ke ~/.zshrc)
alias tj='python3 ~/.qclaw-oversea/skills/transit-jakarta/transit.py'

# 1. Cari halte
tj search "Cibubur Junction"

# 2. Lihat arrivals di satu halte (semua rute)
tj halte B00248P

# 3. Filter by rute (e.g., P11)
tj halte B00248P --rute P11

# 4. Filter by arah (e.g., Blok M)
tj halte B00248P --arah "Blok M"

# 5. Gabungan rute + arah
tj halte B00248P --rute P11 --arah "Blok M"

# 6. Statistik seluruh bus
tj stats

# 7. Info satu bus
tj bus MYS-21238

# 8. Ranking rute tersibuk
tj top-routes 10

# 9. Help
tj help
```

### API Base
- **Base URL**: `https://transit.oyenza.com`
- **Meta**: `GET /api/meta` → staticUrl, patternsUrl
- **Stats**: `GET /api/stats` → buses by kind & route
- **Arrivals**: `GET /api/halte/{halteId}` → etaMin, route, head, bus, ageS
- **Bus detail**: `GET /api/bus/{busId}` → bus position, next halte
- **WebSocket**: `wss://transit.oyenza.com/api/live` → real-time positions

### Key Data Structures

```json
// GET /api/halte/{id}
{
  "id": "B00248P",
  "name": "Cibubur Junction",
  "now": 1791764678524,
  "arrivals": [
    {
      "bus": "MYS-21238",
      "route": "P11",
      "head": "Blok M Jalur 4",
      "kind": "jabodetabek",
      "etaMin": 5,
      "ageS": 34
    }
  ]
}
```

```json
// GET /api/stats
{
  "now": 1791764672962,
  "buses": 3811,
  "byKind": {"mikrotrans": 2330, "brt": 666, ...},
  "byRoute": {"1": 54, "P11": 27, ...}
}
```

### Static Data Cache
- Static data di-cache di `~/.qclaw-oversea/skills/transit-jakarta/cache/`
- Cache invalidation: cek `/api/meta` → compare `static` field
- GTFS data: halte (id, name, lat, lng, routes), routes (id, short, long, kind, color)
- Bus kinds: `brt`, `integrasi`, `mikrotrans`, `jabodetabek`, `royal`, `rusun`, `wisata`

### Contoh Output

```
🚌 P11 • Blok M Jalur 4 — Cibubur Junction
──────────────────────────────────────────
ETA  5 menit  (MYS-21238) ⭐ Tiba sekarang
ETA 11 menit  (BHL-210xxx)
ETA 18 menit  (BHL-209xxx)

🕐 Updated: baru saja (live)
📡 3 bus P11 aktif di rute ini
```

## Script Files
- `transit.py` — CLI entry point ( argparse + all commands)
- `api.py` — API client (requests + error handling)
- `cache.py` — Static data cache manager
- `formatters.py` — Output formatting (colored terminal output)

## Constraints
- API public, no auth needed
- Rate limit: reasonable use (max ~60 req/min)
- Static data cached 24h (compare via /api/meta)
- Fallback: parse static JSON if API fails
