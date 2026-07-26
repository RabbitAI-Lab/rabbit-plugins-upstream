"""Shared HTTP client — timeouts, retry with backoff and no environment inheritance.

Polymarket enforces its Cloudflare rate limit by *delaying* requests instead of
rejecting them outright, and the caps vary widely per endpoint (Data `/trades`
= 200 req/10s, Gamma `/markets` = 300/10s). A naive client degrades silently
under load; this one retries with exponential backoff and distinguishes a
transient error from a permanent one.

`trust_env=False` on every session: without it, the host's `.netrc`,
`REQUESTS_CA_BUNDLE` and proxy variables enter the calls — which is exactly the
vector of CVE-2024-47081 (credential leak to a malicious host via redirect).
"""
from __future__ import annotations

import random
import time
from typing import Any, Dict, Optional

import requests

from . import __version__

USER_AGENT = f"polymarket-agent/{__version__} (+openclaw skill)"
DEFAULT_TIMEOUT = 15.0
MAX_ATTEMPTS = 4
BACKOFF_BASE = 0.6

#: Codes worth retrying: rate limit and temporary unavailability.
RETRYABLE_STATUS = {429, 500, 502, 503, 504}

_SESSIONS: Dict[str, requests.Session] = {}


class ApiError(RuntimeError):
    """Failure querying a Polymarket API."""

    def __init__(self, message: str, status: Optional[int] = None) -> None:
        super().__init__(message)
        self.status = status


def session_for(host: str) -> requests.Session:
    """Persistent session per host (reuses the TLS connection)."""
    sess = _SESSIONS.get(host)
    if sess is None:
        sess = requests.Session()
        sess.trust_env = False
        sess.headers.update({"User-Agent": USER_AGENT, "Accept": "application/json"})
        _SESSIONS[host] = sess
    return sess


def _sleep_for(attempt: int, retry_after: Optional[str]) -> float:
    """Exponential backoff with jitter; honors Retry-After when present."""
    if retry_after:
        try:
            return min(float(retry_after), 30.0)
        except (TypeError, ValueError):
            pass
    # Jitter keeps several skill instances from retrying in lockstep.
    return BACKOFF_BASE * (2 ** attempt) + random.uniform(0, 0.3)


def get_json(
    base: str,
    path: str,
    params: Optional[Dict[str, Any]] = None,
    timeout: float = DEFAULT_TIMEOUT,
    label: str = "API",
) -> Any:
    """GET with retry. Raises ApiError once the attempts are exhausted."""
    url = f"{base}{path}"
    sess = session_for(base)
    last_error = ""

    for attempt in range(MAX_ATTEMPTS):
        try:
            resp = sess.get(url, params=params, timeout=timeout)
        except requests.Timeout:
            last_error = f"{label}: timed out after {timeout:.0f}s"
        except requests.RequestException as exc:
            last_error = f"{label}: network failure ({exc})"
        else:
            if resp.status_code == 200:
                try:
                    return resp.json()
                except ValueError as exc:
                    raise ApiError(f"{label}: non-JSON response", resp.status_code) from exc

            # 4xx (other than 429) is a caller error — retrying does not help.
            if resp.status_code not in RETRYABLE_STATUS:
                detail = resp.text[:200].strip().replace("\n", " ")
                raise ApiError(
                    f"{label}: HTTP {resp.status_code}"
                    + (f" — {detail}" if detail else ""),
                    resp.status_code,
                )

            last_error = f"{label}: HTTP {resp.status_code}"
            if attempt < MAX_ATTEMPTS - 1:
                time.sleep(_sleep_for(attempt, resp.headers.get("Retry-After")))
                continue

        if attempt < MAX_ATTEMPTS - 1:
            time.sleep(_sleep_for(attempt, None))

    raise ApiError(f"{last_error} (after {MAX_ATTEMPTS} attempts)")
