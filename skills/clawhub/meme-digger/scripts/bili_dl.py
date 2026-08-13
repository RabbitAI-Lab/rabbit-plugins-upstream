#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""meme-digger: 梗图下载器（封面/评论区图片/任意图片URL）。

用法:
    python bili_dl.py <url...> --out <目录>
    python bili_dl.py --from <url清单文件> --out <目录>

- 按 URL 哈希去重, 重名自动加序号
- 输出: 下载结果清单 <目录>/manifest.txt (本地文件名 | 原URL)
- 支持 hdslb.com 封面与评论区图片(免登录)
"""
import sys
import os
import hashlib
import urllib.request

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/126.0 Safari/537.36")


def download(url: str, outdir: str, seen: set) -> str | None:
    try:
        req = urllib.request.Request(url, headers={
            "User-Agent": UA, "Referer": "https://www.bilibili.com/"})
        with urllib.request.urlopen(req, timeout=20) as r:
            data = r.read()
    except Exception as e:
        print(f"!! 下载失败 {url[:60]}... : {e}")
        return None
    if len(data) < 1024:  # 空图/占位图
        return None
    h = hashlib.md5(data).hexdigest()[:12]
    if h in seen:
        return None
    seen.add(h)
    ext = os.path.splitext(urllib.parse.urlparse(url).path)[1] or ".jpg"
    if ext.lower() not in (".jpg", ".jpeg", ".png", ".gif", ".webp"):
        ext = ".jpg"
    name = f"{h}{ext}"
    with open(os.path.join(outdir, name), "wb") as f:
        f.write(data)
    return name


def main():
    urls, outdir, fromfile = [], "images", None
    av = sys.argv[1:]
    i = 0
    while i < len(av):
        a = av[i]
        if a == "--out" and i + 1 < len(av): outdir, i = av[i + 1], i + 1
        elif a == "--from" and i + 1 < len(av): fromfile, i = av[i + 1], i + 1
        elif not a.startswith("--"): urls.append(a)
        i += 1
    if fromfile:
        with open(fromfile, encoding="utf-8") as f:
            urls += [u.strip() for u in f if u.strip() and not u.startswith("#")]
    urls = list(dict.fromkeys(urls))
    if not urls:
        print(__doc__)
        sys.exit(1)
    os.makedirs(outdir, exist_ok=True)
    seen, manifest = set(), []
    for u in urls:
        name = download(u, outdir, seen)
        if name:
            manifest.append(f"{name} | {u}")
            print(f"✓ {name} <- {u[:70]}")
    with open(os.path.join(outdir, "manifest.txt"), "w", encoding="utf-8") as f:
        f.write("\n".join(manifest))
    print(f"\n共下载 {len(manifest)} 张到 {outdir}/  (清单: manifest.txt)")


if __name__ == "__main__":
    main()
