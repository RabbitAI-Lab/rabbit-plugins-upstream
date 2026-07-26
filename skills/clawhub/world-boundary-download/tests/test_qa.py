"""Tests for the --qa sidecar summary (Phase 5 optimization)."""

from __future__ import annotations

import json
import os
import sys
from pathlib import Path
from unittest import mock

import pytest

SCRIPTS_DIR = Path(__file__).resolve().parent.parent / "scripts"
if str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))

import world_admin_download  # noqa: E402


def test_write_qa_summary_writes_json(tmp_path: Path):
    """write_qa_summary should write a JSON sidecar with key fields."""
    qa_path = str(tmp_path / "run.qa.json")
    args = mock.Mock()
    args.iso = "CHN"
    args.name = None
    args.level = "ADM1"
    args.format = "shp"
    args.source = "geoboundaries"
    args.simplified = False
    args.bbox = None
    args.isos = None
    args.out = None
    args.expand_km = 0.0
    args.no_cache = False
    payload = {
        "ok": True,
        "saved": str(tmp_path / "out.shp"),
        "size_bytes": 1024,
        "format": "shp",
        "iso3": "CHN",
        "level": "ADM1",
        "source": "geoboundaries",
    }
    world_admin_download.write_qa_summary(
        qa_path=qa_path,
        skill="world-boundary-download",
        command="country",
        args=args,
        payload=payload,
    )
    assert os.path.exists(qa_path)
    data = json.loads(Path(qa_path).read_text(encoding="utf-8"))
    assert data["skill"] == "world-boundary-download"
    assert data["command"] == "country"
    assert data["iso3"] == "CHN"
    assert data["level"] == "ADM1"
    assert data["source"] == "geoboundaries"
    assert data["size_bytes"] == 1024
    assert data["saved"].endswith("out.shp")
    assert "timestamp" in data
    assert "version" in data
    # Echoed input flags
    assert data["iso"] == "CHN"
    assert data["format"] == "shp"


def test_write_qa_summary_creates_parent_dirs(tmp_path: Path):
    """write_qa_summary should create parent directories if missing."""
    qa_path = str(tmp_path / "nested" / "subdir" / "run.qa.json")
    args = mock.Mock(spec=["qa"])
    args.qa = qa_path
    world_admin_download.write_qa_summary(
        qa_path=qa_path,
        skill="world-boundary-download",
        command="region",
        args=args,
        payload={"ok": True},
    )
    assert os.path.exists(qa_path)


def test_country_parser_accepts_qa_flag():
    """The country subcommand should accept --qa."""
    parser = world_admin_download.build_parser()
    ns = parser.parse_args(
        ["country", "--iso", "CHN", "--level", "ADM1", "--qa", "out.qa.json"]
    )
    assert ns.qa == "out.qa.json"
    assert ns.iso == "CHN"
    assert ns.level == "ADM1"
    assert ns.cmd == "country"


def test_region_parser_accepts_qa_flag():
    """The region subcommand should accept --qa."""
    parser = world_admin_download.build_parser()
    ns = parser.parse_args(
        [
            "region",
            "--iso",
            "USA",
            "--level",
            "ADM2",
            "--bbox",
            "100,24,120,49",
            "--qa",
            "out.qa.json",
        ]
    )
    assert ns.qa == "out.qa.json"
    assert ns.bbox == "100,24,120,49"


def test_multi_parser_accepts_qa_flag():
    """The multi subcommand should accept --qa."""
    parser = world_admin_download.build_parser()
    ns = parser.parse_args(
        ["multi", "--isos", "CHN,USA,JPN", "--level", "ADM0", "--qa", "out.qa.json"]
    )
    assert ns.qa == "out.qa.json"
    assert ns.isos == "CHN,USA,JPN"


def test_all_levels_parser_accepts_qa_flag():
    """The all-levels subcommand should accept --qa."""
    parser = world_admin_download.build_parser()
    ns = parser.parse_args(
        ["all-levels", "--iso", "FRA", "--qa", "out.qa.json"]
    )
    assert ns.qa == "out.qa.json"
    assert ns.iso == "FRA"


def test_country_without_qa_does_not_write_file(tmp_path: Path):
    """When --qa is not given, no sidecar file should be written.

    We mock the heavy `sources.fetch` + `fmt_mod.convert` to keep this fast.
    """
    from core import sources, format as fmt_mod

    fake_input = tmp_path / "fake.shp.zip"
    fake_input.write_bytes(b"PK\x03\x04fake")
    fake_output = tmp_path / "out.shp.zip"
    fake_output.write_bytes(b"PK\x03\x04out")

    # Build a fake "result" object
    class _Result:
        path = fake_input
        source = "geoboundaries"

    with mock.patch.object(sources, "fetch", return_value=_Result()), \
         mock.patch.object(fmt_mod, "convert", return_value=fake_output):
        from world_admin_download import cmd_country
        args = mock.Mock()
        args.iso = "CHN"
        args.name = None
        args.level = "ADM0"
        args.format = "shp"
        args.source = "geoboundaries"
        args.simplified = False
        args.out = None
        args.qa = None
        args.plain = False
        args.no_cache = False
        args.cache_dir = None
        args.expand_km = 0.0
        args.isos = None
        args.bbox = None
        ret = cmd_country(args)
    assert ret == 0
    # No sidecar
    assert not (tmp_path / "run.qa.json").exists()


def test_country_with_qa_writes_sidecar(tmp_path: Path):
    """When --qa is given, cmd_country should write the sidecar JSON."""
    from core import sources, format as fmt_mod

    fake_input = tmp_path / "fake.shp.zip"
    fake_input.write_bytes(b"PK\x03\x04fake")
    fake_output = tmp_path / "out.shp.zip"
    fake_output.write_bytes(b"PK\x03\x04out")
    qa_path = tmp_path / "out.qa.json"

    class _Result:
        path = fake_input
        source = "geoboundaries"

    with mock.patch.object(sources, "fetch", return_value=_Result()), \
         mock.patch.object(fmt_mod, "convert", return_value=fake_output):
        from world_admin_download import cmd_country
        args = mock.Mock()
        args.iso = "CHN"
        args.name = None
        args.level = "ADM0"
        args.format = "shp"
        args.source = "geoboundaries"
        args.simplified = False
        args.out = None
        args.qa = str(qa_path)
        args.plain = False
        args.no_cache = False
        args.cache_dir = None
        args.expand_km = 0.0
        args.isos = None
        args.bbox = None
        ret = cmd_country(args)
    assert ret == 0
    assert qa_path.exists()
    data = json.loads(qa_path.read_text(encoding="utf-8"))
    assert data["skill"] == "world-boundary-download"
    assert data["command"] == "country"
    assert data["iso3"] == "CHN"
    assert data["level"] == "ADM0"
    assert data["source"] == "geoboundaries"
    assert "timestamp" in data
