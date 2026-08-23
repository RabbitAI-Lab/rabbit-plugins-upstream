"""Celery application bound to Redis broker."""
from __future__ import annotations

from celery import Celery

from src.config import get_config

redis_url = get_config().redis.url

celery_app = Celery(
    "iran_chem_db",
    broker=redis_url,
    backend=redis_url,
    include=["src.tasks.crawl_tasks", "src.tasks.discovery_tasks",
             "src.tasks.sync_tasks", "src.tasks.social_tasks"],
)

celery_app.conf.update(
    timezone="Asia/Tehran",
    enable_utc=True,
    task_serializer="json",
    result_serializer="json",
    accept_content=["json"],
    beat_schedule={
        "mirror-all-suppliers": {
            "task": "src.tasks.crawl_tasks.mirror_all_suppliers",
            "schedule": 60 * 60,  # hourly sweep checks each supplier's interval
        },
        "weekly-discovery": {
            "task": "src.tasks.discovery_tasks.weekly_discovery",
            "schedule": 7 * 24 * 60 * 60,
        },
        # v2.10 — social channels update far more often than websites, and an
        # incremental sweep is cheap (only pages newer than the cached state).
        "mirror-all-social-channels": {
            "task": "src.tasks.social_tasks.mirror_all_social_channels",
            "schedule": 6 * 60 * 60,
        },
    },
)
