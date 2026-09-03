#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
新闻抓取 + 口播文案生成 主脚本
每天早上8点运行：抓取国内和国际新闻，生成大白话口播文案，存入 SQLite 查重。
"""
import sys
import json
import urllib.request
import ssl
import os
import re
from datetime import datetime

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import news_db

# 忽略 SSL 证书（部分新闻源）
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36"

NEWS_SOURCES = {
    "国内": [
        # 澎湃新闻国内 (JSON)
        {"name": "澎湃", "url": "https://api.thepaper.cn/contentapi/wwwIndex/rightSidebar", "type": "json"},
        # 新浪国内新闻 (HTML RSS-like)
        {"name": "新浪", "url": "https://feed.mix.sina.com.cn/api/roll/get?pageid=153&lid=2516&k=&num=20&page=1", "type": "json"},
    ],
    "国际": [
        {"name": "环球网", "url": "https://feed.mix.sina.com.cn/api/roll/get?pageid=153&lid=2517&k=&num=20&page=1", "type": "json"},
        {"name": "参考消息", "url": "https://www.cankaoxiaoxi.com/", "type": "html"},
    ],
}


def http_get(url, timeout=15):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=timeout, context=ctx) as resp:
        return resp.read().decode("utf-8", errors="ignore")


def strip_html(text):
    text = re.sub(r"<[^>]+>", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def fetch_source(src, category):
    """返回 list of dict: title, url"""
    items = []
    try:
        raw = http_get(src["url"])
        if src["type"] == "json":
            try:
                data = json.loads(raw)
                # 新浪滚动接口
                news = data.get("result", {}).get("data", []) if isinstance(data, dict) else []
                for n in news:
                    title = n.get("title") or n.get("word") or ""
                    link = n.get("url") or n.get("wapurl") or ""
                    if title:
                        items.append({"title": strip_html(title), "url": link, "source": src["name"]})
            except Exception as e:
                print(f"  [!] 解析JSON失败 {src['name']}: {e}")
        elif src["type"] == "html":
            # 提取链接和标题
            links = re.findall(r'<a[^>]+href="([^"]+)"[^>]*>(.*?)</a>', raw, re.S)
            for href, text in links:
                title = strip_html(text)
                if title and len(title) > 8 and ("cankaoxiaoxi" in href or href.startswith("/")):
                    full = href if href.startswith("http") else "https://www.cankaoxiaoxi.com" + href
                    items.append({"title": title, "url": full, "source": src["name"]})
    except Exception as e:
        print(f"  [!] 抓取失败 {src['name']}: {e}")
    return items


def fetch_news():
    """抓取所有来源，返回 {category: [record]}"""
    result = {}
    for category, sources in NEWS_SOURCES.items():
        records = []
        seen = set()
        for src in sources:
            print(f"抓取 {category} <- {src['name']} ...")
            for item in fetch_source(src, category):
                if item["title"] in seen:
                    continue
                seen.add(item["title"])
                records.append(item)
        result[category] = records
        print(f"  {category} 共获取 {len(records)} 条")
    return result


def generate_copy(record):
    """根据标题生成口播文案（大白话）。实际应用中可由 LLM 生成，这里提供结构化模板。"""
    t = record.get("title", "")
    # 简单的口播文案模板 —— 真实场景建议用 LLM 扩写
    copy = (
        f"家人们，今天这条新闻咱得说道说道。\n"
        f"{t}。\n"
        f"具体怎么回事，咱们接着往下看。\n"
        f"这里是自动视频工具，关注我，每天带你看最新鲜的国内外大事。"
    )
    return copy


def main():
    print(f"=== 自动视频工具 新闻抓取开始 {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} ===")
    news_db.init_db()

    all_news = fetch_news()
    saved = 0
    skipped = 0

    for category, records in all_news.items():
        for rec in records:
            # 生成口播文案（大白话）
            content = generate_copy(rec)
            record = {
                "title": rec["title"],
                "intro": rec["title"][:50],           # 简介取标题前50字，后续可优化
                "key_time": "",                        # 重点时间，待人工/LLM填充
                "location": "",                        # 地点
                "people": "",                          # 人物
                "content": content,
                "category": category,
                "source": rec.get("source", ""),
                "url": rec.get("url", ""),
            }
            ok, fp = news_db.insert_news(record)
            if ok:
                saved += 1
                print(f"  [+] 新增: [{category}] {record['title']}")
            else:
                skipped += 1

    print(f"=== 完成: 新增 {saved} 条, 重复跳过 {skipped} 条 ===")

    # 输出新增记录到 output/ 供后续步骤使用
    if saved:
        os.makedirs(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "output"), exist_ok=True)
        out_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                                "output", f"news_{datetime.now().strftime('%Y%m%d_%H%M')}.json")
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump({"date": datetime.now().strftime("%Y-%m-%d"), "saved": saved, "skipped": skipped}, f, ensure_ascii=False, indent=2)
        print(f"运行摘要: {out_path}")

        # 生成合并版口播文案（用于华声一次生成一个视频）
        merge_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                                  "output", f"口播文案_{datetime.now().strftime('%Y%m%d')}.txt")
        merged = build_merged_copy(saved)
        with open(merge_path, "w", encoding="utf-8") as f:
            f.write(merged)
        print(f"合并口播文案已生成: {merge_path}")
    return saved


def build_merged_copy(saved):
    """把当天新增的口播文案合并成一份完整的口播稿（一次生成一个视频）。"""
    rows = news_db.recent_news(limit=saved)
    parts = []
    parts.append("大家好，欢迎收看今天的新闻速递，我是你们的主播。下面为您带来今天的国内外要闻。\n")
    for i, row in enumerate(rows, 1):
        title = row.get("title", "")
        category = row.get("category", "")
        # 简要概述每条新闻，加入分类标记
        parts.append(f"{i}. 【{category}】{title}。")
    parts.append("\n以上就是今天的全部内容，感谢收看，我们明天再见！")
    return "\n".join(parts)


if __name__ == "__main__":
    main()
