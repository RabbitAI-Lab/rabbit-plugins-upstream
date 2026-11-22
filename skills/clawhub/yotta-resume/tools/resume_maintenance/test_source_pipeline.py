#!/usr/bin/env python3
"""Tests for source snapshots, candidate review, apply, and rollback."""

import json
import io
import shutil
import sys
import tempfile
import unittest
from contextlib import redirect_stderr, redirect_stdout
from pathlib import Path
from unittest import mock


HERE = Path(__file__).resolve().parent
SKILL_DIR = HERE.parents[1]
sys.path.insert(0, str(SKILL_DIR / "scripts"))
sys.path.insert(0, str(HERE))

import source_watch  # noqa: E402
import bank_pipeline  # noqa: E402
import yotta_resume_maintenance as ym  # noqa: E402


TODAY = "2026-11-24"
CONTENT_HASH = "a" * 64


class FakeResponse:
    def __init__(self, payload, status=200, url="https://owasp.org/Top10/"):
        self.status = status
        self._payload = payload
        self._url = url
        self.headers = {
            "Content-Length": str(len(payload)),
            "ETag": '"body"',
            "Last-Modified": "Mon, 23 Nov 2026 10:00:00 GMT",
        }

    def geturl(self):
        return self._url

    def read(self, limit):
        return self._payload[:limit]

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, traceback):
        return False


class FakeOpener:
    def __init__(self, response):
        self.response = response
        self.requests = []

    def open(self, request, timeout):
        self.requests.append((request, timeout))
        return self.response


class SourceFixture(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.data = self.root / "data"
        self.data.mkdir()
        shutil.copy2(
            SKILL_DIR / "data" / "source-registry.json",
            self.data / "source-registry.json",
        )
        self.registry = json.loads(
            (self.data / "source-registry.json").read_text(encoding="utf-8")
        )
        self.state = {
            "schema_version": "1.0",
            "contract_version": "1.0",
            "generated_at": "2026-11-21",
            "sources": [],
        }
        self.write_json(self.data / "source-watch-state.json", self.state)
        self.snapshots = self.root / "snapshots"
        self.snapshots.mkdir()
        self.candidate = self.root / "candidate"

    def tearDown(self):
        self.temp.cleanup()

    def write_json(self, path, payload):
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(
            json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )

    def write_snapshot(self, source_id="owasp-top10-2025", content_hash=CONTENT_HASH):
        source = next(
            item for item in self.registry["sources"] if item["source_id"] == source_id
        )
        self.write_json(
            self.snapshots / "{}.json".format(source_id),
            {
                "schema_version": "1.0",
                "source_id": source_id,
                "requested_url": source["url"],
                "final_url": source["url"],
                "fetched_at": TODAY,
                "http_status": 200,
                "content_sha256": content_hash,
                "content_length": 321,
                "etag": '"fixture"',
                "last_modified": "Mon, 23 Nov 2026 10:00:00 GMT",
            },
        )


class SourceCheckTest(SourceFixture):
    def run_cli(self, argv):
        out, err = io.StringIO(), io.StringIO()
        with redirect_stdout(out), redirect_stderr(err):
            code = ym.main(argv)
        return code, out.getvalue(), err.getvalue()

    def test_first_snapshot_creates_baseline_candidate_without_mutating_data(self):
        self.write_snapshot()
        original_state = (self.data / "source-watch-state.json").read_bytes()

        report = source_watch.check_sources(
            self.data,
            self.snapshots,
            self.candidate,
            today=TODAY,
        )

        self.assertTrue(report["ok"])
        self.assertTrue(report["changed"])
        diff = json.loads(
            (self.candidate / "diff.json").read_text(encoding="utf-8")
        )
        source_change = next(
            item
            for item in diff["sources"]
            if item["source_id"] == "owasp-top10-2025"
        )
        self.assertEqual(source_change["change_type"], "baseline")
        state_candidate = json.loads(
            (self.candidate / "source-watch-state.candidate.json").read_text(
                encoding="utf-8"
            )
        )
        self.assertEqual(
            state_candidate["sources"][0]["content_sha256"],
            CONTENT_HASH,
        )
        self.assertEqual(
            (self.data / "source-watch-state.json").read_bytes(),
            original_state,
        )

    def test_changed_fingerprint_is_marked_updated_with_previous_hash(self):
        old_hash = "b" * 64
        self.state["sources"] = [{
            "source_id": "owasp-top10-2025",
            "content_sha256": old_hash,
            "etag": '"old"',
            "last_modified": None,
            "checked_at": "2026-11-21",
        }]
        self.write_json(self.data / "source-watch-state.json", self.state)
        self.write_snapshot(content_hash=CONTENT_HASH)

        source_watch.check_sources(
            self.data,
            self.snapshots,
            self.candidate,
            today=TODAY,
        )

        diff = json.loads(
            (self.candidate / "diff.json").read_text(encoding="utf-8")
        )
        change = diff["sources"][0]
        self.assertEqual(change["change_type"], "updated")
        self.assertEqual(change["previous"]["content_sha256"], old_hash)
        candidate_registry = json.loads(
            (self.candidate / "source-registry.candidate.json").read_text(
                encoding="utf-8"
            )
        )
        source = next(
            item
            for item in candidate_registry["sources"]
            if item["source_id"] == "owasp-top10-2025"
        )
        self.assertEqual(source["last_verified_at"], TODAY)

    def test_matching_fingerprint_and_verification_date_create_no_candidate(self):
        self.state["sources"] = [{
            "source_id": "owasp-top10-2025",
            "content_sha256": CONTENT_HASH,
            "etag": '"fixture"',
            "last_modified": "Mon, 23 Nov 2026 10:00:00 GMT",
            "checked_at": TODAY,
        }]
        self.write_json(self.data / "source-watch-state.json", self.state)
        for source in self.registry["sources"]:
            if source["source_id"] == "owasp-top10-2025":
                source["last_verified_at"] = TODAY
                source["retrieved_at"] = TODAY
        self.write_json(self.data / "source-registry.json", self.registry)
        self.write_snapshot(content_hash=CONTENT_HASH)

        report = source_watch.check_sources(
            self.data,
            self.snapshots,
            self.candidate,
            today=TODAY,
        )

        self.assertTrue(report["ok"])
        self.assertFalse(report["changed"])
        self.assertIsNone(report["candidate"])
        self.assertFalse(self.candidate.exists())

    def test_cross_host_redirect_snapshot_is_rejected(self):
        self.write_snapshot()
        snapshot_path = self.snapshots / "owasp-top10-2025.json"
        snapshot = json.loads(snapshot_path.read_text(encoding="utf-8"))
        snapshot["final_url"] = "https://untrusted.example/redirected"
        self.write_json(snapshot_path, snapshot)

        with self.assertRaisesRegex(source_watch.SourceWatchError, "跨 host"):
            source_watch.check_sources(
                self.data,
                self.snapshots,
                self.candidate,
                today=TODAY,
            )
        self.assertFalse(self.candidate.exists())

    def test_non_https_final_url_snapshot_is_rejected(self):
        self.write_snapshot()
        snapshot_path = self.snapshots / "owasp-top10-2025.json"
        snapshot = json.loads(snapshot_path.read_text(encoding="utf-8"))
        snapshot["final_url"] = "http://owasp.org/Top10/"
        self.write_json(snapshot_path, snapshot)

        with self.assertRaisesRegex(source_watch.SourceWatchError, "HTTPS"):
            source_watch.check_sources(
                self.data,
                self.snapshots,
                self.candidate,
                today=TODAY,
            )
        self.assertFalse(self.candidate.exists())

    def test_sources_check_cli_emits_json_without_network(self):
        self.write_snapshot()

        code, out, err = self.run_cli([
            "sources",
            "check",
            "--root",
            str(self.data),
            "--snapshots",
            str(self.snapshots),
            "--out",
            str(self.candidate),
            "--today",
            TODAY,
            "--format",
            "json",
        ])

        self.assertEqual(code, 0, err)
        payload = json.loads(out)
        self.assertTrue(payload["changed"])
        self.assertTrue((self.candidate / "manifest.json").is_file())

    def test_atomic_replace_retries_transient_windows_denial(self):
        source = self.root / "stage"
        target = self.root / "target"
        source.mkdir()
        (source / "probe.json").write_text("{}\n", encoding="utf-8")
        real_replace = source_watch.os.replace
        attempts = {"count": 0}

        def flaky_replace(source, target):
            attempts["count"] += 1
            if attempts["count"] == 1:
                raise PermissionError("simulated transient lock")
            return real_replace(source, target)

        with mock.patch.object(source_watch.os, "replace", side_effect=flaky_replace):
            source_watch._replace_path(source, target)

        self.assertEqual(attempts["count"], 2)
        self.assertTrue((target / "probe.json").is_file())

    def test_sources_check_cli_wraps_write_error(self):
        self.write_snapshot()
        with mock.patch.object(
            source_watch,
            "check_sources",
            side_effect=OSError("disk full"),
        ):
            code, _, err = self.run_cli([
                "sources",
                "check",
                "--root",
                str(self.data),
                "--snapshots",
                str(self.snapshots),
                "--out",
                str(self.candidate),
                "--today",
                TODAY,
                "--format",
                "json",
            ])

        self.assertEqual(code, 7)
        self.assertIn("写入失败", err)
        self.assertNotIn("Traceback", err)


class SourceFetchTest(SourceFixture):
    def test_explicit_fetch_stores_only_metadata_and_content_hash(self):
        body = b"<html>untrusted source text</html>"
        opener = FakeOpener(FakeResponse(body))
        snapshots = self.root / "fetched"

        report = source_watch.fetch_sources(
            self.data,
            snapshots,
            source_ids=("owasp-top10-2025",),
            today=TODAY,
            opener=opener,
        )

        self.assertTrue(report["ok"])
        snapshot = json.loads(
            (snapshots / "owasp-top10-2025.json").read_text(encoding="utf-8")
        )
        self.assertEqual(
            snapshot["content_sha256"],
            "a4615dde08c3b3cfeb38958fa2780ed4940b7f0b41dd7900fbfa8fdbcaeb6149",
        )
        self.assertEqual(snapshot["content_length"], len(body))
        self.assertNotIn("body", snapshot)
        self.assertNotIn("untrusted source text", json.dumps(snapshot))
        self.assertEqual(opener.requests[0][1], 15)

    def test_fetch_rejects_cross_host_redirect_without_writing_snapshots(self):
        opener = FakeOpener(
            FakeResponse(
                b"body",
                url="https://untrusted.example/redirected",
            )
        )
        snapshots = self.root / "fetched"

        with self.assertRaisesRegex(source_watch.SourceWatchError, "跨 host"):
            source_watch.fetch_sources(
                self.data,
                snapshots,
                source_ids=("owasp-top10-2025",),
                today=TODAY,
                opener=opener,
            )
        self.assertFalse(snapshots.exists())

    def test_fetch_rejects_response_over_byte_limit(self):
        opener = FakeOpener(FakeResponse(b"x" * 32))
        snapshots = self.root / "fetched"

        with self.assertRaisesRegex(source_watch.SourceWatchError, "上限"):
            source_watch.fetch_sources(
                self.data,
                snapshots,
                source_ids=("owasp-top10-2025",),
                today=TODAY,
                max_bytes=16,
                opener=opener,
            )
        self.assertFalse(snapshots.exists())

    def test_sources_fetch_cli_rejects_unknown_source_without_network(self):
        out, err = io.StringIO(), io.StringIO()
        with redirect_stdout(out), redirect_stderr(err):
            code = ym.main([
                "sources",
                "fetch",
                "--root",
                str(self.data),
                "--source-id",
                "missing-source",
                "--out",
                str(self.root / "fetched"),
                "--today",
                TODAY,
                "--format",
                "json",
            ])

        self.assertEqual(code, 5)
        self.assertIn("未登记来源", err.getvalue())
        self.assertFalse((self.root / "fetched").exists())

    def test_fetch_all_only_selects_active_sources(self):
        for source in self.registry["sources"]:
            source["status"] = (
                "active" if source["source_id"] == "owasp-top10-2025" else "retired"
            )
        self.write_json(self.data / "source-registry.json", self.registry)
        opener = FakeOpener(FakeResponse(b"body"))
        snapshots = self.root / "fetched"

        report = source_watch.fetch_sources(
            self.data,
            snapshots,
            source_ids=None,
            today=TODAY,
            opener=opener,
        )

        self.assertEqual(report["source_ids"], ["owasp-top10-2025"])
        self.assertEqual(len(opener.requests), 1)


class BankPipelineFixture(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.data = self.root / "data"
        shutil.copytree(SKILL_DIR / "data", self.data)
        self.state = {
            "schema_version": "1.0",
            "contract_version": "1.0",
            "generated_at": "2026-11-21",
            "sources": [],
        }
        self.write_json(self.data / "source-watch-state.json", self.state)
        self.registry = json.loads(
            (self.data / "source-registry.json").read_text(encoding="utf-8")
        )
        self.bank = json.loads(
            (self.data / "question-bank.json").read_text(encoding="utf-8")
        )
        self.snapshots = self.root / "snapshots"
        self.snapshots.mkdir()
        self.write_snapshot("owasp-top10-2025")
        self.source_candidate = self.root / "source-candidate"
        source_watch.check_sources(
            self.data,
            self.snapshots,
            self.source_candidate,
            today=TODAY,
        )
        self.bank_candidate = self.root / "bank-candidate"

    def tearDown(self):
        self.temp.cleanup()

    def write_json(self, path, payload):
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(
            json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )

    def write_snapshot(self, source_id):
        source = next(
            item for item in self.registry["sources"] if item["source_id"] == source_id
        )
        self.write_json(
            self.snapshots / "{}.json".format(source_id),
            {
                "schema_version": "1.0",
                "source_id": source_id,
                "requested_url": source["url"],
                "final_url": source["url"],
                "fetched_at": TODAY,
                "http_status": 200,
                "content_sha256": CONTENT_HASH,
                "content_length": 321,
                "etag": '"fixture"',
                "last_modified": None,
            },
        )

    def propose(self, patches=None):
        patch_path = self.root / "patches.json"
        self.write_json(
            patch_path,
            patches or {"add": [], "modify": [], "retire": []},
        )
        return bank_pipeline.propose_candidate(
            self.data,
            self.source_candidate,
            patch_path,
            self.bank_candidate,
            target_version="0.2.1",
            today=TODAY,
        )

    def run_cli(self, argv):
        out, err = io.StringIO(), io.StringIO()
        with redirect_stdout(out), redirect_stderr(err):
            code = ym.main(argv)
        return code, out.getvalue(), err.getvalue()


class BankProposeTest(BankPipelineFixture):
    def test_modified_question_is_isolated_to_candidate_and_hash_is_recomputed(self):
        question = self.bank["questions"][0]
        original_content_hash = question["content_hash"]
        patches = {
            "modify": [{
                "question_id": question["question_id"],
                "set": {
                    "prompt": "请基于已授权事件，说明告警分诊的证据和停止条件。",
                },
            }],
        }
        patch_path = self.root / "patches.json"
        self.write_json(patch_path, patches)
        official_before = (self.data / "question-bank.json").read_bytes()

        report = bank_pipeline.propose_candidate(
            self.data,
            self.source_candidate,
            patch_path,
            self.bank_candidate,
            target_version="0.2.1",
            today=TODAY,
        )

        self.assertTrue(report["ok"])
        self.assertEqual(
            (self.data / "question-bank.json").read_bytes(),
            official_before,
        )
        candidate_bank = json.loads(
            (self.bank_candidate / "question-bank.candidate.json").read_text(
                encoding="utf-8"
            )
        )
        self.assertEqual(candidate_bank["bank_version"], "0.2.1")
        candidate_question = next(
            item
            for item in candidate_bank["questions"]
            if item["question_id"] == question["question_id"]
        )
        self.assertEqual(
            candidate_question["prompt"],
            "请基于已授权事件，说明告警分诊的证据和停止条件。",
        )
        self.assertNotEqual(candidate_question["content_hash"], original_content_hash)
        diff = json.loads(
            (self.bank_candidate / "diff.json").read_text(encoding="utf-8")
        )
        self.assertEqual(diff["questions"][0]["change_type"], "modified")
        manifest = json.loads(
            (self.bank_candidate / "manifest.json").read_text(encoding="utf-8")
        )
        self.assertEqual(manifest["question_change_count"], 1)


class BankReviewTest(BankPipelineFixture):
    def test_bank_review_cli_wraps_write_error(self):
        self.propose()
        notes = self.root / "review-notes.md"
        notes.write_text("五项人工核对完成。\n", encoding="utf-8")
        with mock.patch.object(
            bank_pipeline,
            "review_candidate",
            side_effect=OSError("disk full"),
        ):
            code, _, err = self.run_cli([
                "bank", "review",
                "--candidate", str(self.bank_candidate),
                "--reviewer", "local-maintainer",
                "--decision", "approve",
                "--review-notes", str(notes),
                "--confirm", "facts,role,level,boundary,rights",
                "--reviewed-at", "2026-11-24T12:00:00Z",
                "--format", "json",
            ])

        self.assertEqual(code, 7)
        self.assertIn("写入失败", err)
        self.assertNotIn("Traceback", err)

    def test_approved_review_records_all_confirmations_and_candidate_hash(self):
        self.propose()
        notes = self.root / "review-notes.md"
        notes.write_text("来源事实、岗位、职级、边界和权利均已人工核对。\n", encoding="utf-8")

        report = bank_pipeline.review_candidate(
            self.bank_candidate,
            reviewer="local-maintainer",
            decision="approve",
            review_notes_path=notes,
            confirmations=("facts", "role", "level", "boundary", "rights"),
            reviewed_at="2026-11-24T12:00:00Z",
        )

        self.assertTrue(report["ok"])
        review = json.loads(
            (self.bank_candidate / "review.json").read_text(encoding="utf-8")
        )
        self.assertEqual(review["decision"], "approve")
        self.assertEqual(review["reviewer"], "local-maintainer")
        self.assertEqual(
            set(review["confirmations"]),
            {"facts", "role", "level", "boundary", "rights"},
        )
        self.assertEqual(len(review["candidate_sha256"]), 64)

    def test_approval_without_all_confirmations_is_rejected(self):
        self.propose()
        notes = self.root / "review-notes.md"
        notes.write_text("缺少权利确认。\n", encoding="utf-8")

        with self.assertRaisesRegex(bank_pipeline.BankPipelineError, "rights"):
            bank_pipeline.review_candidate(
                self.bank_candidate,
                reviewer="local-maintainer",
                decision="approve",
                review_notes_path=notes,
                confirmations=("facts", "role", "level", "boundary"),
                reviewed_at="2026-11-24T12:00:00Z",
            )
        self.assertFalse((self.bank_candidate / "review.json").exists())


class BankValidateTest(BankPipelineFixture):
    def test_rejected_review_cannot_validate_or_apply(self):
        self.propose()
        notes = self.root / "review-notes.md"
        notes.write_text("事实未通过复核。\n", encoding="utf-8")
        bank_pipeline.review_candidate(
            self.bank_candidate,
            reviewer="local-maintainer",
            decision="reject",
            review_notes_path=notes,
            confirmations=(),
            reviewed_at="2026-11-24T12:00:00Z",
        )

        with self.assertRaisesRegex(bank_pipeline.BankPipelineError, "approve"):
            bank_pipeline.validate_candidate(
                self.bank_candidate,
                self.data,
                today=TODAY,
            )
        self.assertFalse((self.bank_candidate / "validation.json").exists())

    def test_approved_candidate_validates_fifteen_contracts_in_temp_tree(self):
        self.propose()
        notes = self.root / "review-notes.md"
        notes.write_text("五项人工核对完成。\n", encoding="utf-8")
        bank_pipeline.review_candidate(
            self.bank_candidate,
            reviewer="local-maintainer",
            decision="approve",
            review_notes_path=notes,
            confirmations=("facts", "role", "level", "boundary", "rights"),
            reviewed_at="2026-11-24T12:00:00Z",
        )
        official_before = {
            path.name: path.read_bytes()
            for path in self.data.iterdir()
            if path.is_file()
        }

        report = bank_pipeline.validate_candidate(
            self.bank_candidate,
            self.data,
            today=TODAY,
        )

        self.assertTrue(report["ok"])
        self.assertEqual(report["checked_files"], 15)
        self.assertEqual(report["question_count"], 162)
        validation = json.loads(
            (self.bank_candidate / "validation.json").read_text(encoding="utf-8")
        )
        self.assertTrue(validation["ok"])
        self.assertEqual(len(validation["candidate_sha256"]), 64)
        self.assertEqual(
            {
                path.name: path.read_bytes()
                for path in self.data.iterdir()
                if path.is_file()
            },
            official_before,
        )

    def test_candidate_must_keep_at_least_162_active_questions(self):
        first_question_id = self.bank["questions"][0]["question_id"]
        self.propose({
            "add": [],
            "modify": [],
            "retire": [{"question_id": first_question_id}],
        })
        notes = self.root / "review-notes.md"
        notes.write_text("已复核退役题但没有补题。\n", encoding="utf-8")
        bank_pipeline.review_candidate(
            self.bank_candidate,
            reviewer="local-maintainer",
            decision="approve",
            review_notes_path=notes,
            confirmations=("facts", "role", "level", "boundary", "rights"),
            reviewed_at="2026-11-24T12:00:00Z",
        )

        with self.assertRaisesRegex(bank_pipeline.BankPipelineError, "162"):
            bank_pipeline.validate_candidate(
                self.bank_candidate,
                self.data,
                today=TODAY,
            )
        self.assertFalse((self.bank_candidate / "validation.json").exists())

    def test_candidate_with_stale_base_version_is_rejected(self):
        self.propose()
        notes = self.root / "review-notes.md"
        notes.write_text("基础版本已过期。\n", encoding="utf-8")
        bank_pipeline.review_candidate(
            self.bank_candidate,
            reviewer="local-maintainer",
            decision="approve",
            review_notes_path=notes,
            confirmations=("facts", "role", "level", "boundary", "rights"),
            reviewed_at="2026-11-24T12:00:00Z",
        )
        official = json.loads(
            (self.data / "question-bank.json").read_text(encoding="utf-8")
        )
        official["bank_version"] = "0.2.1"
        self.write_json(self.data / "question-bank.json", official)

        with self.assertRaisesRegex(bank_pipeline.BankPipelineError, "基线版本"):
            bank_pipeline.validate_candidate(
                self.bank_candidate,
                self.data,
                today=TODAY,
            )


class BankApplyRollbackTest(BankPipelineFixture):
    def prepare_validated_candidate(self):
        self.propose()
        notes = self.root / "review-notes.md"
        notes.write_text("五项人工核对完成。\n", encoding="utf-8")
        bank_pipeline.review_candidate(
            self.bank_candidate,
            reviewer="local-maintainer",
            decision="approve",
            review_notes_path=notes,
            confirmations=("facts", "role", "level", "boundary", "rights"),
            reviewed_at="2026-11-24T12:00:00Z",
        )
        bank_pipeline.validate_candidate(
            self.bank_candidate,
            self.data,
            today=TODAY,
        )

    def test_apply_then_rollback_restores_source_and_bank_bytes(self):
        self.prepare_validated_candidate()
        original = {
            name: (self.data / name).read_bytes()
            for name in (
                "source-registry.json",
                "source-watch-state.json",
                "question-bank.json",
            )
        }

        applied = bank_pipeline.apply_candidate(
            self.bank_candidate,
            self.data,
            today=TODAY,
            now="2026-11-24T13:00:00Z",
        )

        self.assertTrue(applied["ok"])
        self.assertTrue(applied["snapshot_id"])
        updated_bank = json.loads(
            (self.data / "question-bank.json").read_text(encoding="utf-8")
        )
        self.assertEqual(updated_bank["bank_version"], "0.2.1")
        snapshot_dir = (
            self.data / "history" / applied["snapshot_id"]
        )
        self.assertTrue((snapshot_dir / "manifest.json").is_file())

        rolled_back = bank_pipeline.rollback(
            applied["snapshot_id"],
            self.data,
            today=TODAY,
            now="2026-11-24T14:00:00Z",
        )

        self.assertTrue(rolled_back["ok"])
        self.assertEqual(
            {
                name: (self.data / name).read_bytes()
                for name in original
            },
            original,
        )

    def test_candidate_file_tamper_after_validation_blocks_apply(self):
        self.prepare_validated_candidate()
        official_before = (self.data / "question-bank.json").read_bytes()
        bank_path = self.bank_candidate / "question-bank.candidate.json"
        raw = bank_path.read_bytes()
        self.assertIn(b"0.2.1", raw)
        bank_path.write_bytes(raw.replace(b"0.2.1", b"0.2.2", 1))

        with self.assertRaisesRegex(bank_pipeline.BankPipelineError, "哈希"):
            bank_pipeline.apply_candidate(
                self.bank_candidate,
                self.data,
                today=TODAY,
                now="2026-11-24T13:00:00Z",
            )
        self.assertEqual(
            (self.data / "question-bank.json").read_bytes(),
            official_before,
        )

    def test_tampered_history_snapshot_blocks_rollback(self):
        self.prepare_validated_candidate()
        applied = bank_pipeline.apply_candidate(
            self.bank_candidate,
            self.data,
            today=TODAY,
            now="2026-11-24T13:00:00Z",
        )
        applied_bank = (self.data / "question-bank.json").read_bytes()
        snapshot_bank = (
            self.data / "history" / applied["snapshot_id"] / "question-bank.json"
        )
        raw = snapshot_bank.read_bytes()
        self.assertIn(b"0.2.0", raw)
        snapshot_bank.write_bytes(raw.replace(b"0.2.0", b"0.2.2", 1))

        with self.assertRaisesRegex(bank_pipeline.BankPipelineError, "哈希"):
            bank_pipeline.rollback(
                applied["snapshot_id"],
                self.data,
                today=TODAY,
                now="2026-11-24T14:00:00Z",
            )
        self.assertEqual(
            (self.data / "question-bank.json").read_bytes(),
            applied_bank,
        )

    def test_post_apply_validation_failure_restores_official_files(self):
        self.prepare_validated_candidate()
        original = {
            name: (self.data / name).read_bytes()
            for name in (
                "source-registry.json",
                "source-watch-state.json",
                "question-bank.json",
            )
        }
        real_validator = bank_pipeline.validate_contracts
        calls = {"count": 0}

        def fail_second_call(root, today):
            calls["count"] += 1
            if calls["count"] == 2:
                return {
                    "ok": False,
                    "checked_files": 0,
                    "question_count": 0,
                    "errors": [],
                }
            return real_validator(root, today)

        with mock.patch.object(
            bank_pipeline,
            "validate_contracts",
            side_effect=fail_second_call,
        ):
            with self.assertRaisesRegex(bank_pipeline.BankPipelineError, "应用后"):
                bank_pipeline.apply_candidate(
                    self.bank_candidate,
                    self.data,
                    today=TODAY,
                    now="2026-11-24T13:00:00Z",
                )
        self.assertEqual(
            {
                name: (self.data / name).read_bytes()
                for name in original
            },
            original,
        )

    def test_post_rollback_validation_failure_restores_current_files(self):
        self.prepare_validated_candidate()
        applied = bank_pipeline.apply_candidate(
            self.bank_candidate,
            self.data,
            today=TODAY,
            now="2026-11-24T13:00:00Z",
        )
        current = {
            name: (self.data / name).read_bytes()
            for name in (
                "source-registry.json",
                "source-watch-state.json",
                "question-bank.json",
            )
        }

        with mock.patch.object(
            bank_pipeline,
            "validate_contracts",
            return_value={
                "ok": False,
                "checked_files": 0,
                "question_count": 0,
                "errors": [],
            },
        ):
            with self.assertRaisesRegex(bank_pipeline.BankPipelineError, "回滚后"):
                bank_pipeline.rollback(
                    applied["snapshot_id"],
                    self.data,
                    today=TODAY,
                    now="2026-11-24T14:00:00Z",
                )
        self.assertEqual(
            {
                name: (self.data / name).read_bytes()
                for name in current
            },
            current,
        )

    def test_cli_complete_candidate_apply_and_rollback_flow(self):
        patch_path = self.root / "patches.json"
        self.write_json(
            patch_path,
            {"add": [], "modify": [], "retire": []},
        )
        notes = self.root / "review-notes.md"
        notes.write_text("五项人工核对完成。\n", encoding="utf-8")
        original_bank = (self.data / "question-bank.json").read_bytes()

        code, out, err = self.run_cli([
            "bank", "propose",
            "--root", str(self.data),
            "--source-candidate", str(self.source_candidate),
            "--patches", str(patch_path),
            "--target-version", "0.2.1",
            "--out", str(self.bank_candidate),
            "--today", TODAY,
            "--format", "json",
        ])
        self.assertEqual(code, 0, err)
        self.assertTrue(json.loads(out)["ok"])

        code, _, err = self.run_cli([
            "bank", "review",
            "--candidate", str(self.bank_candidate),
            "--reviewer", "local-maintainer",
            "--decision", "approve",
            "--review-notes", str(notes),
            "--confirm", "facts,role,level,boundary,rights",
            "--reviewed-at", "2026-11-24T12:00:00Z",
            "--format", "json",
        ])
        self.assertEqual(code, 0, err)

        code, out, err = self.run_cli([
            "bank", "validate",
            "--candidate", str(self.bank_candidate),
            "--root", str(self.data),
            "--today", TODAY,
            "--format", "json",
        ])
        self.assertEqual(code, 0, err)
        self.assertEqual(json.loads(out)["checked_files"], 15)

        code, out, err = self.run_cli([
            "bank", "apply",
            "--candidate", str(self.bank_candidate),
            "--root", str(self.data),
            "--today", TODAY,
            "--now", "2026-11-24T13:00:00Z",
            "--format", "json",
        ])
        self.assertEqual(code, 0, err)
        snapshot_id = json.loads(out)["snapshot_id"]

        code, _, err = self.run_cli([
            "bank", "rollback",
            "--snapshot", snapshot_id,
            "--root", str(self.data),
            "--today", TODAY,
            "--now", "2026-11-24T14:00:00Z",
            "--format", "json",
        ])
        self.assertEqual(code, 0, err)
        self.assertEqual(
            (self.data / "question-bank.json").read_bytes(),
            original_bank,
        )


if __name__ == "__main__":
    unittest.main()
