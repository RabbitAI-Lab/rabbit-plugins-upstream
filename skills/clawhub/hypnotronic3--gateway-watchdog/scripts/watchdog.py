#!/usr/bin/env python3
"""
OpenClaw Gateway Watchdog — monitors gateway health, auto-restarts on failure,
writes status/alert JSON files for remote monitoring.

Configurable via watchdog.conf (see watchdog.conf.example).
Runs as a systemd service.

https://clawhub.ai/skills/gateway-watchdog
"""

import subprocess
import time
import json
import logging
import os
import sys
import configparser
from datetime import datetime, timezone
from pathlib import Path

# ─── Config loading ──────────────────────────────────────────────────────────

SCRIPT_DIR = Path(__file__).parent.resolve()
DEFAULT_CONF = SCRIPT_DIR / "watchdog.conf"

def load_config() -> dict:
    """Load configuration from watchdog.conf, falling back to defaults."""
    conf_path = Path(os.environ.get("WATCHDOG_CONF", str(DEFAULT_CONF)))
    defaults = {
        "HEALTH_URL": "http://127.0.0.1:18789/health",
        "CHECK_INTERVAL": "60",
        "RESTART_COOLDOWN": "30",
        "MAX_RESTART_ATTEMPTS": "3",
        "STATE_FILE": str(SCRIPT_DIR / "watchdog-state.json"),
        "ALERT_FILE": str(SCRIPT_DIR / "watchdog-alert.json"),
        "LOG_FILE": "/var/log/openclaw-gateway-watchdog.log",
        "GATEWAY_SERVICE": "openclaw-gateway",
    }

    if conf_path.exists():
        parser = configparser.ConfigParser()
        parser.read(str(conf_path))
        if parser.has_section("watchdog"):
            for key in defaults:
                if key in parser["watchdog"]:
                    defaults[key] = parser["watchdog"][key]

    # Type conversions
    return {
        "HEALTH_URL": defaults["HEALTH_URL"],
        "CHECK_INTERVAL": int(defaults["CHECK_INTERVAL"]),
        "RESTART_COOLDOWN": int(defaults["RESTART_COOLDOWN"]),
        "MAX_RESTART_ATTEMPTS": int(defaults["MAX_RESTART_ATTEMPTS"]),
        "STATE_FILE": defaults["STATE_FILE"],
        "ALERT_FILE": defaults["ALERT_FILE"],
        "LOG_FILE": defaults["LOG_FILE"],
        "GATEWAY_SERVICE": defaults["GATEWAY_SERVICE"],
    }

cfg = load_config()

# ─── Logging ─────────────────────────────────────────────────────────────────

log_path = Path(cfg["LOG_FILE"])
log_path.parent.mkdir(parents=True, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler(str(log_path)),
        logging.StreamHandler(sys.stdout),
    ],
)
log = logging.getLogger("watchdog")

# ─── State persistence ────────────────────────────────────────────────────────

def load_state() -> dict:
    """Load persistent state from disk."""
    try:
        state_path = Path(cfg["STATE_FILE"])
        if state_path.exists():
            with open(state_path) as f:
                return json.load(f)
    except Exception as e:
        log.warning(f"Could not load state file: {e}")
    return {
        "consecutive_failures": 0,
        "restart_attempts": 0,
        "total_restarts": 0,
        "last_known_good": None,
        "last_failure_time": None,
        "status": "starting",
    }


def save_state(state: dict) -> None:
    """Persist state to disk so it survives service restarts."""
    try:
        state_path = Path(cfg["STATE_FILE"])
        state_path.parent.mkdir(parents=True, exist_ok=True)
        with open(str(state_path), "w") as f:
            json.dump(state, f, indent=2)
        os.chmod(str(state_path), 0o644)
    except Exception as e:
        log.warning(f"Could not save state file: {e}")


# ─── Alert file ──────────────────────────────────────────────────────────────

def write_alert(subject: str, message: str, severity: str = "critical") -> None:
    """Write an alert file that remote monitors can read via HTTP or SSH."""
    try:
        alert = {
            "severity": severity,
            "subject": subject,
            "message": message,
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "gateway_url": cfg["HEALTH_URL"],
        }
        alert_path = Path(cfg["ALERT_FILE"])
        alert_path.parent.mkdir(parents=True, exist_ok=True)
        with open(str(alert_path), "w") as f:
            json.dump(alert, f, indent=2)
        os.chmod(str(alert_path), 0o644)
        log.info(f"Alert file written: {subject}")
    except Exception as e:
        log.error(f"Could not write alert file: {e}")


def clear_alert() -> None:
    """Remove the alert file when gateway recovers."""
    try:
        alert_path = Path(cfg["ALERT_FILE"])
        if alert_path.exists():
            alert_path.unlink()
            log.info("Alert file cleared (gateway recovered)")
    except Exception as e:
        log.warning(f"Could not clear alert file: {e}")


# ─── Health check ─────────────────────────────────────────────────────────────

def check_health() -> bool:
    """Return True if the gateway health endpoint responds OK."""
    try:
        result = subprocess.run(
            ["curl", "-sf", "--max-time", "10", cfg["HEALTH_URL"]],
            capture_output=True, text=True, timeout=15,
        )
        if result.returncode == 0:
            try:
                data = json.loads(result.stdout)
                return data.get("ok", False) is True or data.get("status") == "live"
            except json.JSONDecodeError:
                # curl succeeded but non-JSON — still alive
                return True
        return False
    except Exception as e:
        log.error(f"Health check exception: {e}")
        return False


# ─── Gateway restart ─────────────────────────────────────────────────────────

def restart_gateway(attempt: int) -> bool:
    """Attempt to restart the OpenClaw gateway. Returns True if healthy after."""
    log.warning(
        f"Attempting gateway restart (attempt {attempt}/{cfg['MAX_RESTART_ATTEMPTS']})"
    )

    # Set up environment for systemctl --user
    env = os.environ.copy()
    uid = os.getuid()
    env["XDG_RUNTIME_DIR"] = f"/run/user/{uid}"

    # Try systemctl --user restart
    try:
        result = subprocess.run(
            ["systemctl", "--user", "restart", cfg["GATEWAY_SERVICE"]],
            capture_output=True, text=True, timeout=30, env=env,
        )
        if result.returncode == 0:
            log.info(f"systemctl --user restart {cfg['GATEWAY_SERVICE']} succeeded")
        else:
            log.warning(f"systemctl --user restart failed: {result.stderr.strip()}")
    except Exception as e:
        log.error(f"systemctl --user restart exception: {e}")

    # Wait for cooldown then check
    log.info(f"Waiting {cfg['RESTART_COOLDOWN']}s for gateway to start...")
    time.sleep(cfg["RESTART_COOLDOWN"])

    if check_health():
        log.info(f"Gateway recovered after restart attempt {attempt}")
        return True

    log.warning(f"Gateway still unhealthy after restart attempt {attempt}")
    return False


# ─── Main loop ────────────────────────────────────────────────────────────────

def main():
    log.info("=" * 60)
    log.info("OpenClaw Gateway Watchdog starting")
    log.info(f"Monitoring: {cfg['HEALTH_URL']} (every {cfg['CHECK_INTERVAL']}s)")
    log.info(f"Max restart attempts per cycle: {cfg['MAX_RESTART_ATTEMPTS']}")
    log.info(f"Alert file: {cfg['ALERT_FILE']}")
    log.info(f"State file: {cfg['STATE_FILE']}")
    log.info(f"Gateway service: {cfg['GATEWAY_SERVICE']}")
    log.info("=" * 60)

    state = load_state()
    state["status"] = "running"
    save_state(state)
    clear_alert()

    while True:
        try:
            if check_health():
                if state["consecutive_failures"] > 0:
                    log.info(
                        f"Gateway RECOVERED after {state['consecutive_failures']} failure(s)"
                    )
                state["consecutive_failures"] = 0
                state["restart_attempts"] = 0
                state["last_known_good"] = datetime.now(timezone.utc).isoformat()
                state["status"] = "healthy"
                clear_alert()
                save_state(state)
            else:
                state["consecutive_failures"] += 1
                state["last_failure_time"] = datetime.now(timezone.utc).isoformat()
                state["status"] = "degraded"
                log.warning(
                    f"Gateway DOWN — consecutive failures: {state['consecutive_failures']}"
                )

                if state["restart_attempts"] < cfg["MAX_RESTART_ATTEMPTS"]:
                    state["restart_attempts"] += 1
                    state["total_restarts"] += 1
                    save_state(state)

                    if restart_gateway(state["restart_attempts"]):
                        state["consecutive_failures"] = 0
                        state["restart_attempts"] = 0
                        state["status"] = "recovering"
                        state["last_known_good"] = datetime.now(timezone.utc).isoformat()
                        clear_alert()
                        save_state(state)
                        continue
                else:
                    log.error(
                        f"Max restart attempts reached ({cfg['MAX_RESTART_ATTEMPTS']}). "
                        f"Cannot recover gateway automatically."
                    )
                    state["status"] = "critical"
                    save_state(state)
                    write_alert(
                        "Gateway DOWN — Auto-Recovery Failed",
                        f"OpenClaw gateway down for {state['consecutive_failures']} consecutive checks "
                        f"({state['consecutive_failures'] * cfg['CHECK_INTERVAL'] // 60} minutes).\n"
                        f"Auto-restart attempted {cfg['MAX_RESTART_ATTEMPTS']} times without success.\n"
                        f"Manual intervention required.\n"
                        f"Restart: systemctl --user restart {cfg['GATEWAY_SERVICE']}",
                        severity="critical",
                    )

            save_state(state)

        except Exception as e:
            log.error(f"Watchdog main loop error: {e}", exc_info=True)

        time.sleep(cfg["CHECK_INTERVAL"])


if __name__ == "__main__":
    main()