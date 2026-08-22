# -*- coding: utf-8 -*-
"""Europe PMC PDF 下载模板：?pdf=render 端点，代理→直连兜底，校验 %PDF 头。
用法：改 papers 列表 [(PMCID, 输出文件名), ...]；仍 404 时切 templates/pmc_pow_dl.py"""
import requests, os, sys, io, time
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

LIT = os.path.join(os.path.expanduser("~"), "Downloads", "literature")  # 可改：PDF 落盘目录
PROXY = {"http": os.environ.get("LIT_PROXY", ""), "https": os.environ.get("LIT_PROXY", "")}  # 本地代理示例；无代理可置空 dict
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/126.0 Safari/537.36"

papers = [
    ("PMCXXXXXXX", "NCBI_Name-Year_short-title.pdf"),
]

for pmcid, out in papers:
    fpath = os.path.join(LIT, out)
    if os.path.exists(fpath) and os.path.getsize(fpath) > 50000:
        print(pmcid, "exists", os.path.getsize(fpath)); continue
    url = f"https://europepmc.org/articles/{pmcid}?pdf=render"
    done = False
    for proxies in (PROXY, None):
        try:
            r = requests.get(url, proxies=proxies, timeout=120, allow_redirects=True, headers={"User-Agent": UA})
            if r.status_code == 200 and r.content[:4] == b"%PDF" and len(r.content) > 50000:
                with open(fpath, "wb") as f: f.write(r.content)
                print(pmcid, "OK", len(r.content), "via", "proxy" if proxies else "direct")
                done = True; break
            print(pmcid, "try", "proxy" if proxies else "direct", "status", r.status_code, "len", len(r.content))
        except Exception as e:
            print(pmcid, "try", "proxy" if proxies else "direct", "ERR", str(e)[:80])
        time.sleep(1.5)
    if not done:
        print(pmcid, "FAILED ALL -> 切 templates/pmc_pow_dl.py（PMC 官网 POW 直连）")
