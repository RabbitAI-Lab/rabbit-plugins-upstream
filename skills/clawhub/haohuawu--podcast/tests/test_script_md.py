"""Canaries for script_md — the single source of truth for script.md parsing.

These lock the parsing contract that billing estimates, synthesis, validate and
timeline all depend on. If a refactor changes any of these, a test must go red.
"""

import pytest
from script_md import (parse_podcast_script, parse_by_segments, read_title,
                       is_host, is_narration, is_known_speaker)
from tutils import make_script, write_script, CLOSING_LINE


def parse_text(tmp_path, text):
    return parse_podcast_script(str(write_script(tmp_path, text)))


def test_canonical_script_segments_in_order(tmp_path):
    segs = parse_text(tmp_path, make_script())
    speakers = [s for s, _ in segs]
    # 末尾的"主持人"来自 H2 收尾行（BUG-6 修复后收尾句进入合成）
    assert speakers == ["主持人", "嘉宾", "旁白", "主持人", "嘉宾", "主持人"]
    assert segs[0][1] == "欢迎收听本期节目。今天我们聊一个话题。"


def test_fullwidth_and_halfwidth_colons_equivalent(tmp_path):
    half = parse_text(tmp_path, "**主持人**: 你好。")
    full = parse_text(tmp_path, "**主持人**：你好。")
    assert half == full == [("主持人", "你好。")]


def test_continuation_lines_are_joined(tmp_path):
    text = "**嘉宾**: 第一行。\n第二行继续。\n\n**主持人**: 下一轮。"
    segs = parse_text(tmp_path, text)
    assert segs[0] == ("嘉宾", "第一行。 第二行继续。")
    assert segs[1] == ("主持人", "下一轮。")


def test_blank_line_terminates_continuation(tmp_path):
    text = "**嘉宾**: 第一行。\n\n游离的裸文本不属于任何人。"
    segs = parse_text(tmp_path, text)
    assert segs == [("嘉宾", "第一行。")]


def test_headings_quotes_bullets_hr_are_skipped(tmp_path):
    text = (
        "# 标题\n\n## 第 1 段 · 开场\n\n> 引用不读\n\n* 列表不读\n\n---\n\n"
        "**主持人**: 只有这句。\n"
    )
    segs = parse_text(tmp_path, text)
    assert segs == [("主持人", "只有这句。")]


def test_heading_breaks_continuation(tmp_path):
    text = "**嘉宾**: 第一行。\n## 第 2 段 · 插入标题\n不该拼进上一段的行。"
    segs = parse_text(tmp_path, text)
    assert segs[0] == ("嘉宾", "第一行。")


def test_empty_text_speaker_line_dropped(tmp_path):
    segs = parse_text(tmp_path, "**主持人**:\n\n**嘉宾**: 有内容。")
    assert segs == [("嘉宾", "有内容。")]


def test_unknown_speaker_is_parsed_as_segment(tmp_path):
    # Current contract: parser accepts any bold speaker; routing decides the voice.
    # validate_podcast is the layer that must flag unknown speakers (see BUG-11).
    segs = parse_text(tmp_path, "**作者**: 未知角色的台词。")
    assert segs == [("作者", "未知角色的台词。")]


def test_closing_heading_line_is_synthesized(tmp_path):
    # BUG-6 修复：H2 收尾行（## **主持人**：感谢收听…）剥掉标题标记后按说话人行合成
    segs = parse_text(tmp_path, make_script(closing=True))
    assert segs[-1][0] == "主持人"
    assert "感谢收听" in segs[-1][1]


def test_role_predicates():
    assert is_host("主持人") and is_host("Host") and is_host(" host ")
    assert not is_host("嘉宾")
    assert is_narration("旁白") and is_narration("Narrator") and is_narration("narration")
    assert not is_narration("主持人")
    assert is_known_speaker("嘉宾") and is_known_speaker("Guest")
    assert not is_known_speaker("作者")


class TestParseBySegments:
    """时间轴用的分段视图：行级语义必须与 parse_podcast_script 完全一致。"""

    def test_segment_grouping(self, tmp_path):
        path = write_script(tmp_path)
        segs = parse_by_segments(str(path))
        assert [t for t, _ in segs] == ["开场", "主体"]
        assert [s for s, _ in segs[0][1]] == ["主持人", "嘉宾"]
        # 收尾行（H2 说话人行）归属最后一个分段
        assert segs[1][1][-1][0] == "主持人"
        assert "感谢收听" in segs[1][1][-1][1]

    def test_flat_and_grouped_views_agree(self, tmp_path):
        # 同一迭代器的两种视图：拍平 grouped 必须等于 flat（防止语义再度分叉）
        path = write_script(tmp_path)
        flat = parse_podcast_script(str(path))
        grouped = [line for _, lines in parse_by_segments(str(path)) for line in lines]
        assert grouped == flat

    def test_continuation_counted_in_segments(self, tmp_path):
        text = make_script(segments=[("第 1 段 · 甲", [("嘉宾", "第一行。")])], closing=False)
        text = text.replace("第一行。", "第一行。\n续行也算这一段的正文。")
        segs = parse_by_segments(str(write_script(tmp_path, text)))
        assert segs[0][1][0][1] == "第一行。 续行也算这一段的正文。"

    def test_dialogue_before_first_heading_goes_to_untitled_bucket(self, tmp_path):
        text = "**主持人**: 开场白在任何分段之前。\n\n## 第 1 段 · 正题\n\n**嘉宾**: 正文。\n"
        segs = parse_by_segments(str(write_script(tmp_path, text)))
        assert segs[0][0] == "" and segs[0][1] == [("主持人", "开场白在任何分段之前。")]
        assert segs[1][0] == "正题"


class TestReadTitle:
    def test_plain_title(self, tmp_path):
        p = tmp_path / "s.md"
        p.write_text("# My Title -- 副标题\n\n正文", encoding="utf-8")
        assert read_title(p) == "My Title -- 副标题"

    def test_legacy_prefix_stripped(self, tmp_path):
        p = tmp_path / "s.md"
        p.write_text("# 播客脚本：My Title\n", encoding="utf-8")
        assert read_title(p) == "My Title"

    def test_fallback_to_stem(self, tmp_path):
        p = tmp_path / "some_name.md"
        p.write_text("没有标题行", encoding="utf-8")
        assert read_title(p) == "some_name"
