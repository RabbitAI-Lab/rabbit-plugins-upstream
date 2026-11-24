# Alert Configuration Guide

## Telegram Setup
1. Create bot via @BotFather
2. Get token: `TELEGRAM_BOT_TOKEN=123456:ABC-DEF...`
3. Get chat ID: message bot, visit `https://api.telegram.org/bot<token>/getUpdates`
   (Telegram's official Bot API endpoint — the token is in the URL by
   Telegram's own design; see "How credentials are handled" in SKILL.md.)

## Discord Setup
1. Server Settings → Integrations → Webhooks
2. Create webhook, copy URL
3. Set `DISCORD_WEBHOOK_URL=https://discord.com/api/webhooks/...`
   (must be a `discord.com` / `discordapp.com` webhook URL — anything
   else is refused by `alert_bot.py`.)

## Privacy
Alerts sent to Telegram/Discord contain operational information (which
service failed, truncated wallet addresses, balances, short error
details). Use a **private** chat/channel, keep the token and webhook URL
secret, and never put API keys or private keys in alert text — the
scripts scrub key material out of error details before sending. If you
configure neither channel, alerts print to local stdout only. See the
Privacy warning in SKILL.md.

## Alert Levels
| Level | Condition | Channels |
|-------|-----------|----------|
| CRITICAL | Wallet empty, API down | Telegram + Discord |
| WARNING | Gas low, API rate limit | Telegram |
| INFO | Healthcheck passed, balance OK | Discord |

## Webhook Format
```json
{
  "agent": "your-agent-name",
  "level": "critical",
  "message": "Groq API key expired",
  "timestamp": "2026-05-07T04:15:00Z",
  "action": "alert-sent"
}
```
