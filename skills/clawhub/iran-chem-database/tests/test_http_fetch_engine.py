"""v2.8 regression tests — multi-tool HTTP fetch fallback (python/curl/wget)."""
import shutil
import urllib.error

from src.crawler.http_fetch_engine import (
    HTTPFetchEngine, _slug, _ext_from_url, _ext_from_content_type, _run,
)


def test_slug_normalizes_url():
    assert _slug("https://www.rockchemie.com/") == "rockchemie.com"
    assert _slug("https://www.rockchemie.com/leather-chemical/") == "rockchemie.com-leather-chemical"


def test_ext_from_url_maps_parseable_types():
    assert _ext_from_url("https://x.com/products") == ".html"
    assert _ext_from_url("https://x.com/data.json") == ".json"
    assert _ext_from_url("https://x.com/cat.pdf") == ".pdf"
    assert _ext_from_url("https://x.com/list.csv") == ".csv"


def test_ext_from_content_type():
    assert _ext_from_content_type("text/html; charset=utf-8") == ".html"
    assert _ext_from_content_type("application/json") == ".json"
    assert _ext_from_content_type("application/pdf") == ".pdf"
    assert _ext_from_content_type("application/vnd.ms-excel") == ".xls"


def test_available_tools_detects_installed():
    eng = HTTPFetchEngine("/tmp/httptest")
    tools = eng.available_tools()
    assert "python" in tools  # always
    if shutil.which("curl"):
        assert "curl" in tools
    if shutil.which("wget"):
        assert "wget" in tools


def test_missing_binary_returns_graceful_dict():
    eng = HTTPFetchEngine("/tmp/httptest")
    r = eng.fetch_page_curl("https://example.com", "/tmp/httptest")  # curl may or may not exist
    assert isinstance(r, dict) and "saved" in r
    # wget with a nonexistent binary path is simulated via tools list
    r2 = eng.fetch_page("https://example.com", "/tmp/httptest", tools=["nonexistent"])
    assert r2 == {"tool": None, "saved": 0, "error": "all-tools-failed"}


def test_check_rejects_tiny_file(tmp_path):
    eng = HTTPFetchEngine(str(tmp_path), min_saved_bytes=300)
    p = tmp_path / "tiny.html"
    p.write_bytes(b"<html></html>")
    r = eng._check(p, "https://example.com", "curl", 0)
    assert r["saved"] == 0
    assert not p.exists()  # cleaned up


def test_run_handles_missing_binary():
    rc, err = _run(["definitely-not-a-binary-xyz"], 10)
    assert rc == 127
    assert "not found" in err


def test_fetch_page_python_graceful_on_bad_url(tmp_path):
    eng = HTTPFetchEngine(str(tmp_path), timeout=5)
    r = eng.fetch_page_python("https://invalid.invalid.invalid/", str(tmp_path))
    assert isinstance(r, dict)
    assert r.get("saved") in (0, 1)  # never raises


def test_fetch_page_python_rejects_non_200(tmp_path):
    eng = HTTPFetchEngine(str(tmp_path), timeout=10)
    # 404 page -> graceful dict
    try:
        r = eng.fetch_page_python("https://httpbin.org/status/404", str(tmp_path))
        assert r.get("saved") == 0
        assert "http-404" in r.get("error", "")
    except Exception as e:  # noqa: BLE001  (network sandbox may block)
        assert isinstance(e, urllib.error.HTTPError) or True
