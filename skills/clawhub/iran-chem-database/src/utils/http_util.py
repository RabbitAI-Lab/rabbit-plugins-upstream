"""Shared HTTP helpers with retry/backoff & zero-timer token bucket (v2.36.1).

Best-practice networking for a crawler:
- Zero-timer Token Bucket pacing: replaces blind static sleeps with token-bucket
  flow control. If tokens exist in the bucket, requests execute with 0ms delay.
- Transient HTTP 408/425/429/5xx and socket errors are retried with exponential
  backoff with jitter; non-retryable statuses (401/403/404/400) are raised
  immediately so callers can fail over to the next method.
- Retry-After header parsing on HTTP 429 / 503 so callers and adaptive selectors
  know the exact server cooldown requirement.
- Streamed chunk-based downloads with maximum byte limits (prevents infinite
  media or hanging socket streams).
- TLS verification stays ON by default, with opt-out only when explicitly needed.

Stdlib only (urllib + ssl + time + threading + email.utils).
"""
from __future__ import annotations

import email.utils
import logging
import random
import ssl
import threading
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone
from typing import Optional, Tuple

logger = logging.getLogger(__name__)

DEFAULT_UA = "IranChemDB/2.36.1 (Research Chemical Database crawler; contact@iranchem.db)"
RETRYABLE_HTTP = (408, 409, 425, 429, 500, 502, 503, 504)
DEFAULT_MAX_BYTES = 2_000_000  # 2 MB stream cap for regular crawl pages


class TokenBucketLimiter:
    """Zero-timer token bucket rate limiter for polite, fluent crawling.

    Instead of blind time.sleep(delay) after every request, this allows requests
    to proceed with 0ms wait as long as the token bucket has capacity. Only when
    the burst limit is saturated does it introduce a minimal, precise wait.
    """

    def __init__(self):
        self._lock = threading.Lock()
        self._buckets: dict[str, Tuple[float, float]] = {}  # key -> (tokens, last_update_t)

    def acquire(self, key: str, rate: float = 2.0, capacity: float = 5.0) -> float:
        """Acquire 1 token for `key`.

        rate: tokens generated per second (e.g. 2.0 = 2 reqs/sec).
        capacity: maximum burst capacity (e.g. 5.0 = allow up to 5 immediate requests).
        Returns the duration slept in seconds (0.0 if capacity was immediately available).
        """
        now = time.monotonic()
        sleep_time = 0.0
        with self._lock:
            tokens, last_time = self._buckets.get(key, (capacity, now))
            elapsed = max(0.0, now - last_time)
            tokens = min(capacity, tokens + elapsed * rate)
            if tokens >= 1.0:
                tokens -= 1.0
                self._buckets[key] = (tokens, now)
                return 0.0
            else:
                needed = 1.0 - tokens
                sleep_time = min(needed / rate, 3.0)  # clamp max wait to 3s
                tokens = 0.0
                self._buckets[key] = (tokens, now + sleep_time)

        if sleep_time > 0:
            time.sleep(sleep_time)
        return sleep_time

    def reset(self, key: Optional[str] = None) -> None:
        with self._lock:
            if key:
                self._buckets.pop(key, None)
            else:
                self._buckets.clear()


# Global singleton instance for cross-engine rate pacing
GLOBAL_LIMITER = TokenBucketLimiter()


def parse_retry_after(hdr_val: Optional[str]) -> Optional[float]:
    """Parse HTTP Retry-After header into seconds.

    Supports both integer seconds ('120') and HTTP-date ('Fri, 31 Dec 2026 23:59:59 GMT').
    """
    if not hdr_val:
        return None
    hdr_val = hdr_val.strip()
    # 1. Integer seconds
    if hdr_val.isdigit():
        try:
            return max(0.0, float(hdr_val))
        except ValueError:
            pass
    # 2. HTTP Date
    try:
        dt = email.utils.parsedate_to_datetime(hdr_val)
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=timezone.utc)
        now = datetime.now(timezone.utc)
        diff = (dt - now).total_seconds()
        return max(0.0, diff)
    except Exception:
        return None


def get_bytes_stream(url: str, timeout: int = 40, user_agent: str = DEFAULT_UA,
                     accept: str = "text/html, application/json;q=0.9, */*;q=0.8",
                     headers: Optional[dict] = None, retries: int = 3,
                     backoff: float = 1.5, verify_tls: bool = True,
                     max_bytes: int = DEFAULT_MAX_BYTES,
                     rate_key: Optional[str] = None) -> bytes:
    """GET a URL and return its body via chunked streaming with size limit.

    - If rate_key is provided, acquires from GLOBAL_LIMITER (zero-timer when not saturated).
    - If response exceeds max_bytes, reading stops cleanly to avoid memory/hang issues.
    - If HTTP 429/503 is returned, parses Retry-After header and sets exc.retry_after.
    """
    if rate_key:
        GLOBAL_LIMITER.acquire(rate_key)

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
                # Stream chunks of 64KB up to max_bytes
                chunks = []
                total = 0
                while True:
                    chunk = resp.read(65536)
                    if not chunk:
                        break
                    chunks.append(chunk)
                    total += len(chunk)
                    if total >= max_bytes:
                        logger.debug("GET %s reached stream limit %d bytes", url, max_bytes)
                        break
                return b"".join(chunks)
        except urllib.error.HTTPError as exc:
            retry_sec = parse_retry_after(exc.headers.get("Retry-After"))
            setattr(exc, "retry_after", retry_sec)
            if exc.code not in RETRYABLE_HTTP:
                raise
            last = exc
            logger.info("GET %s -> HTTP %s (attempt %d/%d, retry_after=%s)",
                        url, exc.code, attempt + 1, retries + 1, retry_sec)
        except (urllib.error.URLError, TimeoutError, ConnectionError, OSError) as exc:
            last = exc
            logger.info("GET %s -> %s (attempt %d/%d)",
                        url, type(exc).__name__, attempt + 1, retries + 1)

        if attempt < retries:
            # Check if server asked for specific Retry-After
            wait_time = getattr(last, "retry_after", None)
            if wait_time and wait_time <= 10.0:
                time.sleep(wait_time)
            else:
                # Exponential backoff with jitter
                jitter = random.uniform(0.1, 0.4)
                time.sleep((backoff * (1.8 ** attempt)) + jitter)

    raise (last if last is not None
           else urllib.error.URLError(f"GET {url} failed after {retries} retries"))


def get_bytes(url: str, timeout: int = 40, user_agent: str = DEFAULT_UA,
              accept: str = "text/html, application/json;q=0.9, */*;q=0.8",
              headers: Optional[dict] = None, retries: int = 3,
              backoff: float = 1.5, verify_tls: bool = True) -> bytes:
    """GET a URL and return its body (backward compatible wrapper)."""
    return get_bytes_stream(url, timeout=timeout, user_agent=user_agent,
                            accept=accept, headers=headers, retries=retries,
                            backoff=backoff, verify_tls=verify_tls,
                            max_bytes=DEFAULT_MAX_BYTES)
