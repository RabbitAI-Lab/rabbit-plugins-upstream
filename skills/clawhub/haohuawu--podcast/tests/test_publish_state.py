"""Publish-side state management: config validation, episode upsert, TOS I/O,
and the update_metadata flow against the shared fake bucket."""

import json
import sys

import pytest
import generate_podcast as gp
from tutils import assert_exits_nonzero, make_notes


class TestValidateConfig:
    def _valid(self):
        return {"title": "T", "description": "D", "author": "A",
                "email": "a@b.com", "site_url": "https://e.com",
                "cover_url": "https://cdn/c.png"}

    def test_valid_config_gets_defaults(self):
        cfg = gp.validate_config(self._valid())
        assert cfg["language"] == "zh-cn"
        assert cfg["category"] == "Technology"

    def test_init_instance_without_cover_url_validates(self):
        # BUG-13 修复：cover_url 是 --init 的输出而非输入，不在 required 里
        instance = self._valid()
        del instance["cover_url"]
        cfg = gp.validate_config(instance)
        assert cfg["title"] == "T"

    def test_missing_required_exits(self, capsys):
        bad = self._valid()
        del bad["email"]
        with assert_exits_nonzero():
            gp.validate_config(bad)
        assert "email" in capsys.readouterr().out

    def test_unknown_field_exits(self, capsys):
        bad = {**self._valid(), "made_up": "x"}
        with assert_exits_nonzero():
            gp.validate_config(bad)
        assert "made_up" in capsys.readouterr().out

    def test_bad_email_and_url_exit(self, capsys):
        bad = {**self._valid(), "email": "not-an-email", "site_url": "ftp://x"}
        with assert_exits_nonzero():
            gp.validate_config(bad)
        out = capsys.readouterr().out
        assert "邮箱" in out and "http" in out


class TestSlugFormat:
    @pytest.mark.parametrize("slug,ok", [
        ("20260715_my_episode", True),
        ("20260715_a", True),
        ("20260715_My_Episode", False),   # 大写
        ("2026_my_episode", False),       # 日期不完整
        ("20260715-my-episode", False),   # 连字符
        ("20260715_", False),
    ])
    def test_slug_regex(self, slug, ok):
        assert bool(gp.SLUG_RE.match(slug)) is ok


class TestTOSUploader:
    def test_roundtrip_and_404(self, tos_env, tos_bucket):
        from tos_uploader import TOSUploader
        up = TOSUploader()
        url = up.upload_text("hello", "podcasts/x.txt", content_type="text/plain")
        assert url == f"{up.base_url}/podcasts/x.txt"
        assert up.download_text("podcasts/x.txt") == "hello"
        assert up.download_text("podcasts/missing.txt") is None

    def test_upload_file_and_content_type_recorded(self, tos_env, tos_bucket, tmp_path):
        from tos_uploader import TOSUploader
        f = tmp_path / "a.mp3"
        f.write_bytes(b"MP3DATA")
        TOSUploader().upload_file(str(f), "podcasts/a.mp3", content_type="audio/mpeg")
        assert tos_bucket.store["podcasts/a.mp3"] == b"MP3DATA"
        assert tos_bucket.meta["podcasts/a.mp3"]["content_type"] == "audio/mpeg"

    def test_missing_env_raises(self, monkeypatch):
        for var in ("TOS_ACCESS_KEY", "TOS_SECRET_KEY", "TOS_BUCKET", "TOS_REGION"):
            monkeypatch.delenv(var, raising=False)
        from tos_uploader import TOSUploader
        with pytest.raises(ValueError):
            TOSUploader()


def seed_remote_state(tos_bucket, slug="20260101_a"):
    """Seed config.json + episodes.json the way a previous publish would have."""
    config = {"title": "T", "description": "D", "author": "A", "email": "a@b.com",
              "site_url": "https://e.com", "cover_url": "https://cdn/c.png"}
    episodes = [{
        "slug": slug, "title": "EP", "description": "<p>old</p>",
        "audio_url": "https://cdn/a.mp3", "audio_size": 1, "duration": 60,
        "pub_date": "2026-01-01T08:00:00+08:00", "episode_num": 1,
    }]
    tos_bucket.store["podcasts/config.json"] = json.dumps(config).encode()
    tos_bucket.store["podcasts/episodes.json"] = json.dumps(episodes).encode()
    return config, episodes


class TestUpdateMetadataFlow:
    def _run(self, monkeypatch, tmp_path, slug):
        import update_metadata
        notes = tmp_path / "notes.md"
        notes.write_text(make_notes(), encoding="utf-8")
        monkeypatch.setattr(sys, "argv",
                            ["update_metadata.py", "--slug", slug, "--notes", str(notes)])
        update_metadata.main()

    def test_updates_description_and_rebuilds_feed(self, tos_env, tos_bucket,
                                                   monkeypatch, tmp_path):
        seed_remote_state(tos_bucket, slug="20260101_a")
        self._run(monkeypatch, tmp_path, "20260101_a")
        episodes = json.loads(tos_bucket.store["podcasts/episodes.json"])
        assert "一句话主线" in episodes[0]["description"]      # markdown 已渲染进 description
        feed = tos_bucket.store["podcasts/feed.xml"].decode()
        assert "episode:20260101_a" in feed
        assert "podcasts/episodes/20260101_a/notes.md" in tos_bucket.store

    def test_unknown_slug_exits_nonzero(self, tos_env, tos_bucket, monkeypatch, tmp_path):
        seed_remote_state(tos_bucket, slug="20260101_a")
        with assert_exits_nonzero():
            self._run(monkeypatch, tmp_path, "20269999_missing")

    def test_missing_remote_state_friendly_error(self, tos_env, tos_bucket,
                                                 monkeypatch, tmp_path, capsys):
        # BUG-10 修复：远端无 episodes.json → 友好报错 exit 1，而非裸 traceback
        with assert_exits_nonzero():
            self._run(monkeypatch, tmp_path, "20260101_a")
        assert "episodes.json" in capsys.readouterr().out

    def test_write_order_state_before_feed(self, tos_env, tos_bucket, monkeypatch, tmp_path):
        # 写序不变量：episodes.json（事实源）先写，feed.xml（派生物）后写——
        # 中途失败时状态领先 feed，可由任意一次重建自愈；反序会静默丢单集
        seed_remote_state(tos_bucket, slug="20260101_a")
        self._run(monkeypatch, tmp_path, "20260101_a")
        puts = tos_bucket.put_log
        assert puts.index("podcasts/episodes.json") < puts.index("podcasts/feed.xml")


class TestDryRunCharCount:
    """BUG-12 修复：dry-run 计费口径 = preprocess 后实发文本，并报告缓存命中后的净计费。"""

    def _dry_run(self, monkeypatch, tmp_path, script_text, slug="20260716_dryrun"):
        import re as _re
        from tutils import write_script
        monkeypatch.setenv("PODCAST_WORKDIR", str(tmp_path / "work"))
        path = write_script(tmp_path, script_text)
        monkeypatch.setattr(sys, "argv", ["generate_podcast.py", "--script", str(path),
                                          "--slug", slug, "--dry-run"])
        gp.main()
        return path

    def test_dry_run_counts_billable_chars(self, monkeypatch, tmp_path, capsys):
        from script_synthesis import parse_podcast_script, DoubaoTTS
        from tutils import make_script
        text = make_script(segments=[("第 1 段 · 甲", [
            ("主持人", "**加粗的词** 和 [链接](https://example.com/very/long/url) 都不计费。"),
        ])], closing=False)
        path = self._dry_run(monkeypatch, tmp_path, text)
        out = capsys.readouterr().out
        segments = parse_podcast_script(str(path))
        billable = sum(len(c) for _, t in segments
                       for c in DoubaoTTS.split_long_text(DoubaoTTS.preprocess_text(t)))
        raw = sum(len(t) for _, t in segments)
        assert f"共 {billable} 字符" in out    # 报的是实发口径
        assert raw > billable                  # markdown 标记与 URL 确实被剔除了

    def test_dry_run_reports_cache_hits(self, monkeypatch, tmp_path, capsys):
        from script_synthesis import (DoubaoTTS, chunk_cache_key, resolve_voices)
        from tutils import make_script
        line = "这句话会被预置进缓存。"
        text = make_script(segments=[("第 1 段 · 甲", [("主持人", line)])], closing=False)
        # 预置缓存：与 dry-run 相同的 key 推导（host 音色、非旁白）
        host, _ = resolve_voices(None, None)
        chunk = DoubaoTTS.split_long_text(DoubaoTTS.preprocess_text(line))[0]
        cache_dir = tmp_path / "work" / "20260716_dryrun" / "clips_cache"
        cache_dir.mkdir(parents=True)
        (cache_dir / f"{chunk_cache_key(chunk, host, False)}.wav").write_bytes(b"WAV")
        self._dry_run(monkeypatch, tmp_path, text)
        out = capsys.readouterr().out
        assert "缓存命中" in out and "净计费" in out
