#!/usr/bin/env python3
"""script.md 的唯一事实解析层（纯标准库，零三方依赖）。

synthesis / validate / timeline 三个工具对同一份 script.md 必须给出同一种理解——
说话人行的判定、续行语义、收尾 H2 行的特判、旁白节奏常量，全部只在这里定义。
历史教训：三处各写一份解析器后语义分叉（续行被 timeline 丢弃、未知角色静默落到
嘉宾音色），估算/校验/合成三方对不上。

计费/缓存注意：parse_podcast_script 的输出是 TTS 计费与分片缓存 key 的上游，
这里的行为变更会使缓存失效、计费口径漂移——改动前先看 tests/test_script_md.py。
"""

import re
from pathlib import Path
from typing import List, Tuple

# ===== 角色 =====

HOST_ALIASES = {"主持人", "host"}
GUEST_ALIASES = {"嘉宾", "guest"}
NARRATION_ALIASES = {"旁白", "narration", "narrator"}
KNOWN_SPEAKERS = HOST_ALIASES | GUEST_ALIASES | NARRATION_ALIASES


def is_host(speaker: str) -> bool:
    return speaker.strip().lower() in HOST_ALIASES


def is_narration(speaker: str) -> bool:
    return speaker.strip().lower() in NARRATION_ALIASES


def is_known_speaker(speaker: str) -> bool:
    return speaker.strip().lower() in KNOWN_SPEAKERS


# ===== 旁白节奏常量（synthesis 实际使用；timeline 由此推导估算，不得另抄一份）=====

NARRATION_SPEECH_RATE = 0           # 正常语速——区分度交给广播话筒音色链 + 拍话筒提示音
NARRATION_CONTEXT_TEXTS = ["用平缓低沉的纪录片旁白解说腔，语气克制，收尾自然渐弱"]
NARRATION_GAIN_DB = -3.0            # 旁白轨 -3dB
NARRATION_LEAD_SILENCE_MS = 800     # 对话 → 旁白 进场静音 ms
NARRATION_TAIL_SILENCE_MS = 1200    # 旁白 → 对话 退场静音 ms（收束句后多给一拍，消割裂感）
NORMAL_SILENCE_MS = 250             # 普通轮间静音 ms

# ===== 行级正则 =====

SPEAKER_LINE_RE = re.compile(r'\*\*([^*]+?)\*\*[：:](.*)')
# 收尾行按规范是 H2 标题（## **主持人**：感谢收听…），需要被朗读
HEADING_SPEAKER_RE = re.compile(r'#{1,6}\s+(\*\*[^*]+?\*\*[：:].*)')
SEGMENT_RE = re.compile(r'^##\s+第\s*(\d+)\s*段\s*[·•・]\s*(.+)$')


def read_title(script_path) -> str:
    """脚本标题（容忍旧格式'播客脚本:'前缀，读取时剥掉）。"""
    script_path = Path(script_path)
    content = script_path.read_text(encoding="utf-8")
    m = re.search(r'^#\s+(?:播客脚本[：:]\s*)?(.+)', content, re.MULTILINE)
    return m.group(1).strip() if m else script_path.stem


def _iter_dialogue_lines(content: str):
    """底层行迭代器：yield ("segment", 标题) / ("speaker", 说话人, 首行文本) / ("cont", 文本)。

    语义（三工具共享的唯一定义）：
    - `**角色**：文本` 开启一段台词；全角/半角冒号等价；角色名不设白名单（由 validate 把关）
    - 说话人行之后的裸文本行是续行，拼入上一段；空行/标题/引用/列表/分隔线终止续行
    - H2 收尾行（## **角色**：…）剥掉标题标记后按说话人行处理
    - 其余 #/>/*/--- 行跳过
    """
    for line in content.split("\n"):
        stripped = line.strip()

        m_heading_speaker = HEADING_SPEAKER_RE.match(stripped)
        if m_heading_speaker:
            stripped = m_heading_speaker.group(1)
        else:
            m_seg = SEGMENT_RE.match(stripped)
            if m_seg:
                yield ("segment", m_seg.group(2).strip())
                continue
            if stripped.startswith(("#", ">", "* ")) or stripped == "---":
                yield ("break",)
                continue
            if stripped == "":
                yield ("break",)
                continue

        m = SPEAKER_LINE_RE.match(stripped)
        if m:
            yield ("speaker", m.group(1).strip(), m.group(2).strip())
        else:
            yield ("cont", stripped)


def parse_podcast_script(filepath) -> List[Tuple[str, str]]:
    """解析播客脚本，返回 (speaker, text) 扁平列表（合成/计费用）。"""
    content = Path(filepath).read_text(encoding="utf-8")

    segments: List[Tuple[str, str]] = []
    current_speaker = None
    current_text: List[str] = []

    def flush():
        nonlocal current_speaker, current_text
        if current_speaker and current_text:
            segments.append((current_speaker, " ".join(current_text).strip()))
        current_speaker = None
        current_text = []

    for ev in _iter_dialogue_lines(content):
        kind = ev[0]
        if kind == "speaker":
            flush()
            current_speaker = ev[1]
            if ev[2]:
                current_text.append(ev[2])
        elif kind == "cont":
            if current_speaker:
                current_text.append(ev[1])
        else:  # segment / break
            flush()

    flush()
    return [(s, t) for s, t in segments if t]


def parse_by_segments(filepath) -> List[Tuple[str, List[Tuple[str, str]]]]:
    """按分段分组解析，返回 [(segment_title, [(speaker, text), ...]), ...]（时间轴用）。

    行级语义与 parse_podcast_script 完全一致（同一迭代器），只是按段分桶；
    首个分段标题之前的台词落入 "" 标题桶。
    """
    content = Path(filepath).read_text(encoding="utf-8")

    result: List[Tuple[str, List[Tuple[str, str]]]] = []
    current_title = ""
    current_lines: List[Tuple[str, str]] = []
    current_speaker = None
    current_text: List[str] = []

    def flush_line():
        nonlocal current_speaker, current_text
        if current_speaker and current_text:
            current_lines.append((current_speaker, " ".join(current_text).strip()))
        current_speaker = None
        current_text = []

    def flush_segment(new_title):
        nonlocal current_title, current_lines
        flush_line()
        if current_title or current_lines:
            result.append((current_title, current_lines))
        current_title = new_title
        current_lines = []

    for ev in _iter_dialogue_lines(content):
        kind = ev[0]
        if kind == "segment":
            flush_segment(ev[1])
        elif kind == "speaker":
            flush_line()
            current_speaker = ev[1]
            if ev[2]:
                current_text.append(ev[2])
        elif kind == "cont":
            if current_speaker:
                current_text.append(ev[1])
        else:  # break
            flush_line()

    flush_segment("")
    return [(title, [(s, t) for s, t in lines if t]) for title, lines in result]
