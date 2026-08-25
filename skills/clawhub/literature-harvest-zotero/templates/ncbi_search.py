# -*- coding: utf-8 -*-
"""NCBI 检索模板：eutils 搜索 + esummary 元数据 + elink 查 PMC。
密钥从 TOOLS.md「NCBI API」节读取（勿硬编码明文）。"""
import requests, json, time, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

PROXY = {"http": os.environ.get("LIT_PROXY", ""), "https": os.environ.get("LIT_PROXY", "")}  # 本地代理示例；无代理环境可置空 dict
BASE = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"
API = "<NCBI_API_KEY_FROM_TOOLS_MD>"

# 修改点：检索词（结构化，命中率高）
TERMS = [
    ('"PP2A"[Title] AND (fung*[Title/Abstract] OR yeast*[Title/Abstract] OR Aspergillus[Title/Abstract] OR Candida[Title/Abstract] OR Fusarium[Title/Abstract])', "pp2a+fungi"),
]

def call(url, params):
    last = None
    for proxies in (PROXY, None):
        for attempt in range(2):
            try:
                r = requests.get(url, params=params, proxies=proxies, timeout=45)
                return r
            except Exception as e:
                last = e; time.sleep(1.5)
    raise last

def esearch(term, n=25):
    r = call(BASE + "esearch.fcgi", {"db": "pubmed", "term": term, "retmax": n, "retmode": "json", "api_key": API})
    return r.json()["esearchresult"].get("idlist", [])

def esummary(pmids):
    out = {}
    for i in range(0, len(pmids), 50):
        chunk = pmids[i:i+50]
        r = call(BASE + "esummary.fcgi", {"db": "pubmed", "id": ",".join(chunk), "retmode": "json", "api_key": API})
        for k, v in r.json()["result"].items():
            if k != "uids": out[k] = v
        time.sleep(0.5)
    return out

def elink_pmc(pmid):
    r = call(BASE + "elink.fcgi", {"dbfrom": "pubmed", "db": "pmc", "id": pmid, "retmode": "json", "api_key": API})
    try:
        for ls in r.json()["linksets"]:
            for ln in ls.get("linksetdbs", []):
                if ln["dbto"] == "pmc": return ln["links"][0]
    except Exception: pass
    return None

for term, label in TERMS:
    print(f"\n===== {label} =====")
    ids = esearch(term)
    print("hits:", len(ids))
    sums = esummary(ids[:12])
    for pid in ids[:12]:
        s = sums.get(pid)
        if not s: continue
        print(f"PMID {pid} | {s.get('pubdate','')} | cited={s.get('citedbycount','?')} | PMC={elink_pmc(pid)}")
        print(f"   {s.get('title','')[:110]}")
    time.sleep(1)
