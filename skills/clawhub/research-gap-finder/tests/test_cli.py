#!/usr/bin/env python3
"""Offline regression, contract, and adversarial tests for the CLI."""
from __future__ import annotations

import contextlib
import io
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest import mock

ROOT = Path(__file__).resolve().parent.parent
CLI = ROOT / "scripts" / "research_gap_cli.py"
sys.path.insert(0, str(ROOT / "scripts"))
import research_gap_cli as rgc  # noqa: E402


def run_cli(*args: str) -> subprocess.CompletedProcess:
    return subprocess.run([sys.executable, str(CLI), *args], text=True,
                          capture_output=True, check=False)


def ns(**values):
    return SimpleNamespace(**values)


class ResearchGapCliTest(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp(prefix="rgf-test-"))
        self.proj = self.tmp / "proj"

    def init_project(self, topic="Test topic"):
        proc = run_cli("init", "--dir", str(self.proj), "--topic", topic,
                       "--pico", '{"population":"X"}')
        self.assertEqual(proc.returncode, 0, proc.stdout + proc.stderr)
        return proc

    def test_selftest_pipeline(self):
        proc = run_cli("selftest", "--dir", self.proj)
        self.assertEqual(proc.returncode, 0, proc.stdout + proc.stderr)
        self.assertIn("report ok=True", proc.stdout)

    def test_init_and_machine_readable_status(self):
        self.init_project()
        status = run_cli("status", "--dir", str(self.proj), "--json")
        self.assertEqual(status.returncode, 0, status.stdout + status.stderr)
        data = json.loads(status.stdout)
        self.assertEqual(data["schema_version"], rgc.SCHEMA_VERSION)
        self.assertEqual(data["topic"], "Test topic")
        self.assertTrue((self.proj / "evidence.json").is_file())
        self.assertTrue((self.proj / "gaps.json").is_file())

    def test_taxonomy_classifier_is_deterministic(self):
        first = rgc.classify_type("No studies exist in elderly rural populations; the mechanism remains unclear.")
        second = rgc.classify_type("No studies exist in elderly rural populations; the mechanism remains unclear.")
        self.assertEqual(first, second)
        self.assertIn(first[0], {"population", "theoretical", "evidence"})

    def test_config_engine_list_is_usable_without_split_bug(self):
        self.init_project()
        config = json.loads((self.proj / "config.json").read_text())
        config["engines"] = ["openalex"]
        (self.proj / "config.json").write_text(json.dumps(config))
        fake = [{"id": "W1", "title": "A study", "source": "openalex", "source_id": "W1",
                 "doi": "10.1234/example", "url": "https://example.invalid/W1",
                 "authors": [], "abstract": "", "cited_by": 0, "journal": ""}]
        args = ns(dir=str(self.proj), query="topic", engines=None, limit=None, years=None, json=True)
        with mock.patch.dict(rgc.ENGINES, {"openalex": lambda *unused: fake}), contextlib.redirect_stdout(io.StringIO()) as output:
            code = rgc.run_search(args)
        self.assertEqual(code, 0)
        result = json.loads(output.getvalue())
        self.assertEqual(result["new_records"], 1)
        self.assertEqual(len(rgc.load_papers(self.proj)), 1)

    def test_semantic_scholar_engine_parses_metadata(self):
        payload = {"data": [{"paperId": "s2-1", "title": "Semantic result", "authors": [{"name": "A"}],
                              "year": 2022, "externalIds": {"DOI": "10.1000/sem"},
                              "url": "https://semanticscholar.org/paper/s2-1", "abstract": "Abstract",
                              "citationCount": 4, "venue": "Journal"}]}
        with mock.patch.object(rgc, "api_get_json", return_value=payload):
            papers = rgc.engine_semantic(self.proj, "topic", 5, [2020, 2023], rgc.RateLimiter(0))
        self.assertEqual(len(papers), 1)
        self.assertEqual(papers[0]["doi"], "10.1000/sem")
        self.assertEqual(rgc.paper_identifier(papers[0]), "10.1000/sem")

    def test_openalex_uses_current_filter_and_supported_page_bound(self):
        captured = {}
        def fake_get(url, project):
            captured["url"] = url
            return {"results": []}
        with mock.patch.object(rgc, "api_get_json", side_effect=fake_get):
            rgc.engine_openalex(self.proj, "topic", 1000, [2020, 2024], rgc.RateLimiter(0))
        self.assertIn("per_page=100", captured["url"])
        self.assertIn("from_publication_date%3A2020-01-01", captured["url"])
        self.assertIn("to_publication_date%3A2024-12-31", captured["url"])
        self.assertNotIn("from_publication_date=", captured["url"])

    def test_pubmed_open_ended_year_filter_is_valid(self):
        self.assertIn("2020/01/01:3000/12/31[dp]", rgc._pubmed_term("topic", [2020, None]))
        self.assertIn("1/01/01:2024/12/31[dp]", rgc._pubmed_term("topic", [None, 2024]))

    def test_cache_flag_is_dynamic_and_corrupt_cache_is_refetched(self):
        url = "https://api.openalex.org/works?search=cache-test"
        cache = rgc._cache_path(self.proj, url)
        cache.parent.mkdir(parents=True)
        cache.write_text("{not-json")
        original = rgc.USE_CACHE
        try:
            rgc.USE_CACHE = False
            with mock.patch.object(rgc, "_http_json", return_value={"fresh": True}) as request:
                data = rgc.api_get_json(url, self.proj)
            self.assertEqual(data, {"fresh": True})
            self.assertEqual(request.call_count, 1)
        finally:
            rgc.USE_CACHE = original

    def test_bounded_response_rejects_large_content_length(self):
        class Response:
            headers = {"Content-Length": str(rgc.MAX_RESPONSE_BYTES + 1)}
        with self.assertRaises(ValueError):
            rgc._read_bounded(Response())

    def test_csv_exports_neutralize_formula_prefixes(self):
        for prefix in ("=", "+", "-", "@"):
            self.assertEqual(rgc.safe_csv_cell("  " + prefix + "SUM(1,1)")[0], "'")
        self.assertEqual(rgc.safe_csv_cell("ordinary text"), "ordinary text")
        rgc.save_papers(self.proj, [rgc.emit_paper("openalex", "W3", "=HYPERLINK(1)", [], 2023, "", "https://x")])
        csv_text = (self.proj / "evidence_matrix.csv").read_text()
        self.assertIn("'=HYPERLINK(1)", csv_text)

    def test_rate_limit_retries_then_succeeds(self):
        from urllib.error import HTTPError
        throttled = HTTPError("https://api.example.invalid", 429, "busy", {"Retry-After": "0"}, None)
        with mock.patch.object(rgc, "_http_json", side_effect=[throttled, {"ok": True}]), \
             mock.patch.object(rgc.time, "sleep"):
            self.assertEqual(rgc.api_get_json("https://api.openalex.org/works?retry=1", self.proj, use_cache=False), {"ok": True})

    def test_malformed_arxiv_xml_is_rejected_without_execution(self):
        with mock.patch.object(rgc, "api_get_text", return_value="<feed><entry>"):
            with self.assertRaises(ValueError):
                rgc.engine_arxiv(self.proj, "topic", 1, [None, None], rgc.RateLimiter(0))

    def test_offline_engine_failure_is_transparent_and_non_destructive(self):
        self.init_project()
        args = ns(dir=str(self.proj), query="topic", engines="openalex", limit=1, years=None, json=True)
        fake_engine = mock.Mock(side_effect=OSError("offline"))
        with mock.patch.dict(rgc.ENGINES, {"openalex": fake_engine}), \
             contextlib.redirect_stdout(io.StringIO()) as output:
            code = rgc.run_search(args)
        self.assertEqual(code, 2)
        result = json.loads(output.getvalue())
        self.assertEqual(result["failed_engines"], ["openalex"])
        self.assertEqual(rgc.load_papers(self.proj), [])

    def test_dedupe_merges_duplicate_identifier_and_provenance(self):
        a = rgc.emit_paper("openalex", "W1", "A Study", ["A"], 2020, "10.1000/DUP", "https://a")
        b = rgc.emit_paper("crossref", "10.1000/dup", "A Study", ["B"], 2020, "10.1000/dup", "https://b")
        a["provenance"] = [{"engine": "openalex", "identifier": "10.1000/dup"}]
        b["provenance"] = [{"engine": "crossref", "identifier": "10.1000/dup"}]
        merged = rgc.dedupe_papers([a, b])
        self.assertEqual(len(merged), 1)
        self.assertEqual(set(merged[0]["sources"]), {"openalex", "crossref"})
        self.assertEqual(len(merged[0]["provenance"]), 2)

    def test_custom_cuefile_is_executable_and_project_relative(self):
        self.init_project()
        rgc.save_papers(self.proj, [rgc.emit_paper("openalex", "W2", "Title", [], 2022, "10.1000/cue", "https://x",
                                                    "The intervention was not evaluated in primary care.")])
        cuefile = self.proj / "cues.json"
        cuefile.write_text(json.dumps({"cues": ["not evaluated in primary care"]}))
        args = ns(dir=str(self.proj), cuefile="cues.json")
        gaps = rgc.bootstrap_extract(rgc.ensure_project(args), args)
        self.assertTrue(gaps)
        self.assertIn("not evaluated", gaps[0]["statement"])
        with self.assertRaises(ValueError):
            rgc._load_cues(self.proj, "../outside.json")

    def test_validation_confidence_requires_two_independent_resolved_sources(self):
        self.init_project()
        gap = {"id": "gap-1", "statement": "A limitation", "sources": ["10.1000/a", "PMID:123"],
               "source_provenance": [{"source": "crossref"}, {"source": "pubmed"}],
               "importance": {}, "confidence": "", "secondary_type": []}
        rgc.save_gaps(self.proj, [gap])
        args = ns(dir=str(self.proj), check_web=True, json=True)
        with mock.patch.object(rgc, "resolve_citation", return_value=True):
            with contextlib.redirect_stdout(io.StringIO()) as output:
                code = rgc.run_validate(args)
        self.assertEqual(code, 0)
        self.assertEqual(rgc.load_gaps(self.proj)[0]["confidence"], "High")
        self.assertEqual(json.loads(output.getvalue())["validated"], 1)

    def test_invalid_identifier_becomes_exploratory(self):
        self.init_project()
        gap = {"id": "gap-2", "statement": "No evidence", "sources": ["invented citation"],
               "importance": {}, "confidence": "", "secondary_type": []}
        rgc.save_gaps(self.proj, [gap])
        args = ns(dir=str(self.proj), check_web=False, json=False)
        rgc.run_validate(args)
        checked = rgc.load_gaps(self.proj)[0]
        self.assertEqual(checked["confidence"], "Low")
        self.assertTrue(checked["exploratory"])
        report = ns(dir=str(self.proj), top=8, out=None)
        rgc.run_report(report)
        self.assertIn("EXPLORATORY/HYPOTHETICAL", (self.proj / "report.md").read_text())

    def test_safe_report_output_rejects_escape(self):
        self.init_project()
        args = ns(dir=str(self.proj), top=8, out="../escape.md")
        with self.assertRaises(ValueError):
            rgc.run_report(args)

    def test_corrupt_config_fails_closed(self):
        self.init_project()
        (self.proj / "config.json").write_text("not json")
        proc = run_cli("status", "--dir", str(self.proj))
        self.assertEqual(proc.returncode, 1)
        self.assertIn("invalid JSON", proc.stderr)
        self.assertEqual((self.proj / "config.json").read_text(), "not json")

    def test_unknown_engine_json_search_has_explicit_exit_and_contract(self):
        self.init_project()
        proc = run_cli("search", "--dir", str(self.proj), "--engines", "unknown", "--json")
        self.assertEqual(proc.returncode, 2)
        result = json.loads(proc.stdout)
        self.assertEqual(result["failed_engines"], ["unknown"])
        self.assertEqual(result["schema_version"], rgc.SCHEMA_VERSION)

    def test_rank_top_zero_is_respected(self):
        self.init_project()
        gap = {"id": "gap-1", "statement": "A", "sources": [], "importance": {"total": 15},
               "confidence": "High", "secondary_type": []}
        rgc.save_gaps(self.proj, [gap])
        args = ns(dir=str(self.proj), min_total=None, min_confidence=None, top=0, json=True)
        with contextlib.redirect_stdout(io.StringIO()) as output:
            rgc.run_rank(args)
        self.assertEqual(json.loads(output.getvalue())["gaps"], [])


if __name__ == "__main__":
    unittest.main(verbosity=2)
