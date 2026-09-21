"""Queue initial work; do not crawl synchronously during installation (remediation §2).

The installer must return in seconds. Seed crawling is enqueued immediately;
directory discovery is optional, slow, and queued as a separate task so it can
never delay the seed cohort.

v2.5 FIX: the previous release called `mirror_all_suppliers.delay()` on the
bare `@shared_task` object WITHOUT the Redis-bound `celery_app` being the
current app — Celery then fell back to a default app with the AMQP broker
(pyamqp, port 5672) and the dispatch failed with "Connection refused" even
though the worker (which loads `celery_app`) was healthy. All dispatch now
goes through `celery_app.send_task(...)` so the broker/backend always match
the worker's Redis configuration.
"""
from __future__ import annotations

from src.config import get_config
from src.tasks.celery_app import celery_app

SEED_TASK = "src.tasks.crawl_tasks.mirror_all_suppliers"
DISCOVERY_TASK = "src.tasks.discovery_tasks.weekly_discovery"


def _dispatch(name: str):
    """Enqueue by task name on the configured app; returns an AsyncResult."""
    return celery_app.send_task(name)


def main() -> None:
    cfg = get_config()
    seed_job = _dispatch(SEED_TASK)
    result = {
        "seed_mirror_job_id": seed_job.id,
        "discovery_job_id": None,
        "message": "Jobs queued. Query /api/v1/coverage and /api/v1/jobs before export.",
    }
    try:
        discovery_cfg = cfg.as_dict().get("discovery", {}) or {}
        if discovery_cfg.get("initial_directory_discovery"):
            discovery_job = _dispatch(DISCOVERY_TASK)
            result["discovery_job_id"] = discovery_job.id
            result["message"] = ("Jobs queued (seed mirror + directory discovery). "
                                 "Query /api/v1/coverage and /api/v1/jobs before export.")
        else:
            result["message"] = ("Seed mirror job queued; directory discovery disabled "
                                 "(discovery.initial_directory_discovery=false). "
                                 "Query /api/v1/coverage and /api/v1/jobs before export.")
    except Exception as exc:  # noqa: BLE001 (discovery must never block seeding)
        result["discovery_error"] = str(exc)[:200]
    print(result)


if __name__ == "__main__":
    main()
