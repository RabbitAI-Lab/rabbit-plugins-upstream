#!/usr/bin/env python3
"""yilu (1lou) parser - Xiuno BBS 资源论坛（BT之家1LOU站）。

站点: https://1lou.me（及 6 个镜像域名）

实测特性（2026-08 实连验证）:
  - Xiuno BBS 论坛；搜索为 GET 表单: {base}/search.htm?keyword={keyword}（第1页），
    分页为 search-{keyword}-{type}-{page}.htm（keyword 未编码，故 parser 用 GET 形式更稳）。
  - 结果页主体 .threadlist 内 thread 链接格式: thread-{tid}.htm（单段 tid，非 thread-tid-1-1）。
  - 帖子详情页**无 magnet 链接**，下载物为 .torrent 种子文件:
    attach-download-{aid}.htm -> 直接返回 application/octet-stream 的 bencode 种子。
  - 因此本源 link_type 恒为 torrent；downloader-manager 下载该 URL 得 .torrent 再喂 qBittorrent。
    （站方推荐纯 BT 客户端 Transmission/BitComet/qBittorrent/uTorrent，不支持迅雷。）
  - 站内混杂「夸克网盘分享帖」(标题前缀 [夸克下载])，与磁力/种子帖 [BT下载] 并列，
    用标题关键词过滤只留可下载的种子资源。

多域名 failover:
  - dispatcher 不做域名切换，由本 parser 内部逐个遍历 domains[]。
  - 首个能连通并返回结果的域名即采用；不可达切下一个，可达但无结果则不切。

架构约束: parser 只抓「标题串 + 链接」原始字段，不做信息提取（年份/分辨率/编码等
交由 aggregator 调 title_parser 统一解析）。搜索格式/域名失效时只改 config，代码不动。

统一接口: parse(query, source_cfg) -> [candidate]
  query: {"title": "...", "type":..., "year":...}，取 title 构造搜索词
  source_cfg: config.json 中本源配置块（domains / search_url / credibility / ...）
"""
import re
from urllib.parse import quote, urlsplit, urlunsplit, parse_qs

from .common import make_session, fetch_html, build_candidate

# ---- 抓取参数（控制请求数与时延）----
TARGET_RESULTS = 5        # 拿到这么多条种子即提前停止抓详情
MAX_DETAIL_FETCHES = 5    # 最多抓取详情页数上限
MAX_THREAD_LINKS = 15     # 搜索结果采集上限
MAX_DOMAIN_ATTEMPTS = 3   # 域名 failover 上限（7 镜像只试前 3 个，兼顾覆盖与时延）
SEARCH_TIMEOUT = 12
DETAIL_TIMEOUT = 12

# ---- Xiuno BBS 链接模式 ----
# 实测结果页 thread 链接为 thread-{tid}.htm（单段 tid）
THREAD_HREF_RE = re.compile(r"thread-\d+\.htm")
# 帖子页下载物: attach-download-{aid}.htm -> .torrent 种子文件
ATTACH_DOWNLOAD_RE = re.compile(r"attach-download-\d+\.htm")
# magnet 防御性兜底（实测 1lou 帖子无 magnet，保留以防个别帖或将来改版）
MAGNET_XT_RE = re.compile(r"magnet:\?xt=urn:btih:[a-zA-Z0-9]+")

# 网盘/低质分享帖过滤词（1lou 站内特有：[夸克下载] 等是网盘分享而非种子）。
# 可由 source_cfg.exclude_keywords 覆盖，调过滤词无需改代码。
DEFAULT_EXCLUDE_KEYWORDS = ("网盘", "夸克", "片源", "无字")


def parse(query, source_cfg):
    title = query.get("title", "")
    if not title:
        return []
    domains = source_cfg.get("domains") or ["https://1lou.me"]
    exclude_kw = tuple(source_cfg.get("exclude_keywords") or DEFAULT_EXCLUDE_KEYWORDS)
    kw_enc = quote(title)
    session = make_session()

    # ---- 多域名 failover：逐域名尝试搜索，首个可达即用 ----
    threads = None
    used_base = None
    for base in domains[:MAX_DOMAIN_ATTEMPTS]:
        base = base.rstrip("/")
        t = _search(base, kw_enc, session, source_cfg, exclude_kw)
        if t is not None:        # None=不可达(触发 failover)；[]=可达但无结果(不 failover)
            threads = t
            used_base = base
            break
    if not threads:
        return []

    # ---- 抓详情拿种子/磁力，凑满 TARGET 即停 ----
    candidates = []
    seen_links = set()
    detail_fetched = 0
    for thread_url, thread_title in threads:
        if len(candidates) >= TARGET_RESULTS or detail_fetched >= MAX_DETAIL_FETCHES:
            break
        detail_fetched += 1
        link = _fetch_thread_link(thread_url, session, used_base)
        if not link:
            continue  # 该帖无种子/磁力（多为网盘帖被标题过滤漏网），跳过--论坛页不可直接下载
        if link["url"] in seen_links:
            continue
        seen_links.add(link["url"])
        # 标题优先取磁力 dn（资源真名）；1lou 实测无 magnet，故通常用帖子标题(搜索结果链接文本)
        cand_title = link.get("dn") or thread_title
        candidates.append(build_candidate(
            title=cand_title,
            url=link["url"],
            source_cfg=source_cfg,
            link_type=link["type"],
            detail_url=thread_url,
        ))
    return candidates


def _search(base, kw_enc, session, source_cfg, exclude_kw):
    """单域名搜索。

    返回 [(thread_url, title), ...] 或 None。
      None = 域名不可达 -> 触发 failover
      []   = 可达但无结果 -> 不 failover（站点正常，只是没搜到）
    """
    search_url = _build_search_url(base, kw_enc, source_cfg)
    html, soup = fetch_html(search_url, session=session, timeout=SEARCH_TIMEOUT, encoding="utf-8")
    if html is None:
        return None
    threads = []
    seen = set()
    for a in soup.find_all("a", href=True):
        href = a.get("href", "")
        if not THREAD_HREF_RE.search(href):
            continue
        name = (a.get_text(strip=True) or a.get("title", "")).strip()
        if not name:
            continue
        if any(k in name for k in exclude_kw):   # 站内网盘分享帖过滤
            continue
        full = href if href.startswith("http") else base + "/" + href.lstrip("/")
        if full in seen:
            continue
        seen.add(full)
        threads.append((full, name))
        if len(threads) >= MAX_THREAD_LINKS:
            break
    return threads


def _build_search_url(base, kw_enc, source_cfg):
    """用当前 base 重建搜索 URL：取 config.search_url 路径，host 换成 base（保证 failover 一致）。

    默认 Xiuno GET 搜索: search.htm?keyword={q}（{q} 已 URL 编码）。
    """
    tpl = source_cfg.get("search_url") or "https://1lou.me/search.htm?keyword={q}"
    url = tpl.replace("{q}", kw_enc)
    return _with_host(url, base)


def _with_host(url, base):
    """把 url 的 scheme://host 替换为 base，保留路径与查询。"""
    u = urlsplit(url)
    b = urlsplit(base)
    return urlunsplit((b.scheme or "https", b.netloc, u.path, u.query, u.fragment))


def _fetch_thread_link(thread_url, session, base):
    """抓帖子详情页取下载链接。

    1lou 实测: 帖子页无 magnet，下载物为 attach-download-{aid}.htm (.torrent 种子文件)。
    逻辑: 防御性先查 magnet(若有取 dn 作标题)；主路径取首个 attach-download 种子。

    返回 {"url":..., "type":"magnet"|"torrent", "dn":...} 或 None。
    """
    html, soup = fetch_html(thread_url, session=session, timeout=DETAIL_TIMEOUT, encoding="utf-8")
    if not html:
        return None
    magnet = _extract_magnet(html, soup)
    if magnet:
        return {"url": magnet, "type": "magnet", "dn": _magnet_dn(magnet)}
    # 主路径: attach-download 种子文件（一帖可能有多个，取首个；其余视为同资源镜像/分段）
    m = ATTACH_DOWNLOAD_RE.search(html)
    if m:
        attach = m.group(0)
        full = attach if attach.startswith("http") else base + "/" + attach.lstrip("/")
        return {"url": full, "type": "torrent"}
    return None


def _extract_magnet(html, soup):
    """防御性: 优先从 <a href="magnet:..."> 取完整磁力（含 trackers），兜底正则抓 xt。

    1lou 实测帖子无 magnet，此函数通常返回 None；保留以防个别帖或将来改版。
    """
    for a in soup.find_all("a", href=True):
        href = a["href"]
        if href.startswith("magnet:") and "btih:" in href:
            return href.strip()
    m = MAGNET_XT_RE.search(html)
    return m.group(0) if m else None


def _magnet_dn(magnet_uri):
    """从磁力链接解析 dn（资源显示名），已 URL 解码。无则返回 None。"""
    try:
        q = urlsplit(magnet_uri).query
        dns = parse_qs(q).get("dn")
        if dns:
            return dns[0]
    except Exception:
        return None
    return None
