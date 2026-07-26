# Polymarket World Cup Player Goal Value

A Simmer/OpenClaw skill for scanning Polymarket-imported player-goal YES markets and entering only when a player-level fair-value model clears configurable edge, liquidity, cooldown, and budget gates.

This repository is a BridgeAISocial/Hermes-maintained fork/fix of the original ClawHub skill by Alyna. It keeps the original value framework and adds local dogfood fixes around Simmer venue execution, World Cup game-window scheduling, player-data freshness, and safe cron behavior.

## Safety

- Dry-run by default.
- `$SIM` / sim venue runs are virtual and not real money.
- Live Polymarket orders require explicit `--live --venue polymarket` and valid Simmer credentials.
- No private keys or API keys should be committed to this repo.

## Quick start

```bash
python3 -m py_compile player_goal_value.py adaptive_game_runner.py scripts/client_factory.py
python3 player_goal_value.py --config
python3 player_goal_value.py --venue sim
```

Refresh data when needed:

```bash
python3 scripts/fetch_understat_players.py --seasons 2026,2025,2024 --min-minutes 300
python3 scripts/fetch_wc_stats.py
```

Run around World Cup game windows:

```bash
SIMMER_WCPGV_SCAN_LIMIT=75 \
SIMMER_WCPGV_REFRESH_MAX_AGE_MIN=360 \
python3 adaptive_game_runner.py --venue polymarket --force
```

## Release notes

### 0.1.7

- Added adaptive game-window runner support.
- Added player-data freshness gating and scan-limit controls for frequent crons.
- Added local client factory wiring for safer venue/live construction.
- Refreshed bundled World Cup player data from merged Understat + custom player + ESPN World Cup pipeline.

### 0.1.6

- Added fallback discovery search via `/api/sdk/markets?q=...`.
- Added sim-only proxy quote option.
- Fixed venue-specific trade payloads.
- Fixed `--positions` live account inspection.
