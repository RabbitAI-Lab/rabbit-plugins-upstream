#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""meme-digger: B站评论区深挖（免登录，已实测 2025/2026）。

用法:
    python bili_comments.py <bvid> [--pages N] [--top N] [--min-like N] [--out <md文件>]

功能:
- 按热度(mode=3)或时间(mode=2)翻页抓取评论区
- 收集: 评论内容/点赞/用户/时间/回复数
- 提取评论里的图片(梗图候选), 写入 <out>.images.txt
- 支持 --root <rpid> 抓某条评论的二级回复

输出: 结构化 Markdown + 图片URL清单。
"""
import sys
import os
import json
import time
import datetime
import urllib.parse
import urllib.request

import common

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

UA = common.UA


def get_json(url: str, cookie: str = ""):
    return json.loads(common.fetch(url, cookie=cookie))


def fmt_time(ts):
    return datetime.datetime.fromtimestamp(ts).strftime("%Y-%m-%d %H:%M")


def flatten_reply(r, depth=0):
    """把一条评论(含其内嵌二级回复)拍平成行。"""
    c = r.get("content") or {}
    pics = c.get("pictures") or []
    rows = [{
        "rpid": r.get("rpid"),
        "like": r.get("like", 0),
        "uname": (r.get("member") or {}).get("uname", "?"),
        "time": fmt_time(r.get("ctime", 0)),
        "msg": (c.get("message") or "").strip().replace("\n", " "),
        "img": [p.get("img_src") for p in pics],
        "depth": depth,
        "rcount": r.get("rcount", 0),
    }]
    for sub in (r.get("replies") or [])[:3]:  # 每条只带3条热门二级回复
        rows.extend(flatten_reply(sub, depth + 1))
    return rows


def fetch_replies(oid, mode, pages, root=None, cookie=""):
    rows, all_imgs = [], []
    offset, max_id = "", 0
    for _ in range(pages):
        if root:
            url = (f"https://api.bilibili.com/x/v2/reply/reply"
                   f"?type=1&oid={oid}&root={root}&ps=20")
        else:
            pag = json.dumps({"offset": offset, "max_id": max_id},
                             ensure_ascii=False)
            url = (f"https://api.bilibili.com/x/v2/reply/main"
                   f"?type=1&oid={oid}&mode={mode}"
                   f"&pagination_str={urllib.parse.quote(pag)}")
        d = get_json(url, cookie)
        if d.get("code") != 0:
            print(f"!! 评论API错误: code={d.get('code')} {d.get('message')}")
            break
        data = d.get("data") or {}
        reps = data.get("replies") or []
        if not reps:
            break
        for r in reps:
            for row in flatten_reply(r):
                rows.append(row)
                all_imgs.extend(row["img"])
        cur = data.get("cursor") or {}
        if root or cur.get("is_end"):
            break
        offset = cur.get("offset", "")
        max_id = cur.get("max_id", 0)
        time.sleep(0.4)
    return rows, all_imgs


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    pages, top, min_like, out, mode, root = 1, 30, 0, None, 3, None
    av = sys.argv[1:]
    for i, a in enumerate(av):
        if a == "--pages" and i + 1 < len(av): pages = int(av[i + 1])
        if a == "--top" and i + 1 < len(av): top = int(av[i + 1])
        if a == "--min-like" and i + 1 < len(av): min_like = int(av[i + 1])
        if a == "--out" and i + 1 < len(av): out = av[i + 1]
        if a == "--mode" and i + 1 < len(av): mode = int(av[i + 1])
        if a == "--root" and i + 1 < len(av): root = int(av[i + 1])
    if not args:
        print(__doc__)
        sys.exit(1)
    bvid = args[0]

    v = get_json(f"https://api.bilibili.com/x/web-interface/view?bvid={bvid}")
    if v.get("code") != 0:
        print(f"!! 视频不存在: {bvid}")
        sys.exit(1)
    oid = v["data"]["aid"]
    title = v["data"].get("title", "")

    rows, imgs = fetch_replies(oid, mode, pages, root,
                              common.load_cookies()["bilibili"])
    if not rows:
        print(f"!! 「{title}」无评论或未抓到。")
        sys.exit(1)

    # 去重(热度模式的内嵌回复会重复顶层评论) + 按点赞排序 + 过滤
    seen_rpid = set()
    rows = [r for r in rows
            if not (r["rpid"] in seen_rpid or seen_rpid.add(r["rpid"]))]
    rows.sort(key=lambda r: -r["like"])
    rows.sort(key=lambda r: -r["like"])
    keep = [r for r in rows if r["like"] >= min_like][:top]

    lines = [f"# 评论区挖掘: {title}", f"- 视频: https://www.bilibili.com/video/{bvid}",
             f"- 抓取: {len(rows)} 条评论, 显示前 {len(keep)} 条(按点赞)",
             f"- 评论区图片: {len(imgs)} 张", ""]
    for r in keep:
        ind = "  " * r["depth"]
        lines.append(f"{ind}👍{r['like']} | {r['uname']} | {r['time']} | id:{r['rpid']}")
        lines.append(f"{ind}> {r['msg'][:300]}")
        if r["img"]:
            for u in r["img"]:
                lines.append(f"{ind}  ![img]({u})")
        lines.append("")
    text = "\n".join(lines)

    if out:
        os.makedirs(os.path.dirname(out) or ".", exist_ok=True)
        with open(out, "w", encoding="utf-8") as f:
            f.write(text)
        imgfile = out.rsplit(".", 1)[0] + ".images.txt"
        with open(imgfile, "w", encoding="utf-8") as f:
            f.write("\n".join(dict.fromkeys(imgs)))
        print(f"已写入 {out} (评论) 与 {imgfile} (图片URL清单)")
    else:
        print(text)


if __name__ == "__main__":
    main()
