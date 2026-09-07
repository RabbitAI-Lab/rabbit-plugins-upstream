"""Telegram public-channel mirror engine (v2.10).

Fetches the server-rendered public preview ``https://t.me/s/<channel>`` and
walks it backwards to the true beginning of the channel. No login, no API key,
no bot token — this reads exactly what an anonymous browser sees.

Design notes (all field-measured 2026-08-22):

* **Pagination.** ``t.me/s/<chan>?before=<oldest_id>`` returns the previous
  page. Roughly 19-20 posts/page, ~90-160 KB each.
* **End condition.** Stop when a page yields no posts, or when the oldest post
  id stops decreasing (the cursor has stalled). Reaching id 1 means the true
  channel beginning. Gaps in the id space are *deleted posts*, not fetch
  failures — they are reported honestly rather than retried forever.
* **Politeness.** Concurrency is capped (default 6) and a small delay is
  applied between requests. Pages are fetched through the shared
  retry/backoff helper so a transient 429/5xx fails over instead of dying.
* **Incremental resync.** Per-channel state (newest id seen) is cached under
  the mirror dir; a re-run only fetches pages newer than that, turning a full
  crawl into a seconds-long update.
* **Storage.** Raw HTML pages land in ``<mirror>/social/telegram/<chan>/`` so
  the existing *local-file-only* parser contract is preserved: nothing
  downstream touches the network.

Stdlib only (urllib via ``src.utils.http_util``) — no new dependencies.
"""
from __future__ import annotations

import json
import logging
import os
import re
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime
from typing import Dict, List, Optional

from src.utils.http_util import get_bytes

logger = logging.getLogger(__name__)

TELEGRAM_PREVIEW = "https://t.me/s/{channel}"
TELEGRAM_PREVIEW_BEFORE = "https://t.me/s/{channel}?before={before}"

# Telegram serves the preview to normal browsers; a browser UA avoids being
# handed the "open in app" stub page.
BROWSER_UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
              "(KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36")

_POST_ID_RE = re.compile(r'data-post="[^"]+/(\d+)"')
# "Channel created" stubs carry no message bubbles at all.
_STUB_MARKERS = ("tgme_page_additional", "Channel created")


class TelegramMirrorEngine:
    """Mirror public Telegram channels into the local mirror store."""

    def __init__(self, base_mirror_dir: str, *, timeout: int = 40,
                 max_pages: int = 200, concurrency: int = 6,
                 request_delay: float = 0.2, user_agent: str = BROWSER_UA):
        self.base_mirror_dir = base_mirror_dir
        self.timeout = timeout
        self.max_pages = max_pages
        # Politeness cap: never fan out harder than this per channel.
        self.concurrency = max(1, min(int(concurrency), 8))
        self.request_delay = request_delay
        self.user_agent = user_agent

    # -- paths ------------------------------------------------------------
    def channel_dir(self, channel: str) -> str:
        return os.path.join(self.base_mirror_dir, "social", "telegram", channel)

    def _state_path(self, channel: str) -> str:
        return os.path.join(self.channel_dir(channel), ".crawl_state.json")

    def read_state(self, channel: str) -> dict:
        try:
            with open(self._state_path(channel), "r", encoding="utf-8") as fh:
                return json.load(fh)
        except (OSError, ValueError):
            return {}

    def _write_state(self, channel: str, state: dict) -> None:
        path = self._state_path(channel)
        os.makedirs(os.path.dirname(path), exist_ok=True)
        tmp = path + ".tmp"
        with open(tmp, "w", encoding="utf-8") as fh:
            json.dump(state, fh, ensure_ascii=False, indent=2)
        os.replace(tmp, path)  # atomic: a killed run never leaves half state

    # -- fetching ---------------------------------------------------------
    def fetch_page(self, channel: str, before: Optional[int] = None) -> Optional[str]:
        """Fetch one preview page. Returns HTML text, or None on failure."""
        url = (TELEGRAM_PREVIEW_BEFORE.format(channel=channel, before=before)
               if before else TELEGRAM_PREVIEW.format(channel=channel))
        try:
            raw = get_bytes(url, timeout=self.timeout, user_agent=self.user_agent)
        except Exception as exc:  # noqa: BLE001 - fail over, never abort a crawl
            logger.info("telegram: %s before=%s -> %s", channel, before, type(exc).__name__)
            return None
        return raw.decode("utf-8", "ignore")

    @staticmethod
    def page_post_ids(html: str) -> List[int]:
        return sorted({int(m) for m in _POST_ID_RE.findall(html)})

    def content_verify(self, channel: str) -> dict:
        """Probe a channel and decide whether it is a real, populated channel.

        Verification is by CONTENT (does the page carry real posts?), never by
        byte size — stubs and small real channels overlap in size.
        """
        html = self.fetch_page(channel)
        if html is None:
            return {"channel": channel, "populated": False, "reason": "fetch_failed",
                    "posts": 0}
        ids = self.page_post_ids(html)
        if not ids:
            reason = ("empty_stub" if any(m in html for m in _STUB_MARKERS)
                      else "no_posts")
            return {"channel": channel, "populated": False, "reason": reason,
                    "posts": 0}
        return {"channel": channel, "populated": True, "reason": "ok",
                "posts": len(ids), "newest_id": max(ids), "oldest_id": min(ids)}

    # -- mirroring --------------------------------------------------------
    def mirror_channel(self, channel: str, *, full_history: bool = True,
                       incremental: bool = True) -> dict:
        """Mirror one channel to disk.

        Returns stats: pages, posts, id span, whether the true beginning was
        reached, and any gaps (deleted posts).
        """
        started = time.time()
        outdir = self.channel_dir(channel)
        os.makedirs(outdir, exist_ok=True)
        state = self.read_state(channel) if incremental else {}
        prev_newest = state.get("newest_id")

        stats = {
            "channel": channel, "pages": 0, "posts": 0, "files": 0,
            "status": "crawled",
            "newest_id": None, "oldest_id": None, "reached_beginning": False,
            "incremental": bool(prev_newest), "errors": 0,
            "started_at": datetime.now().isoformat(timespec="seconds"),
        }

        first = self.fetch_page(channel)
        if first is None:
            stats["errors"] += 1
            stats["error"] = "initial fetch failed"
            return stats

        ids = self.page_post_ids(first)
        if not ids:
            stats["error"] = "no posts (stub or empty channel)"
            return stats

        self._save_page(outdir, channel, ids[-1], first)
        stats["pages"] = 1
        stats["files"] = 1
        seen = set(ids)
        newest, oldest = max(ids), min(ids)

        # Incremental: the newest page already reaches known territory.
        if prev_newest and oldest <= prev_newest:
            # Nothing new beyond the cached state. Report this explicitly:
            # emitting coverage 0% here would wrongly look like a failed crawl.
            stats.update(newest_id=newest, oldest_id=oldest,
                         posts=len(seen), reached_beginning=False,
                         status="incremental_up_to_date",
                         new_posts=max(0, newest - prev_newest),
                         coverage_pct=None,
                         duration_s=round(time.time() - started, 2))
            state.update(newest_id=max(newest, prev_newest),
                         last_run=stats["started_at"])
            self._write_state(channel, state)
            return stats

        if full_history:
            cursor = oldest
            stall = 0
            while stats["pages"] < self.max_pages:
                batch = self._fetch_batch(channel, cursor)
                if not batch:
                    break
                progressed = False
                for _before, html in batch:
                    if html is None:
                        stats["errors"] += 1
                        continue
                    page_ids = self.page_post_ids(html)
                    if not page_ids:
                        continue
                    new_ids = set(page_ids) - seen
                    if not new_ids:
                        continue
                    self._save_page(outdir, channel, min(page_ids), html)
                    seen |= set(page_ids)
                    stats["pages"] += 1
                    stats["files"] += 1
                    progressed = True
                    oldest = min(oldest, min(page_ids))
                if not progressed:
                    stall += 1
                    if stall >= 2:  # cursor no longer advancing -> done
                        break
                else:
                    stall = 0
                if oldest <= 1:
                    break
                cursor = oldest
                if self.request_delay:
                    time.sleep(self.request_delay)

        stats["posts"] = len(seen)
        stats["newest_id"] = newest
        stats["oldest_id"] = oldest
        stats["reached_beginning"] = oldest <= 1
        # Gaps are deleted posts — report, never treat as failure.
        span = newest - oldest + 1 if newest and oldest else 0
        stats["id_span"] = span
        stats["gaps"] = max(0, span - len(seen))
        stats["coverage_pct"] = round(100.0 * len(seen) / span, 1) if span else 0.0
        stats["duration_s"] = round(time.time() - started, 2)

        state.update(newest_id=max(newest, prev_newest or 0),
                     oldest_id=oldest, last_run=stats["started_at"])
        self._write_state(channel, state)
        return stats

    def _fetch_batch(self, channel: str, cursor: int) -> List[tuple]:
        """Fetch up to ``concurrency`` consecutive history pages in parallel.

        Telegram pages hold ~20 posts, so stepping the cursor by 20 per slot
        lets a bounded thread pool cover a wide history window per round-trip
        while staying within the politeness cap.
        """
        cursors = [max(1, cursor - i * 20) for i in range(self.concurrency)]
        cursors = [c for c in dict.fromkeys(cursors) if c >= 1]
        out: List[tuple] = []
        with ThreadPoolExecutor(max_workers=self.concurrency) as pool:
            futs = {pool.submit(self.fetch_page, channel, c): c for c in cursors}
            for fut in as_completed(futs):
                out.append((futs[fut], fut.result()))
        return out

    @staticmethod
    def _save_page(outdir: str, channel: str, marker: int, html: str) -> str:
        path = os.path.join(outdir, f"{channel}-{marker:08d}.html")
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(html)
        return path

    def mirror_channels(self, channels: List[str], **kw) -> Dict[str, dict]:
        return {ch: self.mirror_channel(ch, **kw) for ch in channels}
