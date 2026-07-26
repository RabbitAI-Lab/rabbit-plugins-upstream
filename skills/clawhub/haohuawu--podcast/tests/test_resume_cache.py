"""断点恢复与幂等：分片缓存（chunk 级 md5 key）、manifest 复用、preflight、--force。

核心不变量：中间步骤失败后重跑，已完成的 TTS 工作绝不重复计费。
"""

import json
import sys
from pathlib import Path

import pytest
import generate_podcast as gp
from script_synthesis import chunk_cache_key, resolve_voices
from tutils import (FakeHTTPResponse, assert_exits_nonzero, install_fake_tts,
                    make_script, ndjson, tts_ok_events, write_script)
from test_publish_state import seed_remote_state


def ok_response(parts):
    return FakeHTTPResponse(lines=ndjson(tts_ok_events(parts)))


class TestChunkCache:
    def test_second_call_hits_cache_no_api(self, tts, monkeypatch, tmp_path):
        cache = str(tmp_path / "cache")
        out1, out2 = tmp_path / "a.wav", tmp_path / "b.wav"
        t = install_fake_tts(monkeypatch, tts, [ok_response([b"AUDIO"])])
        assert tts.synthesize("同一句话。", "voice-host", str(out1), cache_dir=cache)
        assert len(t.calls) == 1
        assert tts.synthesize("同一句话。", "voice-host", str(out2), cache_dir=cache)
        assert len(t.calls) == 1                      # 第二次零 API 调用
        assert out1.read_bytes() == out2.read_bytes()  # 输出逐字节一致（幂等）

    def test_cache_key_isolates_narration_params(self, tts, monkeypatch, tmp_path):
        # 同文本、同音色，旁白与普通参数不同 → 不同缓存条目，互不污染
        cache = str(tmp_path / "cache")
        t = install_fake_tts(monkeypatch, tts, [ok_response([b"AUDIO"])])
        tts.synthesize("同一句话。", "voice-host", str(tmp_path / "a.wav"), cache_dir=cache)
        tts.synthesize("同一句话。", "voice-host", str(tmp_path / "b.wav"),
                       is_narration=True, cache_dir=cache)
        assert len(t.calls) == 2
        assert chunk_cache_key("x", "v", False) != chunk_cache_key("x", "v", True)

    def test_force_bypasses_cache_read_but_rewrites(self, tts, monkeypatch, tmp_path):
        cache = str(tmp_path / "cache")
        t = install_fake_tts(monkeypatch, tts, [ok_response([b"AUDIO"])])
        tts.synthesize("同一句话。", "voice-host", str(tmp_path / "a.wav"), cache_dir=cache)
        tts.synthesize("同一句话。", "voice-host", str(tmp_path / "b.wav"),
                       cache_dir=cache, force=True)
        assert len(t.calls) == 2  # force 跳过缓存读取，真实重新合成

    def test_failed_run_resumes_billing_only_failed_chunk(self, tts, monkeypatch,
                                                          tmp_path, no_sleep):
        # 多分片长文本：首跑第 2 片失败中止；修复后重跑只为失败片计费
        import script_synthesis

        def fake_concat(wav_files, list_path, output_path):
            Path(output_path).write_bytes(
                b"".join(Path(w).read_bytes() for w in wav_files))
            return True

        monkeypatch.setattr(script_synthesis, "_concat_wavs", fake_concat)
        cache = str(tmp_path / "cache")
        # 句子内容互不相同：相同分片会因内容哈希去重命中缓存（那是正确行为，但这里要测失败恢复）
        long_text = "".join(f"第{i}个句子说了一些不同的话。" for i in range(40))
        t1 = install_fake_tts(monkeypatch, tts, [
            ok_response([b"CHUNK0"]),
            FakeHTTPResponse(status_code=500, text="down"),
        ])
        assert tts.synthesize(long_text, "voice-host", str(tmp_path / "a.wav"),
                              cache_dir=cache) is False
        first_run_calls = len(t1.calls)
        assert first_run_calls > 1  # 第 1 片成功 + 第 2 片重试若干次

        t2 = install_fake_tts(monkeypatch, tts, [ok_response([b"CHUNKN"])])
        assert tts.synthesize(long_text, "voice-host", str(tmp_path / "b.wav"),
                              cache_dir=cache) is True
        # 重跑：第 1 片缓存命中，只有其余分片触网
        chunks = tts.split_long_text(tts.preprocess_text(long_text))
        assert len(t2.calls) == len(chunks) - 1


@pytest.fixture()
def publish_env(monkeypatch, tmp_path, tos_env, tos_bucket):
    """隔离的 main() 运行环境：workdir/输出目录进 tmp，TTS 合成打桩计数。

    preflight 的 ffmpeg/ffprobe 探测也打桩——单测不依赖宿主机装了什么
    （与 conftest 的 "ffmpeg not required for unit tests" 保持一致）。"""
    monkeypatch.setenv("PODCAST_WORKDIR", str(tmp_path / "work"))
    monkeypatch.setenv("DOUBAO_TTS_API_KEY", "test-key")
    monkeypatch.setattr(gp, "PODCAST_DIR", tmp_path / "episodes")
    monkeypatch.setattr(gp.shutil, "which", lambda name: f"/stub/bin/{name}")

    calls = []

    def fake_audio(script_path, output_path, tts, postprocess=True,
                   cache_dir=None, force=False):
        calls.append({"cache_dir": cache_dir, "force": force})
        Path(output_path).write_bytes(b"FAKE-MP3")
        return output_path

    monkeypatch.setattr(gp, "generate_podcast_audio", fake_audio)
    monkeypatch.setattr(gp, "get_duration_seconds", lambda _: 60, raising=False)
    return {"calls": calls, "tmp": tmp_path, "bucket": tos_bucket}


def run_main(monkeypatch, *cli):
    monkeypatch.setattr(sys, "argv", ["generate_podcast.py", *cli])
    gp.main()


class TestManifestReuse:
    SLUG = "20260716_resume_test"

    def _script(self, tmp_path, text=None):
        return str(write_script(tmp_path, text))

    def test_preview_then_publish_synthesizes_once(self, publish_env, monkeypatch, tmp_path):
        # 历史上最贵的坑：--no-upload 试听后重跑发布 = 双倍计费。现在必须复用。
        seed_remote_state(publish_env["bucket"], slug="20260101_other")
        script = self._script(tmp_path)
        run_main(monkeypatch, "--script", script, "--slug", self.SLUG, "--no-upload")
        assert len(publish_env["calls"]) == 1
        run_main(monkeypatch, "--script", script, "--slug", self.SLUG, "--no-notes")  # 发布
        assert len(publish_env["calls"]) == 1  # 零新增 TTS
        feed = publish_env["bucket"].store["podcasts/feed.xml"].decode()
        assert f"episode:{self.SLUG}" in feed
        # 目录保留不变量：发布是 upsert 不是替换——历史单集必须还在 feed 与状态里
        assert "episode:20260101_other" in feed
        episodes = json.loads(publish_env["bucket"].store["podcasts/episodes.json"])
        assert {e["slug"] for e in episodes} == {"20260101_other", self.SLUG}

    def test_script_change_triggers_resynthesis(self, publish_env, monkeypatch, tmp_path):
        script = self._script(tmp_path)
        run_main(monkeypatch, "--script", script, "--slug", self.SLUG, "--no-upload")
        Path(script).write_text(make_script().replace("第一个问题。", "改过的问题。"),
                                encoding="utf-8")
        run_main(monkeypatch, "--script", script, "--slug", self.SLUG, "--no-upload")
        assert len(publish_env["calls"]) == 2

    def test_force_resynthesizes_and_propagates(self, publish_env, monkeypatch, tmp_path):
        script = self._script(tmp_path)
        run_main(monkeypatch, "--script", script, "--slug", self.SLUG, "--no-upload")
        run_main(monkeypatch, "--script", script, "--slug", self.SLUG, "--no-upload", "--force")
        assert len(publish_env["calls"]) == 2
        assert publish_env["calls"][-1]["force"] is True

    def test_voice_change_triggers_resynthesis(self, publish_env, monkeypatch, tmp_path):
        # 参数指纹：脚本没变但音色变了，绝不能复用旧音频
        script = self._script(tmp_path)
        run_main(monkeypatch, "--script", script, "--slug", self.SLUG, "--no-upload")
        assert len(publish_env["calls"]) == 1
        monkeypatch.setenv("DOUBAO_TTS_HOST_VOICE", "another_voice_uranus")
        run_main(monkeypatch, "--script", script, "--slug", self.SLUG, "--no-upload")
        assert len(publish_env["calls"]) == 2

    def test_tap_toggle_changes_fingerprint(self, publish_env, monkeypatch, tmp_path):
        # 提示音开关进合成参数指纹：关掉 tap 重跑不能复用带 tap 的旧音频
        script = self._script(tmp_path)
        run_main(monkeypatch, "--script", script, "--slug", self.SLUG, "--no-upload")
        monkeypatch.setenv("PODCAST_NARRATION_TAP", "off")
        run_main(monkeypatch, "--script", script, "--slug", self.SLUG, "--no-upload")
        assert len(publish_env["calls"]) == 2

    def test_manifest_records_stage_and_cache_dir_under_workdir(self, publish_env,
                                                                monkeypatch, tmp_path):
        script = self._script(tmp_path)
        run_main(monkeypatch, "--script", script, "--slug", self.SLUG, "--no-upload")
        workdir = tmp_path / "work" / self.SLUG
        manifest = json.loads((workdir / "manifest.json").read_text())
        assert manifest["stages"]["synthesized"]
        assert manifest["audio"]["md5"]
        assert publish_env["calls"][0]["cache_dir"] == str(workdir / "clips_cache")


class TestPreflight:
    SLUG = "20260716_preflight"

    def test_collects_all_problems_before_spending(self, publish_env, monkeypatch,
                                                   tmp_path, capsys):
        monkeypatch.delenv("DOUBAO_TTS_API_KEY")
        monkeypatch.delenv("TOS_ACCESS_KEY")
        monkeypatch.setattr(gp.shutil, "which", lambda _: None)
        script = str(write_script(tmp_path))
        with assert_exits_nonzero():
            run_main(monkeypatch, "--script", script, "--slug", self.SLUG,
                     "--notes", str(tmp_path / "no_such_notes.md"))
        out = capsys.readouterr().out
        for needle in ("ffmpeg", "DOUBAO_TTS_API_KEY", "no_such_notes.md", "TOS"):
            assert needle in out, f"preflight 应一次性报出全部问题，缺少: {needle}"
        assert publish_env["calls"] == []  # 一个子都没花

    def test_missing_remote_config_blocks_before_tts(self, publish_env, monkeypatch,
                                                     tmp_path, capsys):
        script = str(write_script(tmp_path))  # fake bucket 为空 → 未 --init
        with assert_exits_nonzero():
            run_main(monkeypatch, "--script", script, "--slug", self.SLUG, "--no-notes")
        assert "--init" in capsys.readouterr().out
        assert publish_env["calls"] == []

    def test_publish_without_notes_requires_explicit_flag(self, publish_env, monkeypatch,
                                                          tmp_path, capsys):
        # EP 质量线代码化：发布缺 --notes 必须显式 --no-notes，否则 preflight 拦下
        seed_remote_state(publish_env["bucket"], slug="20260101_other")
        script = str(write_script(tmp_path))
        with assert_exits_nonzero():
            run_main(monkeypatch, "--script", script, "--slug", self.SLUG)
        assert "--no-notes" in capsys.readouterr().out
        assert publish_env["calls"] == []

    def test_article_md_rejected_as_notes(self, publish_env, monkeypatch, tmp_path, capsys):
        seed_remote_state(publish_env["bucket"], slug="20260101_other")
        script = str(write_script(tmp_path))
        article = tmp_path / "article.md"
        article.write_text("完整文章留档", encoding="utf-8")
        with assert_exits_nonzero():
            run_main(monkeypatch, "--script", script, "--slug", self.SLUG,
                     "--notes", str(article))
        assert "article.md" in capsys.readouterr().out
        assert publish_env["calls"] == []

    def test_oversized_notes_rejected(self, publish_env, monkeypatch, tmp_path, capsys):
        seed_remote_state(publish_env["bucket"], slug="20260101_other")
        script = str(write_script(tmp_path))
        notes = tmp_path / "notes.md"
        notes.write_text("很长的正文。" * 1500, encoding="utf-8")  # 渲染后 >8000 字符
        with assert_exits_nonzero():
            run_main(monkeypatch, "--script", script, "--slug", self.SLUG,
                     "--notes", str(notes))
        assert "8000" in capsys.readouterr().out
        assert publish_env["calls"] == []

    def test_invalid_script_blocked_unless_skip_validate(self, publish_env, monkeypatch,
                                                         tmp_path, capsys):
        # 内联校验：缺收尾句的脚本在 TTS 前被拦；--skip-validate 显式放行
        bad = make_script(closing=False)
        script = str(write_script(tmp_path, bad))
        with assert_exits_nonzero():
            run_main(monkeypatch, "--script", script, "--slug", self.SLUG, "--no-upload")
        assert "格式校验" in capsys.readouterr().out
        assert publish_env["calls"] == []
        run_main(monkeypatch, "--script", script, "--slug", self.SLUG,
                 "--no-upload", "--skip-validate")
        assert len(publish_env["calls"]) == 1
