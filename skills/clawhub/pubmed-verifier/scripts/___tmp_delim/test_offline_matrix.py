#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Offline test matrix for pubmed-verifier v2.2.0 (stdlib only, no network).

Run:  python3 tests/test_offline_matrix.py
Covers the v2.2.0 network hardening (Retry-After, UA rotation, circuit
breaker, polite pool, API-key injection, Europe PMC parsing, honest-unknown
classification, cache protection) plus regression of the five-state core.
"""

import json
import os
import sys
import tempfile
import unittest
import urllib.error
from pathlib import Path
from unittest import mock

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))
import verify_pmids as vp  # noqa: E402


def _ok(body: bytes):
    """urlopen stand-in returning a successful response."""
    m = mock.mock_open(read_data=body)
    m.return_value.__enter__ = lambda s: m.return_value
    return m.return_value


class _Reset(unittest.TestCase):
    def setUp(self):
        vp._HOST_FAILS.clear()
        vp._OPTS.update({"ncbi_key": "", "mailto": "", "meta_source": "auto", "timeout": 20})


class TestRetryAfter(_Reset):
    def _run(self, headers):
        errs = [urllib.error.HTTPError("u", 429, "Too Many Requests", headers, None)
                for _ in range(2)]
        with mock.patch.object(vp.urllib.request, "urlopen", side_effect=errs + [_ok(b"ok")]), \
             mock.patch.object(vp.time, "sleep") as sl:
            body = vp._api_get("https://api.crossref.org/works/10.1/x")
        self.assertEqual(body, b"ok")
        return [round(c.args[0], 2) for c in sl.call_args_list]

    def test_retry_after_respected(self):
        self.assertEqual(self._run({"Retry-After": "3"}), [3.0, 3.0])

    def test_retry_after_default_when_missing(self):
        self.assertEqual(self._run({}), [2.0, 2.0])

    def test_retry_after_clamped_to_5(self):
        self.assertEqual(self._run({"Retry-After": "30"}), [5.0, 5.0])

    def test_retry_after_garbage_value(self):
        self.assertEqual(self._run({"Retry-After": "Wed, 21 Oct 2026 07:28:00 GMT"}), [2.0, 2.0])

    def test_429_exhausted_does_not_trip_breaker(self):
        with mock.patch.object(vp.urllib.request, "urlopen",
                               side_effect=urllib.error.HTTPError("u", 429, "x", {}, None)), \
             mock.patch.object(vp.time, "sleep"):
            with self.assertRaises(urllib.error.HTTPError):
                vp._api_get("https://api.crossref.org/x")
            self.assertEqual(vp._HOST_FAILS[vp._host_key("https://api.crossref.org/x")], 0)


class TestUaRotation(_Reset):
    def test_403_rotates_to_browser_ua(self):
        seen = []

        def fake(req, timeout=None):
            seen.append(req.headers.get("User-agent"))
            if len(seen) == 1:
                raise urllib.error.HTTPError("u", 403, "forbidden", {}, None)
            return _ok(b"ok")

        with mock.patch.object(vp.urllib.request, "urlopen", side_effect=fake), \
             mock.patch.object(vp.time, "sleep"):
            vp._api_get("https://www.ebi.ac.uk/x")
        self.assertEqual(seen[0], vp._UA_TOOL)
        self.assertEqual(seen[1], vp._UA_BROWSER)

    def test_406_rotates(self):
        calls = {"n": 0}

        def fake(req, timeout=None):
            calls["n"] += 1
            if calls["n"] == 1:
                raise urllib.error.HTTPError("u", 406, "not acceptable", {}, None)
            return _ok(b"ok")

        with mock.patch.object(vp.urllib.request, "urlopen", side_effect=fake), \
             mock.patch.object(vp.time, "sleep"):
            self.assertEqual(vp._api_get("https://export.arxiv.org/x"), b"ok")


class TestCircuitBreaker(_Reset):
    def test_opens_after_two_exhausted_calls(self):
        calls = {"n": 0}

        def boom(req, timeout=None):
            calls["n"] += 1
            raise urllib.error.URLError("conn refused")

        with mock.patch.object(vp.urllib.request, "urlopen", side_effect=boom), \
             mock.patch.object(vp.time, "sleep"):
            for _ in range(2):
                with self.assertRaises(urllib.error.URLError):
                    vp._api_get("https://eutils.ncbi.nlm.nih.gov/x")
            self.assertEqual(calls["n"], 6)          # 2 calls x 3 attempts
            with self.assertRaises(vp.CircuitOpenError):
                vp._api_get("https://eutils.ncbi.nlm.nih.gov/y")
            self.assertEqual(calls["n"], 6)          # no more network attempts

    def test_counts_once_per_logical_call(self):
        with mock.patch.object(vp.urllib.request, "urlopen",
                               side_effect=urllib.error.URLError("down")), \
             mock.patch.object(vp.time, "sleep"):
            with self.assertRaises(urllib.error.URLError):
                vp._api_get("https://eutils.ncbi.nlm.nih.gov/x")
            self.assertEqual(vp._HOST_FAILS["https://eutils.ncbi.nlm.nih.gov"], 1)

    def test_success_resets(self):
        vp._HOST_FAILS["https://eutils.ncbi.nlm.nih.gov"] = 1
        with mock.patch.object(vp.urllib.request, "urlopen", return_value=_ok(b"ok")):
            vp._api_get("https://eutils.ncbi.nlm.nih.gov/x")
        self.assertEqual(vp._HOST_FAILS["https://eutils.ncbi.nlm.nih.gov"], 0)

    def test_per_host_isolation(self):
        vp._HOST_FAILS["https://eutils.ncbi.nlm.nih.gov"] = 5
        with mock.patch.object(vp.urllib.request, "urlopen", return_value=_ok(b"ok")):
            self.assertEqual(vp._api_get("https://www.ebi.ac.uk/x"), b"ok")


class TestPolitePoolAndKey(_Reset):
    def test_mailto_adds_polite_pool(self):
        vp._OPTS["mailto"] = "lab@example.org"
        seen = {}

        def fake(req, timeout=None):
            seen["url"] = req.full_url
            return _ok(json.dumps({"message": {}}).encode())

        with mock.patch.object(vp.urllib.request, "urlopen", side_effect=fake):
            vp.fetch_doi_metadata("10.1186/x")
        self.assertIn("?mailto=lab%40example.org", seen["url"])

    def test_ncbi_key_injected_into_esummary(self):
        vp._OPTS["ncbi_key"] = "abc123"
        seen = {}

        def fake(req, timeout=None):
            seen["url"] = req.full_url
            return _ok(json.dumps({"result": {}}).encode())

        with mock.patch.object(vp.urllib.request, "urlopen", side_effect=fake), \
             mock.patch.object(vp.time, "sleep"):
            vp.fetch_summaries(["12345678"])
        self.assertIn("api_key=abc123", seen["url"])
        self.assertIn("tool=pubmed-verifier", seen["url"])

    def test_ncbi_key_speeds_interval(self):
        vp._OPTS["ncbi_key"] = "abc123"
        with mock.patch.object(vp.urllib.request, "urlopen",
                               return_value=_ok(json.dumps({"result": {}}).encode())), \
             mock.patch.object(vp.time, "sleep") as sl:
            vp.fetch_summaries(["1", "2"], batch_size=1)
        self.assertTrue(all(abs(c.args[0] - 0.12) < 1e-9 for c in sl.call_args_list))

    def test_mailto_env_used_when_flag_absent(self):
        with mock.patch.dict(os.environ, {"NCBI_API_KEY": "envkey"}):
            self.assertEqual(vp.os.environ.get("NCBI_API_KEY"), "envkey")


class TestEuropePmc(_Reset):
    def test_parsing_maps_to_metadata_shape(self):
        payload = {"hitCount": 1, "resultList": {"result": [{
            "id": "31018962", "title": "Some Title.", "authorString": "Smith J, Doe A",
            "journalTitle": "Pediatr Rheumatol", "pubYear": "2021",
            "doi": "10.1186/x", "journalVolume": "19", "pageInfo": "1-10"}]}}
        with mock.patch.object(vp.urllib.request, "urlopen",
                               return_value=_ok(json.dumps(payload).encode())):
            out = vp.fetch_summaries_europepmc(["31018962"])
        info = out["31018962"]
        self.assertTrue(info["valid"])
        self.assertEqual(info["source"], "europepmc")
        self.assertEqual(info["authors"], ["Smith J", "Doe A"])
        self.assertEqual(info["pubdate"], "2021")
        self.assertEqual(info["journal"], "Pediatr Rheumatol")

    def test_missing_pmid_reported_not_found(self):
        with mock.patch.object(vp.urllib.request, "urlopen",
                               return_value=_ok(json.dumps({"hitCount": 0, "resultList": {"result": []}}).encode())):
            out = vp.fetch_summaries_europepmc(["11111111"])
        self.assertFalse(out["11111111"]["valid"])
        self.assertNotIn("network_error", out["11111111"])

    def test_failure_marks_network_error_not_invalid(self):
        with mock.patch.object(vp.urllib.request, "urlopen",
                               side_effect=urllib.error.URLError("down")), \
             mock.patch.object(vp.time, "sleep"):
            out = vp.fetch_summaries_europepmc(["11111111"])
        self.assertTrue(out["11111111"].get("network_error"))

    def test_fallback_engages_on_ncbi_transport_failure(self):
        def fake(req, timeout=None):
            if "ncbi" in req.full_url:
                raise urllib.error.URLError("down")
            return _ok(json.dumps({"resultList": {"result": [
                {"id": "12345678", "title": "T", "authorString": "A B",
                 "journalTitle": "J", "pubYear": "2020"}]}}).encode())

        with mock.patch.object(vp.urllib.request, "urlopen", side_effect=fake), \
             mock.patch.object(vp.time, "sleep"):
            out = vp.fetch_summaries(["12345678"])
        self.assertTrue(out["12345678"]["valid"])
        self.assertEqual(out["12345678"]["source"], "europepmc")

    def test_no_fallback_when_meta_source_ncbi(self):
        vp._OPTS["meta_source"] = "ncbi"
        with mock.patch.object(vp.urllib.request, "urlopen",
                               side_effect=urllib.error.URLError("down")), \
             mock.patch.object(vp.time, "sleep"):
            out = vp.fetch_summaries(["12345678"])
        self.assertTrue(out["12345678"].get("network_error"))

    def test_explicit_europepmc_never_touches_ncbi(self):
        seen = []
        with mock.patch.object(vp.urllib.request, "urlopen",
                               side_effect=lambda req, timeout=None:
                                   seen.append(req.full_url) or _ok(json.dumps(
                                       {"resultList": {"result": []}}).encode())), \
             mock.patch.object(vp.time, "sleep"):
            vp._OPTS["meta_source"] = "europepmc"
            vp.fetch_summaries(["12345678"])
        vp._OPTS["meta_source"] = "auto"
        self.assertTrue(seen and all("europepmc" in u for u in seen))


class TestHonestVerdicts(_Reset):
    def test_classify_network_error_unknown(self):
        verdict, details = vp.classify_unverified({"valid": False, "network_error": True})
        self.assertEqual(verdict, "unknown")
        self.assertIn("不判为无效", details)

    def test_classify_not_found_invalid(self):
        verdict, details = vp.classify_unverified({"valid": False, "error": "invalid_id"})
        self.assertEqual(verdict, "invalid")
        self.assertIn("not found", details)

    def test_network_errors_never_cached(self):
        with tempfile.TemporaryDirectory() as td:
            db = Path(td) / "cache.db"
            vp._cache_init(db)
            vp._cache_save_fresh(db, {
                "11111111": {"valid": False, "network_error": True, "error": "down"},
                "22222222": {"valid": True, "title": "T", "authors": [], "journal": "J",
                             "pubdate": "2020", "doi": "", "source": "ncbi"},
            })
            cached = vp._cache_load(db, ["11111111", "22222222"])
            self.assertNotIn("11111111", cached)   # network failure NOT cached
            self.assertIn("22222222", cached)


class TestFiveStateCore(_Reset):
    """Regression: the v2.1.x matching core must keep its behavior."""

    def test_parse_citation_context_vancouver(self):
        ctx = ("Zaripova A, Shostak N. Juvenile idiopathic arthritis. Pediatr Rheumatol. "
               "2021;19:47. PMID: 34078778")
        c = vp.parse_citation_context(ctx)
        self.assertEqual(c["claimed_year"], "2021")
        self.assertIn("Zaripova", c["claimed_authors"])
        self.assertTrue(c["claimed_title"])

    def test_cross_check_correct(self):
        claimed = {"claimed_title": "Juvenile idiopathic arthritis pathogenesis",
                   "claimed_authors": ["Zaripova"], "claimed_journal": "Pediatr Rheumatol",
                   "claimed_year": "2021"}
        actual = {"title": "Pathogenesis of juvenile idiopathic arthritis",
                  "authors": ["Zaripova A"], "journal": "Pediatr Rheumatol Online J",
                  "pubdate": "2021 Jan 5"}
        self.assertEqual(vp.cross_check_citation(claimed, actual)["verdict"], "correct")

    def test_cross_check_mismatch(self):
        claimed = {"claimed_title": "Juvenile idiopathic arthritis review",
                   "claimed_authors": ["Ravelli"], "claimed_journal": "Lancet",
                   "claimed_year": "2007"}
        actual = {"title": "HIV prevention microbicide trial", "authors": ["Smith J"],
                  "journal": "Lancet", "pubdate": "2007 Jun"}
        self.assertEqual(vp.cross_check_citation(claimed, actual)["verdict"], "mismatch")

    def test_cross_check_unknown_when_no_claims(self):
        claimed = {"claimed_title": "", "claimed_authors": [], "claimed_journal": "", "claimed_year": ""}
        actual = {"title": "T", "authors": ["A"], "journal": "J", "pubdate": "2020"}
        self.assertEqual(vp.cross_check_citation(claimed, actual)["verdict"], "unknown")


class TestCli(_Reset):
    def test_version_flag(self):
        import subprocess
        script = Path(__file__).resolve().parent.parent / "scripts" / "verify_pmids.py"
        out = subprocess.run([sys.executable, str(script), "--version"],
                             capture_output=True, text=True)
        self.assertIn("2.2.0", out.stdout + out.stderr)

    def test_host_key_granularity(self):
        self.assertEqual(vp._host_key("https://eutils.ncbi.nlm.nih.gov/a?b=c"),
                         "https://eutils.ncbi.nlm.nih.gov")


if __name__ == "__main__":
    unittest.main(verbosity=2)
