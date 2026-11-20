# Configuration — set these before use

Set the values below in your environment (shell, cron, or your own secret
manager). **No script in this skill reads a `.env` file or any credential
file** — v1.0.1 removed the supervisor's `.env` loading entirely. If you
keep secrets in a `.env` file, load it yourself before running the
scripts; the skill will only ever read what is already in its environment.

| Variable | Purpose | Required |
|---|---|---|
| `ALCHEMY_API_KEY` | Alchemy RPC key for balance checks and the Alchemy health check | Yes (balance/health) |
| `GROQ_API_KEY` | Groq key-validity check | No |
| `MISTRAL_API_KEY` | Mistral key-validity check | No |
| `OPENROUTER_API_KEY` | OpenRouter key-validity check | No |
| `GITHUB_TOKEN` | GitHub key-validity check | No |
| `DUNE_API_KEY` | Dune key-validity check | No |
| `BANKR_API_KEY` | Bankr key-validity check (via its SDK — the optional `litcoin` package; without it the check is skipped) | No |
| `MESHLEDGER_API_KEY` | MeshLedger key-validity check | No |
| `EXECUTOR_ADDRESS` | Wallet tracked by `scripts/balance-monitor.py` | No |
| `WALLET_ADDRESS_1` | First extra wallet tracked by `scripts/balance-monitor.py` | No |
| `WALLET_ADDRESS_2` | Second extra wallet tracked by `scripts/balance-monitor.py` | No |
| `LITCOIIN_WALLET_ADDRESS` | Optional wallet checked by `scripts/healthcheck.py` | No |
| `EXECUTOR_PRIVATE_KEY` | Optional. `healthcheck.py` uses it **only locally** to derive the wallet address and compare it with `EXECUTOR_ADDRESS`. It is never transmitted anywhere. Leave unset for dry-run/balance-only checks. | No |
| `TELEGRAM_BOT_TOKEN`, `TELEGRAM_CHAT_ID` | Telegram alerts (operator's own chat) | No |
| `DISCORD_WEBHOOK_URL` | Discord alerts. Must be an `https://discord.com/api/webhooks/...` (or `discordapp.com`) URL — anything else is refused. | No |
| `GAS_ALERT_THRESHOLD` | ETH gas alert threshold (default: 0.005) | No |

Notes (v1.0.1):

- Dependencies (v1.0.3): the scripts need `web3` and `eth-account`
  (`pip install -r requirements.txt`; see `requirements.txt` in the
  skill root). The Bankr check needs the optional `litcoin` SDK;
  without it the check reports "SDK not installed" and skips. Telegram
  alerts work over plain HTTPS; `python-telegram-bot` is optional.

- `AGENT_WORKSPACE` and `WALLET_ADDRESS` were removed: they belonged to
  the deleted `supervisor.sh` / `revenue_reporter.py` and no remaining
  script reads them.
- `SKILL.md` no longer references `scripts/install-services.sh`,
  `scripts/alert.sh`, or `references/recovery-playbook.md` — none of
  those shipped, and the references were removed.
- Keys are sent only to each key owner's own official HTTPS endpoint
  (see "How credentials are handled" in `SKILL.md`), and never appear
  in logs, alerts, or exports.
