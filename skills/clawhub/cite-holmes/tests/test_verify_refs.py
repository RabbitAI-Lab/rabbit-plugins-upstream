#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""cite-holmes verify_refs.py 回归测试套件（v1.3.0 起）。

离线为主（快、稳定）；E-utilities 在线核验单列一组，网络不可达时跳过。
"""
import json
import os
import sys
import tempfile
import unittest
import unittest.mock

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "scripts"))
import verify_refs as vr  # noqa: E402

EXAMPLES = os.path.join(HERE, "..", "examples")
DEMO = os.path.join(EXAMPLES, "demo_refs.json")
# v1.4：offline 只做结构核验，verified 封顶为 partial（诚实优先）
GOLDEN_OFFLINE = ["partial", "partial", "partial", "partial",
                  "partial", "partial", "partial", "invalid"]


def run_offline(refs):
    results = []
    for i, ref in enumerate(refs, 1):
        results.append(vr.verify_one(ref, i, True, 5.0))
    vr.mark_duplicates(results)
    return results


class TestOfflineBaseline(unittest.TestCase):
    """demo_refs.json（3 个埋雷 + 5 条真实）的判定金样本，自 v1.0 冻结。"""

    def test_demo_refs_golden_sequence(self):
        refs = json.load(open(DEMO, encoding="utf-8"))
        results = run_offline(refs)
        self.assertEqual([r["verdict"] for r in results], GOLDEN_OFFLINE)

    def test_scorecard_baseline(self):
        results = run_offline(json.load(open(DEMO, encoding="utf-8")))
        sc = vr.compute_scorecard(results)
        self.assertEqual(sc["counts"]["verified"], 0)
        self.assertEqual(sc["counts"]["partial"], 7)
        self.assertEqual(sc["counts"]["invalid"], 1)
        self.assertEqual(sc["score"], 25)
        self.assertEqual(sc["grade"], "D")


class TestScorecard(unittest.TestCase):
    def test_all_verified_is_100A(self):
        # 纯评分卡单元测试：直接构造 verified 结果（离线封顶另由 verify_one 测试覆盖）
        results = [{"index": i, "verdict": "verified", "title": f"s{i}"} for i in range(1, 10)]
        sc = vr.compute_scorecard(results)
        self.assertEqual((sc["score"], sc["grade"]), (100, "A"))

    def test_all_invalid_is_0D(self):
        refs = [{"title": f"x{i}"} for i in range(5)]
        sc = vr.compute_scorecard(run_offline(refs))
        self.assertEqual((sc["score"], sc["grade"]), (0, "D"))

    def test_empty(self):
        sc = vr.compute_scorecard([])
        self.assertEqual(sc["score"], 0)
        self.assertEqual(sc["total"], 0)

    def test_render_md_contains_scorecard(self):
        md = vr.render_md(run_offline(json.load(open(DEMO, encoding="utf-8"))), True)
        self.assertIn("CiteScore", md)
        self.assertIn("25 / 100 · D 级", md)


class TestDedupThreeKey(unittest.TestCase):
    def test_url_doi_pmid_dedup(self):
        results = [
            {"index": 1, "title": "a", "url": "https://x.com/", "doi": "10.1000/a",
             "pmid": "36443570", "verdict": "verified", "note": ""},
            {"index": 2, "title": "b", "url": "https://x.com", "doi": "", "pmid": "",
             "verdict": "verified", "note": ""},
            {"index": 3, "title": "c", "url": "https://y.com", "doi": "10.1000/A",
             "pmid": "", "verdict": "verified", "note": ""},
            {"index": 4, "title": "d", "url": "https://z.com", "doi": "",
             "pmid": "36443570", "verdict": "verified", "note": ""},
        ]
        vr.mark_duplicates(results)
        self.assertIn("与 #1 重复（同URL）", results[1]["note"])
        self.assertIn("与 #1 重复（同DOI）", results[2]["note"])
        self.assertIn("与 #1 重复（同PMID）", results[3]["note"])
        for r in results[1:]:
            self.assertEqual(r["verdict"], "partial")
        self.assertEqual(results[0]["verdict"], "verified")


class TestMissingFields(unittest.TestCase):
    def test_doi_satisfies_url(self):
        self.assertNotIn("url", vr.missing_fields(
            {"title": "t", "source": "s", "year": 2024, "doi": "10.1000/abc"}))

    def test_pmid_satisfies_url(self):
        self.assertNotIn("url", vr.missing_fields(
            {"title": "t", "source": "s", "year": 2024, "pmid": "36443570"}))

    def test_nothing_satisfies(self):
        miss = vr.missing_fields({"title": "t", "source": "s", "year": 2024})
        self.assertTrue(any("url" in m for m in miss), miss)

    def test_error_notes_are_chinese(self):
        # 异常处理 4.3 评测项：错误提示必须中文可读
        ok, status, note = vr.check_url("https://nonexistent-domain-xyz-12345.example/x", 3)
        self.assertFalse(ok)
        self.assertTrue(any(ch in note for ch in "网络异常连接失败"),
                        f"错误信息应中文化: {note}")


class TestMedicalProfile(unittest.TestCase):
    def test_medical_tier_expansion(self):
        # 万方：默认层为 blog，medical 预设下升入 journal 层
        url = "https://d.wanfangdata.com.cn/periodical/example"
        self.assertEqual(vr.classify_tier(url, False), "blog")
        self.assertEqual(vr.classify_tier(url, True), "journal")

    def test_medical_offline_capped_at_partial(self):
        ref = {"title": "万方文献", "url": "https://d.wanfangdata.com.cn/periodical/x",
               "source": "期刊", "year": 2024}
        r = vr.verify_one(ref, 1, True, 5.0, medical=True)
        # v1.4 离线封顶：可信层 + 字段完整也不再给 verified
        self.assertEqual(r["verdict"], "partial")
        self.assertEqual(r["tier"], "journal")

    def test_medical_community_caveat(self):
        ref = {"title": "知乎讨论", "url": "https://zhuanlan.zhihu.com/p/123",
               "source": "community", "year": 2024}
        r = vr.verify_one(ref, 1, True, 5.0, medical=True)
        self.assertIn("不得支撑医学结论", r["note"])


class TestExports(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp(prefix="ch_test_")

    def _sample_results(self):
        return [
            {"index": 1, "title": "Real Study", "verdict": "verified", "tier": "journal",
             "http_status": 200, "needs_human_check": False, "year": 2023,
             "source": "Journal", "url": "https://a.b/c", "doi": "", "pmid": "36443570", "note": ""},
            {"index": 2, "title": "Fake Study", "verdict": "invalid", "tier": "-",
             "http_status": None, "needs_human_check": True, "year": 2023,
             "source": "", "url": "", "doi": "", "pmid": "99999999", "note": "编造"},
        ]

    def test_bibtex_verified_only(self):
        p = os.path.join(self.tmp, "out.bib")
        n = vr.export_bibtex(self._sample_results(), p)
        self.assertEqual(n, 1)
        content = open(p, encoding="utf-8").read()
        self.assertIn("@misc{", content)
        self.assertIn("Real Study", content)
        self.assertIn("PMID: 36443570", content)
        self.assertNotIn("Fake", content)

    def test_csv_full_ledger(self):
        p = os.path.join(self.tmp, "out.csv")
        vr.export_csv(self._sample_results(), p)
        lines = open(p, encoding="utf-8-sig").read().strip().splitlines()
        self.assertEqual(len(lines), 3)  # header + 2 rows
        self.assertIn("verdict", lines[0])

    def test_main_export_via_cli(self):
        refs_path = os.path.join(self.tmp, "refs.json")
        with open(refs_path, "w", encoding="utf-8") as f:
            json.dump([{"title": "t", "url": "https://www.nature.com/x",
                        "source": "journal", "year": 2025}], f)
        out = os.path.join(self.tmp, "r.md")
        code = vr.main_with_args(["--refs", refs_path, "--out", out,
                                  "--offline", "--export", "bibtex,csv"])
        self.assertEqual(code, 0)
        self.assertTrue(os.path.exists(os.path.join(self.tmp, "r.bib")))
        self.assertTrue(os.path.exists(os.path.join(self.tmp, "r.csv")))


class TestPubMedEUtilities(unittest.TestCase):
    """在线核验（依赖网络；不可达时跳过）。"""

    def setUp(self):
        try:
            ok, _ = vr.pubmed_pmid_exists("36443570", 8.0)
        except Exception:
            ok = None
        if ok is not True:
            self.skipTest("E-utilities 不可达")

    def test_real_pmid_exists(self):
        ok, note = vr.pubmed_pmid_exists("36443570", 8.0)
        self.assertTrue(ok)
        self.assertIn("核实存在", note)

    def test_fake_pmid_rejected(self):
        ok, note = vr.pubmed_pmid_exists("99999999", 8.0)
        self.assertFalse(ok)
        self.assertIn("编造", note)


class TestV140(unittest.TestCase):
    """v1.4.0：DOI 元数据交叉验证 + --easy 傻瓜模式。"""

    def setUp(self):
        self.tmp = tempfile.mkdtemp(prefix="ch_v140_")

    def _mock_urlopen(self, csl):
        """构造一个假的 urlopen 返回 CSL JSON。"""
        import io
        body = json.dumps(csl).encode("utf-8")

        class FakeResp:
            def __enter__(self):
                return self

            def __exit__(self, *a):
                return False

            def read(self):
                return body
        return FakeResp()

    def test_doi_metadata_match_ok(self):
        real = {"title": ["A landmark study about X"], "issued": {"date-parts": [[2023]]}}
        with unittest.mock.patch.object(vr.urllib.request, "urlopen",
                                        return_value=self._mock_urlopen(real)):
            adjust, note, matched = vr.doi_metadata_match("10.1000/real", "a landmark study about x", 2023, 5)
        self.assertEqual(adjust, "")
        self.assertTrue(matched)
        self.assertIn("一致", note)

    def test_doi_metadata_mismatch_is_invalid(self):
        real = {"title": ["A completely different paper about Y"], "issued": {"date-parts": [[2019]]}}
        with unittest.mock.patch.object(vr.urllib.request, "urlopen",
                                        return_value=self._mock_urlopen(real)):
            adjust, note, matched = vr.doi_metadata_match("10.1000/real", "a landmark study about x", 2023, 5)
        self.assertEqual(adjust, "invalid")
        self.assertTrue(matched)
        self.assertIn("编造或错引", note)

    def test_verify_one_flags_wrong_doi_paper(self):
        real = {"title": ["Some other unrelated paper"], "issued": {"date-parts": [[2020]]}}
        ref = {"title": "A landmark study about X", "doi": "10.1000/real",
               "url": f"https://doi.org/10.1000/real", "source": "journal", "year": 2020}
        with unittest.mock.patch.object(vr.urllib.request, "urlopen",
                                        return_value=self._mock_urlopen(real)):
            r = vr.verify_one(ref, 1, False, 5.0)
        self.assertEqual(r["verdict"], "invalid")
        self.assertTrue(r["needs_human_check"])

    def test_easy_mode_auto_medical_and_export(self):
        refs_path = os.path.join(self.tmp, "refs.json")
        with open(refs_path, "w", encoding="utf-8") as f:
            json.dump([{"title": "real study", "pmid": "36443570",
                        "source": "journal", "year": 2023}], f)
        out = os.path.join(self.tmp, "r.md")
        code = vr.main_with_args(["--refs", refs_path, "--out", out,
                                  "--easy", "--timeout", "10"])
        self.assertEqual(code, 0, "easy 模式应成功")
        self.assertTrue(os.path.exists(os.path.join(self.tmp, "r.bib")), "easy 应自动导出 bibtex")
        self.assertTrue(os.path.exists(os.path.join(self.tmp, "r.csv")), "easy 应自动导出 csv")

    def test_version_bumped(self):
        self.assertEqual(vr.VERSION, "1.4.0")


if __name__ == "__main__":
    unittest.main(verbosity=2)


class TestHardening(unittest.TestCase):
    """评审加固项：非字符串标量、SSRF 防护、导出注入中和、offline 封顶。"""

    def setUp(self):
        self.tmp = tempfile.mkdtemp(prefix="ch_hard_")

    def test_non_string_scalars_do_not_crash_batch(self):
        refs = [{"title": 123, "url": 456, "source": "N", "year": 2024},
                {"title": "ok", "url": "https://www.nature.com/x", "source": "j", "year": 2024}]
        results = run_offline(refs)
        self.assertEqual(results[0]["verdict"], "invalid")
        self.assertEqual(results[1]["verdict"], "partial")

    def test_ssrf_guard_blocks_internal(self):
        reachable, status, note = vr.check_url("http://127.0.0.1:9/x", 3)
        self.assertFalse(reachable)
        self.assertIn("SSRF", note)

    def test_offline_never_awards_verified(self):
        refs = json.load(open(DEMO, encoding="utf-8"))
        results = run_offline(refs)
        self.assertNotIn("verified", [r["verdict"] for r in results])

    def test_bib_brace_stripped_and_keys_unique(self):
        results = [
            {"index": 1, "title": "study } one", "verdict": "verified", "year": 2024,
             "source": "j", "url": "https://a", "pmid": "", "doi": "", "note": ""},
            {"index": 2, "title": "🎉🎉🎉", "verdict": "verified", "year": 2024,
             "source": "j", "url": "https://b", "pmid": "", "doi": "", "note": ""},
            {"index": 3, "title": "🎉🎉🎉", "verdict": "verified", "year": 2024,
             "source": "j", "url": "https://c", "pmid": "", "doi": "", "note": ""},
        ]
        p = os.path.join(self.tmp, "o.bib")
        vr.export_bibtex(results, p)
        content = open(p, encoding="utf-8").read()
        self.assertEqual(content.count("@misc{"), 3)
        self.assertNotIn("} }", content.replace("}}", ""))  # 无逃逸花括号残留
        keys = [ln.split("{")[1].split(",")[0] for ln in content.splitlines() if ln.startswith("@misc")]
        self.assertEqual(len(keys), len(set(keys)), f"citation key 重复: {keys}")

    def test_csv_formula_neutralized(self):
        results = [{"index": 1, "title": "=HYPERLINK(\"https://evil.example\",\"x\")",
                    "verdict": "invalid", "tier": "-", "http_status": None,
                    "needs_human_check": False, "year": 2025, "source": "",
                    "url": "", "doi": "", "pmid": "", "note": ""}]
        p = os.path.join(self.tmp, "o.csv")
        vr.export_csv(results, p)
        row = open(p, encoding="utf-8-sig").read().splitlines()[1]
        self.assertTrue(row.startswith("'\"=H") or "\"'=H" in row or "\"=H" in row,
                        f"公式未中和: {row[:60]}")

    def test_md_note_escaped(self):
        results = [{"index": 1, "title": "t", "url": "a|b", "doi": "", "pmid": "",
                    "source": "", "year": 2025, "tier": "blog", "semantic": "",
                    "verdict": "partial", "http_status": None,
                    "note": "url 非 http(s) 格式: a|b", "needs_human_check": False}]
        md = vr.render_md(results, True)
        self.assertNotIn(" | a|b", md.splitlines()[4] if len(md.splitlines()) > 4 else md)
        self.assertIn("a\|b", md)


if __name__ == "__main__":
    unittest.main(verbosity=2)
