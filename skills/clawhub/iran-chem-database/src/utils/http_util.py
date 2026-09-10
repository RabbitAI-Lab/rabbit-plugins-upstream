"""Shared HTTP helpers with retry/backoff (added v2.9).

Best-practice networking for a crawler: transient HTTP 408/425/429/5xx and
socket errors are retried with exponential backoff instead of failing the
supplier; non-retryable statuses (401/403/404/400) are raised immediately so
callers can fail over to the next method. TLS verification stays ON by default
(security), with an opt-out only for callers that explicitly need it.

Stdlib only (urllib + ssl + time).
"""
from __future__ import annotations

import logging
import ssl
import time
import urllib.error
import urllib.request
from typing import Optional

logger = logging.getLogger(__name__)

DEFAULT_UA = "IranChemDB/2.9 (Research Chemical Database crawler; contact@iranchem.db)"
RETRYABLE_HTTP = (408, 409, 425, 429, 500, 502, 503, 504)


def get_bytes(url: str, timeout: int = 40, user_agent: str = DEFAULT_UA,
              accept: str = "text/html, application/json;q=0.9, */*;q=0.8",
              headers: Optional[dict] = None, retries: int = 3,
              backoff: float = 2.0, verify_tls: bool = True) -> bytes:
    """GET a URL and return its body, retrying transient failures.

    Raises urllib.error.HTTPError for non-retryable statuses and the last
    exception after `retries` transient failures — callers decide whether to
    fail over. Never prints credentials (headers are our own).
    """
    hdrs = {"User-Agent": user_agent, "Accept": accept}
    if headers:
        hdrs.update(headers)

    ctx = ssl.create_default_context()
    if not verify_tls:
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE

    last: Optional[Exception] = None
    for attempt in range(retries + 1):
        try:
            req = urllib.request.Request(url, headers=hdrs)
            with urllib.request.urlopen(req, timeout=timeout, context=ctx) as resp:
                return resp.read()
        except urllib.error.HTTPError as exc:
            if exc.code not in RETRYABLE_HTTP:
                raise
            last = exc
            logger.info("GET %s -> HTTP %s (attempt %d/%d)",
                        url, exc.code, attempt + 1, retries + 1)
        except (urllib.error.URLError, TimeoutError, ConnectionError, OSError) as exc:
            last = exc
            logger.info("GET %s -> %s (attempt %d/%d)",
                        url, type(exc).__name__, attempt + 1, retries + 1)
        if attempt < retries:
            time.sleep(backoff * (2 ** attempt))
    raise (last if last is not None
           else urllib.error.URLError(f"GET {url} failed after {retries} retries"))
