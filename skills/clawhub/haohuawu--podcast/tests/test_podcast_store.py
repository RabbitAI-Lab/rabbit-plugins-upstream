"""podcast_store：TOS 状态层的不变量（upsert 语义、description 唯一构建点、写序）。"""

import json

import podcast_store as store
from tutils import make_notes


class TestUpsertEpisode:
    def _ep(self, slug, num=1, pub="2026-01-01T08:00:00+08:00"):
        return {"slug": slug, "title": "t", "pub_date": pub, "episode_num": num}

    def test_new_episode_appended(self):
        eps = store.upsert_episode([], self._ep("20260101_a"))
        assert len(eps) == 1

    def test_same_slug_overwrites_preserving_pubdate_and_num(self):
        old = self._ep("20260101_a", num=3, pub="2026-01-01T08:00:00+08:00")
        new = self._ep("20260101_a", num=99, pub="2026-06-01T08:00:00+08:00")
        new["title"] = "updated"
        eps = store.upsert_episode([old], new)
        assert len(eps) == 1
        assert eps[0]["title"] == "updated"
        assert eps[0]["pub_date"] == "2026-01-01T08:00:00+08:00"   # 首播时间不变
        assert eps[0]["episode_num"] == 3                          # 期号不变 → guid/排序稳定

    def test_different_slug_appends(self):
        eps = store.upsert_episode([self._ep("20260101_a")], self._ep("20260102_b", num=2))
        assert [e["slug"] for e in eps] == ["20260101_a", "20260102_b"]


class TestBuildDescription:
    def test_notes_markdown_rendered_to_html(self, tmp_path):
        notes = tmp_path / "notes.md"
        notes.write_text(make_notes(), encoding="utf-8")
        html_out = store.build_description("标题", notes)
        assert "<strong>内容速览</strong>" in html_out
        assert "一句话主线" in html_out

    def test_no_notes_falls_back_to_escaped_title(self):
        html_out = store.build_description("标题 <b>不许注入</b>")
        assert html_out == "<p>标题 &lt;b&gt;不许注入&lt;/b&gt;</p>"


class TestPublishState:
    CONFIG = {"title": "T", "description": "D", "author": "A", "email": "a@b.com",
              "site_url": "https://e.com", "cover_url": "https://cdn/c.png"}
    EPISODE = {"slug": "20260101_a", "title": "EP", "description": "<p>x</p>",
               "audio_url": "https://cdn/a.mp3", "audio_size": 1, "duration": 60,
               "pub_date": "2026-01-01T08:00:00+08:00", "episode_num": 1}

    def test_writes_state_before_feed_with_correct_types(self, tos_env, tos_bucket):
        from tos_uploader import TOSUploader
        url = store.publish_state(TOSUploader(), self.CONFIG, [self.EPISODE],
                                  target_slug="20260101_a")
        puts = tos_bucket.put_log
        # 写序不变量：事实源（episodes.json）先写，派生物（feed.xml）后写
        assert puts.index(store.EPISODES_KEY) < puts.index(store.FEED_KEY)
        assert url.endswith(store.FEED_KEY)
        assert tos_bucket.meta[store.FEED_KEY]["content_type"].startswith("application/rss+xml")
        assert tos_bucket.meta[store.EPISODES_KEY]["content_type"].startswith("application/json")
        assert json.loads(tos_bucket.store[store.EPISODES_KEY])[0]["slug"] == "20260101_a"
        assert b"episode:20260101_a" in tos_bucket.store[store.FEED_KEY]

    def test_feed_uses_config_cover_url(self, tos_env, tos_bucket):
        from tos_uploader import TOSUploader
        store.publish_state(TOSUploader(), self.CONFIG, [self.EPISODE],
                            target_slug="20260101_a")
        assert b'href="https://cdn/c.png"' in tos_bucket.store[store.FEED_KEY]


def make_episodes(n):
    """n 集正常目录（slug 递增、description 各不相同）。"""
    return [{
        "slug": f"202601{i:02d}_ep{i}", "title": f"EP{i} 标题", "description": f"<p>第 {i} 集内容</p>",
        "audio_url": f"https://cdn/{i}.mp3", "audio_size": i * 100, "duration": 60 + i,
        "pub_date": f"2026-01-{i:02d}T08:00:00+08:00", "episode_num": i,
    } for i in range(1, n + 1)]


class TestCheckStateDiff:
    """守卫 1：除目标 slug 外，线上其余单集必须逐字节不变。"""

    def test_appending_target_passes(self):
        remote = make_episodes(16)
        new = remote + [make_episodes(17)[-1]]
        assert store.check_state_diff(remote, new, new[-1]["slug"]) == []

    def test_modifying_target_passes(self):
        remote = make_episodes(3)
        new = [dict(ep) for ep in remote]
        new[1]["description"] = "<p>改写目标集</p>"
        assert store.check_state_diff(remote, new, new[1]["slug"]) == []

    def test_idempotent_republish_passes(self):
        remote = make_episodes(3)
        assert store.check_state_diff(remote, [dict(ep) for ep in remote],
                                      remote[-1]["slug"]) == []

    def test_first_publish_empty_remote_passes(self):
        new = make_episodes(1)
        assert store.check_state_diff([], new, new[0]["slug"]) == []

    def test_tampered_non_target_named_with_fields(self):
        remote = make_episodes(16)
        new = [dict(ep) for ep in remote] + [make_episodes(17)[-1]]
        new[4]["description"] = "<p>被串位污染</p>"        # CDATA 事故形态：发 A 改了 B
        violations = store.check_state_diff(remote, new, new[-1]["slug"])
        assert len(violations) == 1
        assert remote[4]["slug"] in violations[0] and "description" in violations[0]

    def test_deleting_non_target_flagged(self):
        remote = make_episodes(3)
        new = [remote[0], remote[2]]                        # 丢了第 2 集
        violations = store.check_state_diff(remote, new, remote[2]["slug"])
        assert any(remote[1]["slug"] in v and "删除" in v for v in violations)

    def test_full_replace_flagged(self):
        # 变异金丝雀场景：publish 被写成 episodes = [new_episode]，整表被最新一集替换
        remote = make_episodes(16)
        new = [make_episodes(17)[-1]]
        violations = store.check_state_diff(remote, new, new[0]["slug"])
        assert len(violations) == 16                        # 16 个"将被删除"逐一点名

    def test_sneaking_extra_episode_flagged(self):
        remote = make_episodes(2)
        extra = make_episodes(4)[-1]
        new = remote + [make_episodes(3)[-1], extra]
        violations = store.check_state_diff(remote, new, "20260103_ep3")
        assert any(extra["slug"] in v and "新增" in v for v in violations)

    def test_reorder_flagged(self):
        remote = make_episodes(3)
        new = [remote[1], remote[0], remote[2]]
        violations = store.check_state_diff(remote, new, remote[2]["slug"])
        assert any("顺序" in v for v in violations)


class TestCheckFeedConsistency:
    """守卫 2：渲染出的 feed 逐 item 与事实源比对——CDATA 串位类事故的拦截网。"""

    CONFIG = TestPublishState.CONFIG

    def _render(self, episodes):
        from rss_feed import generate_rss_feed
        return generate_rss_feed(self.CONFIG, episodes,
                                 feed_url="https://cdn/feed.xml",
                                 cover_url="https://cdn/c.png")

    def test_faithful_render_passes_at_two_digit_scale(self):
        # 13 集：覆盖两位数 token 区间（前缀污染当年的触发规模）
        episodes = make_episodes(13)
        episodes[0]["description"] = "<p>含 ]]> 的描述也要原样往返</p>"
        episodes[1]["description"] = ""
        assert store.check_feed_consistency(self._render(episodes), episodes) == []

    def test_swapped_description_flagged(self):
        episodes = make_episodes(13)
        rotated = [dict(ep, description=episodes[(i + 1) % 13]["description"])
                   for i, ep in enumerate(episodes)]
        violations = store.check_feed_consistency(self._render(rotated), episodes)
        assert violations
        assert any("description" in v for v in violations)

    def test_missing_item_flagged(self):
        episodes = make_episodes(3)
        violations = store.check_feed_consistency(self._render(episodes[:2]), episodes)
        assert any("item 数" in v for v in violations)

    def test_foreign_guid_flagged(self):
        episodes = make_episodes(2)
        stranger = dict(episodes[1], slug="20269999_stranger")
        violations = store.check_feed_consistency(
            self._render([episodes[0], stranger]), episodes)
        assert any("20269999_stranger" in v for v in violations)


class TestPublishStateGuardWiring:
    """publish_state 内的守卫接线：中止时不写任何远端 key；备份先于覆盖。"""

    CONFIG = TestPublishState.CONFIG

    def _seed(self, tos_bucket, episodes):
        tos_bucket.store[store.EPISODES_KEY] = json.dumps(
            episodes, ensure_ascii=False).encode()

    def test_publish_17th_on_16_live_passes_and_backs_up(self, tos_env, tos_bucket):
        from tos_uploader import TOSUploader
        remote = make_episodes(16)
        self._seed(tos_bucket, remote)
        new = remote + [make_episodes(17)[-1]]
        store.publish_state(TOSUploader(), self.CONFIG, new, target_slug=new[-1]["slug"])
        assert len(json.loads(tos_bucket.store[store.EPISODES_KEY])) == 17
        backups = [k for k in tos_bucket.store if k.startswith("podcasts/backups/episodes_")]
        assert len(backups) == 1
        assert json.loads(tos_bucket.store[backups[0]]) == remote       # 备份 = 覆盖前的线上态
        assert tos_bucket.put_log.index(backups[0]) \
            < tos_bucket.put_log.index(store.EPISODES_KEY)

    def test_idempotent_republish_skips_backup(self, tos_env, tos_bucket):
        # 与线上逐字节相同的重发（如 feed 写失败后的重跑）：不产生冗余备份，feed 照常重建
        from tos_uploader import TOSUploader
        eps = make_episodes(3)
        tos_bucket.store[store.EPISODES_KEY] = json.dumps(
            eps, ensure_ascii=False, indent=2).encode()
        store.publish_state(TOSUploader(), self.CONFIG, eps, target_slug=eps[-1]["slug"])
        assert not any(k.startswith("podcasts/backups/") for k in tos_bucket.store)
        assert store.FEED_KEY in tos_bucket.put_log

    def test_first_publish_no_backup(self, tos_env, tos_bucket):
        from tos_uploader import TOSUploader
        new = make_episodes(1)
        store.publish_state(TOSUploader(), self.CONFIG, new, target_slug=new[0]["slug"])
        assert not any(k.startswith("podcasts/backups/") for k in tos_bucket.store)

    def test_tampered_non_target_aborts_without_writing(self, tos_env, tos_bucket, capsys):
        from tos_uploader import TOSUploader
        from tutils import assert_exits_nonzero
        remote = make_episodes(16)
        self._seed(tos_bucket, remote)
        new = [dict(ep) for ep in remote] + [make_episodes(17)[-1]]
        new[4]["description"] = "<p>被串位污染</p>"
        with assert_exits_nonzero():
            store.publish_state(TOSUploader(), self.CONFIG, new, target_slug=new[-1]["slug"])
        assert remote[4]["slug"] in capsys.readouterr().out             # 点名被伤的 slug
        assert tos_bucket.put_log == []                                 # 一个 key 都没写
        assert json.loads(tos_bucket.store[store.EPISODES_KEY]) == remote

    def test_render_mixup_aborts_before_any_write(self, tos_env, tos_bucket,
                                                  monkeypatch, capsys):
        from tos_uploader import TOSUploader
        from tutils import assert_exits_nonzero
        remote = make_episodes(12)
        self._seed(tos_bucket, remote)
        real = store.generate_rss_feed

        def mixed_up(config, episodes, **kw):               # 渲染器串位（CDATA 事故形态）
            rotated = [dict(ep, description=episodes[(i + 1) % len(episodes)]["description"])
                       for i, ep in enumerate(episodes)]
            return real(config, rotated, **kw)

        monkeypatch.setattr(store, "generate_rss_feed", mixed_up)
        new = [dict(ep) for ep in remote]
        new[-1]["description"] = "<p>目标集更新</p>"
        with assert_exits_nonzero():
            store.publish_state(TOSUploader(), self.CONFIG, new, target_slug=new[-1]["slug"])
        assert "不一致" in capsys.readouterr().out
        assert tos_bucket.put_log == []

    def test_force_state_skips_diff_but_not_feed_check(self, tos_env, tos_bucket,
                                                       monkeypatch):
        from tos_uploader import TOSUploader
        from tutils import assert_exits_nonzero
        remote = make_episodes(3)
        self._seed(tos_bucket, remote)
        migrated = [dict(ep, description=ep["description"] + "<p>批量迁移追加</p>")
                    for ep in remote]
        # 状态 diff 被跳过：批量改动全部单集也能推
        store.publish_state(TOSUploader(), self.CONFIG, migrated,
                            target_slug=migrated[-1]["slug"], force_state=True)
        assert json.loads(tos_bucket.store[store.EPISODES_KEY]) == migrated
        # 但渲染校验永不跳过
        real = store.generate_rss_feed
        monkeypatch.setattr(
            store, "generate_rss_feed",
            lambda config, episodes, **kw: real(
                config, [dict(ep, description="<p>坏渲染</p>") for ep in episodes], **kw))
        with assert_exits_nonzero():
            store.publish_state(TOSUploader(), self.CONFIG, migrated,
                                target_slug=migrated[-1]["slug"], force_state=True)