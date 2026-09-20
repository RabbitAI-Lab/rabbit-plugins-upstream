"""Celery tasks for the v2.10 social (Telegram) catalogue.

Dispatch always goes through ``celery_app.send_task`` — calling ``.delay()`` on
a bare ``@shared_task`` was the v2.4 bug that silently fell back to the AMQP
broker and failed with "Connection refused" while the worker was healthy.
"""
from __future__ import annotations

import logging

from celery import shared_task

from src.config import get_config
from src.crawler.telegram_engine import TelegramMirrorEngine
from src.discovery.social_seed_list import active_channels
from src.parser.social_catalog_pipeline import build_catalog

logger = logging.getLogger(__name__)


def _cfg_section(name: str, default: dict | None = None) -> dict:
    """Read a config section as a plain dict (get_config() returns a Config)."""
    try:
        data = get_config().as_dict()
    except Exception:  # noqa: BLE001 - config is optional for local parsing
        return dict(default or {})
    sec = data.get(name)
    return dict(sec) if isinstance(sec, dict) else dict(default or {})


def _config() -> tuple:
    social = _cfg_section("social")
    httrack = _cfg_section("httrack")
    base = httrack.get("base_mirror_dir", "/var/lib/iran_chem_db/mirrors")
    return base, social


@shared_task(bind=True, max_retries=2)
def mirror_social_channel(self, channel: str):
    """Mirror one public Telegram channel into the local mirror store."""
    base, social = _config()
    if not social.get("enabled", True):
        return {"channel": channel, "skipped": "social.enabled=false"}
    eng = TelegramMirrorEngine(
        base,
        timeout=social.get("timeout_seconds", 40),
        max_pages=social.get("max_pages_per_channel", 200),
        concurrency=social.get("concurrency", 6),
        request_delay=social.get("request_delay_seconds", 0.2),
    )
    try:
        return eng.mirror_channel(
            channel, incremental=social.get("incremental", True))
    except Exception as exc:  # noqa: BLE001 - retry, never abort the sweep
        logger.warning("social mirror failed for %s: %s", channel, exc)
        raise self.retry(exc=exc, countdown=60) from exc


@shared_task
def mirror_all_social_channels():
    """Sweep every verified channel (research sellers first)."""
    from src.tasks.celery_app import celery_app

    channels = active_channels()
    for ch in channels:
        celery_app.send_task(
            "src.tasks.social_tasks.mirror_social_channel", args=[ch])
    return {"dispatched": len(channels), "channels": channels}


@shared_task
def rebuild_social_catalog():
    """Re-parse mirrored channels into the catalogue (local files only)."""
    base, social = _config()
    cat = build_catalog(base, offline=not social.get("pubchem_enrichment", False))
    return cat["metrics"]
