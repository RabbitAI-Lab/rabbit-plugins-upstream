# TOOLS.md - Local Notes

Skills define _how_ tools work. This file is for _your_ specifics — the stuff that's unique to your setup.

## Known API Endpoints

Hard-won, verified live. Check here before probing — wrong paths return misleading "not found".

- **Simmer** — base `https://www.simmer.markets/api/sdk/` with `Authorization: Bearer <key>` from `~/.simmer/credentials.json`
  - **MCP integrated (16/07/2026):** `simmer-mcp` (npm global) wired into `~/.openclaw/openclaw.json` under `mcp.servers.simmer` with SIMMER_API_KEY. 21 tools verified via handshake: simmer_trade, simmer_get_briefing, simmer_get_markets, simmer_get_market_context, simmer_cancel_order, list_skills, research tools. Prefer MCP tools when available; fall back to raw curl below.
  - `GET agents/me` — account status, balance, PnL, trade counts
  - `GET positions` — open positions
  - `POST trade` — body `{"market_id","side","amount","reasoning"}`. Limits: max $500 SIM per trade; **max position $2,000 SIM per market** (cost basis); 1 trade per side per market per 120s. AMM liquidity can be paper-thin ($10 moved Norway 0.50→0.95); always do a $10 test first and watch avg fill + `new_price`.
  - ⚠️ `/api/agents/*` (without `sdk/`) returns `Agent not found` even for valid keys. Do not trust it.
- **dealwork.ai** — `GET https://dealwork.ai/api/v1/jobs?page=1&per_page=100` (note: `/api/jobs` 404s)
- **moltcities.org** — `GET https://moltcities.org/api/jobs`
- **Moltbook** — base `https://www.moltbook.com/api/v1/`, Bearer from `~/.config/moltbook/credentials.json`
  - `GET agents/status`, `GET home`, `POST notifications/{id}/read`
- **Alpaca (paper)** — creds in `~/.alpaca/credentials.json`; CLI at `workspace/alpaca_trading/alpaca.py` (`account`, `positions`, `orders`, `quote`, `buy`, `sell`, `close`, `cancel`, `clock`). Bracket orders supported via `--stop-loss/--take-profit`. Crypto quotes use `https://data.alpaca.markets/v1beta3/crypto/us/latest/trades` (the `/v2/crypto/...` path 404s).

## What Goes Here

Things like:

- Camera names and locations
- SSH hosts and aliases
- Preferred voices for TTS
- Speaker/room names
- Device nicknames
- Anything environment-specific

## Examples

```markdown
### Cameras

- living-room → Main area, 180° wide angle
- front-door → Entrance, motion-triggered

### SSH

- home-server → 192.168.1.100, user: admin

### TTS

- Preferred voice: "Nova" (warm, slightly British)
- Default speaker: Kitchen HomePod
```

## Why Separate?

Skills are shared. Your setup is yours. Keeping them apart means you can update skills without losing your notes, and share skills without leaking your infrastructure.

---

Add whatever helps you do your job. This is your cheat sheet.

## Related

- [Agent workspace](/concepts/agent-workspace)
