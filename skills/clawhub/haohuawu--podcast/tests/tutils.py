"""Shared test utilities: script/notes builders and the fake Doubao TTS transport.

Mock policy for the suite (keep it uniform, do not ad-hoc elsewhere):
  - TOS boundary   -> fake_tos injected as sys.modules["tos"]        (conftest)
  - TTS HTTP       -> FakeTTSTransport monkeypatched onto session.post (here)
  - ffmpeg/ffprobe -> monkeypatch script_synthesis._run_ffmpeg / get_duration_seconds
                      in the test itself; never shell out in unit tests
"""

import json
from contextlib import contextmanager
from pathlib import Path
from typing import List, Optional

import pytest


@contextmanager
def assert_exits_nonzero():
    """SystemExit(0) 也能骗过裸的 pytest.raises(SystemExit)——
    所有"必须失败拦截"的断言一律用本 helper 锁定非零退出码。"""
    with pytest.raises(SystemExit) as e:
        yield
    assert e.value.code not in (0, None), \
        f"expected non-zero exit code, got {e.value.code!r}"

# ---------- script.md / notes.md builders ----------

CANONICAL_TITLE = "Test Episode -- 中文副标题"

CANONICAL_SEGMENTS = [
    ("第 1 段 · 开场", [
        ("主持人", "欢迎收听本期节目。今天我们聊一个话题。"),
        ("嘉宾", "好的，我们开始。"),
    ]),
    ("第 2 段 · 主体", [
        ("旁白", "往下听之前，先解释一个词。好，回到对话。"),
        ("主持人", "第一个问题。"),
        ("嘉宾", "第一个回答，内容比较长，有细节。"),
    ]),
]

CLOSING_LINE = "## **主持人**：感谢收听，完整原文列表在 show notes 里。我们下期见"


def make_script(title: str = CANONICAL_TITLE, segments=None, closing: bool = True) -> str:
    """Build a spec-compliant script.md; segments = [(seg_title, [(speaker, text), ...])]."""
    segments = CANONICAL_SEGMENTS if segments is None else segments
    out = [f"# {title}", ""]
    for seg_title, lines in segments:
        out.append(f"## {seg_title}")
        out.append("")
        for speaker, text in lines:
            out.append(f"**{speaker}**: {text}")
            out.append("")
    if closing:
        out.append(CLOSING_LINE)
        out.append("")
    return "\n".join(out)


def write_script(tmp_path: Path, text: Optional[str] = None, name: str = "script.md") -> Path:
    p = tmp_path / name
    p.write_text(make_script() if text is None else text, encoding="utf-8")
    return p


def make_notes(first_line: str = "本期聊测试。一句话主线：测试是地基。",
               sections=("**内容速览**", "**时间轴**", "**原文链接**"),
               timeline_entries=("- 00:00 开场", "- 02:00 主体")) -> str:
    out = [first_line, ""]
    for sec in sections:
        out.append(sec)
        out.append("")
        if sec == "**时间轴**":
            out.extend(timeline_entries)
            out.append("")
        elif sec == "**内容速览**":
            out.append("- 要点一")
            out.append("")
        else:
            out.append("- [原文](https://example.com/a)")
            out.append("")
    return "\n".join(out)


# ---------- fake Doubao TTS HTTP transport ----------

class FakeHTTPResponse:
    def __init__(self, status_code: int = 200, lines: Optional[List[bytes]] = None,
                 text: str = ""):
        self.status_code = status_code
        self._lines = lines or []
        self.text = text

    def iter_lines(self):
        yield from self._lines


def ndjson(events: List[dict]) -> List[bytes]:
    return [json.dumps(e).encode("utf-8") for e in events]


def tts_ok_events(audio_parts: List[bytes]) -> List[dict]:
    """Normal stream: N data chunks then the terminal code=0 event."""
    import base64
    events = [{"data": base64.b64encode(p).decode()} for p in audio_parts]
    events.append({"code": 0})
    return events


class FakeTTSTransport:
    """Scripted replacement for requests.Session.post.

    responses: list of FakeHTTPResponse (or callables returning one), consumed per call;
    the last entry repeats if more calls arrive. Records every call's payload.
    """

    def __init__(self, responses: List):
        assert responses, "FakeTTSTransport needs at least one scripted response"
        self._responses = list(responses)
        self.calls: List[dict] = []   # each: {"url":..., "headers":..., "json":...}

    def __call__(self, url, headers=None, json=None, stream=None, timeout=None):
        self.calls.append({"url": url, "headers": headers, "json": json})
        resp = self._responses.pop(0) if len(self._responses) > 1 else self._responses[0]
        if len(self._responses) == 0:
            self._responses.append(resp)
        return resp() if callable(resp) else resp

    # -- convenience accessors --
    @property
    def last_req_params(self) -> dict:
        return self.calls[-1]["json"]["req_params"]


def install_fake_tts(monkeypatch, tts, responses: List) -> FakeTTSTransport:
    transport = FakeTTSTransport(responses)
    monkeypatch.setattr(tts._session, "post", transport)
    return transport
