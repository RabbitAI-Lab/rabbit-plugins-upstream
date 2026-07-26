#!/usr/bin/env python3
"""
briefing_preflight.py — Morning Briefing Pre-Flight Health Check

Runs at 6:45 AM daily, 15 minutes before the morning briefing.
Validates all dependencies are healthy. Alerts on failure via WhatsApp DM
to Harsh, with macOS notification fallback if WhatsApp gateway is down.
"""

import json
import os
import subprocess
import sys
from datetime import datetime, timedelta
from pathlib import Path

from core.config_loader import SKILL_DIR as _SKILL_DIR_STR
SKILL_DIR = Path(_SKILL_DIR_STR)
LOG_DIR = SKILL_DIR / "logs"
LOG_DIR.mkdir(exist_ok=True)

PREFLIGHT_LOG = LOG_DIR / "preflight_alert.log"


def _log(msg: str):
    ts = datetime.now().isoformat()
    line = f"[{ts}] {msg}"
    print(line)
    with open(PREFLIGHT_LOG, "a") as f:
        f.write(line + "\n")


def _macos_notify(message: str):
    try:
        subprocess.run([
            "osascript", "-e",
            f'display notification "{message}" with title "OpenClaw Preflight"'
        ], timeout=5)
    except Exception:
        pass


def _send_alert(message: str, wa_available: bool):
    """Alert via macOS notification. All WA delivery goes through OpenClaw."""
    _macos_notify(message[:200])
    _log(f"ALERT: {message}")


def check_google_auth() -> tuple[bool, str]:
    try:
        from core.keychain_secrets import load_google_secrets, last_keyring_error
        load_google_secrets()

        client_id = os.environ.get("GOOGLE_CLIENT_ID", "")
        client_secret = os.environ.get("GOOGLE_CLIENT_SECRET", "")
        refresh_token = os.environ.get("GOOGLE_REFRESH_TOKEN", "")

        if not all([client_id, client_secret, refresh_token]):
            kr_err = last_keyring_error()
            executable = sys.executable
            detail = f" [keyring: {kr_err}]" if kr_err else " [keyring: no error recorded — secrets simply absent]"
            return False, f"Google credentials unavailable (python={executable}){detail}"

        from google.oauth2.credentials import Credentials
        from google.auth.transport.requests import Request

        creds = Credentials(
            token="",
            refresh_token=refresh_token,
            token_uri="https://oauth2.googleapis.com/token",
            client_id=client_id,
            client_secret=client_secret,
        )
        creds.refresh(Request())
        return True, "Token refreshed OK"
    except Exception as e:
        return False, f"Google auth failed: {str(e)[:100]}"


def check_calendar_id() -> tuple[bool, str]:
    try:
        config = json.loads((SKILL_DIR / "config.json").read_text())
        cal_id = config.get("calendar", {}).get("id", "")
        primary_email = config.get("calendar", {}).get("primary_email_id", "")

        if not cal_id:
            return False, "calendar.id is empty in config.json"

        if primary_email and cal_id == primary_email:
            return False, f"calendar.id points at personal email calendar ({primary_email})"

        # Verify the calendar ID exists in Google
        from core.keychain_secrets import load_google_secrets
        load_google_secrets()

        from google.oauth2.credentials import Credentials
        from google.auth.transport.requests import Request
        from googleapiclient.discovery import build

        creds = Credentials(
            token="",
            refresh_token=os.environ.get("GOOGLE_REFRESH_TOKEN", ""),
            token_uri="https://oauth2.googleapis.com/token",
            client_id=os.environ.get("GOOGLE_CLIENT_ID", ""),
            client_secret=os.environ.get("GOOGLE_CLIENT_SECRET", ""),
        )
        creds.refresh(Request())
        service = build("calendar", "v3", credentials=creds)
        service.calendarList().get(calendarId=cal_id).execute()
        return True, f"Calendar ID valid and accessible"
    except Exception as e:
        err = str(e)[:100]
        if "404" in err or "notFound" in err:
            return False, f"Calendar ID not found in Google account"
        return False, f"Calendar ID check failed: {err}"


def check_calendar_freshness() -> tuple[bool, str]:
    cache_file = SKILL_DIR / "calendar_data" / "family_calendar.json"
    if not cache_file.exists():
        return False, "No cached calendar data — will sync fresh"

    mtime = datetime.fromtimestamp(cache_file.stat().st_mtime)
    age = datetime.now() - mtime
    if age > timedelta(hours=24):
        # Clear stale cache
        cache_file.write_text("{}")
        return False, f"Calendar cache was {age.total_seconds()/3600:.0f}h old — cleared"

    return True, f"Calendar cache is {age.total_seconds()/3600:.1f}h old"


def check_weather_api() -> tuple[bool, str]:
    try:
        from features.briefing.weather import fetch_weather
        result = fetch_weather()
        if result and "temp_current" in result:
            return True, f"Weather OK: {result['temp_current']}°F"
        return False, "Weather API returned no temperature data"
    except Exception as e:
        return False, f"Weather API error: {str(e)[:80]}"


GATEWAY_LOG = Path.home() / ".openclaw" / "logs" / "gateway.log"
GATEWAY_LIVENESS_TAIL_BYTES = 64 * 1024
GATEWAY_LIVENESS_WINDOW_MIN = 60


def _gateway_log_recently_active(window_min: int = GATEWAY_LIVENESS_WINDOW_MIN) -> tuple[bool, str]:
    """Check the gateway log tail for recent WhatsApp activity.

    Works around openclaw bug #56648 where the WhatsApp socket force-disconnects
    every 30 min when idle (status 499). During the reconnect cycle, the
    `openclaw status` CLI may stall and the live status check returns timeout
    even though the gateway is functionally healthy. The log tail is the
    cheapest authoritative signal — any "Sent message" or "Listening for
    personal WhatsApp inbound" line newer than the window means the socket
    has cycled successfully.
    """
    if not GATEWAY_LOG.exists():
        return False, "gateway.log not found"
    try:
        size = GATEWAY_LOG.stat().st_size
        with open(GATEWAY_LOG, "rb") as f:
            if size > GATEWAY_LIVENESS_TAIL_BYTES:
                f.seek(size - GATEWAY_LIVENESS_TAIL_BYTES)
                f.readline()  # discard partial first line
            tail = f.read().decode("utf-8", errors="replace")
    except OSError as e:
        return False, f"gateway.log read error: {e}"

    cutoff = datetime.now().astimezone() - timedelta(minutes=window_min)
    for line in reversed(tail.splitlines()):
        if "[whatsapp]" not in line:
            continue
        if "Sent message" not in line and "Listening for personal WhatsApp inbound" not in line:
            continue
        ts_str = line.split(" ", 1)[0]
        try:
            ts = datetime.fromisoformat(ts_str)
        except ValueError:
            continue
        if ts >= cutoff:
            age_min = (datetime.now().astimezone() - ts).total_seconds() / 60
            kind = "send" if "Sent message" in line else "listen"
            return True, f"gateway log shows {kind} {age_min:.0f}m ago"
    return False, f"no whatsapp activity in last {window_min}m"


def check_whatsapp_gateway() -> tuple[bool, str]:
    try:
        result = subprocess.run(
            ["openclaw", "status"],
            capture_output=True, text=True, timeout=10
        )
        if result.returncode == 0:
            return True, "WhatsApp gateway running"
        cli_err = result.stderr[:80]
    except FileNotFoundError:
        return False, "openclaw CLI not found"
    except subprocess.TimeoutExpired:
        cli_err = "status command timed out (gateway may be in reconnect cycle)"
    except Exception as e:
        cli_err = f"{type(e).__name__}: {str(e)[:60]}"

    # Fallback: gateway may be in the 30-min idle reconnect cycle (bug #56648).
    # Trust the log tail if it shows recent send/listen activity.
    log_ok, log_msg = _gateway_log_recently_active()
    if log_ok:
        return True, f"WhatsApp gateway healthy via log ({log_msg}); CLI: {cli_err}"
    return False, f"WhatsApp gateway check failed: {cli_err}; {log_msg}"


def check_config_integrity() -> tuple[bool, str]:
    try:
        from core.config_loader import config
        errors = config.validate()
        if errors:
            return False, f"Config validation: {', '.join(errors)}"
        return True, "Config valid"
    except Exception as e:
        return False, f"Config load error: {str(e)[:80]}"


def run_preflight():
    _log("=== Preflight starting ===")

    checks = [
        ("Google auth", check_google_auth, True),
        ("Calendar ID", check_calendar_id, True),
        ("Calendar freshness", check_calendar_freshness, False),
        ("Weather API", check_weather_api, False),
        ("WhatsApp gateway", check_whatsapp_gateway, True),
        ("Config integrity", check_config_integrity, True),
    ]

    wa_ok = False
    failures = []

    for name, check_fn, is_critical in checks:
        try:
            ok, msg = check_fn()
        except Exception as e:
            ok, msg = False, f"Unexpected error: {str(e)[:80]}"

        status = "✅" if ok else ("❌" if is_critical else "⚠️")
        _log(f"  {status} {name}: {msg}")

        if name == "WhatsApp gateway":
            wa_ok = ok

        if not ok and is_critical:
            failures.append(f"{name}: {msg}")

    if failures:
        alert_msg = "Pre-flight check FAILED:\n" + "\n".join(f"• {f}" for f in failures)
        _send_alert(alert_msg, wa_ok)
        _log(f"=== Preflight FAILED ({len(failures)} critical) ===")
        return False

    _log("=== Preflight PASSED ===")
    return True


if __name__ == "__main__":
    success = run_preflight()
    sys.exit(0 if success else 1)
