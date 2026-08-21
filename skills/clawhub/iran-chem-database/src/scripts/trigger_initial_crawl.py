"""Queue initial work; do not crawl synchronously during installation (remediation §2).

The installer must return in seconds. Seed crawling is enqueued immediately;
directory discovery is optional, slow, and queued as a separate task so it can
never delay the seed cohort.
"""
from __future__ import annotations

from src.config import get_config
from src.tasks.crawl_tasks import mirror_all_suppliers
from src.tasks.discovery_tasks import weekly_discovery


def main() -> None:
    cfg = get_config()
    seed_job = mirror_all_suppliers.delay()
    result = {
        "seed_mirror_job_id": seed_job.id,
        "discovery_job_id": None,
        "message": "Jobs queued. Query /api/v1/coverage and /api/v1/jobs before export.",
    }
    try:
        discovery_cfg = cfg.as_dict().get("discovery", {}) or {}
        if discovery_cfg.get("initial_directory_discovery"):
            discovery_job = weekly_discovery.delay()
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
