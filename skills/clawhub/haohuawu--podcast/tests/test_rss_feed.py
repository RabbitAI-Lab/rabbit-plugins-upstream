"""RSS feed invariants: valid XML, stable guid, CDATA semantics, determinism."""

import xml.etree.ElementTree as ET

import pytest
from rss_feed import generate_rss_feed, _cdata

CONFIG = {
    "title": "测试频道", "description": "频道描述", "author": "作者",
    "email": "a@b.com", "site_url": "https://example.com",
}


def make_episode(slug="20260101_ep_one", description="<p>hello</p>", **over):
    ep = {
        "slug": slug, "title": "EP One -- 第一期", "description": description,
        "audio_url": f"https://cdn.example.com/{slug}.mp3", "audio_size": 12345,
        "duration": 600, "pub_date": "2026-01-01T08:00:00+08:00", "episode_num": 1,
    }
    ep.update(over)
    return ep


def gen(episodes):
    return generate_rss_feed(CONFIG, episodes,
                             feed_url="https://cdn.example.com/feed.xml",
                             cover_url="https://cdn.example.com/cover.png")


NS = {"itunes": "http://www.itunes.com/dtds/podcast-1.0.dtd",
      "atom": "http://www.w3.org/2005/Atom"}


def test_output_is_parseable_xml_with_channel_fields():
    root = ET.fromstring(gen([make_episode()]))
    ch = root.find("channel")
    assert ch.find("title").text == "测试频道"
    assert ch.find("language").text == "zh-cn"
    assert ch.find("link").text == "https://example.com"
    assert ch.find("atom:link", NS).get("rel") == "self"
    assert ch.find("itunes:owner/itunes:email", NS).text == "a@b.com"
    assert ch.find("itunes:image", NS).get("href") == "https://cdn.example.com/cover.png"
    assert ch.find("itunes:category", NS).get("text") == "Technology"


def test_item_guid_is_slug_derived_and_not_permalink():
    item = ET.fromstring(gen([make_episode()])).find("channel/item")
    guid = item.find("guid")
    assert guid.text == "episode:20260101_ep_one"
    assert guid.get("isPermaLink") == "false"
    enclosure = item.find("enclosure")
    assert enclosure.get("type") == "audio/mpeg"
    assert enclosure.get("length") == "12345"


def test_feed_generation_is_deterministic():
    eps = [make_episode(), make_episode(slug="20260102_ep_two", episode_num=2)]
    assert gen(eps) == gen(eps)


def test_description_html_survives_raw_in_cdata():
    xml = gen([make_episode(description='<p>粗体 <b>x</b> &amp; 链接</p>')])
    assert "<![CDATA[<p>粗体 <b>x</b> &amp; 链接</p>]]>" in xml
    # and it round-trips through an XML parser
    item = ET.fromstring(xml).find("channel/item")
    assert "粗体" in item.find("description").text


def test_cdata_terminator_inside_description_is_split():
    assert _cdata("a]]>b") == "<![CDATA[a]]]]><![CDATA[>b]]>"
    xml = gen([make_episode(description="前]]>后")])
    ET.fromstring(xml)  # must stay well-formed


def test_control_chars_are_stripped():
    xml = gen([make_episode(title="标题\x08有控制符", description="正文\x0b")])
    ET.fromstring(xml)
    assert "\x08" not in xml and "\x0b" not in xml


def test_pub_date_iso_to_rfc2822_and_legacy_passthrough():
    xml = gen([make_episode()])
    assert "01 Jan 2026" in xml and "+0800" in xml
    legacy = "Mon, 05 May 2025 12:00:00 +0800"
    xml2 = gen([make_episode(pub_date=legacy)])
    assert legacy in xml2


def test_many_items_each_keep_their_own_description():
    # 回归测试（真实事故 EP16）：token 无终结符时 "-1" 是 "-10".."-15" 的前缀，
    # item 1 的 CDATA 串进所有两位数 item。必须用 ≥11 个 item 才能触发。
    eps = [make_episode(slug=f"2026010{i:02d}_ep{i}", episode_num=i + 1,
                        description=f"<p>第{i}集独有正文</p>")
           for i in range(13)]
    root = ET.fromstring(gen(eps))
    descs = [it.find("description").text for it in root.findall("channel/item")]
    for i, d in enumerate(descs):
        assert d == f"<p>第{i}集独有正文</p>", f"item {i} 的 description 被污染: {d[:40]}"


def test_placeholder_collision_does_not_corrupt_feed():
    # BUG-3 修复：占位符带每次生成的随机 nonce，正文字面量不再可能碰撞
    eps = [make_episode(description="正文提到 CDATAPLACEHOLDER1X 这个词"),
           make_episode(slug="20260102_ep_two", episode_num=2,
                        description="<p>第二集正文</p>")]
    root = ET.fromstring(gen(eps))
    first_desc = root.find("channel/item/description").text
    assert "第二集正文" not in (first_desc or "")
    assert "CDATAPLACEHOLDER1X" in (first_desc or "")
