"""Tests for the on-disk HTTP cache."""

from __future__ import annotations

import os
from pathlib import Path

import pytest

from core import cache as cache_mod


class TestHttpCache:
    def test_put_and_get(self, tmp_path: Path):
        c = cache_mod.HttpCache(tmp_path)
        c.put("https://example.com/a.bin", b"hello world")
        assert c.has("https://example.com/a.bin")
        assert c.get_bytes("https://example.com/a.bin") == b"hello world"

    def test_key_deterministic(self, tmp_path: Path):
        c = cache_mod.HttpCache(tmp_path)
        k1 = c.key_for("https://x.com/y?z=1")
        k2 = c.key_for("https://x.com/y?z=1")
        assert k1 == k2
        assert len(k1) == 40  # SHA1 hex

    def test_different_urls_different_keys(self, tmp_path: Path):
        c = cache_mod.HttpCache(tmp_path)
        assert c.key_for("a") != c.key_for("b")

    def test_missing_returns_none(self, tmp_path: Path):
        c = cache_mod.HttpCache(tmp_path)
        assert c.get_path("nope") is None
        assert c.get_bytes("nope") is None
        assert not c.has("nope")

    def test_size_tracks_data(self, tmp_path: Path):
        c = cache_mod.HttpCache(tmp_path)
        c.put("u1", b"x" * 100)
        c.put("u2", b"y" * 250)
        assert c.size_bytes() == 350

    def test_clear(self, tmp_path: Path):
        c = cache_mod.HttpCache(tmp_path)
        c.put("u1", b"aaa")
        c.put("u2", b"bbb")
        n = c.clear()
        # At least the 2 .bin files.
        assert n >= 2
        assert c.size_bytes() == 0
        assert not c.has("u1")
        assert not c.has("u2")

    def test_persists_across_instances(self, tmp_path: Path):
        c1 = cache_mod.HttpCache(tmp_path)
        c1.put("u1", b"data")
        c2 = cache_mod.HttpCache(tmp_path)
        assert c2.has("u1")
        assert c2.get_bytes("u1") == b"data"

    def test_overwrite(self, tmp_path: Path):
        c = cache_mod.HttpCache(tmp_path)
        c.put("u1", b"first")
        c.put("u1", b"second")
        assert c.get_bytes("u1") == b"second"
