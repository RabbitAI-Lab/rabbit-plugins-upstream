"""generate_timeline: estimation/calibration invariants and cross-tool consistency."""

import pytest
import generate_timeline as gt
from tutils import make_script, write_script


def test_format_timestamp():
    assert gt.format_timestamp(0) == "00:00"
    assert gt.format_timestamp(65) == "01:05"
    assert gt.format_timestamp(3600) == "60:00"


def test_estimate_per_segment_positive_and_ordered(tmp_path):
    path = write_script(tmp_path)
    timeline = gt.estimate_timeline(str(path))
    assert [t for t, _ in timeline] == ["开场", "主体"]
    assert all(s >= 1 for _, s in timeline)


def test_narration_estimated_slower_than_normal(tmp_path):
    text_line = "这句话固定长度用来对比估算时长设定。"
    normal = make_script(segments=[("第 1 段 · 甲", [("主持人", text_line)])], closing=False)
    narr = make_script(segments=[("第 1 段 · 甲", [("旁白", text_line)])], closing=False)
    n = gt.estimate_timeline(str(write_script(tmp_path, normal, name="a.md")))[0][1]
    m = gt.estimate_timeline(str(write_script(tmp_path, narr, name="b.md")))[0][1]
    assert m > n  # 旁白慢速 + 前后静音，估算必须更长


def test_continuation_lines_counted(tmp_path):
    # BUG-8 修复：timeline 改用 script_md.parse_by_segments，续行语义与 synthesis 一致
    single = make_script(segments=[("第 1 段 · 甲", [("嘉宾", "第一行内容。")])], closing=False)
    contd = single.replace("第一行内容。", "第一行内容。\n这是续行，也是要读出来的正文，字数不少。")
    a = gt.estimate_timeline(str(write_script(tmp_path, single, name="a.md")))[0][1]
    b = gt.estimate_timeline(str(write_script(tmp_path, contd, name="b.md")))[0][1]
    assert b > a


class TestCalibrate:
    def _calibrate(self, tmp_path, monkeypatch, total, n_segments=20):
        line = "这一段的台词长度完全一样，用来构造均匀的估算分布，检验取整误差。"
        segments = [(f"第 {i+1} 段 · 段{i+1}", [("主持人", line)]) for i in range(n_segments)]
        path = write_script(tmp_path, make_script(segments=segments, closing=False))
        monkeypatch.setattr(gt, "get_duration_seconds", lambda _: total)
        return gt.calibrate_timeline(str(path), "fake.mp3")

    def test_starts_at_zero_and_monotonic(self, tmp_path, monkeypatch):
        timeline = self._calibrate(tmp_path, monkeypatch, total=1200)
        starts = [s for _, s in timeline]
        assert starts[0] == 0
        assert starts == sorted(starts)

    def test_rounding_drift_bounded(self, tmp_path, monkeypatch):
        # BUG-7 修复：起点按累计比例整体折算，取整误差不再累积
        total = 1999
        timeline = self._calibrate(tmp_path, monkeypatch, total=total, n_segments=20)
        # 末段起点的理论值 = total * 19/20 ≈ 1899；漂移应在 ±1s 内
        assert abs(timeline[-1][1] - round(total * 19 / 20)) <= 1
