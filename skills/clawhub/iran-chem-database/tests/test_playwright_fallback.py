"""Tests for Playwright fallback path-conversion + graceful absence."""
import pytest

from src.crawler.playwright_fallback import PlaywrightFallbackEngine


def test_url_to_mirror_path_page():
    engine = PlaywrightFallbackEngine("/tmp/m")
    p = engine.url_to_mirror_path("https://acme.ir/catalog/page.html", "/tmp/m/acme")
    assert str(p).endswith("acme.ir/catalog/page.html")


def test_url_to_mirror_path_index():
    engine = PlaywrightFallbackEngine("/tmp/m")
    p = engine.url_to_mirror_path("https://acme.ir/catalog/", "/tmp/m/acme")
    assert str(p).endswith("acme.ir/catalog/index.html")


def test_absent_playwright_returns_error():
    engine = PlaywrightFallbackEngine("/tmp/m")

    class FakeConfig:
        user_agent = "test"
        output_dir = "/tmp/m/acme"

    result = engine.render_and_save(FakeConfig(), ["https://example.com"])
    # Either it rendered (playwright installed) or it reported the missing dep.
    assert "rendered" in result or "error" in result
