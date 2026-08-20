#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
xhs-track-analysis · 受监督有界采集器原型（collect.py）
=====================================================================
⚠️ 合规与责任边界（运行前必读）
---------------------------------------------------------------------
1. 本脚本仅用于**你本人拥有/授权的账号**，在你的浏览器、你本人在场监督下，
   对小红书**公开搜索结果页与公开笔记页**做有限摘取，用于「赛道深度分析」
   的资料准备（即本 Skill 定义的工作：把最慢、最容易漏的资料整理清楚）。
2. 本脚本**不实现任何反爬/风控对抗**：不伪造请求签名（x-s/x-t）、不自动过
   滑块、不伪造设备指纹、不突破登录态私有接口。它只是用普通浏览器把"人手动
   翻页查看"的过程自动化，且全程你可见、可中断。
3. 小红书用户协议可能禁止自动化访问。运行即表示你已知悉并自行承担由此产生的
   账号与合规风险（含《个人信息保护法》项下评论数据处理的合规责任）。本工具作
   者/提供方不承担任何后果。
4. 仅采集公开内容；不采集非公开数据；不对采集数据做超出分析目的的使用。
5. 严格限频、限量与范围（见 config.json）。超出即停止。

运行方式（需先安装）：
    pip install -r requirements.txt
    playwright install chromium
    python3 collect.py config.json
首次会打开浏览器并展示登录二维码，请用手机扫码；扫码后脚本自动开始采集。
=====================================================================
"""

import sys
import json
import time
import csv
import datetime
import os

try:
    from playwright.sync_api import sync_playwright
except ImportError:
    sys.exit("未安装 playwright。请先: pip install -r requirements.txt && playwright install chromium")

# ---------------------------------------------------------------------------
# 免责确认：必须显式键入确认短语才继续
# ---------------------------------------------------------------------------
CONFIRM_PHRASE = "我已知悉并承担合规责任"
DISCLAIMER = """
╔════════════════════════════════════════════════════════════════════════╗
║  受监督有界采集器 · 合规边界                                          ║
║  1) 仅本人/授权账号、本人监督、仅公开页、有限摘取。                    ║
║  2) 不实现任何反爬/签名伪造/风控对抗。                                ║
║  3) 你自行承担账号与法律合规风险。                                    ║
║  4) 仅采集公开内容，不超范围使用。                                    ║
╚════════════════════════════════════════════════════════════════════════╝
"""


def confirm_compliance() -> bool:
    print(DISCLAIMER)
    ans = input(f"请输入确认短语（{CONFIRM_PHRASE}）以继续，其他输入将退出：\n> ").strip()
    return ans == CONFIRM_PHRASE


# ---------------------------------------------------------------------------
# 选择器（XHS 前端会变，集中在此便于维护；运行前按需核对）
# ---------------------------------------------------------------------------
SELECTORS = {
    "search_input": ["input[name='keyword']", "#search-input", "input[placeholder*='搜索']"],
    "search_button": ["button.search-button", "button[type='submit']", ".search-button"],
    "sort_tab": "div.sort-bar div[class*='sort']",   # 按文本匹配 综合/最新/...
    "note_card": ["section.note-item", "div.note-item", "a.cover", ".feeds-container .note-item"],
    "note_title": [".title", ".content", ".note-title", "a.title"],
    "note_author": [".author .name", ".name", ".author-wrapper .name"],
    "note_likes": [".like-wrapper .count", ".like .count", ".count"],
    "note_url": "a.cover",
}

XHS_BASE = "https://www.xiaohongshu.com"


def _first_match(page, selectors, **kwargs):
    """尝试多个候选选择器，返回首个命中的元素。"""
    for sel in selectors:
        try:
            el = page.query_selector(sel, **kwargs)
            if el:
                return el
        except Exception:
            continue
    return None


def _text_or(page, selectors, default=""):
    el = _first_match(page, selectors)
    return el.inner_text().strip() if el else default


def login_via_qr(page, timeout=180):
    """打开首页，等待用户扫码登录。通过 web_session cookie 判断是否登录。"""
    print("[登录] 打开小红书首页，请在弹出的浏览器中用手机扫码登录…")
    page.goto(XHS_BASE + "/explore", wait_until="domcontentloaded")
    # 若出现登录二维码弹窗，等待用户在浏览器中扫码
    deadline = time.time() + timeout
    while time.time() < deadline:
        cookies = page.context.cookies()
        if any(c["name"] == "web_session" for c in cookies):
            print("[登录] 检测到 web_session，登录成功。")
            return True
        time.sleep(3)
    print("[登录] 超时未登录，退出。")
    return False


def apply_sort(page, sort_name, cfg):
    """点击排序标签（按文本匹配）。失败则忽略（使用默认综合排序）。"""
    try:
        tabs = page.query_selector_all(SELECTORS["sort_tab"])
        for t in tabs:
            if sort_name in (t.inner_text() or ""):
                t.click()
                time.sleep(1.5)
                return True
    except Exception as e:
        print(f"[排序] 应用「{sort_name}」失败，继续使用当前排序：{e}")
    return False


def parse_count(text):
    """把 '1.2万' / '3.4k' / '1234' 转成整数。"""
    if not text:
        return 0
    text = text.strip().replace(" ", "")
    try:
        if "万" in text:
            return int(float(text.replace("万", "")) * 10000)
        if "w" in text.lower():
            return int(float(text.lower().replace("w", "")) * 10000)
        return int(float(text))
    except Exception:
        return 0


def collect_search(page, keyword, sort_name, cfg):
    """对一个关键词+排序做有限摘取，返回笔记字典列表。"""
    q = "/search_result?keyword=" + keyword
    page.goto(XHS_BASE + q, wait_until="domcontentloaded")
    time.sleep(2)
    apply_sort(page, sort_name, cfg)

    notes = []
    scrolls = int(cfg.get("scroll_times", 5))
    max_notes = int(cfg.get("max_notes_per_query", 20))
    for _ in range(scrolls):
        if len(notes) >= max_notes:
            break
        cards = page.query_selector_all(".note-item") or []
        for card in cards:
            if len(notes) >= max_notes:
                break
            try:
                title = _text_or(card, SELECTORS["note_title"])
                author = _text_or(card, SELECTORS["note_author"])
                likes = parse_count(_text_or(card, SELECTORS["note_likes"]))
                href = ""
                try:
                    a = card.query_selector("a.cover") or card.query_selector("a")
                    href = a.get_attribute("href") if a else ""
                except Exception:
                    pass
                note_id = href.rstrip("/").split("/")[-1].split("?")[0] if href else ""
                notes.append({
                    "keyword": keyword,
                    "sort": sort_name,
                    "note_id": note_id,
                    "url": (XHS_BASE + href) if href.startswith("/") else href,
                    "title": title,
                    "author": author,
                    "likes": likes,
                    "captured_at": datetime.date.today().isoformat(),
                })
            except Exception as e:
                print(f"[摘取] 单卡失败，跳过: {e}")
        # 去重后再滚
        seen = {n["note_id"] for n in notes if n["note_id"]}
        page.mouse.wheel(0, 1200)
        time.sleep(float(cfg.get("delay_sec", 3)))
    # 去重
    uniq = {}
    for n in notes:
        uniq.setdefault(n["note_id"] or n["url"], n)
    return list(uniq.values())


def save_outputs(all_notes, cfg):
    out_dir = cfg.get("output_dir", "output")
    os.makedirs(out_dir, exist_ok=True)
    ts = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

    csv_path = os.path.join(out_dir, f"raw_notes_{ts}.csv")
    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["keyword", "sort", "note_id", "url", "title", "author", "likes", "captured_at"])
        w.writeheader()
        for n in all_notes:
            w.writerow(n)
    print(f"[输出] CSV: {csv_path}（{len(all_notes)} 条）")

    # 主表-风格 Markdown（仅原始资料，判断留给 Skill/人工）
    md_path = os.path.join(out_dir, f"collection_report_{ts}.md")
    with open(md_path, "w", encoding="utf-8") as f:
        f.write(f"# 采集报告 · {ts}\n\n")
        f.write("> 本文件为**原始公开资料**摘取，未做商业化浓度/达人解读/评论四行为判断；\n")
        f.write("> 请交给 xhs-track-analysis Skill 按 methodology 完成分析。\n\n")
        f.write(f"共采集 {len(all_notes)} 条笔记（按关键词×排序）。\n\n")
        f.write("## 三、采集记录（每轮一行，已合并去重）\n\n")
        f.write("| 关键词 | 排序角度 | note_id | 作者 | 赞 | 链接 | 采集时间 |\n")
        f.write("| --- | --- | --- | --- | --- | --- | --- |\n")
        for n in all_notes:
            f.write(f"| {n['keyword']} | {n['sort']} | {n['note_id']} | {n['author']} | {n['likes']} | {n['url']} | {n['captured_at']} |\n")
    print(f"[输出] Markdown: {md_path}")


def main():
    if not confirm_compliance():
        sys.exit("未确认合规，已退出。")
    if len(sys.argv) < 2:
        sys.exit("用法: python3 collect.py <config.json>")
    cfg_path = sys.argv[1]
    with open(cfg_path, encoding="utf-8") as f:
        cfg = json.load(f)

    keywords = cfg.get("keywords", [])
    sorts = cfg.get("sorts", ["综合", "最新", "最多点赞", "最多收藏", "最多评论"])
    assert keywords, "config.json 需包含 keywords 列表"

    all_notes = []
    with sync_playwright() as p:
        # headed=True：用户在场监督，可见二维码与页面，可随时中断
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(
            user_agent=("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                        "AppleWebKit/537.36 (KHTML, like Gecko) "
                        "Chrome/124.0 Safari/537.36")
        )
        page = context.new_page()
        if not login_via_qr(page):
            browser.close()
            sys.exit("登录失败。")

        for kw in keywords:
            for s in sorts:
                print(f"[采集] 关键词={kw} 排序={s}")
                try:
                    notes = collect_search(page, kw, s, cfg)
                    all_notes.extend(notes)
                except Exception as e:
                    print(f"[采集] {kw}/{s} 出错跳过: {e}")
                time.sleep(float(cfg.get("delay_sec", 3)))
        browser.close()

    save_outputs(all_notes, cfg)
    print("[完成] 受监督采集结束。请人工核对并对商业化浓度/达人/评论做判断。")


if __name__ == "__main__":
    main()
