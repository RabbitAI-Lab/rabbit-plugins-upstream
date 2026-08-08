#!/usr/bin/env python3
"""tmdb_lookup.py - TMDB 媒体元信息查询（media-lookup 技能）。

TMDB 查询 + 豆瓣兜底 + 检索前识别(identify)。

功能：
  - 媒体识别：按片名[+年份]查询 TMDB，返回标准 JSON 媒体条目。
  - 豆瓣兜底：TMDB 不可达时，用豆瓣 suggest API 补年份信息（国内直连、免 Key）。
  - 频率限制：滑动窗口请求队列调度，认证 40 次/10s、未认证 10 次/10s，不超频。
  - 429 重试：超频返回 HTTP 429 时，按 Retry-After 或指数退避(1->2->4->8s)重试自愈。

用法:
  tmdb_lookup.py identify "功夫" 2004    # 自动判定 movie/tv
  tmdb_lookup.py movie "功夫" 2004       # 查询电影详情
  tmdb_lookup.py tv "权力的游戏" 2011     # 查询剧集详情
  tmdb_lookup.py douban "狂飙" tv         # 豆瓣查询

环境变量:
  TMDB_API_KEY - TMDB API 密钥（https://www.themoviedb.org/settings/api 申请，免费）。
    本脚本只从环境变量读取，不关心密钥来源（由编排器/agent 注入环境变量）；
    未配置则降级为豆瓣兜底，识别精度下降。
"""
import json
import os
import re
import socket
import sys
import time
import threading
import urllib.error
import urllib.parse
import urllib.request

TMDB_BASE = "https://api.themoviedb.org/3"
SKILL_DIR = os.path.dirname(os.path.abspath(__file__))
CACHE_FILE = os.path.join(SKILL_DIR, ".cache", "tmdb_cache.json")
CACHE_TTL = 86400 * 7  # 7 天

# 豆瓣搜索建议 API（国内直连，无需 API Key）
DOUBAN_SUGGEST_URL = "https://movie.douban.com/j/subject_suggest"

# 网络不可达标记：首次 TMDB 网络/超时失败后置 True，后续全部跳过网络回退启发式
_NET_DOWN = False


# ==================== DNS 修复（NAS 专用）====================
# TMDB 域名可能被本地 DNS 解析到不可达的中国 CDN IP。
# 强制使用 AWS CloudFront IP，绕过本地 DNS 问题。

_TMDB_HOST = "api.themoviedb.org"
_TMDB_FALLBACK_IPS = ["18.244.94.59", "13.224.103.10", "13.225.7.7"]
_ip_override_active = False
_orig_getaddrinfo = socket.getaddrinfo


def _patched_getaddrinfo(host, port, family=0, type=0, proto=0, flags=0):
    """将 TMDB 域名重定向到可用的 AWS CloudFront IP。"""
    if host == _TMDB_HOST:
        ip = _TMDB_FALLBACK_IPS[0]
        return [(socket.AF_INET, socket.SOCK_STREAM, 6, "", (ip, port))]
    return _orig_getaddrinfo(host, port, family, type, proto, flags)


def _setup_ip_override():
    """启用 IP 覆盖（首次连接失败后调用）。"""
    global _ip_override_active
    if not _ip_override_active:
        socket.getaddrinfo = _patched_getaddrinfo
        _ip_override_active = True


def _check_dns_health():
    """快速检测 TMDB DNS 解析的 IP 是否可达。不可达返回 False。"""
    try:
        infos = _orig_getaddrinfo(_TMDB_HOST, 443, socket.AF_INET)
        for info in infos:
            ip = info[4][0]
            try:
                with socket.create_connection((ip, 443), timeout=3):
                    return True
            except Exception:
                continue
        return False
    except Exception:
        return False


# 启动时检测 DNS，不可达则立即启用 IP 覆盖
if not _check_dns_health():
    _setup_ip_override()


# ==================== 中文数字辅助 ====================

_CN_DIGITS = {"零": 0, "一": 1, "二": 2, "三": 3, "四": 4, "五": 5,
              "六": 6, "七": 7, "八": 8, "九": 9}


def _cn_to_int(s):
    """中文数字转整数：'一'->1, '十二'->12, '二十'->20, '十'->10。"""
    if not s:
        return 0
    if s == "十":
        return 10
    if "十" in s:
        parts = s.split("十")
        tens = _CN_DIGITS.get(parts[0], 1) if parts[0] else 1
        ones = _CN_DIGITS.get(parts[1], 0) if len(parts) > 1 and parts[1] else 0
        return tens * 10 + ones
    return _CN_DIGITS.get(s, 0)


# ==================== 豆瓣 fallback ====================
# TMDB 不可达时，用豆瓣 suggest API 至少拿到年份信息。
# 限制：豆瓣 type 字段不区分电影/电视剧，无 collection 信息。

_DOUBAN_LAST_CALL = 0.0
_DOUBAN_MIN_INTERVAL = 0.5  # 秒：避免豆瓣限流（实测连续 >5 次可能返回空）


def _douban_suggest(name, timeout=5):
    """查询豆瓣搜索建议 API，返回结果列表。

    特点：国内直连、免 Key、响应快（~0.1s）；返回 title/year/type/id/subtitle。
    电视剧标题含「第X季」后缀，可用于解析季年份。内置 0.5s 间隔 + 重试防限流。
    """
    global _DOUBAN_LAST_CALL
    elapsed = time.time() - _DOUBAN_LAST_CALL
    if elapsed < _DOUBAN_MIN_INTERVAL:
        time.sleep(_DOUBAN_MIN_INTERVAL - elapsed)
    _DOUBAN_LAST_CALL = time.time()
    url = DOUBAN_SUGGEST_URL + "?" + urllib.parse.urlencode({"q": name})
    for attempt in range(3):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                results = json.loads(resp.read().decode("utf-8"))
                if results:
                    return results
                if attempt < 2:  # 空列表 = 可能被限流，等待后重试
                    time.sleep(1.0 * (attempt + 1))
        except Exception:
            if attempt < 2:
                time.sleep(1.0 * (attempt + 1))
    return []


def _douban_search_movie(title, year_hint=""):
    """豆瓣 fallback：返回最小电影 dict（含年份，无 collection）。
    当 TMDB 完全不可达时，至少能拿到上映年份用于文件命名。"""
    results = _douban_suggest(title)
    if not results:
        return None
    # 精确匹配优先，其次模糊匹配
    for r in results:
        if r.get("title", "") == title:
            y = r.get("year", "")
            return {"title": r["title"], "release_date": f"{y}-01-01" if y else "",
                    "belongs_to_collection": None, "_source": "douban"}
    for r in results:
        rt = r.get("title", "")
        y = r.get("year", "")
        if title in rt or rt in title:
            if year_hint and y and y != year_hint:
                continue
            return {"title": rt, "release_date": f"{y}-01-01" if y else "",
                    "belongs_to_collection": None, "_source": "douban"}
    return None


def _douban_search_tv(title, year_hint=""):
    """豆瓣 fallback：返回最小 TV dict（含季年份，无 episode_count）。
    豆瓣标题含「第X季」后缀，解析后构造 seasons 列表。无后缀视为整剧(S01)。"""
    results = _douban_suggest(title)
    if not results:
        return None
    seasons = []
    show_year = ""
    matched = False
    for r in results:
        rt = r.get("title", "")
        y = r.get("year", "")
        # 解析季数：绝命毒师 第一季 -> season 1
        m = re.search(r"第([一二三四五六七八九十]+)季", rt)
        if m:
            snum = _cn_to_int(m.group(1))
            if snum > 0:
                base = rt[:m.start()].strip()
                if base == title or title in base:
                    matched = True
                    seasons.append({
                        "season_number": snum,
                        "air_date": f"{y}-01-01" if y else "",
                        "name": "", "episode_count": 0,
                    })
                    if not show_year or (y and show_year > y):
                        show_year = y
        elif rt == title or (title in rt and "季" not in rt):
            matched = True
            if not show_year:
                show_year = y
    if not matched:
        return None
    if not seasons:
        seasons.append({"season_number": 1, "air_date": f"{show_year}-01-01" if show_year else "",
                        "name": "", "episode_count": 0})
    seasons.sort(key=lambda s: s["season_number"])
    return {"name": title, "first_air_date": f"{show_year}-01-01" if show_year else "",
            "seasons": seasons, "number_of_episodes": 0, "_source": "douban"}


# ==================== 缓存管理 ====================

def _load_cache():
    """加载 TMDB 响应缓存。"""
    if os.path.exists(CACHE_FILE):
        try:
            with open(CACHE_FILE, encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return {}
    return {}


def _save_cache(cache):
    """保存 TMDB 响应缓存。"""
    os.makedirs(os.path.dirname(CACHE_FILE), exist_ok=True)
    with open(CACHE_FILE, "w", encoding="utf-8") as f:
        json.dump(cache, f, ensure_ascii=False, indent=2)


# ==================== TMDB 频率限制与指数退避 ====================
#
# TMDB API 在国内受限主因：网络链路阻断（DNS/IP 封锁）与频率限制（429）。
# 已启用智能缓存（见 _load_cache / 各 search_* 函数）+ 合规限流重试（本节）。
#
#   频率限制：未认证请求 10 次/10 秒，认证后 40 次/10 秒；超频返回 HTTP 429。
#   应对：滑动窗口请求队列调度（不超频）+ 429 指数退避重试（超频后自愈）。

_RATE_WINDOW = 10.0           # 滑动窗口长度（秒），与 TMDB 限额窗口对齐
_RATE_LIMIT_AUTH = 40         # 认证（带 API Key）：40 次/10 秒
_RATE_LIMIT_UNAUTH = 10       # 未认证：10 次/10 秒
_RATE_ACQUIRE_TIMEOUT = 30.0  # 获取配额最长等待（秒），避免无限阻塞
_RATE_LOCK = threading.Lock()
_rate_call_times = []         # 滑动窗口内的请求时间戳队列

_MAX_429_RETRIES = 4          # 429 最多指数退避重试次数
_429_BASE_DELAY = 1.0         # 退避基数（秒）：1, 2, 4, 8 ...
_429_MAX_DELAY = 30.0         # 单次退避上限（秒）


def _rate_limit_for(api_key):
    """根据是否携带 API Key 返回对应频率上限。"""
    return _RATE_LIMIT_AUTH if api_key else _RATE_LIMIT_UNAUTH


def _acquire_rate_slot(api_key):
    """滑动窗口请求队列调度：确保不超 TMDB 频率上限。

    在发起网络请求前调用。若当前 10 秒窗口内请求数已达上限，
    阻塞等待直到最早的请求滑出窗口（腾出配额）或超时。
    返回 True 表示已占用一个配额槽位，False 表示超时未获取。
    """
    limit = _rate_limit_for(api_key)
    deadline = time.time() + _RATE_ACQUIRE_TIMEOUT
    while True:
        with _RATE_LOCK:
            now = time.time()
            while _rate_call_times and now - _rate_call_times[0] >= _RATE_WINDOW:
                _rate_call_times.pop(0)
            if len(_rate_call_times) < limit:
                _rate_call_times.append(now)
                return True
            # 窗口已满：等待最早请求滑出窗口
            wait = _RATE_WINDOW - (now - _rate_call_times[0]) + 0.05
        if time.time() + wait > deadline:
            return False
        time.sleep(min(wait, 0.5))


def _parse_retry_after(err):
    """解析 429 响应的 Retry-After 头，返回建议等待秒数；无法解析返回 None。

    支持两种格式：纯数字（秒）或 HTTP 日期。TMDB 通常返回秒数。
    """
    headers = getattr(err, "headers", None)
    val = headers.get("Retry-After") if headers else None
    if not val:
        return None
    val = val.strip()
    if val.isdigit():
        return min(float(val), _429_MAX_DELAY * 2)
    try:
        import email.utils
        target = email.utils.parsedate_to_datetime(val).timestamp()
        delay = target - time.time()
        return delay if 0 < delay < _429_MAX_DELAY * 2 else None
    except Exception:
        return None


def _is_network_error(ename, msg):
    """判断异常是否为网络层错误（应触发 fail-fast 标记网络不可达）。"""
    return (ename in ("URLError", "TimeoutError", "OSError", "gaierror")
            or "timeout" in msg or "connection" in msg
            or "unreachable" in msg or "name or service" in msg
            or "temporary failure" in msg or "nodename" in msg
            or "no address" in msg)


# ==================== TMDB API 核心 ====================

def get_api_key():
    """从环境变量读取 TMDB API Key。"""
    return os.environ.get("TMDB_API_KEY", "")


def _api_get(path, params, api_key):
    """TMDB API GET 请求，带频率限制 + 指数退避重试 + fail-fast + IP 覆盖。

    策略：
      - 频率限制：滑动窗口队列调度，认证 40 次/10s、未认证 10 次/10s，不超频。
      - HTTP 429：读取 Retry-After 或指数退避(1->2->4->8s)后重试。
      - 首次网络失败 -> 启用 IP 覆盖并重试一次。
      - 第二次仍失败 -> 标记 _NET_DOWN，后续全部跳过网络请求。
      - HTTPError(404/401 等) 表示 API 可达但无数据，不标记网络不可达。
      - 自动处理 gzip 响应。
    """
    global _NET_DOWN, _ip_override_active
    if _NET_DOWN:
        return {"error": "network unavailable (fail-fast after first failure)"}
    params["api_key"] = api_key
    params.setdefault("language", "zh-CN")
    url = f"{TMDB_BASE}{path}?{urllib.parse.urlencode(params)}"
    headers = {"Accept": "application/json", "Accept-Encoding": "identity"}

    _429_count = 0          # 429 连续重试计数
    _net_ip_tried = False   # IP 覆盖是否已尝试一次
    while True:
        # 1. 频率限制：滑动窗口获取请求配额（不超 TMDB 限额）
        if not _acquire_rate_slot(api_key):
            return {"error": "rate-limit timeout: no TMDB quota within window"}

        # 2. 发起请求
        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=8) as resp:
                raw = resp.read()
                # 某些代理可能忽略 Accept-Encoding: identity，返回 gzip
                if raw[:2] == b'\x1f\x8b':
                    import gzip
                    raw = gzip.decompress(raw)
                return json.loads(raw.decode("utf-8"))
        except urllib.error.HTTPError as e:
            if e.code == 429:
                # 频率超限：指数退避重试
                _429_count += 1
                if _429_count > _MAX_429_RETRIES:
                    return {"error": f"HTTP 429 rate limited after {_MAX_429_RETRIES} retries"}
                delay = _parse_retry_after(e)
                if delay is None:
                    delay = min(_429_BASE_DELAY * (2 ** (_429_count - 1)), _429_MAX_DELAY)
                time.sleep(delay)
                continue  # 退避后重新获取配额并重试
            # 404/401 等：API 可达但无数据，不标记网络不可达
            return {"error": str(e)}
        except Exception as e:
            ename = type(e).__name__
            msg = str(e).lower()
            # 网络错误：首次失败启用 IP 覆盖并重试一次
            if not _net_ip_tried:
                _net_ip_tried = True
                _setup_ip_override()
                continue
            # 第二次仍失败：标记网络不可达
            if _is_network_error(ename, msg):
                _NET_DOWN = True
            return {"error": str(e)}


# ==================== 电影查询 ====================

def search_movie(title, year="", api_key=None):
    """搜索电影，返回完整详情（含 belongs_to_collection）。
    TMDB 不可达时回退豆瓣补年份（无 collection 信息）。"""
    api_key = api_key or get_api_key()
    if not api_key:
        return None

    cache = _load_cache()
    cache_key = f"movie:{title}:{year}"
    if cache_key in cache:
        entry = cache[cache_key]
        if time.time() - entry.get("ts", 0) < CACHE_TTL:
            return entry.get("data")

    result = _api_get("/search/movie", {"query": title, "year": year}, api_key)
    if "error" in result or not result.get("results"):
        # 尝试不带年份搜索
        if year:
            result = _api_get("/search/movie", {"query": title}, api_key)
        if "error" in result or not result.get("results"):
            # TMDB 不可达或无结果 -> 豆瓣 fallback
            douban = _douban_search_movie(title, year)
            if douban:
                cache[cache_key] = {"data": douban, "ts": time.time()}
                _save_cache(cache)
                return douban
            return None

    movie = result["results"][0]

    # 获取完整详情（含 belongs_to_collection）
    if movie.get("id"):
        details = _api_get(f"/movie/{movie['id']}", {}, api_key)
        if "error" not in details:
            movie = details

    cache[cache_key] = {"data": movie, "ts": time.time()}
    _save_cache(cache)
    return movie


def lookup_collection(title, year="", api_key=None):
    """查询电影是否属于某个系列/合集，返回合集详情或 None。"""
    movie = search_movie(title, year, api_key)
    if not movie:
        return None

    collection = movie.get("belongs_to_collection")
    if not collection:
        return None

    # 获取合集详情（含所有成员）
    collection_id = collection.get("id")
    if collection_id:
        cache = _load_cache()
        cache_key = f"collection:{collection_id}"
        if cache_key in cache:
            entry = cache[cache_key]
            if time.time() - entry.get("ts", 0) < CACHE_TTL:
                return entry.get("data")

        details = _api_get(f"/collection/{collection_id}", {}, api_key)
        if "error" not in details:
            collection = details
            cache[cache_key] = {"data": collection, "ts": time.time()}
            _save_cache(cache)

    return collection




# ==================== 电视剧查询 ====================

def search_tv(title, year="", api_key=None):
    """搜索电视剧，返回详情（含季列表）。
    TMDB 不可达时回退豆瓣补季年份（无 episode_count）。"""
    api_key = api_key or get_api_key()
    if not api_key:
        return None

    cache = _load_cache()
    cache_key = f"tv:{title}:{year}"
    if cache_key in cache:
        entry = cache[cache_key]
        if time.time() - entry.get("ts", 0) < CACHE_TTL:
            return entry.get("data")

    params = {"query": title}
    if year:
        params["first_air_date_year"] = year
    result = _api_get("/search/tv", params, api_key)
    if "error" in result or not result.get("results"):
        if year:
            result = _api_get("/search/tv", {"query": title}, api_key)
        if "error" in result or not result.get("results"):
            # TMDB 不可达或无结果 -> 豆瓣 fallback
            douban = _douban_search_tv(title, year)
            if douban:
                cache[cache_key] = {"data": douban, "ts": time.time()}
                _save_cache(cache)
                return douban
            return None

    show = result["results"][0]

    # 获取完整详情（含 genres/seasons）
    if show.get("id"):
        details = _api_get(f"/tv/{show['id']}", {}, api_key)
        if "error" not in details:
            show = details

    cache[cache_key] = {"data": show, "ts": time.time()}
    _save_cache(cache)
    return show






# ==================== 归一化（标准 JSON 契约） ====================

def _normalize_movie(movie, year="", query_title=""):
    """将电影详情归一化为标准 JSON 契约。
    兼容 TMDB 详情 dict 与豆瓣兜底 dict（带 _source=douban 标记时判定为兜底）。"""
    is_douban = movie.get("_source") == "douban"
    coll = movie.get("belongs_to_collection")
    return {
        "media_type": "movie",
        "title": movie.get("title", query_title),
        "original_title": movie.get("original_title", ""),
        "year": (movie.get("release_date") or "")[:4] or year,
        "tmdb_id": None if is_douban else movie.get("id"),
        "overview": (movie.get("overview") or "")[:300],
        "collection": coll.get("name") if coll else None,
        "genres": [g.get("name", "") for g in movie.get("genres", []) if g.get("name")],
        "poster_path": movie.get("poster_path"),
        "source": "douban_fallback" if is_douban else "tmdb",
    }


def _normalize_tv(show, year="", query_title=""):
    """将剧集详情归一化为标准 JSON 契约。
    兼容 TMDB 详情 dict 与豆瓣兜底 dict（带 _source=douban 标记时判定为兜底）。"""
    is_douban = show.get("_source") == "douban"
    seasons = [
        {"season": f"S{s.get('season_number', 0):02d}",
         "name": s.get("name", ""),
         "year": (s.get("air_date") or "")[:4],
         "episode_count": s.get("episode_count", 0)}
        for s in show.get("seasons", [])
    ]
    return {
        "media_type": "tv",
        "title": show.get("name", query_title),
        "original_title": show.get("original_name", ""),
        "year": (show.get("first_air_date") or "")[:4] or year,
        "tmdb_id": None if is_douban else show.get("id"),
        "overview": (show.get("overview") or "")[:300],
        "collection": None,
        "seasons": seasons,
        "genres": [g.get("name", "") for g in show.get("genres", []) if g.get("name")],
        "poster_path": show.get("poster_path"),
        "source": "douban_fallback" if is_douban else "tmdb",
    }


def _normalize_douban(db, query_title="", year=""):
    """将豆瓣兜底结果归一化为标准 JSON 契约（tmdb_id=None, source=douban_fallback）。
    豆瓣 TV dict 含 first_air_date/seasons/name，电影 dict 含 release_date/title，据此判定类型。"""
    is_tv = bool(db.get("first_air_date") or db.get("seasons") or db.get("name"))
    if is_tv:
        seasons = [
            {"season": f"S{s.get('season_number', 0):02d}",
             "name": s.get("name", ""),
             "year": (s.get("air_date") or "")[:4],
             "episode_count": s.get("episode_count", 0)}
            for s in db.get("seasons", [])
        ]
        return {
            "media_type": "tv",
            "title": db.get("name", query_title),
            "original_title": "",
            "year": (db.get("first_air_date") or "")[:4] or year,
            "tmdb_id": None,
            "overview": "",
            "collection": None,
            "seasons": seasons,
            "genres": [],
            "poster_path": None,
            "source": "douban_fallback",
        }
    return {
        "media_type": "movie",
        "title": db.get("title", query_title),
        "original_title": "",
        "year": (db.get("release_date") or "")[:4] or year,
        "tmdb_id": None,
        "overview": "",
        "collection": None,
        "genres": [],
        "poster_path": None,
        "source": "douban_fallback",
    }


# ==================== CLI ====================


def identify(title, year="", api_key=None):
    """检索前媒体识别：返回归一化标准 JSON，供多链路检索消歧与透传。

    依次尝试 movie -> tv，命中即返回归一化条目。无 TMDB_API_KEY 或 TMDB 不可达时
    自动豆瓣兜底补年份/季。返回标准 JSON 契约或 {"error": ...}。
    """
    api_key = api_key or get_api_key()
    # 先按 movie 查（电影最常见），无果再 tv
    movie = search_movie(title, year, api_key) if api_key else None
    if movie and (movie.get("id") or movie.get("title")):
        return _normalize_movie(movie, year, title)
    show = search_tv(title, year, api_key) if api_key else None
    if show and (show.get("id") or show.get("name")):
        return _normalize_tv(show, year, title)
    # 豆瓣兜底（无 TMDB key 或网络不可达）
    db = _douban_search_tv(title, year) or _douban_search_movie(title, year)
    if db:
        return _normalize_douban(db, title, year)
    return {"error": "未找到匹配媒体", "query": title, "year": year}


def main():
    """命令行入口。子命令 identify / movie / tv / douban，统一返回标准 JSON 契约。"""
    usage = ("用法: tmdb_lookup.py <identify|movie|tv|douban> <片名> [年份|类型]\n"
             "  identify <片名> [年份]   自动判定 movie/tv，无 Key 时豆瓣兜底（主入口）\n"
             "  movie   <片名> [年份]   强制按电影查询（需 TMDB_API_KEY）\n"
             "  tv      <片名> [年份]   强制按剧集查询（需 TMDB_API_KEY）\n"
             "  douban  <片名> [movie|tv]  豆瓣兜底直查（免 TMDB_API_KEY）")
    dump = lambda obj: print(json.dumps(obj, ensure_ascii=False, indent=2))
    if len(sys.argv) < 2 or sys.argv[1] in ("-h", "--help", "help"):
        print(usage)
        sys.exit(0 if (len(sys.argv) >= 2 and sys.argv[1] in ("-h", "--help", "help")) else 1)

    cmd = sys.argv[1]
    api_key = get_api_key()

    if cmd == "douban":
        if len(sys.argv) < 3:
            dump({"error": "用法: tmdb_lookup.py douban <片名> [movie|tv]"})
            sys.exit(1)
        title = sys.argv[2]
        kind = sys.argv[3] if len(sys.argv) > 3 else "auto"
        if kind == "movie":
            r = _douban_search_movie(title)
        elif kind == "tv":
            r = _douban_search_tv(title)
        else:  # auto: 优先 tv 再 movie
            r = _douban_search_tv(title) or _douban_search_movie(title)
        dump(_normalize_douban(r, title) if r else {"error": "豆瓣未找到", "query": title})

    elif cmd == "identify":
        if len(sys.argv) < 3:
            dump({"error": "用法: tmdb_lookup.py identify <片名> [年份]"})
            sys.exit(1)
        title, year = sys.argv[2], (sys.argv[3] if len(sys.argv) > 3 else "")
        dump(identify(title, year, api_key))

    elif cmd == "movie":
        if not api_key:
            dump({"error": "未配置 TMDB_API_KEY（movie/tv 需 TMDB；改用 identify 可豆瓣兜底，或 douban 直查）"})
            sys.exit(1)
        if len(sys.argv) < 3:
            dump({"error": "用法: tmdb_lookup.py movie <片名> [年份]"})
            sys.exit(1)
        title, year = sys.argv[2], (sys.argv[3] if len(sys.argv) > 3 else "")
        result = search_movie(title, year, api_key)
        dump(_normalize_movie(result, year, title) if result else {"error": "未找到", "query": title, "year": year})

    elif cmd == "tv":
        if not api_key:
            dump({"error": "未配置 TMDB_API_KEY（movie/tv 需 TMDB；改用 identify 可豆瓣兜底，或 douban 直查）"})
            sys.exit(1)
        if len(sys.argv) < 3:
            dump({"error": "用法: tmdb_lookup.py tv <片名> [年份]"})
            sys.exit(1)
        title, year = sys.argv[2], (sys.argv[3] if len(sys.argv) > 3 else "")
        show = search_tv(title, year, api_key)
        dump(_normalize_tv(show, year, title) if show else {"error": "未找到", "query": title, "year": year})

    else:
        dump({"error": f"未知命令: {cmd}", "usage": usage})
        sys.exit(1)


if __name__ == "__main__":
    main()
