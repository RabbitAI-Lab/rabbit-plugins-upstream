"""validate_podcast rules: the quality gate must itself be trustworthy."""

import pytest
from validate_podcast import validate_script, validate_notes
from tutils import make_script, make_notes, write_script


def check_script(tmp_path, text):
    return validate_script(str(write_script(tmp_path, text)))


def check_notes(tmp_path, text):
    p = tmp_path / "notes.md"
    p.write_text(text, encoding="utf-8")
    return validate_notes(str(p))


class TestScriptRules:
    def test_canonical_script_passes(self, tmp_path):
        assert check_script(tmp_path, make_script()) == []

    def test_missing_title_flagged(self, tmp_path):
        text = make_script().replace("# Test Episode -- 中文副标题\n", "")
        assert any("标题" in i for i in check_script(tmp_path, text))

    def test_missing_closing_flagged(self, tmp_path):
        issues = check_script(tmp_path, make_script(closing=False))
        assert any("收尾" in i for i in issues)

    def test_missing_segments_flagged(self, tmp_path):
        text = "# 标题\n\n**主持人**: 无分段。\n\n感谢收听，show notes，我们下期见\n"
        assert any("分段" in i for i in check_script(tmp_path, text))

    def test_old_segment_format_flagged(self, tmp_path):
        text = make_script().replace("## 第 1 段 · 开场", "## 第 1 段：开场")
        assert any("中点" in i or "·" in i for i in check_script(tmp_path, text))

    def test_narration_at_segment_head_ok(self, tmp_path):
        assert check_script(tmp_path, make_script()) == []  # canonical has head narration

    def test_narration_mid_dialogue_flagged(self, tmp_path):
        segments = [("第 1 段 · 开场", [
            ("主持人", "先问一个问题。"),
            ("旁白", "插在中间的旁白。"),
            ("嘉宾", "回答。"),
        ])]
        issues = check_script(tmp_path, make_script(segments=segments))
        assert any("问答中间" in i for i in issues)

    def test_old_title_prefix_reported_not_crash(self, tmp_path):
        # BUG-1 修复：旧格式标题报告为不合规项，而不是 NameError 崩溃
        text = make_script(title="播客脚本：某期标题").replace(
            "# 播客脚本：某期标题", "# 播客脚本：某期标题")
        issues = check_script(tmp_path, text)
        assert any("播客脚本" in i for i in issues)

    def test_unknown_speaker_flagged(self, tmp_path):
        # BUG-11 修复：白名单外角色报错，不再静默落到嘉宾音色
        segments = [("第 1 段 · 开场", [("作者", "未知角色。"), ("主持人", "正常。")])]
        issues = check_script(tmp_path, make_script(segments=segments))
        assert any("作者" in i for i in issues)

    def test_title_format_english_dash_chinese(self, tmp_path):
        issues = check_script(tmp_path, make_script(title="纯中文标题没有分隔"))
        assert any("English" in i or " -- " in i for i in issues)
        assert check_script(tmp_path, make_script(title="Good Title -- 合规副标题")) == []

    def test_too_many_narrations_flagged(self, tmp_path):
        seg = [(f"第 {i+1} 段 · 段{i+1}",
                [("旁白", f"第{i+1}段旁白。好，回到对话。"), ("主持人", "正文。")])
               for i in range(5)]
        issues = check_script(tmp_path, make_script(segments=seg))
        assert any("上限" in i for i in issues)

    def test_narration_missing_closing_phrase_flagged(self, tmp_path):
        segments = [("第 1 段 · 开场", [("旁白", "没有收束句的旁白。"), ("主持人", "正文。")])]
        issues = check_script(tmp_path, make_script(segments=segments))
        assert any("收束句" in i for i in issues)

    def test_url_in_dialogue_flagged(self, tmp_path):
        segments = [("第 1 段 · 开场",
                     [("嘉宾", "详见 https://example.com/paper 这篇论文。")])]
        issues = check_script(tmp_path, make_script(segments=segments))
        assert any("URL" in i for i in issues)


class TestNotesRules:
    def test_canonical_notes_pass(self, tmp_path):
        assert check_notes(tmp_path, make_notes()) == []

    def test_first_line_rule(self, tmp_path):
        issues = check_notes(tmp_path, make_notes(first_line="随便写的首行"))
        assert any("本期" in i for i in issues)

    def test_image_first_line_allowed(self, tmp_path):
        text = "![cover](https://e.com/c.png)\n\n" + make_notes()
        assert check_notes(tmp_path, text) == []

    def test_missing_sections_flagged(self, tmp_path):
        text = make_notes(sections=("**时间轴**",))
        issues = check_notes(tmp_path, text)
        assert any("内容速览" in i for i in issues)
        assert any("原文链接" in i for i in issues)

    def test_empty_timeline_flagged(self, tmp_path):
        text = make_notes(timeline_entries=())
        assert any("时间轴" in i for i in check_notes(tmp_path, text))

    def test_top_level_heading_flagged(self, tmp_path):
        text = "# 大标题\n\n" + make_notes()
        assert any("顶级标题" in i for i in check_notes(tmp_path, text))
