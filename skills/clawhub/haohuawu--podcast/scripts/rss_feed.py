#!/usr/bin/env python3
"""播客 RSS 2.0 feed 生成（纯标准库，零三方依赖）。

输出对齐 RSS 2.0 / Apple Podcasts / PSP-1 要求：
- itunes:category 用 text 属性；itunes:image / itunes:owner 必出
- atom:link rel="self"；guid isPermaLink="false" 且与 URL 解耦（重跑不产生新单集）
- pubDate 用 email.utils.format_datetime（locale 无关的 RFC 2822）
"""

import re
import uuid
import xml.etree.ElementTree as ET
from datetime import datetime, timezone, timedelta
from email.utils import format_datetime
from typing import Optional

ITUNES_NS = "http://www.itunes.com/dtds/podcast-1.0.dtd"
ATOM_NS = "http://www.w3.org/2005/Atom"
CONTENT_NS = "http://purl.org/rss/1.0/modules/content/"
CST = timezone(timedelta(hours=8))

ET.register_namespace("itunes", ITUNES_NS)
ET.register_namespace("atom", ATOM_NS)
ET.register_namespace("content", CONTENT_NS)


def _cdata(html: str) -> str:
    """CDATA 包裹 HTML；内部出现的 ]]> 拆到两个 CDATA 段避免提前终止"""
    return "<![CDATA[" + html.replace("]]>", "]]]]><![CDATA[>") + "]]>"


def _clean(text: str) -> str:
    """去除 XML 1.0 非法控制字符（爬取文本常见，会让序列化/解析崩溃）"""
    return re.sub(r"[\x00-\x08\x0b\x0c\x0e-\x1f]", "", text or "")


def _itunes(parent, tag: str, value: Optional[str] = None, **attrs):
    """value 为文本节点内容；attrs 为 XML 属性（如 category 的 text、image 的 href）"""
    el = ET.SubElement(parent, f"{{{ITUNES_NS}}}{tag}", {k: _clean(v) for k, v in attrs.items()})
    if value is not None:
        el.text = _clean(value)
    return el


def _to_rfc2822(pub_date) -> str:
    """episodes.json 里存 ISO 字符串（如 2026-07-13T08:00:00+08:00），输出 RFC 2822。
    兼容旧记录里已是 RFC 2822 的字符串（原样透传）。"""
    if isinstance(pub_date, datetime):
        dt = pub_date
    elif isinstance(pub_date, str):
        try:
            dt = datetime.fromisoformat(pub_date)
        except ValueError:
            return pub_date  # 旧格式，视为已是 RFC 2822
    else:
        dt = datetime.now(CST)
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=CST)
    return format_datetime(dt)


def generate_rss_feed(config: dict, episodes: list, feed_url: str, cover_url: str) -> str:
    """生成标准播客 RSS 2.0 feed。

    Args:
        config: 频道配置，必填 title/description/author/email/site_url，
                可选 language（默认 zh-cn）/ category（默认 Technology）
        episodes: 单集列表，每项含 title/description/slug/audio_url/audio_size/
                  duration/pub_date(ISO 字符串)/episode_num
        feed_url: feed 自身公网 URL（atom:link rel=self）
        cover_url: 封面公网 URL（itunes:image）

    Returns:
        RSS XML 字符串（str，非 bytes）
    """
    rss = ET.Element("rss", {"version": "2.0"})
    channel = ET.SubElement(rss, "channel")

    ET.SubElement(channel, "title").text = _clean(config["title"])
    ET.SubElement(channel, "description").text = _clean(config["description"])
    ET.SubElement(channel, "language").text = config.get("language", "zh-cn")
    # RSS 2.0：channel link 是节目主页，不是 feed 自身
    ET.SubElement(channel, "link").text = _clean(config["site_url"])
    ET.SubElement(
        channel, f"{{{ATOM_NS}}}link",
        {"href": feed_url, "rel": "self", "type": "application/rss+xml"},
    )

    _itunes(channel, "author", config["author"])
    owner = _itunes(channel, "owner")
    _itunes(owner, "name", config["author"])
    _itunes(owner, "email", config["email"])  # 小宇宙认领节目靠这个邮箱收验证码
    _itunes(channel, "image", href=cover_url)
    _itunes(channel, "category", text=config.get("category", "Technology"))
    _itunes(channel, "explicit", "false")

    # description 为 HTML（小宇宙等客户端按 HTML 渲染 shownotes），经 CDATA 注入：
    # ET 无原生 CDATA，用占位符在序列化后替换
    # 占位符带随机 nonce（防正文字面量碰撞）+ 尾部终结符 END（防前缀污染：
    # 无终结符时 "-1" 是 "-10".."-15" 的前缀，item 1 的 CDATA 会串进两位数 item——
    # 真实事故：EP16 的 description 变成了 EP2 的内容）
    nonce = uuid.uuid4().hex
    cdata_blocks = {}
    for n, ep in enumerate(episodes):
        item = ET.SubElement(channel, "item")
        ET.SubElement(item, "title").text = _clean(ep["title"])
        token = f"CDATA-{nonce}-{n}-END"
        cdata_blocks[token] = _cdata(_clean(ep.get("description", "")))
        ET.SubElement(item, "description").text = token
        ET.SubElement(item, f"{{{CONTENT_NS}}}encoded").text = token
        ET.SubElement(item, "pubDate").text = _to_rfc2822(ep.get("pub_date"))

        enclosure = ET.SubElement(item, "enclosure")
        enclosure.set("url", ep["audio_url"])
        enclosure.set("length", str(ep.get("audio_size", 0)))
        enclosure.set("type", "audio/mpeg")

        # guid 与域名/URL 解耦：slug 稳定则 guid 稳定，重跑覆盖同一单集而非新增
        ET.SubElement(item, "guid", isPermaLink="false").text = f"episode:{ep['slug']}"

        _itunes(item, "duration", str(ep.get("duration", 0)))
        if ep.get("episode_num"):
            _itunes(item, "episode", str(ep["episode_num"]))

    ET.indent(rss)  # Python 3.9+，仅美化
    body = ET.tostring(rss, encoding="unicode")
    for token, block in cdata_blocks.items():
        body = body.replace(token, block)
    return '<?xml version="1.0" encoding="UTF-8"?>\n' + body + "\n"
