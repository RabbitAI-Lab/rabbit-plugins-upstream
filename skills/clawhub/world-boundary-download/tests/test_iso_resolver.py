"""Unit tests for the ISO / country name resolver.

These tests are pure-Python: no network access, no downloads.
"""

from __future__ import annotations

import pytest

from core.iso_resolver import resolve, search, get_display
from core.exceptions import ResolutionError


class TestResolve:
    def test_iso3(self):
        m = resolve("CHN")
        assert m.iso3 == "CHN"
        assert m.iso2 == "CN"
        assert m.score == 1.0

    def test_iso2(self):
        m = resolve("JP")
        assert m.iso3 == "JPN"

    def test_chinese_short_name_china(self):
        m = resolve("中国")
        assert m.iso3 == "CHN"
        assert m.name_en == "China"

    def test_chinese_short_name_usa(self):
        m = resolve("美国")
        assert m.iso3 == "USA"

    def test_chinese_short_name_uk(self):
        m = resolve("英国")
        assert m.iso3 == "GBR"

    def test_chinese_short_name_japan(self):
        m = resolve("日本")
        assert m.iso3 == "JPN"

    def test_chinese_short_name_russia(self):
        m = resolve("俄罗斯")
        assert m.iso3 == "RUS"

    def test_chinese_alias_prc(self):
        m = resolve("中华人民共和国")
        assert m.iso3 == "CHN"

    def test_chinese_alias_hk(self):
        m = resolve("中国香港")
        assert m.iso3 == "HKG"
        m = resolve("香港")
        assert m.iso3 == "HKG"

    def test_chinese_alias_taiwan(self):
        m = resolve("中国台湾")
        assert m.iso3 == "TWN"
        m = resolve("台湾")
        assert m.iso3 == "TWN"

    def test_english_name(self):
        m = resolve("United States")
        assert m.iso3 == "USA"
        m = resolve("Brazil")
        assert m.iso3 == "BRA"

    def test_partial_chinese(self):
        # Partial alias like 美利坚 should still hit USA via the alias table.
        m = resolve("美利坚")
        assert m.iso3 == "USA"

    def test_partial_english(self):
        # "United" alone should still match the United States.
        m = resolve("United")
        assert m.iso3 == "USA"

    def test_fuzzy_fallback(self):
        # A misspelled name should fall back to fuzzy.
        m = resolve("Inda")  # close to "India"
        # We don't require an exact match here, but a result should be returned.
        assert m.iso3 in ("IND",)

    def test_unknown_raises(self):
        with pytest.raises(ResolutionError):
            resolve("Atlantis")

    def test_empty_raises(self):
        with pytest.raises(ResolutionError):
            resolve("")

    def test_case_insensitive(self):
        m1 = resolve("chn")
        m2 = resolve("CHN")
        assert m1.iso3 == m2.iso3


class TestSearch:
    def test_returns_at_least_one(self):
        out = search("China", limit=5)
        assert len(out) > 0
        assert out[0].iso3 == "CHN"

    def test_chinese_search(self):
        out = search("日本", limit=5)
        # At least one of the top hits should be JPN.
        assert any(m.iso3 == "JPN" for m in out)

    def test_empty_returns_all_or_empty(self):
        # Empty keyword should not crash.
        out = search("", limit=5)
        assert isinstance(out, list)


class TestGetDisplay:
    def test_known(self):
        m = get_display("FRA")
        assert m.iso3 == "FRA"
        assert m.name_en == "France"

    def test_unknown_raises(self):
        with pytest.raises(ResolutionError):
            get_display("XYZ")
