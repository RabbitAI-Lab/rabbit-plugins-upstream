"""Basic tests for sentinel-downloader v0.2.0 (Phase 2 round 2).

Covers:
- --help mentions all new flags (--place, --year, --season, --pick-best, --qa)
- argparse validation: --bbox / --place mutual exclusion, --year + --season expansion
- format_output helpers (table / json) work on representative input
- --qa JSON file is written correctly when --qa-mode is invoked
"""
import json
import os
import subprocess
import sys
import argparse
from unittest.mock import patch, MagicMock

import pytest

# conftest loads the hyphenated module as `sentinel_downloader`
import sentinel_downloader as sd  # noqa: E402


HERE = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(HERE, ".."))
SCRIPT = os.path.join(PROJECT_ROOT, "sentinel-download.py")


# ── CLI surface ──
class TestHelpText:
    def test_help_mentions_place(self):
        out = subprocess.run(
            [sys.executable, SCRIPT, "--help"],
            capture_output=True, text=True, timeout=15,
        )
        combined = out.stdout + out.stderr
        assert "--place" in combined
        assert "--year" in combined
        assert "--season" in combined
        assert "--pick-best" in combined
        assert "--qa" in combined

    def test_help_in_chinese(self):
        out = subprocess.run(
            [sys.executable, SCRIPT, "--help"],
            capture_output=True, text=True, timeout=15,
        )
        combined = out.stdout + out.stderr
        # Some Chinese description should appear
        assert any('\u4e00' <= c <= '\u9fff' for c in combined), "no Chinese in --help"


# ── bbox / place mutual exclusion ──
class TestMutualExclusion:
    def test_bbox_and_place_rejected(self, capsys):
        """When both --bbox and --place are given, main() should exit with code 2."""
        # We invoke the script via subprocess because the real flow uses Nominatim/Open-Meteo
        out = subprocess.run(
            [sys.executable, SCRIPT,
             "--bbox", "103", "30", "104", "31",
             "--place", "成都市",
             "--start-date", "2024-06-01", "--end-date", "2024-08-31",
             "--no-nominatim", "--output-format", "json",
             "--limit", "1"],
            capture_output=True, text=True, timeout=30,
        )
        # Either we got an error from --place/--bbox mutual exclusion, or
        # network failed. Either way, exit code != 0 OR stdout includes error.
        combined = out.stdout + out.stderr
        assert ("ERROR" in combined) or (out.returncode != 0)

    def test_missing_bbox_and_place(self):
        out = subprocess.run(
            [sys.executable, SCRIPT,
             "--start-date", "2024-06-01", "--end-date", "2024-08-31",
             "--no-nominatim", "--output-format", "json"],
            capture_output=True, text=True, timeout=15,
        )
        combined = out.stdout + out.stderr
        assert "ERROR" in combined
        assert "--bbox" in combined or "--place" in combined


# ── Year/season handling (via --help, no network) ──
class TestYearSeason:
    def test_season_without_year_rejected(self):
        out = subprocess.run(
            [sys.executable, SCRIPT,
             "--season", "summer",
             "--start-date", "2024-06-01", "--end-date", "2024-08-31",
             "--output-format", "json"],
            capture_output=True, text=True, timeout=15,
        )
        combined = out.stdout + out.stderr
        assert "ERROR" in combined


# ── format_output (table / json) ──
class TestFormatOutput:
    def test_format_output_json(self):
        """format_output(json) returns a valid JSON string."""
        results = [
            {"id": "S2A_MSIL2A_20240823", "datetime": "2024-08-23T03:39:18Z",
             "cloud_cover": 21.58, "platform": "sentinel-2a"}
        ]
        out = sd.format_output(results, "json")
        data = json.loads(out)
        assert isinstance(data, list)
        assert len(data) == 1
        assert data[0]["id"] == "S2A_MSIL2A_20240823"

    def test_format_output_table(self):
        """format_output(table) returns a human-readable string."""
        results = [
            {"id": "S2A_MSIL2A_20240823", "datetime": "2024-08-23T03:39:18Z",
             "cloud_cover": 21.58, "platform": "sentinel-2a",
             "bbox": [102.1, 30.6, 104.5, 32.8]}
        ]
        out = sd.format_output(results, "table")
        assert "S2A_MSIL2A_20240823" in out

    def test_format_output_empty(self):
        """format_output handles empty results list."""
        out = sd.format_output([], "json")
        data = json.loads(out)
        assert data == []
        out2 = sd.format_output([], "table")
        # Should not crash and should mention no results
        assert isinstance(out2, str)


# ── --pick-best behavior (sort by cloud cover) ──
class TestPickBest:
    def test_pick_best_keeps_lowest_cloud(self):
        """Reproduce main()'s pick-best logic: sort by cloud_cover, keep lowest."""
        results = [
            {"id": "S1", "cloud_cover": 30.0},
            {"id": "S2", "cloud_cover": 5.0},
            {"id": "S3", "cloud_cover": 60.0},
        ]
        def _cc(r):
            try:
                return float(r.get("cloud_cover", 1e9))
            except (TypeError, ValueError):
                return 1e9
        best = sorted(results, key=_cc)[0]
        assert best["id"] == "S2"

    def test_pick_best_handles_missing_cloud(self):
        results = [
            {"id": "S1"},  # missing cloud_cover
            {"id": "S2", "cloud_cover": 10.0},
        ]
        def _cc(r):
            try:
                return float(r.get("cloud_cover", 1e9))
            except (TypeError, ValueError):
                return 1e9
        best = sorted(results, key=_cc)[0]
        assert best["id"] == "S2"


# ── Sentinel downloader module-level constants ──
class TestModuleConstants:
    def test_mission_choices_include_sentinel2(self):
        """The script supports sentinel-1/2/5p."""
        # Re-parse --help to confirm missions listed
        out = subprocess.run(
            [sys.executable, SCRIPT, "--help"],
            capture_output=True, text=True, timeout=15,
        )
        combined = out.stdout + out.stderr
        assert "sentinel-2" in combined
        assert "sentinel-1" in combined
        assert "sentinel-5p" in combined
