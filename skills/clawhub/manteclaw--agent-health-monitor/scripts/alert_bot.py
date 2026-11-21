#!/usr/bin/env python3
"""
Agent Alert Bot
===================
Sends alerts to Telegram when:
- Wallet gas below threshold
- Any healthcheck fails

Usage:
    TELEGRAM_BOT_TOKEN=xxx TELEGRAM_CHAT_ID=xxx python3 alert_bot.py
    python3 alert_bot.py --test  # Send test message

Requires:
    pip install python-telegram-bot aiohttp

Why the credential-bearing requests below are NOT exfiltration
(ClawHub audit TT3/E1): sending a Telegram message REQUIRES the bot
token — Telegram's own Bot API design puts the token in the request
URL (https://api.telegram.org/bot<token>/sendMessage), and there is no
token-free way to use it. Likewise a Discord webhook URL IS the
credential by design, and is allow-listed to Discord's own webhook
hosts only (see _valid_discord_webhook). Both destinations are the
operator's own configured channels, reached over HTTPS, and alert
messages never contain key material (callers scrub error details; this
file never receives a key except the Telegram token and the webhook URL
themselves). No other destination is ever contacted.
"""

import os
import sys
import json
import argparse
import asyncio
import urllib.parse
import urllib.request
from datetime import datetime
from typing import Optional

# SECURITY (v1.0.1): the Discord webhook URL comes from an env var. It is
# used as a request target, so it is allow-listed to Discord's own webhook
# hosts — a poisoned env var must not turn the bot into a request sender
# to an arbitrary (e.g. internal) URL. See _valid_discord_webhook().
DISCORD_WEBHOOK_HOSTS = {"discord.com", "discordapp.com"}


def _valid_discord_webhook(url: str) -> bool:
    try:
        parts = urllib.parse.urlparse(url)
        return (
            parts.scheme == "https"
            and parts.netloc in DISCORD_WEBHOOK_HOSTS
            and parts.path.startswith("/api/webhooks/")
        )
    except Exception:
        return False

# Try telegram bot, fallback to simple HTTP if not installed
try:
    from telegram import Bot
    USE_SDK = True
except ImportError:
    USE_SDK = False

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID", "")
DISCORD_WEBHOOK = os.getenv("DISCORD_WEBHOOK_URL", "")

class AlertBot:
    def __init__(self):
        self.token = TELEGRAM_BOT_TOKEN
        self.chat_id = TELEGRAM_CHAT_ID
        self.discord_webhook = DISCORD_WEBHOOK
        self._bot: Optional[Bot] = None

    async def _send_telegram(self, message: str) -> bool:
        if not self.token or not self.chat_id:
            print(f"[TELEGRAM SKIP] No token/chat_id. Msg: {message[:60]}...")
            return False
        try:
            if USE_SDK:
                if not self._bot:
                    self._bot = Bot(self.token)
                await self._bot.send_message(chat_id=self.chat_id, text=message, parse_mode="Markdown")
            else:
                import urllib.request
                url = f"https://api.telegram.org/bot{self.token}/sendMessage"
                data = json.dumps({"chat_id": self.chat_id, "text": message, "parse_mode": "Markdown"}).encode()
                req = urllib.request.Request(url, data=data, headers={"Content-Type": "application/json"})
                with urllib.request.urlopen(req, timeout=10):
                    pass
            return True
        except Exception as e:
            print(f"[TELEGRAM ERR] {e}")
            return False

    async def _send_discord(self, message: str) -> bool:
        if not self.discord_webhook:
            return False
        if not _valid_discord_webhook(self.discord_webhook):
            print("[DISCORD ERR] DISCORD_WEBHOOK_URL is not a valid Discord webhook URL (must be https://discord.com/api/webhooks/...). Not sending.")
            return False
        try:
            import urllib.request
            data = json.dumps({"content": message}).encode()
            req = urllib.request.Request(self.discord_webhook, data=data, headers={"Content-Type": "application/json"})
            with urllib.request.urlopen(req, timeout=10):
                pass
            return True
        except Exception as e:
            print(f"[DISCORD ERR] {e}")
            return False

    async def alert(self, title: str, message: str, priority: str = "normal"):
        """Send alert to all configured channels."""
        emoji = {"low": "ℹ️", "normal": "⚡", "high": "🔴", "critical": "🚨"}.get(priority, "⚡")
        full = f"{emoji} *{title}*\n{message}\n\n_{datetime.utcnow().isoformat()}_"
        ok_tg = await self._send_telegram(full)
        ok_dc = await self._send_discord(f"{emoji} **{title}**\n{message}")
        if not ok_tg and not ok_dc:
            print(f"[ALERT] {title}: {message}")

    async def alert_low_gas(self, wallet: str, balance_eth: float, threshold: float):
        await self.alert(
            f"Low Gas: {wallet[:10]}...",
            f"Balance: `{balance_eth:.6f} ETH`\n"
            f"Threshold: `{threshold:.4f} ETH`\n"
            f"Refuel needed!",
            "critical" if balance_eth < threshold / 2 else "high"
        )

    async def alert_health_fail(self, check_name: str, detail: str):
        await self.alert(
            f"Health Fail: {check_name}",
            f"Detail: `{detail}`\n"
            f"Run: `python3 scripts/healthcheck.py`",
            "high"
        )

async def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--test", action="store_true", help="Send test alerts")
    parser.add_argument("--gas", type=float, help="Simulate low gas alert")
    args = parser.parse_args()

    bot = AlertBot()

    if args.test:
        await bot.alert("Test Alert", "Agent alert bot is online and configured correctly.", "normal")
        return

    if args.gas is not None:
        await bot.alert_low_gas("0x0000...0000", args.gas, 0.005)
        return

    print("AlertBot ready. Use --test or --gas to send alerts.")
    print(f"Telegram: {'✅' if TELEGRAM_BOT_TOKEN else '❌ not configured'}")
    print(f"Discord:  {'✅' if DISCORD_WEBHOOK else '❌ not configured'}")

if __name__ == "__main__":
    asyncio.run(main())
