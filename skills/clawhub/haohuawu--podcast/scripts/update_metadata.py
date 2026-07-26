#!/usr/bin/env python3
# /// script
# requires-python = ">=3.9"
# dependencies = ["tos", "markdown"]
# ///
"""只更新元数据（notes/描述），不重跑 TTS。

用法：
  python3 scripts/update_metadata.py --slug 20260715_agent_foundations --notes notes.md

会做三件事（状态读写与写序由 podcast_store 固化）：
  1. 上传 notes.md 到 TOS episodes/{slug}/notes.md
  2. 用 notes.md 重新生成 HTML description，更新 episodes.json 中对应 episode
  3. 重新生成 feed.xml 并上传

脚本正文不变则音频不变，不触发 TTS。独立入口是有意设计：与合成物理隔离，
杜绝"只改元数据却重跑 34 分钟 TTS"的误操作。
"""
import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from podcast_store import (CONFIG_KEY, EPISODES_KEY, MD_CT, PREFIX,
                           build_description, fetch_config, fetch_episodes,
                           publish_state)
from tos_uploader import TOSUploader


def main():
    parser = argparse.ArgumentParser(description="只更新元数据，不重跑 TTS")
    parser.add_argument("--slug", required=True, help="单集 slug")
    parser.add_argument("--notes", required=True, help="notes.md 文件路径")
    parser.add_argument("--force-state", action="store_true",
                        help="跳过发布前的线上状态 diff 守卫（除目标单集外其余必须不变）；"
                             "仅预期中的批量迁移使用")
    args = parser.parse_args()

    notes_path = Path(args.notes)
    if not notes_path.exists():
        print(f"❌ notes 文件不存在: {notes_path}")
        sys.exit(1)

    uploader = TOSUploader()

    episodes = fetch_episodes(uploader)
    if not episodes:
        print(f"❌ TOS 上没有 {EPISODES_KEY}（还没有发布过任何单集？）。"
              f"先用 generate_podcast.py 完成一次发布。")
        sys.exit(1)
    config = fetch_config(uploader)
    if config is None:
        print(f"❌ TOS 上没有 {CONFIG_KEY}。先执行 generate_podcast.py --init 完成初始化。")
        sys.exit(1)

    # 1. 上传 notes.md
    notes_key = f"{PREFIX}episodes/{args.slug}/notes.md"
    uploader.upload_text(notes_path.read_text(encoding="utf-8").strip(),
                         notes_key, content_type=MD_CT)
    print(f"✅ notes.md 已上传: {uploader.base_url}/{notes_key}")

    # 2. 更新 episodes.json 中对应 episode 的 description
    found = False
    for ep in episodes:
        if ep.get("slug") == args.slug:
            ep["description"] = build_description(ep.get("title", ""), notes_path)
            found = True
            print(f"✅ 更新 description: {ep['title']}")
            break
    if not found:
        print(f"❌ 未在 episodes.json 中找到 slug={args.slug}")
        sys.exit(1)

    # 3. 回传状态并重建 feed（episodes.json 先、feed.xml 后）
    rss_url = publish_state(uploader, config, episodes,
                            target_slug=args.slug, force_state=args.force_state)
    print("✅ episodes.json 已更新")
    print(f"✅ feed.xml 已更新: {rss_url}")


if __name__ == "__main__":
    main()
