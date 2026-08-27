# -*- coding: utf-8 -*-
"""PMC 官网 POW 直连下载模板（Europe PMC render/fullTextPDF 404 时的兜底）。
原理：curl.exe 直连（不开代理）→ 遇 POW_CHALLENGE 解算 sha256 前缀 nonce →
带 cookie cloudpmc-viewer-pow=<challenge>,<nonce> 重试。
2026-08-18 实测 Nature/MMBR/mBio 3/3 全通。
用法：改 jobs 列表 [(PMCID, 输出文件名), ...]"""
import subprocess, hashlib, re, os, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

DST = os.path.join(os.path.expanduser("~"), "Downloads", "literature")  # 可改：PDF 落盘目录

def solve_pow(challenge, difficulty=4):
    target = "0" * difficulty
    nonce = 0
    while True:
        h = hashlib.sha256(f"{challenge}{nonce}".encode()).hexdigest()
        if h.startswith(target):
            return nonce, h
        nonce += 1

def curl_get(url, cookie=None):
    cmd = ["curl.exe", "-s", "-L", "--connect-timeout", "10", "--max-time", "90",
           "-A", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/126.0 Safari/537.36",
           "-w", "\n%{http_code}"]
    if cookie:
        cmd += ["-b", cookie]
    cmd.append(url)
    result = subprocess.run(cmd, capture_output=True, timeout=120)
    output = result.stdout
    lines = output.split(b"\n")
    status = int(lines[-1].strip()) if lines[-1].strip().isdigit() else 0
    content = b"\n".join(lines[:-1])
    return status, content

def download_pmc_pdf(pmcid, outfile):
    if os.path.exists(outfile) and os.path.getsize(outfile) > 50000:
        return f"already: {os.path.getsize(outfile)} B"
    url = f"https://pmc.ncbi.nlm.nih.gov/articles/{pmcid}/pdf/main.pdf"
    status, content = curl_get(url)
    if content[:4] == b"%PDF":
        with open(outfile, "wb") as f:
            f.write(content)
        return f"OK direct ({len(content)} B)"
    text = content.decode("utf-8", errors="replace")
    m = re.search(r'POW_CHALLENGE\s*=\s*"([^"]+)"', text)
    if not m:
        return f"no POW, status={status}: {text[:120]}"
    challenge = m.group(1)
    dm = re.search(r'POW_DIFFICULTY\s*=\s*"(\d+)"', text)
    diff = int(dm.group(1)) if dm else 4
    nonce, _ = solve_pow(challenge, diff)
    cookie = f"cloudpmc-viewer-pow={challenge},{nonce}; Domain=.ncbi.nlm.nih.gov; Path=/"
    status, content = curl_get(url, cookie=cookie)
    if content[:4] == b"%PDF" and len(content) > 50000:
        with open(outfile, "wb") as f:
            f.write(content)
        return f"OK POW ({len(content)} B)"
    return f"FAIL status={status} len={len(content)}"

jobs = [
    ("PMCXXXXXXX", "NCBI_Name-Year_short-title.pdf"),
]
for pmcid, name in jobs:
    print(f"{pmcid} ->", end=" ")
    try:
        print(download_pmc_pdf(pmcid, os.path.join(DST, name)))
    except Exception as e:
        print(f"ERR {e}")
