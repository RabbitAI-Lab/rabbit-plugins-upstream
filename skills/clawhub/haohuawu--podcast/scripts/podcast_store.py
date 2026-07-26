#!/usr/bin/env python3
"""TOS 状态层：config.json / episodes.json / feed.xml 的唯一读写入口。

generate_podcast（发布）与 update_metadata（元数据更新）共用这一层——
key 常量、episode upsert、description 构建、feed 重建与写入顺序只在这里定义。

写序不变量固化在 publish_state()：**episodes.json（事实源）先写、feed.xml
（派生物）后写**。中途失败时状态领先 feed，任何一次后续发布/元数据更新都会
从状态重建完整 feed（自愈）；反序则 feed 里的新单集会在下次重建时被静默抹掉。

发布守卫同样固化在 publish_state()（CDATA 前缀污染事故的复盘产物——一次
"发布 EP16"重写了全部 16 集的线上表示，渲染层 bug 因此放大成 6 集内容串位）：
推送前比对线上状态，除目标单集外其余必须逐字节不变；渲染出的 feed 逐 item
校验归属后才允许触网。预期中的批量迁移用 --force-state 显式跳过状态 diff。
"""

import html
import json
import sys
import xml.etree.ElementTree as ET
from datetime import datetime
from pathlib import Path
from typing import Optional

import markdown

sys.path.insert(0, str(Path(__file__).parent))
# _clean 是渲染侧的文本清洗；feed 层校验必须用同一套清洗做期望值，否则误报
from rss_feed import CONTENT_NS, CST, _clean, generate_rss_feed

PREFIX = "podcasts/"
CONFIG_KEY = f"{PREFIX}config.json"
EPISODES_KEY = f"{PREFIX}episodes.json"
COVER_KEY = f"{PREFIX}cover.png"   # 历史兜底 key；--init 实际上传带日期文件名并写入 config.cover_url
FEED_KEY = f"{PREFIX}feed.xml"

JSON_CT = "application/json; charset=utf-8"
RSS_CT = "application/rss+xml; charset=utf-8"
MD_CT = "text/markdown; charset=utf-8"
NO_CACHE = "no-cache, max-age=60"


def fetch_config(uploader) -> Optional[dict]:
    """频道配置；未 --init 时返回 None（调用方决定报错口径）。"""
    text = uploader.download_text(CONFIG_KEY)
    return json.loads(text) if text else None


def fetch_episodes(uploader) -> list:
    text = uploader.download_text(EPISODES_KEY)
    return json.loads(text) if text else []


def upsert_episode(episodes: list, new_ep: dict) -> list:
    """按 slug 幂等更新：已存在则原地覆盖（保留首次 pub_date 与期号），否则追加。"""
    for i, ep in enumerate(episodes):
        if ep.get("slug") == new_ep["slug"]:
            new_ep["pub_date"] = ep.get("pub_date", new_ep["pub_date"])
            new_ep["episode_num"] = ep.get("episode_num", new_ep["episode_num"])
            episodes[i] = new_ep
            return episodes
    episodes.append(new_ep)
    return episodes


def build_description(title: str, notes_path=None) -> str:
    """notes.md（Markdown）→ HTML description；无 notes 退化为纯标题。

    EP6 教训的敏感路径：这里是 description 的唯一构建点，两个 CLI 不再各写一份。
    """
    if notes_path:
        text = Path(notes_path).read_text(encoding="utf-8").strip()
        return markdown.markdown(text, extensions=["extra"])
    return f"<p>{html.escape(title)}</p>"


def _normalize_ep(ep: dict) -> str:
    return json.dumps(ep, ensure_ascii=False, sort_keys=True)


def _changed_fields(old: dict, new: dict) -> list:
    return [k for k in sorted(set(old) | set(new)) if old.get(k) != new.get(k)]


def check_state_diff(remote_episodes: list, new_episodes: list, target_slug: str) -> list:
    """「改 A 不伤 B」守卫：比对线上 episodes.json，返回违规清单（空 = 安全）。

    允许的差异只有两种：新增 target_slug、或修改 target_slug 自身字段。
    删除、篡改、顺序变化、夹带新增其他单集一律违规——发布是全量重写，
    任何非目标差异都会原样落到线上。
    """
    remote = {ep.get("slug"): ep for ep in remote_episodes}
    new = {ep.get("slug"): ep for ep in new_episodes}
    violations = []
    for slug, rep in remote.items():
        if slug == target_slug:
            continue
        if slug not in new:
            violations.append(f"{slug}: 线上存在，推送后将被删除")
        elif _normalize_ep(rep) != _normalize_ep(new[slug]):
            fields = ", ".join(_changed_fields(rep, new[slug]))
            violations.append(f"{slug}: 非目标单集字段被改动（{fields}）")
    for slug in new:
        if slug != target_slug and slug not in remote:
            violations.append(f"{slug}: 非目标单集却被新增")
    remote_order = [s for s in (ep.get("slug") for ep in remote_episodes) if s in new]
    new_order = [s for s in (ep.get("slug") for ep in new_episodes) if s in remote]
    if remote_order != new_order:
        violations.append(f"单集顺序发生变化: 线上 {remote_order} -> 推送 {new_order}")
    return violations


def check_feed_consistency(rss_xml: str, episodes: list) -> list:
    """渲染层守卫：解析生成的 feed，逐 item 校验内容归属与 episodes.json 一致。

    正是 CDATA 前缀污染这类"渲染器把 A 的内容装进 B 的 item"事故的拦截网：
    guid 定位 slug，description / content:encoded / title 必须与事实源同 slug
    条目逐字节一致（期望值经 _clean，与渲染共用同一清洗）。
    """
    root = ET.fromstring(rss_xml)
    items = root.findall("./channel/item")
    violations = []
    if len(items) != len(episodes):
        violations.append(f"feed item 数 {len(items)} != episodes 数 {len(episodes)}")
    by_slug = {ep.get("slug"): ep for ep in episodes}
    feed_slugs = []
    for i, item in enumerate(items):
        guid = item.findtext("guid") or ""
        slug = guid[len("episode:"):] if guid.startswith("episode:") else guid
        feed_slugs.append(slug)
        ep = by_slug.get(slug)
        if ep is None:
            violations.append(f"feed item[{i}] guid={guid!r} 不在 episodes.json 中")
            continue
        expected_desc = _clean(ep.get("description", ""))
        for tag, label in (("description", "description"),
                           (f"{{{CONTENT_NS}}}encoded", "content:encoded")):
            got = item.findtext(tag) or ""
            if got != expected_desc:
                violations.append(f"{slug}: feed {label} 与 episodes.json 不一致"
                                  f"（feed 侧开头: {got[:60]!r}）")
        if (item.findtext("title") or "") != _clean(ep.get("title", "")):
            violations.append(f"{slug}: feed title 与 episodes.json 不一致")
    if set(feed_slugs) != set(by_slug) or len(set(feed_slugs)) != len(feed_slugs):
        violations.append("feed guid 集合与 episodes.json slug 集合不一致")
    return violations


def publish_state(uploader, config: dict, episodes: list, target_slug: str,
                  force_state: bool = False) -> str:
    """写远端状态并重建 feed（episodes.json 先、feed.xml 后），返回 feed URL。

    推送前三道守卫，任一失败即中止且**不写任何远端 key**：
      1. 状态 diff：除 target_slug 外，线上其余单集必须逐字节不变
         （force_state 跳过这一道，供预期中的批量迁移使用）
      2. feed 渲染校验：坏 feed 在触网前拦截（任何模式下都不跳过）
      3. 覆盖前把线上旧 episodes.json 备份到 backups/（误发可回滚）
    """
    remote_text = uploader.download_text(EPISODES_KEY)
    remote_episodes = json.loads(remote_text) if remote_text else []
    if not force_state:
        violations = check_state_diff(remote_episodes, episodes, target_slug)
        if violations:
            print(f"❌ 发布中止：本次目标是 {target_slug}，但推送会影响其他单集：")
            for v in violations:
                print(f"   - {v}")
            print("   预期中的批量迁移请显式使用 --force-state；若线上在本次运行期间"
                  "被并发更新，重新运行即可基于最新状态重建（分片缓存不重复计费）。")
            sys.exit(1)

    cover_url = config.get("cover_url") or f"{uploader.base_url}/{COVER_KEY}"
    rss_xml = generate_rss_feed(
        config, episodes,
        feed_url=f"{uploader.base_url}/{FEED_KEY}",
        cover_url=cover_url,
    )
    feed_violations = check_feed_consistency(rss_xml, episodes)
    if feed_violations:
        print("❌ 发布中止：渲染出的 feed 与 episodes.json（事实源）不一致：")
        for v in feed_violations:
            print(f"   - {v}")
        sys.exit(1)

    new_text = json.dumps(episodes, ensure_ascii=False, indent=2)
    # 幂等重发（如 feed 写失败后的重跑）跳过备份：内容逐字节相同，没有旧值会丢失
    if remote_text and remote_text != new_text:
        ts = datetime.now(CST).strftime("%Y%m%dT%H%M%S")
        uploader.upload_text(remote_text, f"{PREFIX}backups/episodes_{ts}.json",
                             content_type=JSON_CT)
    uploader.upload_text(new_text,
                         EPISODES_KEY, content_type=JSON_CT, cache_control=NO_CACHE)
    return uploader.upload_text(rss_xml, FEED_KEY,
                                content_type=RSS_CT, cache_control=NO_CACHE)
