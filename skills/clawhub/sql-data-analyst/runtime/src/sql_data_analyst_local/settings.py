from __future__ import annotations

import os
import re
from ipaddress import ip_address
from pathlib import Path
from urllib.parse import urlsplit


RUNNER_VERSION = "1.0.0"
PLATFORM_API_ORIGIN = "https://ai-skills.open-idea.net"
TRUSTED_KEYS_SHA256 = "c63dac7aabe8f839746a4f35ceef60422dbab434c0536a6607905208d91706a5"
AUTHORIZE_PATH = "/api/v1/sql-data-analyst/executions/authorize"
MAX_PLATFORM_RESPONSE_BYTES = 64 * 1024
MAX_PLATFORM_TIMEOUT_SECONDS = 15.0
_SHA256 = re.compile(r"^[a-f0-9]{64}$")


class SettingsError(RuntimeError):
    """A stable, sanitized local configuration error."""

    def __init__(self, code: str = "configuration_invalid") -> None:
        self.code = code
        super().__init__(code)


def api_key_from_environment() -> str:
    api_key = os.environ.get("SQL_DATA_ANALYST_API_KEY", "").strip()
    if not api_key:
        raise SettingsError()
    return api_key


def validate_release_settings() -> None:
    try:
        parsed = urlsplit(PLATFORM_API_ORIGIN)
        host = (parsed.hostname or "").lower()
        if (
            parsed.scheme != "https"
            or not host
            or parsed.username is not None
            or parsed.password is not None
            or parsed.path
            or parsed.query
            or parsed.fragment
            or host == "localhost"
            or host.endswith((".invalid", ".example", ".test"))
            or _is_ip_address(host)
            or _SHA256.fullmatch(TRUSTED_KEYS_SHA256) is None
        ):
            raise SettingsError()
    except (ValueError, UnicodeError):
        raise SettingsError() from None


def _is_ip_address(host: str) -> bool:
    try:
        ip_address(host)
    except ValueError:
        return False
    return True


def default_workspace_root() -> Path:
    return Path.home() / ".openclaw" / "workspace" / "sql-data-analyst"
