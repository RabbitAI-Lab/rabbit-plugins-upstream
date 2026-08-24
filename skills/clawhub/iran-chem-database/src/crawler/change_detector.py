"""hts-changes.json parser — determines what an HTTrack update actually did."""
from __future__ import annotations

import json
from pathlib import Path
from typing import List

from src.crawler.httrack_engine import HTTrackMirrorEngine


class ChangeDetector:
    """Reads HTTrack's hts-changes.json and classifies file changes.

    hts-changes.json lists what a crawl left new, changed, unchanged and gone
    against the previous mirror — it is the quick way to see what an update did.
    """

    def __init__(self, mirror_dir: str | Path):
        self.mirror_dir = Path(mirror_dir)

    def read_changes(self) -> dict:
        changes_file = self.mirror_dir / "hts-changes.json"
        if not changes_file.exists():
            return {"new": [], "modified": [], "unchanged": [], "removed": []}
        return HTTrackMirrorEngine.parse_changes(changes_file)

    def new_files(self) -> List[str]:
        return self.read_changes()["new"]

    def modified_files(self) -> List[str]:
        return self.read_changes()["modified"]

    def removed_files(self) -> List[str]:
        return self.read_changes()["removed"]

    def parseable_changed_files(self) -> List[str]:
        changes = self.read_changes()
        return changes["new"] + changes["modified"]

    def summary(self) -> dict:
        changes = self.read_changes()
        return {
            "files_new": len(changes["new"]),
            "files_modified": len(changes["modified"]),
            "files_unchanged": len(changes["unchanged"]),
            "files_removed": len(changes["removed"]),
        }


def load_changes_json(path: str | Path) -> dict:
    """Directly load a hts-changes.json file as raw JSON."""
    with open(path, encoding="utf-8", errors="replace") as fh:
        return json.load(fh)
