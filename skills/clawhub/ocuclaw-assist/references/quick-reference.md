# OcuClaw quick reference

**Guide version:** 2026-07-06 (1.0.6)

Reminders only. For recovery procedures, load
`{baseDir}/references/troubleshooting.md`. Back to the skill's SKILL.md. The
`Step N` pointers in the table resolve in
`{baseDir}/references/fresh-install.md`.

## Quick reference

| What | Value |
|---|---|
| Relay address (OcuClaw app) | `wss://<node>.<tailnet>.ts.net:8444` |
| Even AI agent URL | `https://<node>.<tailnet>.ts.net:8443/v1/chat/completions` |
| Relay backend | `localhost:<wsPort>` (plugin-hosted; `wsPort` = `47800` on a fresh install — confirm with `openclaw config get plugins.entries.ocuclaw.config.wsPort`) |
| Install / enable / update | `openclaw plugins install clawhub:ocuclaw` · `enable` · `update` (npm fallback: `install npm:ocuclaw`) |
| Restart / status / doctor | `openclaw gateway restart` · `openclaw gateway status` · `openclaw plugins doctor` |
| Config root | `plugins.entries.ocuclaw.config.*` via `openclaw config set` |
| Containerized host (Docker / VPS) | `wsBind` `0.0.0.0` + Docker publish `127.0.0.1:<wsPort>:<wsPort>` — never `0.0.0.0` on the host side (Step 5 / DOCKER-RELAY-UNREACHABLE) |
| Agent tool access | `allow` or `alsoAllow` must admit `"ocuclaw"` (or `"group:plugins"`); never set both lists in one scope; deny wins (Step 4 / AGENT-TOOLS-FILTERED) |
| Check versions | `npm view ocuclaw version` (latest) · `dist-tags` (channels) · `versions` (history) |
| Update / switch channel | `openclaw plugins update ocuclaw` (follows the recorded install source) · `update ocuclaw@beta` (move to beta — npm) · `install clawhub:ocuclaw --force` (roll back / move to the stable ClawHub lane) |
| Bug report with diagnostics | app Settings → **Client Debug Enabled** → yellow bug icon → **Send Bug Report** → post the `OCU-…` ticket in Discord (host pre-req: BOTH `externalDebugToolsEnabled` AND `allowDebugUpload` true, plugin ≥ 1.3 — ESCALATE Lane 1 / Step 12b) |
| Community / support | Discord `https://ocuclaw.com` |
| Donate (optional — not paid support) | `https://buymeacoffee.com/ocuclaw` |
