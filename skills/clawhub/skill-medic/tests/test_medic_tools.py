"""SkillMedic 判据回归测试（标准库 unittest，零第三方依赖）。

跑法：
    python -m unittest discover -s tests -v
    python tests/test_medic_tools.py

覆盖范围：
1. 关键词提取质量——纯数字、分词残片、跨词碎片不得进入语义信号
2. C1/C2 冲突判定——阈值边界不得回退到「人人有冲突」的过报状态
3. 分类与生命周期——静态初值的域映射与 mtime 兜底
4. 规模分档边界
"""

import os
import sys
import tempfile
import time
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from medic_tools import run as R


class TestKeywordExtraction(unittest.TestCase):
    """关键词是 C1/C2 判定的唯一输入源，噪声会直接放大成假冲突。"""

    def test_pure_digits_dropped(self):
        """纯数字（年份/版本号/计数）不构成语义信号。"""
        kws = R.extract_keywords("2024 年 10 次 9704 条 49 种")
        self.assertTrue(kws, "不应把所有词都过滤掉")
        self.assertEqual([k for k in kws if k.isdigit()], [])

    def test_alnum_token_kept(self):
        """含字母的短 token 保留（v6 / gpt4 / 3d 有区分度）。"""
        kws = R.extract_keywords("v6 gpt4 3d")
        for tok in ("v6", "gpt4", "3d"):
            self.assertIn(tok, kws)

    def test_single_char_ascii_dropped(self):
        kws = R.extract_keywords("a b cc")
        self.assertNotIn("a", kws)
        self.assertNotIn("b", kws)
        self.assertIn("cc", kws)

    def test_cross_word_fragment_dropped(self):
        """跨词碎片（边界落在结构虚词上）应被丢弃。"""
        kws = R.extract_keywords("检查错误与去重效果，以及完成的结论")
        for frag in ("与去", "的完", "的结", "以及"):
            self.assertNotIn(frag, kws)

    def test_fragment_table_dropped(self):
        """已知分词残片（多字词被切半）应被丢弃。"""
        kws = R.extract_keywords("核心能力 生命周期 接力棒 持久化 输出结果")
        for frag in ("心能", "命周", "力棒", "出结"):
            self.assertNotIn(frag, kws)

    def test_meaningful_bigrams_kept(self):
        """真正的业务词不能被误杀。"""
        kws = R.extract_keywords("报表 看板 公文 润色 演示文稿")
        for word in ("报表", "看板", "公文", "润色"):
            self.assertIn(word, kws)

    def test_stopword_bigrams_dropped(self):
        """模板词不参与相似度计算。"""
        kws = R.extract_keywords("适用于各种场景，你可以通过系统分析处理")
        for w in ("适用", "场景", "可以", "通过", "系统", "分析"):
            self.assertNotIn(w, kws)

    def test_lowercased(self):
        kws = R.extract_keywords("AUTHENTICATION Token")
        self.assertIn("authentication", kws)
        self.assertIn("token", kws)


class TestRankKeywords(unittest.TestCase):
    def test_long_words_first(self):
        """展示位优先给长词：短噪声曾长期占据前排。"""
        ranked = R.rank_keywords({"ab", "abcd", "abcdef"}, limit=2)
        self.assertEqual(ranked, ["abcdef", "abcd"])

    def test_limit_applied(self):
        self.assertEqual(len(R.rank_keywords({"报表", "看板", "公文"}, limit=2)), 2)

    def test_stable_order_within_same_length(self):
        self.assertEqual(R.rank_keywords({"乙乙", "甲甲"}), ["乙乙", "甲甲"])


def _skill(name, desc, status="active", **extra):
    d = {"name": name, "description": desc, "status": status, "path": ""}
    d.update(extra)
    return d


class TestConflictThresholds(unittest.TestCase):
    """阈值回退会让报告出现「12 个技能 24 组抢占」的伪结论。"""

    def test_near_duplicate_hits_c1(self):
        """高重合描述应判 C1（同质），而非悄悄降级为 C2。"""
        desc = "公文写作助手，支持公文起草与润色，遵循国标格式，可评估文稿质量"
        inv = [_skill("a", desc), _skill("b", desc)]
        res = R.build_conflict_candidates("", inv, {"a": "写作编排", "b": "写作编排"})
        self.assertEqual(len(res["C1"]), 1, "完全相同的描述必须判同质冲突")
        self.assertEqual(res["C1"][0]["severity"], "candidate")

    def test_low_jaccard_not_reported_as_c2(self):
        """交集够但相似度极低的对不报 C2（长描述天然交集多，属噪声）。"""
        shared = "公文写作润色起草撰文"
        filler = ("山川日月星辰云雨雷电风雪天地江河湖海花草树木鸟兽虫鱼"
                  "金石土木水火风霜露雾虹霞峰岭崖谷溪涧泉潭湖泊海洋")
        inv = [
            _skill("a", shared + filler * 3),
            _skill("b", shared),
        ]
        res = R.build_conflict_candidates("", inv, {"a": "写作编排", "b": "写作编排"})
        self.assertEqual(res["C2"], [], "jaccard 低于下限不应判意图抢占")

    def test_c2_threshold_constant_guarded(self):
        """守护常量：删掉 jaccard 下限等于恢复过报。"""
        self.assertTrue(hasattr(R, "C2_MIN_JACCARD"))
        self.assertGreater(R.C2_MIN_JACCARD, 0)
        self.assertLess(R.C2_MIN_JACCARD, 1)

    def test_anti_trigger_suppresses_c2(self):
        """双方都写了反触发说明的对，优先级让给更具体的 Skill，不报 C2。"""
        desc = "技能清单扫描与分类统计，输出看板报表"
        anti = desc + "，不适用创意写作与代码生成"
        inv = [_skill("a", anti), _skill("b", anti)]
        res = R.build_conflict_candidates("", inv, {"a": "数据分析报表", "b": "数据分析报表"})
        self.assertEqual(res["C2"], [])

    def test_result_shape_stable(self):
        """下游 report/prescribe 依赖固定键名。"""
        inv = [_skill("a", "公文写作润色"), _skill("b", "公文写作润色")]
        res = R.build_conflict_candidates("", inv)
        for k in ("C1", "C2", "C3", "C4", "C5"):
            self.assertIn(k, res)
        if res["C1"]:
            for key in ("skill_a", "skill_b", "type", "jaccard", "overlap_count", "keywords"):
                self.assertIn(key, res["C1"][0])


class TestClassify(unittest.TestCase):
    def test_presentation_domain(self):
        """演示文稿生成类曾误判为系统探索采集。"""
        s = _skill("sz-html", "HTML 演示文稿生成助手，按风格资产产出 PPT 与汇报页")
        self.assertEqual(R.classify_skill(s, "")["domain_hint"], "演示文稿")

    def test_writing_domain(self):
        s = _skill("sz-writer", "公文写作助手，支持起草、润色与改写")
        self.assertEqual(R.classify_skill(s, "")["domain_hint"], "写作编排")

    def test_english_game_design_domain(self):
        """英文描述需要英文关键词，否则会被 PPT 之类的缩写带偏。"""
        s = _skill("gdd", "Generates professional Game Design Documents (GDD) as .docx and .pdf")
        self.assertEqual(R.classify_skill(s, "")["domain_hint"], "设计创意")

    def test_no_hint_when_nothing_matches(self):
        s = _skill("x", "完全无关的一段占位文本")
        self.assertIsNone(R.classify_skill(s, "")["domain_hint"])

    def test_lifecycle_by_changelog(self):
        s = _skill("x", "描述", has_changelog=True)
        self.assertEqual(R.classify_skill(s, "")["lifecycle"], "活跃维护")

    def test_lifecycle_recent_mtime_without_changelog(self):
        """无 CHANGELOG 但近期改过 SKILL.md，不应判停滞。"""
        s = _skill("x", "描述", has_changelog=False, mtime=time.time())
        self.assertEqual(R.classify_skill(s, "")["lifecycle"], "活跃维护")

    def test_lifecycle_stale(self):
        s = _skill("x", "描述", has_changelog=False, mtime=time.time() - 86400 * 400)
        self.assertEqual(R.classify_skill(s, "")["lifecycle"], "维护停滞")

    def test_design_phase_detected(self):
        with tempfile.TemporaryDirectory() as td:
            open(os.path.join(td, "_design.md"), "w", encoding="utf-8").close()
            s = _skill("x", "描述", has_changelog=False, path=td)
            self.assertEqual(R.classify_skill(s, "")["lifecycle"], "开发中")


class TestScale(unittest.TestCase):
    def test_boundaries(self):
        cases = {0: "S1", 20: "S1", 21: "S2", 80: "S2", 81: "S3", 300: "S3", 301: "S4"}
        for n, expect in cases.items():
            self.assertEqual(R.scale_of(n), expect, f"{n} 个活跃 Skill 应为 {expect}")


class TestFrontmatter(unittest.TestCase):
    def test_parses_skill_md(self):
        here = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        content, err = R.read_file_safe(os.path.join(here, "SKILL.md"))
        self.assertIsNone(err)
        fm = R.parse_frontmatter(content)
        for key in ("name", "version", "description", "license"):
            self.assertIn(key, fm, f"frontmatter 缺 {key}")
        self.assertIn("Use when", fm["description"])
        self.assertIn("Skip for", fm["description"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
