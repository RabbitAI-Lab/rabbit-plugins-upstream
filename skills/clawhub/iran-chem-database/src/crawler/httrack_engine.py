"""HTTrackMirrorEngine — Python wrapper around the `httrack` CLI (spec §3.1).

Every website fetch goes through HTTrack. This class:
  * verifies httrack is installed
  * builds CLI commands from HTTrackMirrorConfig
  * runs initial mirrors and incremental `--update` runs
  * parses hts-changes.json for selective re-parsing
  * walks the local mirror store (the parser NEVER hits the network)
"""
from __future__ import annotations

import json
import logging
import shutil
import subprocess
from datetime import datetime
from pathlib import Path
from typing import List

from src.crawler.httrack_config import HTTRACK_BASE_DIR, HTTrackMirrorConfig

logger = logging.getLogger(__name__)

# v2.5: ".json" added so the WooCommerce-REST / sitemap engine's persisted
# JSON responses are picked up by the same local-file parse pass as mirrors.
# v2.6: ".md"/".txt" added for the free-access (Jina Reader) fallback fetches.
PARSEABLE_EXTENSIONS = {".html", ".htm", ".php", ".asp", ".aspx", ".jsp",
                        ".pdf", ".xlsx", ".xls", ".csv", ".json", ".md", ".txt"}


class HTTrackMirrorEngine:
    def __init__(self, base_dir: str = HTTRACK_BASE_DIR, require_httrack: bool = True):
        self.base_dir = Path(base_dir)
        self.httrack_bin = shutil.which("httrack")
        if require_httrack and not self.httrack_bin:
            raise RuntimeError(
                "HTTrack is not installed! Install it:\n"
                "  Ubuntu/Debian: sudo apt install httrack\n"
                "  Fedora: sudo dnf install httrack\n"
                "  Arch: sudo pacman -S httrack\n"
                "(or instantiate HTTrackMirrorEngine(require_httrack=False) to "
                "degrade gracefully to the curl/wget/python fallback)"
            )
        if self.httrack_bin:
            self._log_httrack_version()

    def _log_httrack_version(self) -> None:
        try:
            result = subprocess.run(
                [self.httrack_bin, "--version"], capture_output=True, text=True, timeout=10
            )
            version_line = (result.stdout or result.stderr).strip().splitlines()
            logger.info("HTTrack found: %s", version_line[0] if version_line else "unknown")
        except Exception as exc:  # noqa: BLE001 — version probe is cosmetic
            logger.warning("Could not probe httrack version: %s", exc)

    # ── command building ──────────────────────────────────────────────────
    def build_command(self, config: HTTrackMirrorConfig, update: bool = False) -> List[str]:
        cmd = config.to_flags(update=update)
        # v2.9: use the resolved binary path, not the literal "httrack".
        if cmd and cmd[0] == "httrack":
            cmd[0] = self.httrack_bin or "httrack"
        return cmd

    # ── mirror / update ───────────────────────────────────────────────────
    def mirror_supplier(self, config: HTTrackMirrorConfig) -> dict:
        # v2.9: degrade gracefully when httrack is missing — return an empty
        # mirror stats dict so the fallback chain (playwright, curl/wget/python,
        # free-access) takes over instead of the crawl task failing.
        if not self.httrack_bin:
            logger.warning("httrack not installed — returning empty mirror stats for %s",
                           config.project_name)
            return {
                "supplier_id": config.supplier_id,
                "project_name": config.project_name,
                "is_update": False,
                "return_code": 127,
                "error": "httrack-not-installed",
                "html_files": 0, "total_files": 0, "pdf_files": 0, "excel_files": 0,
                "mirror_size_bytes": 0,
                "stdout_tail": "", "stderr_tail": "httrack binary not found",
                "start_time": datetime.now().isoformat(),
                "end_time": datetime.now().isoformat(),
                "duration_seconds": 0,
            }

        output_path = Path(config.output_dir)
        self.base_dir.mkdir(parents=True, exist_ok=True)
        is_update = output_path.exists() and (output_path / "hts-cache").exists()
        cmd = self.build_command(config, update=is_update)
        logger.info("%s supplier %s: %s",
                    "Updating" if is_update else "Mirroring", config.project_name, " ".join(cmd))

        start_time = datetime.now()
        try:
            result = subprocess.run(
                cmd, capture_output=True, text=True,
                timeout=config.max_time + 300, cwd=str(self.base_dir),
            )
        except subprocess.TimeoutExpired:
            return {"supplier_id": config.supplier_id, "project_name": config.project_name,
                    "is_update": is_update, "return_code": -1, "error": "timeout"}
        end_time = datetime.now()

        stats = {
            "supplier_id": config.supplier_id,
            "project_name": config.project_name,
            "is_update": is_update,
            "start_time": start_time.isoformat(),
            "end_time": end_time.isoformat(),
            "duration_seconds": (end_time - start_time).total_seconds(),
            "return_code": result.returncode,
            "stdout_tail": (result.stdout or "")[-2000:],
            "stderr_tail": (result.stderr or "")[-2000:],
        }

        changes_file = output_path / "hts-changes.json"
        if changes_file.exists():
            stats["changes"] = self.parse_changes(changes_file)

        stats["total_files"] = self.count_mirror_files(output_path)
        stats["mirror_size_bytes"] = self.dir_size(output_path)
        stats["html_files"] = self.count_files_by_ext(output_path, [".html", ".htm", ".php", ".asp", ".aspx", ".jsp"])
        stats["pdf_files"] = self.count_files_by_ext(output_path, [".pdf"])
        stats["excel_files"] = self.count_files_by_ext(output_path, [".xlsx", ".xls", ".csv"])

        logger.info("Mirror complete for %s: %s files, %s bytes",
                    config.project_name, stats["total_files"], stats["mirror_size_bytes"])
        return stats

    # ── change detection ──────────────────────────────────────────────────
    @staticmethod
    def parse_changes(changes_file: Path) -> dict:
        if not changes_file.exists():
            return {"new": [], "modified": [], "unchanged": [], "removed": []}
        with open(changes_file, encoding="utf-8", errors="replace") as fh:
            raw = fh.read().strip()
        if not raw:
            return {"new": [], "modified": [], "unchanged": [], "removed": []}
        try:
            changes = json.loads(raw)
        except json.JSONDecodeError:
            # hts-changes.json may be a flat list of {path, status} or use other shapes
            return {"new": [], "modified": [], "unchanged": [], "removed": [], "_unparsed": raw[:200]}

        summary: dict = {"new": [], "modified": [], "unchanged": [], "removed": []}
        if isinstance(changes, list):
            for entry in changes:
                if not isinstance(entry, dict):
                    continue
                status = str(entry.get("status", entry.get("type", "unknown"))).lower()
                filename = entry.get("filename", entry.get("path", entry.get("file", "")))
                summary = HTTrackMirrorEngine._classify(summary, status, filename)
        elif isinstance(changes, dict):
            for key, val in changes.items():
                if key in summary and isinstance(val, list):
                    summary[key] = [str(x) for x in val]
                elif isinstance(val, list):
                    for item in val:
                        if isinstance(item, dict):
                            status = str(item.get("status", "")).lower()
                            filename = item.get("filename", item.get("path", ""))
                            summary = HTTrackMirrorEngine._classify(summary, status, filename)
        return summary

    @staticmethod
    def _classify(summary: dict, status: str, filename: str) -> dict:
        if status in ("new", "added", "created"):
            summary["new"].append(filename)
        elif status in ("modified", "changed", "updated", "moved"):
            summary["modified"].append(filename)
        elif status == "unchanged":
            summary["unchanged"].append(filename)
        elif status in ("removed", "deleted", "gone"):
            summary["removed"].append(filename)
        return summary

    def get_changed_files(self, config: HTTrackMirrorConfig) -> List[str]:
        changes_file = Path(config.output_dir) / "hts-changes.json"
        if changes_file.exists():
            changes = self.parse_changes(changes_file)
            if changes["new"] or changes["modified"]:
                return changes["new"] + changes["modified"]
        # Fallback: HTTrack writes newly downloaded files into hts-cache/new.lst
        new_lst = Path(config.output_dir) / "hts-cache" / "new.lst"
        if new_lst.exists():
            try:
                return [ln.strip() for ln in new_lst.read_text(errors="replace").splitlines() if ln.strip()]
            except OSError:
                pass
        return self.get_all_parseable_files(config)

    def get_removed_files(self, config: HTTrackMirrorConfig) -> List[str]:
        changes_file = Path(config.output_dir) / "hts-changes.json"
        if changes_file.exists():
            removed = self.parse_changes(changes_file)["removed"]
            if removed:
                return removed
        # Fallback: parse hts-log.txt for deleted/removed entries
        log_file = Path(config.output_dir) / "hts-log.txt"
        if log_file.exists():
            try:
                lines = log_file.read_text(errors="replace").splitlines()
                return [ln.split(":", 1)[-1].strip() for ln in lines
                        if any(k in ln.lower() for k in ("deleted", "removed", "gone"))
                        and ":" in ln]
            except OSError:
                pass
        return []

    # ── mirror walking ────────────────────────────────────────────────────
    def get_all_parseable_files(self, config: HTTrackMirrorConfig) -> List[str]:
        output_path = Path(config.output_dir)
        if not output_path.exists():
            return []
        files: List[str] = []
        for file_path in output_path.rglob("*"):
            if file_path.suffix.lower() in PARSEABLE_EXTENSIONS and file_path.is_file():
                if "hts-cache" not in file_path.parts and "hts-log" not in str(file_path):
                    files.append(str(file_path))
        return sorted(files)

    # ── URL list mirrors ──────────────────────────────────────────────────
    def mirror_using_url_list(self, urls: List[str], output_dir: str, project_name: str,
                              timeout: int = 180, depth: int = 2) -> dict:
        """Mirror a small URL list with a strict, configurable time budget.

        Used by directory discovery, where a 3600-second timeout would block
        the seed-crawling cohort for hours (remediation §2).
        """
        url_list_file = Path(output_dir) / f"{project_name}_urls.txt"
        url_list_file.parent.mkdir(parents=True, exist_ok=True)
        url_list_file.write_text("\n".join(urls) + "\n", encoding="utf-8")
        cmd = [
            "httrack", "-%L", str(url_list_file), "-O", output_dir,
            f"--depth={depth}", "--stay-on-same-domain", "--connection-per-second=1", "-q",
        ]
        try:
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)
            return {"return_code": result.returncode, "url_count": len(urls),
                    "timed_out": False}
        except subprocess.TimeoutExpired:
            return {"return_code": -1, "url_count": len(urls), "timed_out": True}

    # ── helpers ───────────────────────────────────────────────────────────
    @staticmethod
    def count_mirror_files(path: Path) -> int:
        if not path.exists():
            return 0
        return sum(1 for p in path.rglob("*") if p.is_file() and "hts-cache" not in p.parts)

    @staticmethod
    def count_files_by_ext(path: Path, extensions: List[str]) -> int:
        if not path.exists():
            return 0
        exts = {e.lower() for e in extensions}
        return sum(1 for p in path.rglob("*") if p.suffix.lower() in exts and p.is_file())

    @staticmethod
    def dir_size(path: Path) -> int:
        if not path.exists():
            return 0
        return sum(p.stat().st_size for p in path.rglob("*") if p.is_file())


def is_httrack_installed() -> bool:
    return shutil.which("httrack") is not None
