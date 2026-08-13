#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""collect_gallery: 一次性生成尽可能完整的梗图图鉴（多源 × 高相关过滤 × 去重）。

设计目标（meme-digger v1.1 升级）：
  1. 一次运行覆盖所有可及图源，产出"完整图鉴候选池"；
  2. 候选必须与梗"高度相关、有直接联系"——按来源分档 + 上下文关键词过滤 + 评分排序；
  3. 显式增加"二创梗图"检索通道（B站二创/整活视频 + 百度"表情包/梗图/二创"查询）；
  4. 自动去重（URL + 下载后 sha256）；生成 05-梗图.md 候选清单，人工复核后定稿。

来源分档（T 级，权威度/直接联系从高到低）：
  T1  B站代表视频封面（直接联系=标题含梗）
  T2  B站高赞评论配图（直接联系=评论含梗词/反应词）
  T3  B站二创/合集/整活视频封面（query=梗名+二创/表情包/合集/整活/抽象）
  T4  百度图片（query=梗名+表情包/梗图/二创；内容需人工复核）
  T5  贴吧帖子首楼图（cookie + PC 网页；风控验证页自动降级）
  T6  斗图啦/发表情类站点（尽力而为，失败静默降级）

用法:
  python collect_gallery.py "<梗名>" [--variants "a,b,c"] [--out <工作区>]
      [--limit N] [--max-per-source N] [--min-like N] [--no-download] [--reuse]
"""
from __future__ import annotations

import sys
import os
import re
import json
import time
import hashlib
import urllib.parse

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import common  # noqa: E402
import bili_search  # noqa: E402
import bili_memes  # noqa: E402

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

BILI_REF = "https://www.bilibili.com/"
BAIDU_IMG_REF = "https://image.baidu.com/"
DOUTULA_REF = "https://www.doutula.com/"

# 二创/整活/图鉴向搜索词（直接关系过滤器）
ECHO_QUERIES = ["二创", "整活", "表情包", "梗图", "合集", "抽象"]
# 评论上下文里的"强相关"词（出现即加分/放行）
REACT = ["典", "笑死", "绷不住", "绝了", "表情包", "梗图", "图", "哈哈", "蚌埠", "难绷", "爆笑"]

cookies = common.load_cookies()
BILI_COOKIE = cookies.get("bilibili", "")
TIEBA_COOKIE = cookies.get("tieba", "")


# ---------------- 工具 ----------------
def norm_url(u: str) -> str:
    """URL 去重规整：去协议、去常见追踪参数、去尺寸后缀。"""
    u = re.sub(r"^https?:", "", u)
    u = re.sub(r"[?&](?:from|source|refer|client|timestamp|_t)=\S+", "", u)
    return u


def dl(url: str, referer: str = "", retries: int = 2, timeout: int = 20) -> bytes | None:
    """下载二进制；返回 None 表示失败。"""
    hdrs = {"User-Agent": common.UA, "Accept-Language": "zh-CN,zh;q=0.9"}
    if referer:
        hdrs["Referer"] = referer
    last = None
    for _ in range(retries + 1):
        try:
            req = urllib.request.Request(url, headers=hdrs)
            with urllib.request.urlopen(req, timeout=timeout) as r:
                return r.read()
        except Exception as e:
            last = e
            time.sleep(1.0)
    return None


# ---------------- 图源收集器（每个返回 candidate 列表）----------------
def _bili_search(kw: str, page: int = 1) -> list[dict]:
    """B站搜索（复用 bili_search 的抓取与解析）。"""
    url = ("https://search.bilibili.com/all?keyword="
           + urllib.parse.quote(kw) + f"&page={page}")
    return bili_search.parse_cards(bili_search.fetch(url))


def _cand(url: str, tier: int, score: float, ctx: str, src: str, query: str = "") -> dict:
    return {"url": url, "tier": tier, "score": score, "ctx": ctx[:120], "src": src, "query": query}


def collect_bili_primary(variants: list[str], min_like: int, max_per: int) -> list[dict]:
    """T1+T2：主视频封面 + 高赞评论配图（直接联系最强）。"""
    out: list[dict] = []
    seen_titles: set[str] = set()
    for v in variants:
        try:
            cards = _bili_search(v)
        except Exception as e:
            print(f"  !! B站搜索「{v}」失败: {e}")
            continue
        for c in cards[:5]:
            bvid = c.get("bvid", "")
            if not bvid or c.get("title") in seen_titles:
                continue
            seen_titles.add(c.get("title"))
            cands, title, cover = bili_memes.collect_video(bvid, pages=2, min_like=min_like, cookie=BILI_COOKIE)
            for x in cands:
                x["query"] = v
                x["src"] = f"bili-{v}"
                out.append(x)
            if len([c for c in out if c["tier"] <= 2]) >= max_per:
                return out
            time.sleep(0.3)
    return out


def collect_bili_echo(variants: list[str], max_per: int) -> list[dict]:
    """T3：二创/表情包/合集/整活/抽象 视频封面（二创检索通道）。"""
    out: list[dict] = []
    seen: set[str] = set()
    for v in variants:
        for q in ECHO_QUERIES:
            kw = f"{v} {q}"
            try:
                cards = _bili_search(kw)
            except Exception:
                continue
            for c in cards[:4]:
                bvid = c.get("bvid", "")
                u = norm_url(f"https://www.bilibili.com/video/{bvid}")
                if not bvid or u in seen:
                    continue
                seen.add(u)
                try:
                    cands, title, cover = bili_memes.collect_video(bvid, pages=0, min_like=0, cookie=BILI_COOKIE)
                except Exception:
                    continue
                if cover:
                    out.append(_cand(cover, 3, 1e8 - len(out), f"[{q}向视频] {title}",
                                     f"bili-echo-{v}", kw))
            time.sleep(0.2)
            if len(out) >= max_per:
                return out
    return out


def collect_baidu(variants: list[str], max_per: int) -> list[dict]:
    """T4：百度图片 acjson（query=梗名+表情包/梗图/二创）。内容人工复核。"""
    out: list[dict] = []
    seen: set[str] = set()
    for v in variants:
        for q in [f"{v} 表情包", f"{v} 梗图", f"{v} 二创", v]:
            qq = urllib.parse.quote(q)
            url = ("https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592"
                   f"&fp=result&queryWord={qq}&cl=2&lm=-1&ie=utf-8&oe=utf-8&word={qq}"
                   "&adpicid=&st=-1&z=&ic=0&face=0&istype=2&nc=1&pn=0&rn=30&gsm=1e")
            try:
                body = common.fetch(url, referer=BAIDU_IMG_REF)
                data = json.loads(body).get("data") or []
            except Exception as e:
                print(f"  !! 百度图片「{q}」失败: {e}")
                continue
            for i, d in enumerate(data):
                if not isinstance(d, dict):
                    continue
                u = d.get("thumbURL") or d.get("middleURL") or ""
                if not u:
                    continue
                n = norm_url(u)
                if n in seen:
                    continue
                seen.add(n)
                ctx = urllib.parse.unquote(d.get("fromPageTitleEnc", "") or "") or f"[百度图片:{q}]"
                boost = 400 if ("表情包" in q or "梗图" in q) else 0
                out.append(_cand(u, 4, 1000 - i * 10 + boost, ctx, "baidu", q))
            time.sleep(0.4)
            if len(out) >= max_per:
                return out
    return out


def collect_tieba(variants: list[str], max_per: int) -> list[dict]:
    """T5：贴吧帖子首楼图（cookie + PC 网页；风控验证页自动降级）。"""
    if not TIEBA_COOKIE:
        print("  !! 贴吧: 未配置 cookie，跳过（降级: web_search site:tieba.baidu.com）")
        return []
    out: list[dict] = []
    seen: set[str] = set()
    # 候选吧名：梗名本身 / 关联人物（由 variants 提供）+ 通用搜索
    bars = variants[:3]
    for bar in bars:
        kw = urllib.parse.quote(bar)
        url = f"https://tieba.baidu.com/f?kw={kw}&ie=utf-8"
        try:
            req = urllib.request.Request(url, headers={
                "User-Agent": common.UA, "Cookie": TIEBA_COOKIE,
                "Referer": "https://tieba.baidu.com/", "Accept-Language": "zh-CN,zh;q=0.9"})
            html = urllib.request.urlopen(req, timeout=15).read().decode("utf-8", "replace")
        except Exception as e:
            print(f"  !! 贴吧「{bar}」请求失败: {e}")
            continue
        # 风控验证页检测：无帖子结构 → 降级
        if "thread_list" not in html and "j_thread_list" not in html and 'data-field' not in html:
            print(f"  !! 贴吧「{bar}」返回风控验证页（当前网络/IP 被风控），跳过 → 降级 web_search")
            continue
        # 解析帖子：data-field JSON（title/tid）与首楼图
        for m in re.finditer(r'data-field="({.*?})"', html, re.S):
            try:
                f = json.loads(m.group(1).replace("&quot;", '"'))
            except Exception:
                continue
            title = f.get("title", "")
            tid = f.get("id") or f.get("tid") or ""
            if not title:
                continue
            # 帖子页抓首楼图
            try:
                turl = f"https://tieba.baidu.com/p/{tid}"
                req = urllib.request.Request(turl, headers={
                    "User-Agent": common.UA, "Cookie": TIEBA_COOKIE,
                    "Referer": url, "Accept-Language": "zh-CN,zh;q=0.9"})
                ph = urllib.request.urlopen(req, timeout=15).read().decode("utf-8", "replace")
                imgs = re.findall(r'https?://imgsa?e?\.baidu\.com/[^"\']+?\.(?:jpg|jpeg|png|gif)',
                                  ph)
            except Exception:
                imgs = []
            for u in imgs[:3]:
                n = norm_url(u)
                if n in seen:
                    continue
                seen.add(n)
                out.append(_cand(u, 5, 1e6 - len(out), f"[贴吧:{bar}] {title}", "tieba", bar))
            if len(out) >= max_per:
                return out
            time.sleep(0.3)
    return out


def collect_doutula(variants: list[str], max_per: int) -> list[dict]:
    """T6：斗图啦搜索结果图（尽力而为）。"""
    out: list[dict] = []
    seen: set[str] = set()
    for v in variants:
        qq = urllib.parse.quote(v)
        try:
            req = urllib.request.Request(f"https://www.doutula.com/search?keyword={qq}",
                headers={"User-Agent": common.UA, "Referer": DOUTULA_REF})
            html = urllib.request.urlopen(req, timeout=15).read().decode("utf-8", "replace")
        except Exception:
            continue
        # 斗图啦 图片懒加载：data-original / data-backup / class="lazy" src
        urls = re.findall(r'(?:data-original|data-backup|data-src)="(https?://[^"]+)"', html)
        for u in urls:
            n = norm_url(u)
            if n in seen or n.endswith((".gif",)) is False and "wx" not in n:
                pass
            if n in seen:
                continue
            seen.add(n)
            out.append(_cand(u, 6, 800 - len(out), f"[斗图啦:{v}]", "doutula", v))
        if len(out) >= max_per:
            return out
    return out


# ---------------- 主流程 ----------------
def main() -> int:
    import argparse
    ap = argparse.ArgumentParser(description="一次性完整梗图图鉴收集器")
    ap.add_argument("meme", help="梗名")
    ap.add_argument("--variants", default="", help="变体词（逗号分隔），用于搜索与相关性过滤")
    ap.add_argument("--out", default=".", help="工作区目录（写入 images/ 与 05-梗图.md）")
    ap.add_argument("--limit", type=int, default=60, help="总候选上限")
    ap.add_argument("--max-per-source", type=int, default=25)
    ap.add_argument("--min-like", type=int, default=20)
    ap.add_argument("--no-download", action="store_true", help="只出候选清单，不下载")
    ap.add_argument("--reuse", action="store_true", help="保留已有 images/ 不重下")
    args = ap.parse_args()

    variants = [x.strip() for x in
                ([args.meme] + ([v for v in args.variants.split(",") if v.strip()]))]
    variants = list(dict.fromkeys(variants))  # 去重保序
    print(f"# 图鉴收集: {args.meme} | 变体: {variants} | 上限 {args.limit}")

    pool: list[dict] = []
    sources = [
        ("B站主源(T1/T2)", lambda: collect_bili_primary(variants, args.min_like, args.max_per_source)),
        ("B站二创(T3)", lambda: collect_bili_echo(variants, args.max_per_source)),
        ("百度图片(T4)", lambda: collect_baidu(variants, args.max_per_source)),
        ("贴吧(T5)", lambda: collect_tieba(variants, args.max_per_source)),
        ("斗图啦(T6)", lambda: collect_doutula(variants, args.max_per_source)),
    ]
    for name, fn in sources:
        print(f"\n== {name} ==")
        try:
            got = fn()
        except Exception as e:
            print(f"  !! {name} 异常: {e}")
            got = []
        print(f"  → {len(got)} 个候选")
        pool.extend(got)
        time.sleep(0.5)

    # 去重 + 排序 + 上限
    seen = set()
    uniq = []
    for c in sorted(pool, key=lambda x: -x["score"]):
        n = norm_url(c["url"])
        if n in seen:
            continue
        seen.add(n)
        uniq.append(c)
        if len(uniq) >= args.limit:
            break

    print(f"\n# 去重后候选: {len(uniq)}")
    outdir = os.path.abspath(args.out)
    os.makedirs(os.path.join(outdir, "images"), exist_ok=True)

    # 生成 05-梗图.md 候选清单（人工复核表）
    rows = []
    for i, c in enumerate(uniq, 1):
        rows.append(f"| images/{i:03d}-t{c['tier']}.jpg | {c['url']} | {c['src']} | "
                    f"{c['ctx']} | 评分 {c['score']:.0f} | （人工确认） | （人工标注） |")
    md = """# 05-梗图图鉴（候选清单 · 人工复核后定稿）

> 本表由 collect_gallery.py 一次生成：多源收集 → 相关性分档 → 去重。**人工复核规则**：① 图片内容与梗主题相关（看 ctx/原图确认）；② 拿不准的一律删除；③ 定稿后在"含义/使用场景"列补注。

| 本地文件 | 原图URL | 来源 | 上下文/出处 | 评分 | 含义 | 使用场景 |
|---|---|---|---|---|---|---|
""" + "\n".join(rows) + f"""

## 来源统计
| 源 | 候选数 | 说明 |
|---|---|---|
| T1/T2 B站主源 | {sum(1 for c in uniq if c['tier']<=2)} | 视频封面+高赞评论配图（直接联系最强） |
| T3 B站二创 | {sum(1 for c in uniq if c['tier']==3)} | 二创/表情包/合集/整活视频封面 |
| T4 百度图片 | {sum(1 for c in uniq if c['tier']==4)} | 表情包/梗图/二创 查询（内容需复核） |
| T5 贴吧 | {sum(1 for c in uniq if c['tier']==5)} | 帖子首楼图（风控时降级） |
| T6 斗图啦 | {sum(1 for c in uniq if c['tier']==6)} | 表情包站（尽力而为） |

_生成时间: {time.strftime('%Y-%m-%d %H:%M')} · 梗: {args.meme}_
"""
    md_path = os.path.join(outdir, "05-梗图.md")
    with open(md_path, "w", encoding="utf-8") as f:
        f.write(md)
    print(f"✅ 候选清单已写: {md_path}")

    if args.no_download:
        print("\n（--no-download 模式：未下载，清单如上）")
        return 0

    # 下载 + 内容去重 + manifest
    manifest = []
    hashes: set[str] = set()
    n_ok = 0
    for i, c in enumerate(uniq, 1):
        ref = BILI_REF if c["src"].startswith("bili") else (
            BAIDU_IMG_REF if c["src"] == "baidu" else DOUTULA_REF if c["src"] == "doutula" else "https://tieba.baidu.com/")
        data = dl(c["url"], ref)
        if not data or len(data) < 1024:
            print(f"  ✗ {i:03d} 下载失败/过小: {c['url'][:60]}")
            continue
        ext = "gif" if data[:6] in (b"GIF89a", b"GIF87a") else \
              "png" if data[:8] == b"\x89PNG\r\n\x1a\n" else \
              "webp" if data[:4] == b"RIFF" else "jpg"
        h = hashlib.sha256(data).hexdigest()
        if h in hashes:
            print(f"  ~ {i:03d} 内容重复，跳过")
            continue
        hashes.add(h)
        fname = f"{i:03d}-t{c['tier']}.{ext}"
        with open(os.path.join(outdir, "images", fname), "wb") as f:
            f.write(data)
        manifest.append({"file": f"images/{fname}", "url": c["url"], "src": c["src"],
                         "ctx": c["ctx"], "score": c["score"]})
        n_ok += 1
        print(f"  ✓ {fname} <- {c['url'][:70]}")
        time.sleep(0.3)

    with open(os.path.join(outdir, "images", "manifest.json"), "w", encoding="utf-8") as f:
        json.dump(manifest, f, ensure_ascii=False, indent=2)
    print(f"\n✅ 下载完成: {n_ok} 张 → {os.path.join(outdir, 'images')}")
    print("   下一步: 人工复核 05-梗图.md（删除无关图、补含义/使用场景），再 make_report.py 出百科页")
    return 0


if __name__ == "__main__":
    sys.exit(main())
