"""Health check command (remediation §8).

Verifies dependencies and DATA READINESS — not just that services booted:

  python -m src.scripts.health

Exit 0 when the software stack is healthy AND the database is reachable AND
crawling has produced data or is visibly in progress. A fresh installation is
"initialized", NOT "complete" — this command reports the difference.
"""
from __future__ import annotations

import shutil
import socket
import sys


def _pg_reachable() -> bool:
    try:
        from src.database.session import get_engine
        with get_engine().connect() as conn:
            conn.exec_driver_sql("SELECT 1")
        return True
    except Exception:  # noqa: BLE001
        return False


def _redis_reachable() -> bool:
    try:
        from src.config import get_config
        import os as _os
        url = _os.environ.get("IRANCHEM__REDIS__URL") or get_config().redis.url
        host_part = url.replace("redis://", "").split("/")[0]
        host, _, port = host_part.partition(":")
        port = int(port or 6379)
        # bare-metal fallback: the compose service name "redis" is not a host
        candidates = [host]
        if host == "redis":
            candidates.append("localhost")
        for h in candidates:
            try:
                with socket.create_connection((h, port), timeout=2):
                    return True
            except Exception:  # noqa: BLE001
                continue
        return False
    except Exception:  # noqa: BLE001
        return False


def main() -> int:
    checks = []
    checks.append(("httrack", shutil.which("httrack") is not None))
    checks.append(("postgresql", _pg_reachable()))
    checks.append(("redis", _redis_reachable()))

    db_ok = checks[1][1]
    data_ready = False
    coverage = None
    if db_ok:
        try:
            from src.api.coverage_logic import coverage_snapshot
            from src.database.session import get_db_session
            db = get_db_session()
            try:
                coverage = coverage_snapshot(db)
            finally:
                db.close()
            r = coverage["records"]
            data_ready = (r["accepted_molecules"] > 0 or r["offerings"] > 0)
        except Exception as exc:  # noqa: BLE001
            checks.append(("coverage_query", False, str(exc)[:120]))
        else:
            checks.append(("coverage_query", True))

    for name, ok in [(c[0], c[1]) for c in checks]:
        print(f"[{'ok' if ok else '!!'}] {name}")
    if coverage:
        print("coverage:", coverage["suppliers"])
        print("export_readiness:", coverage["export_readiness"])

    if not all(c[1] for c in checks):
        print("HEALTH: FAILED (software stack incomplete)")
        return 1
    if data_ready:
        print("HEALTH: OK (stack healthy, data present)")
        return 0
    print("HEALTH: INITIALIZED (stack healthy, crawls not yet populated the database — "
          "query /api/v1/coverage; do not present exports as complete)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
