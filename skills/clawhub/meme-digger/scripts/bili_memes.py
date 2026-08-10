#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""meme-digger: 定向挖掘正确的梗图（分级 + 评分，杜绝"抓到什么算什么"）。

用法:
    python bili_memes.py <bvid> [bvid...] [--pages N] [--min-like N]
                         [--download N] [--out <目录>]

分级策略:
  T1 视频封面   —— 代表视频(科普/考古/盘点/起源)的封面 = 该梗的权威视觉，必收
  T2 高赞评论图 —— 只收"点赞高 且 正文含梗词/反应词"的评论配图（评分排序）
  T3 待人工复核 —— 其余带图评论（低分，仅供人工翻查）

评分模型: score = 点赞数 × (1 + 0.8×含梗反应词 + 0.5×含"图/表情" + 0.3×短评贴图)
输出: 排序后的候选清单(markdown) + 可自动下载前 N 张到 --out 目录。
"""
import sys
import os
import re
import json
import time
import urllib.parse

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

import common

REACT = ["典", "笑死", "太典", "抽象", "绷不住", "难绷", "蚌埠", "麻了",
         "哈哈哈", "哈哈", "666", "绝了", "逆天", "好活", "精髓", "生草",
         "乐", "草", "好图", "表情包", "收藏了", "这图", "笑喷", "绷", "绷不住了"]


def get_json(url, cookie=""):
    return json.loads(common.fetch(url, cookie=cookie))


def score_comment(text: str, like: int) -> float:
    boost = 1.0
    if any(w in text for w in REACT):
        boost += 0.8
    if ("图" in text) or ("表情" in text):
        boost += 0.5
    if len(text) <= 24:
        boost += 0.3
    return like * boost


def collect_video(bvid: str, pages: int, min_like: int, cookie: str):
    """返回 (candidates, video_title, cover_url)。candidates: list[dict]"""
    v = get_json(f"https://api.bilibili.com/x/web-interface/view?bvid={bvid}", cookie)
    if v.get("code") != 0:
        print(f"!! {bvid} 不存在或不可访问")
        return [], "", ""
    data = v["data"]
    title = data.get("title", "")
    cover = "https:" + data["pic"] if data.get("pic", "").startswith("//") else data.get("pic", "")
    oid = data["aid"]
    cands = []
    if cover:
        cands.append({"tier": 1, "score": 1e9, "like": "封面", "ctx": f"[代表视频封面] {title}",
                      "url": cover, "bvid": bvid})
    # 评论区
    offset, max_id = "", 0
    for _ in range(pages):
        pag = json.dumps({"offset": offset, "max_id": max_id}, ensure_ascii=False)
        url = (f"https://api.bilibili.com/x/v2/reply/main?type=1&oid={oid}&mode=3"
               f"&pagination_str={urllib.parse.quote(pag)}")
        d = get_json(url, cookie)
        if d.get("code") != 0:
            break
        data2 = d.get("data") or {}
        reps = data2.get("replies") or []
        if not reps:
            break
        for r in reps:
            c = r.get("content") or {}
            msg = (c.get("message") or "").strip().replace("\n", " ")
            like = r.get("like", 0)
            pics = c.get("pictures") or []
            if not pics or like < min_like:
                continue
            for p in pics:
                u = p.get("img_src", "")
                if not u:
                    continue
                u = "https:" + u if u.startswith("//") else u
                s = score_comment(msg, like)
                tier = 2 if s >= min_like * 2 else 3
                cands.append({"tier": tier, "score": s, "like": like,
                              "ctx": msg[:80], "url": u, "bvid": bvid})
        cur = data2.get("cursor") or {}
        if cur.get("is_end"):
            break
        offset = cur.get("offset", "")
        max_id = cur.get("max_id", 0)
        time.sleep(0.4)
    return cands, title, cover


def main():
    av = sys.argv[1:]
    pages, min_like, dl_n, out = 2, 30, 0, "images/memes"
    bvids = []
    i = 0
    while i < len(av):
        a = av[i]
        if a == "--pages" and i + 1 < len(av):
            pages, i = int(av[i + 1]), i + 2
        elif a == "--min-like" and i + 1 < len(av):
            min_like, i = int(av[i + 1]), i + 2
        elif a == "--download" and i + 1 < len(av):
            dl_n, i = int(av[i + 1]), i + 2
        elif a == "--out" and i + 1 < len(av):
            out, i = av[i + 1], i + 2
        elif a.startswith("--"):
            i += 1
        else:
            bvids.append(a)
            i += 1
    if not bvids:
        print(__doc__)
        sys.exit(1)
    cookies = common.load_cookies()
    bili_cookie = cookies["bilibili"]

    all_cands = []
    for bvid in bvids:
        cands, title, _ = collect_video(bvid, pages, min_like, bili_cookie)
        print(f"· {bvid} 《{title[:30]}》: 候选 {len(cands)} 个")
        all_cands.extend(cands)

    # 去重(按url) + 排序
    seen = set()
    uniq = [c for c in all_cands if not (c["url"] in seen or seen.add(c["url"]))]
    uniq.sort(key=lambda c: -c["score"])

    t1 = [c for c in uniq if c["tier"] == 1]
    t2 = [c for c in uniq if c["tier"] == 2]
    t3 = [c for c in uniq if c["tier"] == 3]

    lines = ["# 梗图候选清单（评分排序）", ""]
    if t1:
        lines.append("## T1 代表视频封面（权威视觉，必收）")
        for c in t1:
            lines.append(f"- [封面] {c['ctx']} | {c['url']}")
    if t2:
        lines.append("\n## T2 高赞评论配图（score = 点赞×语境加成）")
        for c in t2[:20]:
            lines.append(f"- [score {c['score']:.0f} | 👍{c['like']}] {c['ctx']} | {c['url']}")
    if t3:
        lines.append(f"\n## T3 待人工复核（{len(t3)} 个，低分/语境不明，跳过或抽查）")
        for c in t3[:10]:
            lines.append(f"- [👍{c['like']}] {c['ctx']} | {c['url']}")
    print("\n".join(lines))

    if dl_n > 0 and (t1 or t2):
        top = (t1 + t2)[:dl_n]
        print(f"\n下载前 {len(top)} 张到 {out}/ ...")
        import subprocess
        tmp = out + ".urls.txt"
        os.makedirs(os.path.dirname(tmp) or ".", exist_ok=True)
        with open(tmp, "w", encoding="utf-8") as f:
            f.write("\n".join(c["url"] for c in top))
        subprocess.run([sys.executable, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                                     "bili_dl.py"), "--from", tmp, "--out", out])
        os.remove(tmp)


if __name__ == "__main__":
    main()
