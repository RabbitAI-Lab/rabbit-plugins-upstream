"""DoubaoTTS client behavior against the scripted fake transport.

Covers: happy path, mid-stream error semantics, retry counting, narration
params (future cache-key fields), and the truncated-stream bug (BUG-2).
"""

import base64
import json
from pathlib import Path

import pytest
from tutils import (FakeHTTPResponse, FakeTTSTransport, install_fake_tts,
                    ndjson, tts_ok_events)


def ok_response(parts):
    return FakeHTTPResponse(lines=ndjson(tts_ok_events(parts)))


class TestChunkSynthesis:
    def test_happy_path_concats_chunks_single_call(self, tts, monkeypatch):
        t = install_fake_tts(monkeypatch, tts, [ok_response([b"AB", b"CD"])])
        audio = tts._synthesize_chunk("你好。", "voice-host")
        assert audio == b"ABCD"
        assert len(t.calls) == 1

    def test_mid_stream_error_returns_none(self, tts, monkeypatch):
        # 部分 data 后流内报错（敏感词/配额）：绝不能拿截断音频当成功
        events = [{"data": base64.b64encode(b"AB").decode()},
                  {"code": 55000001, "message": "sensitive"}]
        install_fake_tts(monkeypatch, tts, [FakeHTTPResponse(lines=ndjson(events))])
        assert tts._synthesize_chunk("你好。", "voice-host") is None

    def test_http_error_returns_none(self, tts, monkeypatch):
        install_fake_tts(monkeypatch, tts, [FakeHTTPResponse(status_code=500, text="boom")])
        assert tts._synthesize_chunk("你好。", "voice-host") is None

    def test_truncated_stream_without_terminal_event_fails(self, tts, monkeypatch):
        # BUG-2 修复：无终止 code=0 事件的流按失败处理，截断音频绝不当成功
        events = [{"data": base64.b64encode(b"AB").decode()}]  # no terminal {"code": 0}
        install_fake_tts(monkeypatch, tts, [FakeHTTPResponse(lines=ndjson(events))])
        assert tts._synthesize_chunk("你好。", "voice-host") is None

    def test_narration_payload_carries_rate_and_context(self, tts, monkeypatch):
        from script_md import NARRATION_SPEECH_RATE
        t = install_fake_tts(monkeypatch, tts, [ok_response([b"X"])])
        tts._synthesize_chunk("旁白句。", "voice-host", is_narration=True)
        rp = t.last_req_params
        assert rp["audio_params"]["speech_rate"] == NARRATION_SPEECH_RATE
        assert "旁白" in json.loads(rp["additions"])["context_texts"][0]

    def test_normal_payload_has_no_narration_params(self, tts, monkeypatch):
        t = install_fake_tts(monkeypatch, tts, [ok_response([b"X"])])
        tts._synthesize_chunk("普通句。", "voice-guest")
        rp = t.last_req_params
        assert "speech_rate" not in rp["audio_params"]
        assert "additions" not in rp


class TestRetry:
    def test_retry_then_success(self, tts, monkeypatch, no_sleep):
        t = install_fake_tts(monkeypatch, tts, [
            FakeHTTPResponse(status_code=500, text="flaky"),
            ok_response([b"OK"]),
        ])
        assert tts._chunk_with_retry("你好。", "voice-host") == b"OK"
        assert len(t.calls) == 2

    def test_exhausted_retries_return_none(self, tts, monkeypatch, no_sleep):
        t = install_fake_tts(monkeypatch, tts, [FakeHTTPResponse(status_code=500, text="down")])
        assert tts._chunk_with_retry("你好。", "voice-host") is None
        assert len(t.calls) == tts.MAX_ATTEMPTS

    def test_auth_error_is_not_retried(self, tts, monkeypatch, no_sleep):
        # BUG-9 修复：4xx 确定性失败（凭证/参数/内容审核）立即失败不重试
        t = install_fake_tts(monkeypatch, tts, [FakeHTTPResponse(status_code=401, text="bad key")])
        assert tts._chunk_with_retry("你好。", "voice-host") is None
        assert len(t.calls) == 1


class TestSynthesizeToFile:
    def test_single_chunk_writes_output_without_ffmpeg(self, tts, monkeypatch, tmp_path):
        install_fake_tts(monkeypatch, tts, [ok_response([b"WAVDATA"])])
        out = tmp_path / "seg.wav"
        assert tts.synthesize("短句。", "voice-host", str(out)) is True
        assert out.read_bytes() == b"WAVDATA"
        assert list(tmp_path.iterdir()) == [out]  # no leftover part files

    def test_failed_chunk_cleans_up_parts_and_returns_false(self, tts, monkeypatch,
                                                            tmp_path, no_sleep):
        long_text = "这是一个句子。" * 60  # forces multiple chunks
        install_fake_tts(monkeypatch, tts, [
            ok_response([b"PART0"]),
            FakeHTTPResponse(status_code=500, text="down"),  # chunk 2 fails forever
        ])
        out = tmp_path / "seg.wav"
        assert tts.synthesize(long_text, "voice-host", str(out)) is False
        assert not out.exists()
        assert list(tmp_path.iterdir()) == []  # billed part files wiped (documented behavior)

    def test_empty_after_preprocess_skips_api(self, tts, monkeypatch, tmp_path, no_sleep):
        # BUG-5 修复：预处理后为空 → 返回 False 且不触网
        t = install_fake_tts(monkeypatch, tts, [FakeHTTPResponse(status_code=400, text="empty")])
        assert tts.synthesize("🎉", "voice-host", str(tmp_path / "seg.wav")) is False
        assert len(t.calls) == 0


class TestAudioAssembly:
    """generate_podcast_audio 的拼接序列：不对称静音、拍话筒提示音、旁白广播链。"""

    def _assemble(self, tts, monkeypatch, tmp_path):
        import script_synthesis as ss

        recorded = {"concat": None, "filters": []}

        def fake_run_ffmpeg(args):
            if "-af" in args:
                recorded["filters"].append(args[args.index("-af") + 1])
            Path(args[-1]).write_bytes(b"WAV")
            return True, ""

        def fake_concat(wav_files, list_path, output_path):
            if recorded["concat"] is None:  # 只记录首次（主拼接）
                recorded["concat"] = list(wav_files)
            Path(output_path).write_bytes(b"MERGED")
            return True

        monkeypatch.setattr(ss, "_run_ffmpeg", fake_run_ffmpeg)
        monkeypatch.setattr(ss, "_concat_wavs", fake_concat)
        monkeypatch.setattr(ss, "get_duration_seconds", lambda _: 60)
        monkeypatch.setattr(
            tts, "synthesize",
            lambda text, voice, out, is_narration=False, cache_dir=None, force=False:
                Path(out).write_bytes(b"WAV") or True)

        from tutils import make_script, write_script
        segments = [("第 1 段 · 甲", [
            ("主持人", "开场白。"),
            ("旁白", "插播解释。好，回到对话。"),
            ("嘉宾", "继续对话。"),
        ])]
        path = write_script(tmp_path, make_script(segments=segments, closing=False))
        assert ss.generate_podcast_audio(str(path), str(tmp_path / "out.mp3"), tts)
        return recorded

    def test_boundary_sequence_lead_tap_tail(self, tts, monkeypatch, tmp_path):
        rec = self._assemble(tts, monkeypatch, tmp_path)
        names = [Path(p).name for p in rec["concat"]]
        # 对话 → 进场静音 → 拍话筒 → 旁白（广播链产物）→ 退场静音 → 对话
        assert names == ["clip_0000.wav", "silence_lead.wav", "mic_tap.wav",
                         "clip_0001_gain.wav", "silence_tail.wav", "clip_0002.wav"]

    def test_tap_can_be_disabled(self, tts, monkeypatch, tmp_path):
        monkeypatch.setenv("PODCAST_NARRATION_TAP", "off")
        rec = self._assemble(tts, monkeypatch, tmp_path)
        assert not any("mic_tap" in p for p in rec["concat"])

    def test_narration_goes_through_radio_chain(self, tts, monkeypatch, tmp_path):
        rec = self._assemble(tts, monkeypatch, tmp_path)
        # 用旁白链独有的带限值区分（母带后处理链同样含 acompressor，但无 7.5k 低通）
        radio = [f for f in rec["filters"] if "lowpass=f=7500" in f]
        assert len(radio) == 1                      # 只有旁白片段过广播链
        assert "highpass=f=120" in radio[0] and "acompressor" in radio[0] \
               and "volume=-3.0dB" in radio[0]
