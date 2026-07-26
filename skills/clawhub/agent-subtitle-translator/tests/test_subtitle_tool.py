from __future__ import annotations

import codecs
import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "subtitle_tool.py"
FIXTURES = Path(__file__).parent / "fixtures"

SPEC = importlib.util.spec_from_file_location("subtitle_tool", SCRIPT)
assert SPEC and SPEC.loader
subtitle_tool = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = subtitle_tool
SPEC.loader.exec_module(subtitle_tool)


class SubtitleToolTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.tmp = Path(self.temp.name)

    def run_cli(self, *args: str, ok: bool = True) -> subprocess.CompletedProcess[str]:
        result = subprocess.run(
            [sys.executable, str(SCRIPT), *map(str, args)],
            cwd=self.tmp,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=False,
        )
        if ok and result.returncode != 0:
            self.fail(f"CLI failed ({result.returncode}):\nstdout={result.stdout}\nstderr={result.stderr}")
        if not ok and result.returncode == 0:
            self.fail(f"CLI unexpectedly succeeded:\n{result.stdout}")
        return result

    def copy_fixture(self, name: str) -> Path:
        source = FIXTURES / name
        target = self.tmp / name
        target.write_bytes(source.read_bytes())
        return target

    def prepare(self, input_path: Path, target: str = "zh-hans", **kwargs: str) -> Path:
        work = self.tmp / f"work-{input_path.stem}"
        args = [
            "prepare",
            str(input_path),
            "--target-language",
            target,
            "--work-dir",
            str(work),
        ]
        for key, value in kwargs.items():
            args.extend([f"--{key.replace('_', '-')}", str(value)])
        self.run_cli(*args)
        return work

    def write_response(self, work: Path, batch: int, bodies: dict[str, str]) -> Path:
        manifest = json.loads((work / "manifest.json").read_text(encoding="utf-8"))
        ids = next(item["ids"] for item in manifest["batches"] if item["batch"] == batch)
        response = self.tmp / f"response-{batch}.txt"
        response.write_text(
            "\n\n".join(f"⟦ID:{stable_id}⟧\n{bodies[stable_id]}\n⟦/ID:{stable_id}⟧" for stable_id in ids),
            encoding="utf-8",
        )
        return response

    def validate(self, work: Path, response: Path, batch: int = 1, *extra: str) -> None:
        self.run_cli(
            "validate-response",
            "--manifest",
            str(work / "manifest.json"),
            "--batch",
            str(batch),
            "--response",
            str(response),
            *extra,
        )

    def compose(self, work: Path, output: Path | None = None, *extra: str) -> Path:
        manifest = json.loads((work / "manifest.json").read_text(encoding="utf-8"))
        path = output or Path(manifest["default_output_path"])
        self.run_cli(
            "compose",
            "--manifest",
            str(work / "manifest.json"),
            "--output",
            str(path),
            *extra,
        )
        return path

    def test_srt_batches_have_at_most_32_entries_and_no_timeline(self) -> None:
        source = self.tmp / "many.srt"
        blocks = [
            f"{index}\n00:00:{index % 60:02d},000 --> 00:00:{index % 60:02d},500\nLine {index}"
            for index in range(1, 34)
        ]
        source.write_text("\n\n".join(blocks), encoding="utf-8")
        work = self.prepare(source, target="pt-br", batch_size="32")
        manifest = json.loads((work / "manifest.json").read_text(encoding="utf-8"))
        self.assertEqual(manifest["target_language"], "pt-BR")
        self.assertEqual([len(batch["ids"]) for batch in manifest["batches"]], [32, 1])
        prompt = (work / "batches" / "batch-0001.txt").read_text(encoding="utf-8")
        self.assertNotIn("-->", prompt)
        self.assertNotIn("00:00:", prompt)
        self.assertIn("自然、流畅、简洁的口语", prompt)
        self.assertIn("可随目标语言语序成对移动", prompt)

    def test_batches_validated_out_of_order_still_compose_by_stable_id(self) -> None:
        source = self.tmp / "many.srt"
        source.write_text(
            "\n\n".join(
                f"{index}\n00:00:{index:02d},000 --> 00:00:{index:02d},500\nLine {index}"
                for index in range(1, 4)
            ),
            encoding="utf-8",
        )
        work = self.prepare(source, batch_size="2")
        second = self.write_response(work, 2, {"000003": "译文 3"})
        self.validate(work, second, 2)
        first = self.write_response(work, 1, {"000001": "译文 1", "000002": "译文 2"})
        self.validate(work, first, 1)
        output = self.compose(work, self.tmp / "stable.srt")
        rendered = output.read_text(encoding="utf-8-sig")
        self.assertLess(rendered.index("译文 1"), rendered.index("译文 2"))
        self.assertLess(rendered.index("译文 2"), rendered.index("译文 3"))

    def test_srt_round_trip_preserves_times_and_writes_utf8_bom(self) -> None:
        source = self.copy_fixture("basic.srt")
        work = self.prepare(source)
        response = self.write_response(work, 1, {"000001": "你好。", "000002": "你好吗？"})
        self.validate(work, response)
        output = self.compose(work, self.tmp / "basic.zh-Hans.srt")
        data = output.read_bytes()
        self.assertTrue(data.startswith(codecs.BOM_UTF8))
        text = data.decode("utf-8-sig")
        self.assertIn("00:00:01,000 --> 00:00:02,500", text)
        self.assertIn("00:00:03,000 --> 00:00:04,000", text)
        self.assertEqual(text.count("-->"), 2)

    def test_unsorted_srt_is_reported_and_normalized_without_count_change(self) -> None:
        source = self.tmp / "unsorted.srt"
        source.write_text(
            "1\n00:00:03,000 --> 00:00:04,000\nLater\n\n"
            "2\n00:00:01,000 --> 00:00:02,000\nEarlier\n",
            encoding="utf-8",
        )
        work = self.prepare(source)
        manifest = json.loads((work / "manifest.json").read_text(encoding="utf-8"))
        self.assertFalse(manifest["checks"]["before"]["sorted"])
        self.assertTrue(manifest["checks"]["after"]["sorted"])
        self.assertEqual(manifest["checks"]["original_entry_count"], 2)
        self.assertEqual(manifest["checks"]["normalized_entry_count"], 2)
        self.assertEqual(manifest["entries"][0]["source_text"], "Earlier")

    def test_vtt_normalizes_to_srt_and_default_name(self) -> None:
        source = self.copy_fixture("basic.vtt")
        work = self.prepare(source, target="zh-Hans")
        manifest = json.loads((work / "manifest.json").read_text(encoding="utf-8"))
        self.assertEqual(manifest["output_format"], "srt")
        self.assertTrue(manifest["default_output_path"].endswith("basic.zh-Hans.srt"))
        response = self.write_response(work, 1, {"000001": "你好。", "000002": "你好吗？"})
        self.validate(work, response)
        output = self.compose(work, self.tmp / "from-vtt.srt")
        self.assertIn("00:00:01,000 --> 00:00:02,500", output.read_text(encoding="utf-8-sig"))

    def test_ass_semantic_style_moves_with_translation_and_preserves_structure(self) -> None:
        source = self.copy_fixture("styled.ass")
        work = self.prepare(source)
        prompt = (work / "batches" / "batch-0001.txt").read_text(encoding="utf-8")
        self.assertIn("What date is ⟦S1⟧today⟦/S1⟧?", prompt)
        self.assertIn("Hello⟦BR1⟧world", prompt)
        self.assertNotIn(r"\b1", prompt)
        self.assertNotIn("0:00:01.00", prompt)
        response = self.write_response(
            work,
            1,
            {
                "000001": "⟦S1⟧今天⟦/S1⟧是几号？",
                "000002": "世界⟦BR1⟧你好",
            },
        )
        self.validate(work, response)
        output = self.compose(work, self.tmp / "styled.zh-Hans.ass")
        rendered = output.read_text(encoding="utf-8-sig")
        self.assertIn(r"{\b1\c&H00FFFF&}今天{\r}是几号？", rendered)
        self.assertIn(r"世界\N你好", rendered)
        self.assertIn("Comment: 0,0:00:00.00,0:00:02.00,Default,Editor,0,0,0,,Do not translate this comment", rendered)
        self.assertIn(r"Dialogue: 2,0:00:07.00,0:00:09.00,Default,,0,0,0,,{\p1}m 0 0 l 10 10{\p0}", rendered)
        self.assertIn("Style: Sign,Arial,40", rendered)
        self.assertTrue(output.read_bytes().startswith(codecs.BOM_UTF8))

    def test_marker_mismatch_fails_then_explicit_style_fallback_is_reported(self) -> None:
        source = self.copy_fixture("styled.ass")
        work = self.prepare(source)
        response = self.write_response(
            work,
            1,
            {"000001": "今天是几号？", "000002": "你好⟦BR1⟧世界"},
        )
        failed = self.run_cli(
            "validate-response",
            "--manifest",
            str(work / "manifest.json"),
            "--batch",
            "1",
            "--response",
            str(response),
            ok=False,
        )
        self.assertIn("style markers mismatch", failed.stderr)
        self.validate(work, response, 1, "--allow-style-fallback")
        output = self.compose(work, self.tmp / "fallback.ass")
        rendered = output.read_text(encoding="utf-8-sig")
        self.assertIn(",fx,今天是几号？", rendered)
        self.assertNotIn(r"\b1", rendered.split(",fx,", 1)[1].splitlines()[0])
        report = json.loads((self.tmp / "fallback.ass.report.json").read_text(encoding="utf-8"))
        self.assertEqual(report["style_fallback_ids"], ["000001"])

    def test_karaoke_degrades_per_entry_but_preserves_style_event_and_break(self) -> None:
        source = self.copy_fixture("karaoke.ass")
        work = self.prepare(source)
        manifest = json.loads((work / "manifest.json").read_text(encoding="utf-8"))
        self.assertEqual(manifest["checks"]["karaoke_degraded_ids"], ["000001"])
        prompt = (work / "batches" / "batch-0001.txt").read_text(encoding="utf-8")
        self.assertIn("Karaoke⟦BR1⟧now", prompt)
        self.assertNotIn(r"\k20", prompt)
        response = self.write_response(work, 1, {"000001": "现在⟦BR1⟧卡拉 OK"})
        self.validate(work, response)
        output = self.compose(work, self.tmp / "karaoke.zh-Hans.ass")
        rendered = output.read_text(encoding="utf-8-sig")
        dialogue = next(line for line in rendered.splitlines() if line.startswith("Dialogue:"))
        self.assertIn(r"{\an8}现在\N卡拉 OK", dialogue)
        self.assertNotRegex(dialogue, r"\\(?:k|K|kf|ko)\d")
        self.assertNotIn(r"\t(", dialogue)
        self.assertIn(",Default,Singer,", dialogue)
        report = json.loads((self.tmp / "karaoke.zh-Hans.ass.report.json").read_text())
        self.assertEqual(report["karaoke_degraded_count"], 1)

    def test_ass_mixed_position_and_inline_style_are_separated_safely(self) -> None:
        neutral = subtitle_tool.neutralize_ass_text(r"{\pos(100,200)\b1}Hello{\r}")
        self.assertEqual(neutral["ass_prefix"], r"{\pos(100,200)}")
        self.assertEqual(neutral["payload_text"], "⟦S1⟧Hello⟦/S1⟧")
        entry = {"id": "000001", **neutral}
        restored = subtitle_tool.restore_ass_text("⟦S1⟧你好⟦/S1⟧", entry, False)
        self.assertEqual(restored, r"{\pos(100,200)}{\b1}你好{\r}")

    def test_empty_ass_dialogue_is_preserved_and_reported(self) -> None:
        source = self.tmp / "empty-dialogue.ass"
        source.write_text(
            "[Script Info]\nTitle: empty\n\n[Events]\n"
            "Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text\n"
            "Dialogue: 0,0:00:01.00,0:00:02.00,Default,,0,0,0,,\n"
            "Dialogue: 0,0:00:03.00,0:00:04.00,Default,,0,0,0,,Hello\n",
            encoding="utf-8",
        )
        work = self.prepare(source)
        manifest = json.loads((work / "manifest.json").read_text(encoding="utf-8"))
        self.assertEqual(manifest["checks"]["empty_dialogue_numbers_preserved"], [1])
        self.assertEqual(manifest["checks"]["translatable_entry_count"], 1)

    def test_drawing_only_ass_composes_without_an_llm_batch(self) -> None:
        source = self.tmp / "drawing-only.ass"
        source.write_text(
            "[Script Info]\nTitle: drawing\n\n[Events]\n"
            "Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text\n"
            r"Dialogue: 0,0:00:01.00,0:00:02.00,Default,,0,0,0,,{\p1}m 0 0 l 10 10{\p0}" + "\n",
            encoding="utf-8",
        )
        work = self.prepare(source)
        manifest = json.loads((work / "manifest.json").read_text(encoding="utf-8"))
        self.assertEqual(manifest["entry_count"], 0)
        self.assertEqual(manifest["batches"], [])
        self.assertEqual(manifest["checks"]["after"]["time_range_ms"], [1000, 2000])
        output = self.compose(work, self.tmp / "drawing.zh-Hans.ass")
        rendered = output.read_text(encoding="utf-8-sig")
        self.assertIn(r"{\p1}m 0 0 l 10 10{\p0}", rendered)

    def test_response_count_id_and_break_mismatches_fail(self) -> None:
        source = self.copy_fixture("basic.srt")
        work = self.prepare(source)
        response = self.tmp / "bad.txt"
        response.write_text("⟦ID:000001⟧Only one⟦/ID:000001⟧", encoding="utf-8")
        result = self.run_cli(
            "validate-response",
            "--manifest",
            str(work / "manifest.json"),
            "--batch",
            "1",
            "--response",
            str(response),
            ok=False,
        )
        self.assertIn("entry count mismatch", result.stderr)

        response.write_text(
            "⟦ID:000002⟧Second⟦/ID:000002⟧\n\n"
            "⟦ID:000001⟧First⟦/ID:000001⟧",
            encoding="utf-8",
        )
        result = self.run_cli(
            "validate-response",
            "--manifest",
            str(work / "manifest.json"),
            "--batch",
            "1",
            "--response",
            str(response),
            ok=False,
        )
        self.assertIn("IDs/order mismatch", result.stderr)

        response.write_text(
            "extra\n⟦ID:000001⟧First⟦/ID:000001⟧\n\n"
            "⟦ID:000002⟧Second⟦/ID:000002⟧",
            encoding="utf-8",
        )
        result = self.run_cli(
            "validate-response",
            "--manifest",
            str(work / "manifest.json"),
            "--batch",
            "1",
            "--response",
            str(response),
            ok=False,
        )
        self.assertIn("outside the required ID wrappers", result.stderr)

        ass_source = self.copy_fixture("styled.ass")
        ass_work = self.prepare(ass_source)
        bad_break = self.write_response(
            ass_work,
            1,
            {"000001": "⟦S1⟧今天⟦/S1⟧是几号？", "000002": "你好世界"},
        )
        result = self.run_cli(
            "validate-response",
            "--manifest",
            str(ass_work / "manifest.json"),
            "--batch",
            "1",
            "--response",
            str(bad_break),
            ok=False,
        )
        self.assertIn("BR markers mismatch", result.stderr)

    def test_encoding_bom_legacy_and_low_confidence(self) -> None:
        utf16 = self.tmp / "utf16.srt"
        utf16.write_bytes("1\n00:00:01,000 --> 00:00:02,000\n你好\n".encode("utf-16"))
        work = self.prepare(utf16)
        manifest = json.loads((work / "manifest.json").read_text(encoding="utf-8"))
        self.assertTrue(manifest["encoding"]["bom"].startswith("UTF-16"))

        legacy = self.tmp / "legacy.srt"
        legacy.write_bytes(
            ("1\n00:00:01,000 --> 00:00:02,000\n" + "Café déjà vu — résumé français." * 3 + "\n").encode("cp1252")
        )
        legacy_work = self.prepare(legacy, target="en")
        legacy_manifest = json.loads((legacy_work / "manifest.json").read_text(encoding="utf-8"))
        self.assertNotEqual(legacy_manifest["encoding"]["name"].lower(), "utf-8")

        ambiguous = self.tmp / "ambiguous.srt"
        ambiguous.write_bytes(b"1\n0\n\x81")
        result = self.run_cli(
            "prepare",
            str(ambiguous),
            "--target-language",
            "en",
            "--work-dir",
            str(self.tmp / "ambiguous-work"),
            ok=False,
        )
        self.assertIn("Encoding detection confidence is too low", result.stderr)

    def test_collision_protection_for_work_validated_and_output(self) -> None:
        source = self.copy_fixture("basic.srt")
        work = self.prepare(source)
        collision = self.run_cli(
            "prepare",
            str(source),
            "--target-language",
            "zh-Hans",
            "--work-dir",
            str(work),
            ok=False,
        )
        self.assertIn("Work directory already exists", collision.stderr)
        response = self.write_response(work, 1, {"000001": "你好。", "000002": "你好吗？"})
        self.validate(work, response)
        duplicate_validation = self.run_cli(
            "validate-response",
            "--manifest",
            str(work / "manifest.json"),
            "--batch",
            "1",
            "--response",
            str(response),
            ok=False,
        )
        self.assertIn("already exists", duplicate_validation.stderr)
        output = self.compose(work, self.tmp / "collision.srt")
        duplicate_output = self.run_cli(
            "compose",
            "--manifest",
            str(work / "manifest.json"),
            "--output",
            str(output),
            ok=False,
        )
        self.assertIn("Output already exists", duplicate_output.stderr)

    def test_bcp47_validation(self) -> None:
        self.assertEqual(subtitle_tool.normalize_bcp47("zh_hans"), "zh-Hans")
        self.assertEqual(subtitle_tool.normalize_bcp47("pt-br"), "pt-BR")
        with self.assertRaises(subtitle_tool.SubtitleError):
            subtitle_tool.normalize_bcp47("not a tag")


if __name__ == "__main__":
    unittest.main()
