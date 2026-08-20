"""Trigger the initial discovery + mirror cycle (spec §7.4 installer step)."""
from __future__ import annotations

from src.tasks.crawl_tasks import full_discovery_and_mirror_cycle


def main() -> None:
    result = full_discovery_and_mirror_cycle()
    print("Initial crawl triggered:", result)


if __name__ == "__main__":
    main()
