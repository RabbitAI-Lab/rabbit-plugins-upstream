#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""verify_refs.py — cite-holmes skill 的引用机械验证器。

对研究引用清单做机器可判定的检查（可达性 / 域名权威度 / 字段完整性 / 去重），
输出五态判定报告（Markdown + JSON）。语义验证（来源是否真的支持论断）由模型
在研究流程中完成，本脚本不做语义判断。

五态：
  verified     可达 + 权威层(official/journal/preprint/media) + 字段完整
  partial      可达，但社区/博客层来源，或必填字段缺失
  unreachable  404/超时/反爬（needs_human_check，≠ 不存在）
  invalid      无 URL/DOI 或格式错误
  unverified   --offline 或跳过检查

纯标准库，跨平台（win32/linux/darwin），控频访问。
用法：
  python verify_refs.py --refs research_refs.json --out verify_report.md
  python verify_refs.py --claims '[{"title":"...","url":"https://...","source":"X","year":2026}]'
  python verify_refs.py --refs refs.json --offline        # 不联网，仅结构检查
  python verify_refs.py --refs refs.json --strict         # unreachable/invalid 视为失败(CI 用)
  python verify_refs.py --refs refs.json --profile medical # 医学信源预设(期刊层域名扩展+社区层降级警示)
  python verify_refs.py --refs refs.json --export bibtex,csv # 导出verified-only参考文献(bibtex)+全量台账(csv)

引用字段支持 url / doi / pmid / arxiv 四选一（pmid 自动解析为 PubMed 页面，arxiv 自动解析为
arXiv abs 页面），去重覆盖 URL+DOI+PMID 及 arXiv 解析后的 URL。
v1.5：arXiv ID 元数据校验（export.arxiv.org 官方 API，不存在的 ID 直接判 invalid，
不被可达性检查误判 unreachable——沿用 DOI 元数据先行的判定顺序）；unreachable 条目
自动查 Wayback Machine 存档（有存档附对照链接，人工复核有抓手）。
v1.6：主机断路器（同一主机连续 2 次传输层失败 → 本批次跳过该主机外呼并诚实备注，
断网环境不再整批卡死）；可操作报错（超时给 --timeout 20 建议、DNS/拒连分类措辞、
待人工复核区加建议动作）；DOI↔PMID 交叉一致性（双键引用互证，抓「真 ID 拼接」伪造）；
期刊名一致性核查（复用 DOI 登记元数据，不符降 partial——抓「真 DOI 真论文假期刊」）。
"""

import argparse
import csv
import difflib
import ipaddress
import json
import re
import sys
import time
import urllib.error
import urllib.request
from urllib.parse import urlparse, urlunparse, quote

VERSION = "1.6.0"


# ---------------- 主机断路器（v1.6，国内适配主攻） ----------------
# 同一主机连续 _CB_THRESHOLD 次传输层失败（超时/连接重置/DNS 解析失败）→ 本批次内
# 跳过该主机的后续外呼并诚实备注，避免断网环境整批卡死（评测："需要等网络响应"）。
# HTTP 层失败（404/403/429 等站点有响应的情况）不触发熔断。main() 每次运行重置。
_CB_THRESHOLD = 2
_CB = {}


def _cb_host(url: str) -> str:
    p = urlparse(url)
    return f"{p.scheme}://{(p.hostname or '').lower()}" if p.hostname else ""


def _cb_open(url: str) -> bool:
    st = _CB.get(_cb_host(url))
    return bool(st and st["open"])


def _cb_record(url: str, transport_fail: bool) -> None:
    """transport_fail=True 记一次传输层失败（累计到阈值即熔断）；
    False（拿到任意 HTTP 响应或成功）清零。"""
    h = _cb_host(url)
    if not h:
        return
    st = _CB.setdefault(h, {"fails": 0, "open": False})
    if transport_fail:
        st["fails"] += 1
        if st["fails"] >= _CB_THRESHOLD:
            st["open"] = True
    else:
        st["fails"] = 0


def _cb_skip_note(url: str) -> str:
    h = _cb_host(url)
    return (f"网络断路器：{h} 本批次已连续 {_CB_THRESHOLD} 次传输失败，"
            "跳过本次外呼（避免整批卡死），本条仅按结构/其他信息判定")

# ---------------- 公共安全/转义帮手（v1.4 评审加固） ----------------

def ssrf_blocked(url: str) -> bool:
    """SSRF 字面量防护：URL 主机部分写明回环/内网/链路本地/保留 IP 或 localhost
    时拒绝请求。**刻意不做 DNS 解析判定**——污染网络环境下解析结果不可信，
    会把正常域名误判成内网地址（实测 pubmed/doi.org 均被解析污染误伤）。
    域名类 URL 的 DNS 层防护不在本工具承诺内。"""
    host = (urlparse(url).hostname or "").lower().rstrip(".")
    if not host:
        return False
    if host == "localhost" or host.endswith(".localhost") or \
            host.endswith(".local") or host.endswith(".internal"):
        return True
    try:
        addr = ipaddress.ip_address(host)  # 仅当主机部分本身就是 IP 字面量
    except ValueError:
        return False
    return (addr.is_private or addr.is_loopback or addr.is_link_local
            or addr.is_reserved or addr.is_multicast)


def md_cell(text, limit=90):
    """Markdown 表格单元格转义：竖线转义、换行剥除、截断。"""
    t = str(text if text is not None else "")
    t = t.replace("\r", " ").replace("\n", " ").replace("|", "\\|")
    return t[:limit]


def csv_safe(cell: str) -> str:
    """CSV 公式注入中和（OWASP 做法）：= + - @ 制表符 回车 开头的单元格前置单引号。"""
    c = str(cell)
    if c[:1] in ("=", "+", "-", "@", "\t", "\r"):
        return "'" + c
    return c


def bib_safe(value: str) -> str:
    """BibTeX 字段值加固：剥除花括号与换行/控制字符，防 @entry 逃逸。"""
    v = str(value if value is not None else "")
    return v.replace("{", "").replace("}", "").replace("\r", " ").replace("\n", " ")

# ---------------- CiteScore 置信度评分（v1.3.0） ----------------
# 五态加权：verified +10 / partial +4 / unreachable 0 / unverified -2 / invalid -8
# 归一化到 0-100，等级 A(>=85) B(70-84) C(50-69) D(<50)
SCORE_WEIGHTS = {"verified": 10, "partial": 4, "unreachable": 0,
                 "unverified": -2, "invalid": -8}


def compute_scorecard(results: list) -> dict:
    counts = {v: sum(1 for r in results if r["verdict"] == v)
              for v in SCORE_WEIGHTS}
    n = len(results)
    raw = sum(SCORE_WEIGHTS[v] * c for v, c in counts.items())
    score = round(100 * max(raw, 0) / (10 * n)) if n else 0
    grade = "A" if score >= 85 else "B" if score >= 70 else "C" if score >= 50 else "D"
    return {"score": score, "grade": grade, "total": n,
            "counts": counts, "weights": SCORE_WEIGHTS}

# ---------------- 输出编码（Windows GBK 控制台兜底） ----------------
for _stream in (sys.stdout, sys.stderr):
    if hasattr(_stream, "reconfigure"):
        _stream.reconfigure(encoding="utf-8", errors="replace")

# ---------------- 域名权威度分层 ----------------
# 自上而下首个命中者生效；未命中默认 blog。
TIER_RULES = [
    ("official", [
        r"\.gov(\.[a-z]{2})?$", r"\.edu(\.[a-z]{2})?$", r"\.gov\.cn$", r"\.edu\.cn$",
        r"^docs\.", r"^developer\.", r"^documentation\.", r"^support\.",
        r"^www\.anthropic\.com$", r"^openai\.com$", r"^www\.nature\.com$",
        r"^www\.nejm\.org$", r"^www\.who\.int$", r"^www\.fda\.gov$",
        r"^www\.ema\.europa\.eu$", r"^arxiv\.org$", r"^export\.arxiv\.org$",
        r"^www\.thelancet\.com$",
        r"^jamanetwork\.com$", r"^pubmed\.ncbi\.nlm\.nih\.gov$", r"^doi\.org$",
        r"^www\.sciencedirect\.com$", r"^link\.springer\.com$", r"^ieeexplore\.ieee\.org$",
        r"^www\.stats\.gov\.cn$", r"^www\.nhc\.gov\.cn$",
    ]),
    ("journal", [
        r"^pubmed\.ncbi\.nlm\.nih\.gov$", r"^doi\.org$", r"^journals?\.",
        r"^academic\.", r"^scholar\.", r"^kns\.", r"^oa\.cqvip\.com$", r"^yiigle\.com$",
    ]),
    ("preprint", [r"^arxiv\.org$", r"^biorxiv\.org$", r"^medrxiv\.org$", r"^ssrn\.com$", r"^chemrxiv\.org$"]),
    ("media", [
        r"^www\.reuters\.com$", r"^apnews\.com$", r"^www\.bbc\.", r"^www\.nytimes\.com$",
        r"^www\.bloomberg\.com$", r"^www\.ft\.com$", r"^www\.economist\.com$",
        r"^news\.yahoo\.com$", r"^www\.thepaper\.cn$", r"^www\.caixin\.com$",
        r"^www\.jiemian\.com$", r"^36kr\.com$", r"^www\.infoq\.cn$", r"^techcrunch\.com$",
        r"^www\.theverge\.com$", r"^arstechnica\.com$", r"^www\.wired\.com$",
    ]),
    ("community", [
        r"^github\.com$", r"^stackoverflow\.com$", r"^en\.wikipedia\.org$",
        r"^zh\.wikipedia\.org$", r"^www\.zhihu\.com$", r"^zhuanlan\.zhihu\.com$",
        r"^stackexchange\.com$", r"^www\.reddit\.com$", r"^news\.ycombinator\.com$",
        r"^www\.v2ex\.com$", r"^segmentfault\.com$", r"^juejin\.cn$",
    ]),
    ("social", [
        r"(^|\.)x\.com$", r"(^|\.)twitter\.com$", r"(^|\.)weibo\.com$", r"(^|\.)t\.me$",
        r"(^|\.)facebook\.com$", r"(^|\.)youtube\.com$", r"(^|\.)bilibili\.com$",
        r"(^|\.)douyin\.com$", r"(^|\.)xiaohongshu\.com$", r"(^|\.)medium\.com$",
    ]),
]
TRUSTED_TIERS = {"official", "journal", "preprint", "media"}

# ---------------- 医学信源预设（--profile medical 时并入 journal 层） ----------------
MEDICAL_JOURNAL_PATTERNS = [
    r"\.cochranelibrary\.com$", r"^bestpractice\.bmj\.com$", r"^www\.bmj\.com$",
    r"^www\.embase\.com$", r"^clinicaltrials\.gov$", r"^www\.chinacdc\.cn$",
    r"^www\.cdc\.gov$", r"^www\.nmpa\.gov\.cn$", r"^www\.nice\.org\.uk$",
    r"\.wanfangdata\.com\.cn$", r"^guide\.medlive\.cn$", r"^rs\.yiigle\.com$",
    r"^(www\.)?chictr\.org\.cn$",
]

DOI_RE = re.compile(r"^10\.\d{4,9}/\S+$")
PMID_RE = re.compile(r"^\d{6,9}$")
# arXiv ID：新式 YYMM.NNNNN——MM 限 01-12（月份段非法的伪 ID 会让官方 API 挂起，
# 必须在客户端拒掉）——可带 v2 版本号；旧式 类目/编号（hep-th/9901001、math.GT/0309136）
ARXIV_NEW_RE = re.compile(r"^\d{2}(?:0[1-9]|1[0-2])\.\d{4,5}(v\d+)?$", re.IGNORECASE)
ARXIV_OLD_RE = re.compile(r"^[a-z\-]+(?:\.[A-Z]{2})?/\d{7}(v\d+)?$", re.IGNORECASE)
ARXIV_URL_RE = re.compile(
    r"^https?://(?:www\.|export\.)?arxiv\.org/(?:abs|pdf|format)/"
    r"([a-z\-]+(?:\.[A-Z]{2})?/\d{7}|\d{2}(?:0[1-9]|1[0-2])\.\d{4,5})(v\d+)?", re.IGNORECASE)
REQUIRED_FIELDS = ("title", "url", "source", "year")


def extract_arxiv_id(ref: dict) -> str:
    """从引用中提取 arXiv ID（v1.5）：显式 arxiv 字段优先（支持 "arXiv:" 前缀），
    其次识别 url 中的 arxiv.org/abs|pdf/<id>。格式校验通过才返回，否则 ""。"""
    raw = str(ref.get("arxiv") or "").strip()
    if not raw:
        m = ARXIV_URL_RE.match(str(ref.get("url") or "").strip())
        if m:
            raw = m.group(1) + (m.group(2) or "")
    raw = re.sub(r"(?i)^arxiv\s*:\s*", "", raw).strip()
    if ARXIV_NEW_RE.match(raw) or ARXIV_OLD_RE.match(raw):
        return raw
    return ""


def classify_tier(url: str, medical: bool = False) -> str:
    host = (urlparse(url).hostname or "").lower()
    if not host:
        return "unknown"
    for tier, patterns in TIER_RULES:
        for pat in patterns:
            if re.search(pat, host):
                return tier
    if medical:
        for pat in MEDICAL_JOURNAL_PATTERNS:
            if re.search(pat, host):
                return "journal"
    return "blog"


def normalize_url(url: str) -> str:
    p = urlparse(url.strip())
    return urlunparse((p.scheme.lower(), (p.netloc or "").lower(), p.path.rstrip("/"),
                       "", "", ""))


PUBMED_URL_RE = re.compile(r"^https?://pubmed\.ncbi\.nlm\.nih\.gov/(\d+)/?$")


def doi_metadata_match(doi: str, title: str, year, timeout: float,
                       source: str = "") -> tuple:
    """DOI 元数据交叉验证（v1.4）：doi.org 内容协商取官方登记的 CSL 元数据，
    与引用声称的标题/年份比对——专抓「真 DOI 假论文」这类最像真引用的伪造。
    v1.6 新增：期刊名一致性核查（复用已取回的 container-title，零网络成本；
    不符降 partial——期刊改名常见，不判 invalid），抓「真 DOI 真论文假期刊」。
    瞬态网络错误自动重试一次。主机断路器生效。
    返回 (adjust, note, matched)：adjust ∈ {"", "partial", "invalid"}；
    matched=True 表示元数据成功取得且与声称标题一致。"""
    import difflib
    cb_url = f"https://doi.org/{doi}"
    if _cb_open(cb_url):
        return "", "网络断路器：doi.org 本批次连续传输失败已跳过元数据核验", False
    req = urllib.request.Request(
        cb_url, headers={
            "Accept": "application/vnd.citationstyles.csl+json",
            "User-Agent": "cite-holmes/1.6; +verified-deep-research"})
    meta, fetch_err = None, ""
    for attempt in range(2):
        try:
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                meta = json.loads(resp.read().decode("utf-8", "ignore"))
            fetch_err = ""
            _cb_record(cb_url, False)
            break
        except urllib.error.HTTPError as e:
            _cb_record(cb_url, False)
            if e.code == 404:
                return "invalid", "DOI 在 DOI.org 不存在（404）→ 疑似编造引用", False
            fetch_err = f"HTTP {e.code}"
        except Exception as e:
            fetch_err = type(e).__name__
        if attempt == 0:
            time.sleep(1.2)  # 瞬态抖动稍候重试
    if meta is None:
        _cb_record(cb_url, True)  # 整次调用只记 1 次传输失败（重试是同一逻辑失败）
        return "", f"DOI 元数据获取失败（{fetch_err}），跳过内容核验", False
    mt = meta.get("title")
    meta_title = (mt[0] if isinstance(mt, list) else mt) or ""
    sim = difflib.SequenceMatcher(None, (title or "").lower(),
                                  str(meta_title).lower()).ratio()
    meta_year = None
    parts = (meta.get("issued") or {}).get("date-parts") or []
    if parts and parts[0]:
        meta_year = parts[0][0]
    # v1.6 期刊名一致性核查（零网络成本）：规范化后互不包含视为不符，
    # 降 partial（期刊改名常见，不判 invalid）。
    # 二轮评审 P1 修正：NLM 式缩写（N Engl J Med vs New England Journal of
    # Medicine）不算不符——短名各词按序匹配长名词首（可跳过虚词）即视为同一
    # 期刊；跨语言（拉丁 vs CJK）不具可比性，跳过判定。
    ct = meta.get("container-title")
    reg_journal = (ct[0] if isinstance(ct, list) and ct else ct) or ""
    jadj, jnote = "", ""
    src = (source or "").strip()
    if reg_journal and src:
        def _nj(s):
            return re.sub(r"[^a-z0-9\u4e00-\u9fff]+", "", str(s).lower())

        def _tokens(s):
            return re.findall(r"[a-z0-9]+|[\u4e00-\u9fff]", str(s).lower())

        def _is_abbrev(short_toks, long_toks):
            j = 0
            for st in short_toks:
                while j < len(long_toks) and not (
                        long_toks[j].startswith(st) or st[0] == long_toks[j][0]):
                    j += 1
                if j >= len(long_toks):
                    return False
                j += 1
            return True

        def _journal_same(x, y):
            a, b = _nj(x), _nj(y)
            if not a or not b:
                return True
            # 跨语言不可比（如中文译名 vs 英文登记名）：不判不符
            a_cjk = any("\u4e00" <= c <= "\u9fff" for c in a)
            b_cjk = any("\u4e00" <= c <= "\u9fff" for c in b)
            if a_cjk != b_cjk:
                return True
            if a in b or b in a:
                return True
            ta, tb = _tokens(x), _tokens(y)
            return _is_abbrev(ta, tb) or _is_abbrev(tb, ta)

        if not _journal_same(src, reg_journal):
            jadj = "partial"
            jnote = (f"；期刊名不符（声称 {str(src)[:40]} / DOI 登记 "
                     f"{str(reg_journal)[:40]}）→ 建议核对是否引错论文")
    if not title:
        return jadj, (f"DOI 元数据核验完成（引用未提供标题，无法比对；登记年份 "
                      f"{meta_year or '未知'}）{jnote}"), True
    if title and sim < 0.50:
        return "invalid", (f"DOI 元数据标题相似度仅 {sim:.2f} → DOI 指向的不是这篇论文，"
                           f"疑似编造或错引（DOI 实际为《{str(meta_title)[:60]}》）"), True
    year_note = ""
    if meta_year and year:
        try:
            if abs(int(year) - int(meta_year)) >= 2:
                year_note = f"；年份不符（声称 {year} vs DOI 登记 {meta_year}）"
        except (TypeError, ValueError):
            pass
    if title and sim < 0.82:
        return "partial", f"DOI 元数据标题相似度 {sim:.2f}，建议人工复核{year_note}{jnote}", True
    return jadj, f"DOI 元数据核验一致（相似度 {sim:.2f}）{year_note}{jnote}", True


def pubmed_pmid_exists(pmid: str, timeout: float) -> tuple:
    """经 NCBI E-utilities 核实 PMID 真实存在。

    PubMed 网页对不存在的 PMID 也返回 2xx/203（且带反爬壳页），HTTP 状态码
    无法区分真假——AI 编造的 PMID 必须靠 API 核实才能抓住。
    返回 (exists, note)。
    """
    u = ("https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"
         f"?db=pubmed&id={pmid}&retmode=json")
    if _cb_open(u):
        return True, "网络断路器：E-utilities 本批次连续传输失败已跳过，按可达处理"
    try:
        req = urllib.request.Request(
            u, headers={"User-Agent": "cite-holmes/1.6; +verified-deep-research"})
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            j = json.loads(resp.read().decode("utf-8", "ignore"))
        _cb_record(u, False)
        res = j.get("result") or {}
        item = res.get(str(pmid)) or {}
        if item.get("error") or str(pmid) not in (res.get("uids") or []):
            return False, "PMID 在 PubMed 不存在（E-utilities 核实）→ 疑似编造引用"
        return True, "PMID 经 E-utilities 核实存在"
    except urllib.error.HTTPError as e:
        _cb_record(u, False)
        return True, f"E-utilities 校验失败（HTTP {e.code}），按可达处理"
    except Exception as e:
        _cb_record(u, True)
        return True, f"E-utilities 校验失败（{type(e).__name__}），按可达处理"


def pmid_doi_crosscheck(pmid: str, doi: str, timeout: float) -> tuple:
    """v1.6 DOI↔PMID 交叉一致性：两键各自真实也可能「拼接造假」（PMID 是 A 论文的、
    DOI 是 B 论文的）。取 PMID 在 PubMed 登记的 DOI 与声称 DOI 比对：
    不一致 → invalid「拼接伪造特征」；一致 → 加一致备注；登记无 DOI → 跳过。
    返回 (adjust, note)，adjust ∈ {"", "invalid"}。断路器生效。"""
    u = ("https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"
         f"?db=pubmed&id={pmid}&retmode=json")
    if _cb_open(u):
        return "", "网络断路器：E-utilities 本批次连续传输失败已跳过，DOI↔PMID 交叉未做"
    try:
        req = urllib.request.Request(
            u, headers={"User-Agent": "cite-holmes/1.6; +verified-deep-research"})
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            j = json.loads(resp.read().decode("utf-8", "ignore"))
    except urllib.error.HTTPError as e:
        _cb_record(u, False)
        return "", f"E-utilities 交叉查询失败（HTTP {e.code}），跳过 DOI↔PMID 交叉"
    except Exception as e:
        _cb_record(u, True)
        return "", f"E-utilities 交叉查询失败（{type(e).__name__}），跳过 DOI↔PMID 交叉"
    _cb_record(u, False)
    res = j.get("result") or {}
    item = res.get(str(pmid)) or {}
    reg = ""
    for a in item.get("articleids") or []:
        if a.get("idtype") == "doi":
            reg = (a.get("value") or "").strip()
            break
    if not reg:
        return "", "PMID 未登记 DOI，跳过 DOI↔PMID 交叉"
    if reg.lower().rstrip(".").rstrip("/") == doi.lower().strip().rstrip(".").rstrip("/"):
        return "", "DOI↔PMID 交叉一致（两键指向同一论文）"
    return "invalid", (f"DOI 与 PMID 指向不同论文（PMID {pmid} 登记为 {reg}，"
                       f"引用声称 {doi}）→ 拼接伪造特征，疑似编造引用")


_ARXIV_LAST = [0.0]


def _arxiv_rate_wait():
    """export.arxiv.org 官方礼貌上限：同一客户端 ≥3 秒/请求（仅 arXiv 查询互相控频）。"""
    wait = 3.0 - (time.time() - _ARXIV_LAST[0])
    if wait > 0:
        time.sleep(wait)
    _ARXIV_LAST[0] = time.time()


def arxiv_metadata_match(arxiv_id: str, title: str, year, timeout: float) -> tuple:
    """arXiv ID 元数据交叉验证（v1.5）：export.arxiv.org 官方 API 取登记的 Atom 元数据，
    与引用声称的标题/年份比对——复用 DOI 的 0.50/0.82 相似度阈值体系。
    查无记录/格式错误的 ID 直接判 invalid（疑似编造），调用方（verify_one）保证
    该判定先于可达性检查，假 ID 不会被误判为 unreachable。
    返回 (adjust, note, matched)：adjust ∈ {"", "partial", "invalid"}；
    matched=True 表示元数据成功取得且与声称标题一致。"""
    import xml.etree.ElementTree as ET
    ns = {"a": "http://www.w3.org/2005/Atom",
          "ax": "http://arxiv.org/schemas/atom"}
    api_url = ("https://export.arxiv.org/api/query?id_list="
               + quote(arxiv_id, safe="") + "&max_results=1")
    if _cb_open(api_url):
        return "", "网络断路器：export.arxiv.org 本批次连续传输失败已跳过 arXiv 元数据核验", False
    _arxiv_rate_wait()
    req = urllib.request.Request(
        api_url,
        headers={"User-Agent": "cite-holmes/1.6; +verified-deep-research"})
    xml_text, fetch_err = None, ""
    for attempt in range(2):
        try:
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                xml_text = resp.read().decode("utf-8", "ignore")
            fetch_err = ""
            _cb_record(api_url, False)
            break
        except urllib.error.HTTPError as e:
            _cb_record(api_url, False)
            fetch_err = f"HTTP {e.code}"
        except Exception as e:
            fetch_err = type(e).__name__
        if attempt == 0:
            _arxiv_rate_wait()  # 重试同样守 3 秒礼貌上限（v1.5 评审修正）
    if xml_text is None:
        _cb_record(api_url, True)  # 整次调用只记 1 次传输失败
        return "", f"arXiv 元数据获取失败（{fetch_err}），跳过内容核验", False
    try:
        root = ET.fromstring(xml_text)
    except ET.ParseError as e:
        return "", f"arXiv 返回非预期格式（{e}），跳过内容核验", False
    entries = root.findall("a:entry", ns)
    if not entries:
        return "invalid", "arXiv ID 在官方 API 查无记录 → 疑似编造引用", False
    entry = entries[0]
    t = entry.find("a:title", ns)
    meta_title = re.sub(r"\s+", " ", (t.text or "")).strip() if t is not None else ""
    # 错误判据以官方 ax:error 元素为准；标题恰为 "Error" 的真实论文不误杀，
    # 仅当 summary 明确含格式错误文案时才作辅助判据（v1.5 评审修正）
    err = entry.find("ax:error", ns)
    summ = entry.find("a:summary", ns)
    err_text = ""
    if err is not None and err.text:
        err_text = err.text.strip()
    elif summ is not None and summ.text and "incorrect id format" in summ.text:
        err_text = summ.text.strip()
    if err_text:
        return "invalid", f"arXiv 官方 API 拒绝该 ID（{err_text[:60]}）→ 疑似编造引用", False
    pub = entry.find("a:published", ns)
    meta_year = None
    if pub is not None and pub.text:
        m = re.match(r"(\d{4})", pub.text.strip())
        if m:
            meta_year = int(m.group(1))
    sim = difflib.SequenceMatcher(None, (title or "").lower(),
                                  meta_title.lower()).ratio()
    if not title:
        return "", f"arXiv 元数据核验完成（引用未提供标题，无法比对；登记年份 {meta_year or '未知'}）", True
    if sim < 0.50:
        return "invalid", (f"arXiv 元数据标题相似度仅 {sim:.2f} → ID 指向的不是这篇论文，"
                           f"疑似编造或错引（arXiv 实际为《{meta_title[:60]}》）"), True
    year_note = ""
    if meta_year and year:
        try:
            if abs(int(year) - int(meta_year)) >= 2:
                year_note = f"；年份不符（声称 {year} vs arXiv 登记 {meta_year}）"
        except (TypeError, ValueError):
            pass
    if sim < 0.82:
        return "partial", f"arXiv 元数据标题相似度 {sim:.2f}，建议人工复核{year_note}", True
    return "", f"arXiv 元数据核验一致（相似度 {sim:.2f}）{year_note}", True


def wayback_available(url: str, timeout: float) -> str:
    """v1.5 unreachable 存档兜底：查 Wayback Machine 是否有历史存档。
    有 → 返回「Wayback 存档可用（YYYY-MM-DD）：<存档URL>（人工复核可对照）」；
    无存档/查询失败 → 返回 ""（静默跳过，不加额外文案）。SSRF 字面量防护同样
    适用——内网/保留地址不外发到 archive.org。"""
    if ssrf_blocked(url):
        return ""
    # 实测教训：archive.org 对全量百分号编码的 url 参数不匹配（原样 200+快照，
    # %3A%2F 编码形式 200 但快照集为空）——必须原文直传，仅编码破坏外层查询的字符
    q = quote(url, safe=":/?&=#%@+!$,;'~()*[]-._")
    wb_url = ("https://archive.org/wayback/available?url=" + q)
    # 断路器看真正的外呼对象 archive.org（v1.6 二轮评审 P1 修正）——
    # 目标主机熔断不影响存档查询（死站查存档正是本函数的主用例）
    if _cb_open(wb_url):
        return ""
    req = urllib.request.Request(
        wb_url,
        headers={"User-Agent": "cite-holmes/1.6; +verified-deep-research"})
    for attempt in range(2):
        try:
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                j = json.loads(resp.read().decode("utf-8", "ignore"))
            _cb_record(wb_url, False)
            closest = (j.get("archived_snapshots") or {}).get("closest") or {}
            if closest.get("available") and closest.get("url"):
                ts = str(closest.get("timestamp") or "")
                nice = f"{ts[0:4]}-{ts[4:6]}-{ts[6:8]}" if len(ts) >= 8 else ts
                return f"Wayback 存档可用（{nice}）：{closest['url']}（人工复核可对照）"
            return ""  # 有明确响应但无存档：确定性结果，不重试
        except urllib.error.HTTPError as e:
            _cb_record(wb_url, False)
            if e.code == 429 and attempt == 0:
                time.sleep(3.0)  # archive.org 对公共 IP 常见限流：退避一次
                continue
            return ""
        except Exception:
            _cb_record(wb_url, True)
            return ""
    return ""


def check_url(url: str, timeout: float, retries: int = 1) -> tuple:
    """返回 (reachable, status, note)。reachable 以 2xx/3xx/429(反爬) 计。
    瞬态网络错误（超时/连接重置）自动重试一次——国内网络偶发抖动不误判。
    内网/环回地址直接拒绝（SSRF 防护），不发起请求。
    v1.6：主机断路器生效；传输失败按成因给可操作话术（超时给 --timeout 建议）。"""
    if ssrf_blocked(url):
        return False, None, "内网/保留地址，验证请求已拒绝（SSRF 防护）"
    if _cb_open(url):
        return False, None, _cb_skip_note(url)
    note = ""
    for attempt in range(retries + 1):
        req = urllib.request.Request(url, method="HEAD", headers={
            "User-Agent": "Mozilla/5.0 (compatible; cite-holmes/1.6; +verified-deep-research)",
            "Accept": "*/*",
        })
        opener = urllib.request.build_opener(urllib.request.HTTPRedirectHandler())
        transient = False
        for method in ("HEAD", "GET"):
            try:
                req.method = method
                with opener.open(req, timeout=timeout) as resp:
                    _cb_record(url, False)
                    return True, resp.status, f"{method} {resp.status}"
            except urllib.error.HTTPError as e:
                _cb_record(url, False)  # 站点有响应：不算传输失败
                if method == "HEAD" and e.code in (403, 405, 501):
                    continue  # 站点拒绝 HEAD，降级 GET 重试
                if e.code == 429:
                    return True, 429, "HTTP 429（反爬限流，站点实际存在）"
                return False, e.code, f"HTTP {e.code}（站点拒绝或页面不存在）"
            except (urllib.error.URLError, TimeoutError, OSError) as e:
                if method == "HEAD":
                    continue
                transient = True
                msg = str(e)
                if isinstance(e, TimeoutError) or "timed out" in msg or "timeout" in msg.lower():
                    note = "连接超时（站点慢或网络受限），建议 --timeout 20 重试"
                elif ("getaddrinfo" in msg or "name or service" in msg.lower()
                        or "no address" in msg.lower()):
                    note = "域名无法解析，连接失败（站点可能已下线或被网络拦截）"
                elif "refused" in msg or "reset" in msg.lower():
                    note = "连接被拒/重置（站点或网络问题）"
                else:
                    note = f"网络异常：{e}"[:120]
            except ValueError as e:
                return False, None, f"URL 格式无效：{e}"[:120]
        if transient and attempt < retries:
            time.sleep(1.5)  # 瞬态抖动稍候重试
    # 重试耗尽仍失败：每次 check_url 调用只记 1 次传输失败（重试是同一逻辑失败，
    # 逐次记录会导致一次调用即熔断）
    _cb_record(url, True)
    return False, None, note or "连接失败（站点不可达、域名不存在或网络受限）"


FIELD_ZH = {"title": "标题(title)", "url": "链接(url)", "source": "来源(source)", "year": "年份(year)"}


def missing_fields(ref: dict) -> list:
    miss = [f for f in REQUIRED_FIELDS if not ref.get(f)]
    if "url" in miss and (
            (ref.get("doi") and DOI_RE.match(str(ref["doi"]).strip())) or
            (ref.get("pmid") and PMID_RE.match(str(ref["pmid"]).strip())) or
            extract_arxiv_id(ref)):
        miss.remove("url")
    return [FIELD_ZH.get(f, f) for f in miss]


def ref_to_url(ref: dict) -> str:
    """url → doi → arxiv → pmid 四级解析，返回最终可检查的 URL。字段统一强转为字符串。"""
    url = str(ref.get("url") or "").strip()
    if url:
        return url
    doi = str(ref.get("doi") or "").strip()
    if doi and DOI_RE.match(doi):
        return f"https://doi.org/{doi}"
    arxiv = extract_arxiv_id(ref)
    if arxiv:
        return f"https://arxiv.org/abs/{arxiv}"
    pmid = str(ref.get("pmid") or "").strip()
    if pmid and PMID_RE.match(pmid):
        return f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/"
    return ""


def verify_one(ref: dict, idx: int, offline: bool, timeout: float, medical: bool = False) -> dict:
    def _s(v):
        return str(v) if v is not None else ""

    title_in = _s(ref.get("title"))
    out = {"index": idx, "title": title_in or "(无标题)",
           "url": _s(ref.get("url")).strip(),
           "doi": _s(ref.get("doi")).strip(), "pmid": _s(ref.get("pmid")).strip(),
           "arxiv": extract_arxiv_id(ref),
           "source": _s(ref.get("source")).strip(), "year": ref.get("year"),
           "tier": ref.get("tier") or "", "semantic": ref.get("semantic", ""),
           "verdict": "unverified", "http_status": None, "note": "", "needs_human_check": False}

    pmid = out["pmid"]
    doi_adj, doi_matched = "", False
    arxiv_adj, arxiv_matched = "", False
    url = ref_to_url(ref)
    if not url:
        raw_arxiv = str(ref.get("arxiv") or "").strip()
        if raw_arxiv and not out["arxiv"]:
            out.update(verdict="invalid",
                       note="arxiv 字段格式无法识别（应为 YYMM.NNNNN 或 category/NNNNNNN）")
        else:
            out.update(verdict="invalid",
                       note="缺少 url 且无可解析的 doi/pmid/arxiv" +
                            ("（pmid 须为 6-9 位数字）" if pmid else ""))
        return out
    if not re.match(r"^https?://", url, re.IGNORECASE):
        out.update(verdict="invalid", note=f"url 非 http(s) 格式: {url[:60]}")
        return out

    if not out["tier"]:
        out["tier"] = classify_tier(url, medical)
    out["url"] = url
    if medical and out["tier"] in ("community", "social", "blog"):
        out["note"] = "医学模式：社区/社交/博客层来源不得支撑医学结论（仅作线索）"
    elif medical and out["tier"] == "preprint":
        out["note"] = "医学模式：预印本未经同行评审，证据强度受限"

    if offline:
        out["note"] = (out["note"] + "；" if out["note"] else "") + "offline 模式未做可达性检查"
    else:
        # 带 DOI 的引用优先走元数据核验：能同时判定「存在性」与「内容匹配」，
        # 且假 DOI 的 404 在这里直接判 invalid（不会先被可达性检查误判为 unreachable）
        if out["doi"] and DOI_RE.match(out["doi"]):
            doi_adj, note, doi_matched = doi_metadata_match(
                out["doi"], str(ref.get("title") or ""), ref.get("year"), timeout,
                str(ref.get("source") or ""))
            if note:
                out["note"] = (out["note"] + "；" if out["note"] else "") + note
            if doi_adj == "invalid":
                out.update(verdict="invalid", needs_human_check=True)
                return out
        # 带 arXiv ID 的引用同层核验（无 DOI 时）：官方 API 查无记录 → 直接 invalid，
        # 同样先于可达性检查，避免假 ID 被误判为 unreachable（v1.5）
        elif out["arxiv"]:
            arxiv_adj, note, arxiv_matched = arxiv_metadata_match(
                out["arxiv"], str(ref.get("title") or ""), ref.get("year"), timeout)
            if note:
                out["note"] = (out["note"] + "；" if out["note"] else "") + note
            if arxiv_adj == "invalid":
                out.update(verdict="invalid", needs_human_check=True)
                return out
        # v1.6：双键引用（doi+pmid）做交叉一致性——两键各自真实也可能拼接造假，
        # 元数据层判定，先于可达性检查
        if (out["doi"] and DOI_RE.match(out["doi"])
                and out["pmid"] and PMID_RE.match(out["pmid"])):
            xadj, xnote = pmid_doi_crosscheck(out["pmid"], out["doi"], timeout)
            if xnote:
                out["note"] = (out["note"] + "；" if out["note"] else "") + xnote
            if xadj == "invalid":
                out.update(verdict="invalid", needs_human_check=True)
                return out
        reachable, status, note = check_url(url, timeout)
        out["http_status"] = status
        out["note"] = (out["note"] + "；" if out["note"] else "") + note
        if not reachable:
            # DOI/arXiv 注册元数据已核验一致 + 着陆页反爬（403/429）→ 引用存在性已被
            # 官方注册库证实，不能因反爬误判为 unreachable。评审修正：救回不再无条件
            # 盖 verified——层级/字段门控照走，防"真 ID + 403 博客链接"骗过权威层
            if (doi_matched or arxiv_matched) and status in (403, 429):
                label = "DOI" if doi_matched else "arXiv"
                out["note"] = (out["note"] + "；" if out["note"] else "") + \
                    f"着陆页反爬（HTTP {status}），但 {label} 注册元数据核验一致——存在性已确认"
                # v1.5 二轮评审 P1：元数据本身判 partial（相似度 0.50-0.82）时，
                # 救回同样不得给 verified——与 200 路径末尾的降级不变量保持一致，
                # 防"疑似错引"借反爬救回混进 verified（进而流入 bibtex/strict CI）
                if (out["tier"] in TRUSTED_TIERS and not missing_fields(ref)
                        and doi_adj != "partial" and arxiv_adj != "partial"):
                    out["verdict"] = "verified"
                else:
                    out["verdict"] = "partial"
                return out
            # v1.5：arXiv ID 以 arxiv.org/abs 为官方解析器——官方站可达却对该 ID
            # 返回 404 → 官方库查无此 ID，判 invalid（官方 API 被墙时兜底）。
            # 评审修正（P0）：仅当元数据核验未能确认存在时才允许此判定——
            # 官方 API 刚确认过存在时，脏 URL 的 404 不得反转成 invalid；
            # 此逻辑仅适用于解析器域名，普通网页 404 仍是 unreachable
            elif status == 404 and not (doi_matched or arxiv_matched) and re.match(
                    r"^https?://(?:www\.|export\.)?arxiv\.org/(?:abs|pdf)/", url, re.IGNORECASE):
                out.update(verdict="invalid", needs_human_check=True,
                           note=(out["note"] + "；" if out["note"] else "") +
                                "arXiv 官方站对该 ID 返回 404（官方库查无）→ 疑似编造引用")
                return out
            out.update(verdict="unreachable", needs_human_check=True,
                       note=(out["note"] + "；" if out["note"] else "") + "可能反爬/临时故障，不等于不存在")
            # v1.5 存档兜底：不可达 ≠ 不存在，附 Wayback 存档链给人工复核做对照
            wb = wayback_available(url, timeout)
            if wb:
                out["note"] = (out["note"] + "；" if out["note"] else "") + wb
            return out
        m = PUBMED_URL_RE.match(url)
        if m:
            pmid_ok, pmid_note = pubmed_pmid_exists(m.group(1), timeout)
            if not pmid_ok:
                out.update(verdict="invalid", needs_human_check=True,
                           note=(out["note"] + "；" if out["note"] else "") + pmid_note)
                return out
            out["note"] = (out["note"] + "；" if out["note"] else "") + pmid_note

    miss = missing_fields(ref)
    if out["tier"] in TRUSTED_TIERS and not miss:
        out["verdict"] = "verified"
    else:
        why = []
        if out["tier"] not in TRUSTED_TIERS:
            why.append(f"来源层级为 {out['tier']}（非权威层）")
        if miss:
            why.append(f"缺字段 {','.join(miss)}")
        out["verdict"] = "partial"
        out["note"] = (out["note"] + "；" if out["note"] else "") + "；".join(why)

    # v1.4：元数据核验判为 partial 时，verified 降级为 partial
    if (doi_adj == "partial" or arxiv_adj == "partial") and out["verdict"] == "verified":
        out["verdict"] = "partial"
    # offline 模式只做结构核验（格式/字段/层级/去重），可达性未验证——
    # 诚实起见 verified 封顶为 partial（避免离线盖章"已验证"）
    if offline and out["verdict"] == "verified":
        out["verdict"] = "partial"
        out["note"] = (out["note"] + "；" if out["note"] else "") + \
            "offline 模式最高判 partial（可达性未验证）"
    return out


def mark_duplicates(results: list) -> None:
    seen = {}
    kind_zh = {"url": "URL", "doi": "DOI", "pmid": "PMID"}
    for r in results:
        keys = []
        if r.get("url"):
            keys.append(("url", normalize_url(r["url"])))
        if r.get("doi"):
            keys.append(("doi", r["doi"].lower()))
        if r.get("pmid"):
            keys.append(("pmid", r["pmid"]))
        hit = next(((k, seen[v]) for k, v in keys if v in seen), None)
        if hit:
            kind, first = hit
            r["note"] = (r["note"] + "；" if r["note"] else "") + f"与 #{first} 重复（同{kind_zh[kind]}）"
            if r["verdict"] == "verified":
                r["verdict"] = "partial"
        else:
            for _, v in keys:
                seen[v] = r["index"]


VERDICT_ZH = {"verified": "✅ verified", "partial": "🟡 partial", "unreachable": "⚠️ unreachable",
              "invalid": "❌ invalid", "unverified": "⏸ unverified"}


def export_bibtex(results: list, path: str) -> int:
    """仅导出 verified 条目为 BibTeX（可直接导入论文参考文献管理器）。返回条数。
    字段值经 bib_safe 加固（剥除花括号/换行，防 @entry 逃逸），citation key 保证唯一。"""
    n = 0
    used_keys = set()
    with open(path, "w", encoding="utf-8") as f:
        for r in results:
            if r["verdict"] != "verified":
                continue
            n += 1
            title = bib_safe(r.get("title") or "untitled").strip() or "untitled"
            # 评审修正：year 未经消毒可携带换行/花括号逃逸 @entry，只留数字
            ys = re.sub(r"[^0-9]", "", str(r.get("year") or ""))[:4] if r.get("year") else ""
            year = ys or "n.d."
            words = re.findall(r"[A-Za-z0-9\u4e00-\u9fff]+", title)[:3]
            key = ("holmes" + ys + "".join(words))[:42] or f"ref{r['index']}"
            k2 = key
            sfx = 2
            while k2 in used_keys:
                k2 = f"{key}_{sfx}"
                sfx += 1
            used_keys.add(k2)
            fields = [f"  title = {{{bib_safe(title)}}}"]
            if r.get("source"):
                fields.append(f"  journal = {{{bib_safe(r.get('source'))}}}")
            if r.get("year"):
                fields.append(f"  year = {{{year}}}")
            if r.get("url"):
                fields.append(f"  url = {{{bib_safe(r.get('url'))}}}")
            if r.get("doi"):
                fields.append(f"  doi = {{{bib_safe(r.get('doi'))}}}")
            if r.get("arxiv"):
                fields.append(f"  eprint = {{{bib_safe(r.get('arxiv'))}}}")
                fields.append("  archivePrefix = {arXiv}")
            notes = ["cite-holmes verified"]
            if r.get("pmid"):
                notes.append(f"PMID: {r['pmid']}")
            fields.append("  note = {{{}}}".format(bib_safe("; ".join(notes))))
            f.write("@misc{" + k2 + ",\n" + ",\n".join(fields) + "}\n\n")
    return n


def export_csv(results: list, path: str) -> None:
    """全量审计台账 CSV（utf-8-sig，Excel 直接打开不乱码）。单元格做公式注入中和。"""
    cols = ["index", "title", "verdict", "tier", "http_status", "needs_human_check",
            "year", "source", "url", "doi", "pmid", "arxiv", "note"]
    with open(path, "w", encoding="utf-8-sig", newline="") as f:
        w = csv.writer(f)
        w.writerow(cols)
        for r in results:
            row = [csv_safe(str(r.get(c) if r.get(c) is not None else "")) for c in cols]
            w.writerow(row)


def render_md(results: list, offline: bool, profile: str = "general") -> str:
    sc = compute_scorecard(results)
    c = sc["counts"]
    lines = [
        "# 引用机械验证报告",
        f"- 验证器：verify_refs.py v{VERSION} · 模式：{'offline（未联网）' if offline else 'online'}"
        + (" · 医学信源预设" if profile == "medical" else ""),
    ]
    if profile == "medical":
        lines.append("- ⚠️ 免责声明：本报告仅为信源机械核验，不构成证据分级结论或医疗建议；"
                     "预印本/社区层来源不得支撑医学结论。")
    lines += [
        "",
        "## CiteScore 置信度评分",
        f"### **{sc['score']} / 100 · {sc['grade']} 级**",
        "",
        f"- 总计 {sc['total']} 条：✅verified {c['verified']} · 🟡partial {c['partial']} · "
        f"⚠️unreachable {c['unreachable']} · ❌invalid {c['invalid']} · ⏸unverified {c['unverified']}",
        "- 计分：verified +10 / partial +4 / unreachable 0 / unverified −2 / invalid −8，"
        "满分 = 10 × 条数，归一化 0-100",
        "",
        "| # | 标题 | 层级 | HTTP | 判定 | 说明 |",
        "|---|---|---|---|---|---|",
    ]
    for r in results:
        title = md_cell(r["title"], 48)
        # 含 Wayback 存档链的备注放宽截断（存档 URL 普遍 >90 字符，截断即废链）
        note = md_cell(r["note"], 200 if "web.archive.org" in (r.get("note") or "") else 90)
        lines.append(f"| {r['index']} | {title} | {r['tier']} | "
                     f"{r['http_status'] or '-'} | {VERDICT_ZH[r['verdict']]} | {note} |")
    flagged = [r for r in results if r["needs_human_check"] or r["verdict"] in ("invalid", "unverified")]
    if flagged:
        lines += ["", "## 待人工复核", ""]
        for r in flagged:
            lim = 200 if "web.archive.org" in (r.get("note") or "") else 110
            act = {"invalid": "建议：删除或更换信源",
                   "unreachable": "建议：人工打开原链复核",
                   "unverified": "建议：在线环境重跑验证"}.get(r["verdict"], "建议：按备注复核")
            lines.append(f"- #{r['index']} {md_cell(r['title'], 60)} → {r['verdict']}"
                         f"（{act}）：{md_cell(r['note'], lim)}")
    lines += ["", "## 判定说明", "",
              "- `verified`：可达 + 权威层(official/journal/preprint/media) + 字段完整 —— 可支撑正文结论",
              "- `partial`：可达但社区/博客层来源，或字段缺失 —— 降级使用，结论需注明",
              "- `unreachable`：抓取失败（404/超时/反爬）—— 不等于不存在，需人工打开复核",
              "- `invalid`：无 URL/DOI 或格式错误 —— 不得进入报告",
              "- 语义验证（来源是否支持论断）由模型完成，本报告只覆盖机械层", ""]
    return "\n".join(lines)


def main() -> int:
    ap = argparse.ArgumentParser(description="deep-research 引用机械验证器（五态判定）")
    ap.add_argument("--refs", help="research_refs.json 路径")
    ap.add_argument("--claims", help="内联 JSON 引用数组（同 --refs 的 schema）")
    ap.add_argument("--out", default="verify_report.md", help="Markdown 报告输出路径")
    ap.add_argument("--json-out", help="JSON 报告输出路径（默认 <out>.json）")
    ap.add_argument("--offline", action="store_true", help="不联网，仅结构/字段检查")
    ap.add_argument("--strict", action="store_true", help="unreachable/invalid 计为失败（exit 1）")
    ap.add_argument("--timeout", type=float, default=10.0, help="单 URL 超时秒数（默认 10）")
    ap.add_argument("--interval", type=float, default=1.0, help="请求间隔秒数（默认 1.0）")
    ap.add_argument("--profile", choices=["general", "medical"], default="general",
                    help="信源预设：medical=医学期刊层域名扩展(Cochrane/CTS/NMPA/CDC/万方等)+社区层降级警示")
    ap.add_argument("--export", help="附加导出，逗号分隔：bibtex（仅verified，可直接进论文）/ csv（全量审计台账）")
    ap.add_argument("--easy", action="store_true",
                    help="傻瓜模式：自动识别医学引用启用医学预设，验证后自动导出 bibtex+csv，无需其他参数")
    args = ap.parse_args()
    medical = args.profile == "medical"
    _CB.clear()  # 断路器按批次重置（v1.6）

    if not args.refs and not args.claims:
        ap.error("需要 --refs 或 --claims 之一")
    try:
        refs = (json.loads(args.claims) if args.claims
                else json.load(open(args.refs, encoding="utf-8")))
    except (OSError, json.JSONDecodeError) as e:
        print(f"❌ 读取引用清单失败：{e}", file=sys.stderr)
        return 2
    if not isinstance(refs, list) or not refs:
        print("❌ 引用清单须为非空 JSON 数组", file=sys.stderr)
        return 2

    if args.easy:
        # 傻瓜模式：有 PMID/PubMed 链接/医学期刊域名 → 自动启用医学预设；自动导出台账
        hints = False
        for r in refs:
            if not isinstance(r, dict):
                continue
            u = str(r.get("url") or "")
            if str(r.get("pmid") or "").strip() or "pubmed" in u.lower():
                hints = True
                break
            try:
                if classify_tier(u, True) == "journal" and classify_tier(u, False) == "blog":
                    hints = True
                    break
            except Exception:
                pass
        if hints:
            args.profile = "medical"
        if not args.export:
            args.export = "bibtex,csv"
        medical = args.profile == "medical"
        print(f"[easy] 傻瓜模式：医学预设={'开' if hints else '关'}；自动导出 {args.export}")

    results = []
    for i, ref in enumerate(refs, 1):
        if not isinstance(ref, dict):
            results.append({"index": i, "title": str(ref)[:48], "url": "", "doi": "", "pmid": "",
                            "arxiv": "", "source": "", "year": None, "tier": "-", "semantic": "",
                            "verdict": "invalid",
                            "http_status": None, "note": "条目不是对象", "needs_human_check": False})
            continue
        try:
            r = verify_one(ref, i, args.offline, args.timeout, medical)
        except Exception as e:
            # 单条坏数据（如非字符串标量）降级为该条 invalid，绝不拖垮整批
            r = {"index": i, "title": str(ref.get("title") or "")[:48] or "(无标题)",
                 "url": "", "doi": "", "pmid": "", "arxiv": "", "source": "", "year": None,
                 "tier": "-", "semantic": "", "verdict": "invalid",
                 "http_status": None, "note": f"条目处理异常（{type(e).__name__}）",
                 "needs_human_check": True}
        results.append(r)
        print(f"[{i}/{len(refs)}] {VERDICT_ZH[r['verdict']]} {r['title'][:40]}")
        if not args.offline and i < len(refs) and args.interval > 0:
            time.sleep(args.interval)

    mark_duplicates(results)
    scorecard = compute_scorecard(results)
    md = render_md(results, args.offline, args.profile)
    with open(args.out, "w", encoding="utf-8") as f:
        f.write(md)
    json_path = args.json_out or (args.out.rsplit(".", 1)[0] + ".json")
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump({"version": VERSION, "profile": args.profile, "offline": args.offline,
                   "scorecard": scorecard, "results": results},
                  f, ensure_ascii=False, indent=2)
    print(f"CiteScore: {scorecard['score']}/100 ({scorecard['grade']} 级，{scorecard['total']} 条)")

    if args.export:
        base = args.out.rsplit(".", 1)[0] if "." in args.out else args.out
        for fmt in [x.strip().lower() for x in args.export.split(",") if x.strip()]:
            if fmt == "bibtex":
                p = base + ".bib"
                n = export_bibtex(results, p)
                print(f"导出：{p}（{n} 条 verified，可直接进论文）")
            elif fmt == "csv":
                p = base + ".csv"
                export_csv(results, p)
                print(f"导出：{p}（{len(results)} 条全量审计台账）")
            else:
                print(f"⚠️ 未知导出格式 {fmt}（支持 bibtex,csv）", file=sys.stderr)

    bad = [r for r in results if r["verdict"] in ("unreachable", "invalid")]
    print(f"\n报告：{args.out}\nJSON：{json_path}")
    if bad:
        print(f"⚠️ {len(bad)} 条 unreachable/invalid" + ("（strict 模式 → exit 1）" if args.strict else ""))
    return 1 if (args.strict and bad) else 0


def main_with_args(argv: list) -> int:
    """程序化调用入口（测试/其他脚本用）。argv 不含脚本名。"""
    old = sys.argv
    sys.argv = [sys.argv[0]] + list(argv)
    try:
        return main()
    finally:
        sys.argv = old


if __name__ == "__main__":
    sys.exit(main())
