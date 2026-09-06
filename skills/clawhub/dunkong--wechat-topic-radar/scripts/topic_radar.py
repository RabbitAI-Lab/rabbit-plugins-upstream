#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
选题雷达 (wechat-topic-radar)

输入一个种子词，沿「搜一搜推荐词」扩散出候选长尾词，对每个词抓取微信搜一搜的
公开文章结果与文章公开互动数据，用本地启发式模型计算「需求热度 / 竞争度 / 机会分」，
输出机会矩阵与蓝海选题清单。

严格依据曼格云公开接口契约，只使用契约已声明的字段；契约未声明但实际返回的字段
（如推荐词项的 word、搜索项的 source）采用防御式读取，取不到则降级处理。

用法见 --help。--self-test 可离线跑通全链路，不消耗任何额度。
"""

import argparse
import json
import math
import os
import re
import sys
import threading
import time
import urllib.error
import urllib.request
import uuid
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone

API_ROOT = "https://api.we-media.cn"
PATHS = {
    "suggestions": "/openapi/wechat-native-search-suggestions/search/suggestions",
    "search": "/openapi/wechat-native-search-articles/search/articles",
    "metrics": "/openapi/wechat-native-article-metrics/articles/metrics",
    # 内容统计走接口 3 的 analysis 模式（¥0.008）而非接口 30（¥0.063）：
    # 实测两者返回的 content / media 字段完全一致，单价只有 1/8
    "content": "/openapi/wechat-native-article-content/articles/content",
    # 热点模式：接口 20 在 query 留空时返回搜一搜实时热搜榜
    "guide": "/openapi/wechat-native-search-guide/search/guide",
    # 账号模式：接口 4 按文章链接或 ghid 分页取公众号历史文章
    "account_articles": "/openapi/wechat-native-account-articles/accounts/articles",
    # 接口 4 返回的账号快照 accountName 实测为空，用它单独取账号名
    "profile": "/openapi/wechat-native-account-profile/accounts/profile",
}

DEEP_TOP_WORDS = 3        # 深度采样覆盖的蓝海词数量

# 契约声明的公众号原始 ID 格式：^gh_[0-9a-fA-F]{12,32}$
GHID_RE = re.compile(r"^gh_[0-9a-fA-F]{12,32}$")

# 契约声明的文章链接格式：^https://mp\.weixin\.qq\.com/s(?:/|\?|$)
ARTICLE_URL_RE = re.compile(r"^https://mp\.weixin\.qq\.com/s(?:/|\?|$)")

DEFAULT_RATE = 4.0          # 每秒请求数上限，远低于 300 次/分钟的限额
DEFAULT_RETRIES = 2
FRESH_DAYS = 90


# --------------------------------------------------------------------------
# 通用工具
# --------------------------------------------------------------------------

def _get(obj, *keys, default=None):
    """沿嵌套 dict 安全取值，任一层缺失即返回 default。"""
    cur = obj
    for k in keys:
        if not isinstance(cur, dict):
            return default
        cur = cur.get(k)
        if cur is None:
            return default
    return cur


def log_norm(value, lo, hi):
    """把正数按 log10 映射到 [0,1]；value 无效或超出范围则截断。"""
    if value is None or value <= 0 or hi <= lo or lo <= 0:
        return 0.0
    x = math.log10(max(value, 1))
    a, b = math.log10(lo), math.log10(hi)
    return max(0.0, min(1.0, (x - a) / (b - a)))


def median(values):
    vals = sorted(v for v in values if v is not None)
    if not vals:
        return None
    n = len(vals)
    mid = n // 2
    if n % 2:
        return float(vals[mid])
    return (float(vals[mid - 1]) + float(vals[mid])) / 2.0


def fmt_num(n):
    """整数千分位；非整数原样返回。"""
    if n is None:
        return "—"
    if isinstance(n, bool):
        return str(n)
    if isinstance(n, (int, float)):
        return f"{int(n):,}" if float(n).is_integer() else f"{n:,.1f}"
    return str(n)


def esc(text):
    if text is None:
        return ""
    return (str(text).replace("&", "&amp;").replace("<", "&lt;")
            .replace(">", "&gt;").replace('"', "&quot;"))


def md_paras(text):
    """把 AI 洞察的多段文本渲染成 <p>，支持 **加粗**（先转义再还原）。"""
    out = []
    for p in str(text or "").split("\n\n"):
        p = esc(p.strip())
        if not p:
            continue
        out.append(f"<p>{re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', p)}</p>")
    return "".join(out)


def iso_date(ts):
    if not ts:
        return ""
    try:
        return datetime.fromtimestamp(int(ts), tz=timezone.utc).strftime("%Y-%m-%d")
    except (ValueError, OSError, OverflowError):
        return ""


# --------------------------------------------------------------------------
# 客户端：限流 + 重试（复用 Idempotency-Key 避免重复扣费）+ 成本累计
# --------------------------------------------------------------------------

class CostLedger:
    def __init__(self):
        self.total = 0.0
        self.balance = None
        self.calls = 0
        self.by_path = {}          # 按接口路径累计 {path: {"calls": n, "cost": x}}
        self._lock = threading.Lock()

    def record(self, consumption, balance, path=None):
        with self._lock:
            c = float(consumption) if isinstance(consumption, (int, float)) else 0.0
            if isinstance(consumption, (int, float)):
                self.total += c
            if isinstance(balance, (int, float)):
                self.balance = float(balance)
            self.calls += 1
            if path:
                rec = self.by_path.setdefault(path, {"calls": 0, "cost": 0.0})
                rec["calls"] += 1
                rec["cost"] += c


class Client:
    def __init__(self, api_key, rate=DEFAULT_RATE, retries=DEFAULT_RETRIES, ledger=None):
        self.api_key = api_key
        self.retries = retries
        self.ledger = ledger or CostLedger()
        self._gap = 1.0 / max(rate, 0.1)
        self._lock = threading.Lock()
        self._next_slot = 0.0

    def _throttle(self):
        with self._lock:
            now = time.time()
            slot = max(now, self._next_slot)
            self._next_slot = slot + self._gap
            wait = slot - now
        if wait > 0:
            time.sleep(wait)

    def post(self, path, payload):
        """返回响应 data；失败返回 None。code 非 OK 时抛出 ApiError。"""
        key = payload.pop("__idempotency__", None) or str(uuid.uuid4())
        body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
        last_err = None
        for attempt in range(self.retries + 1):
            self._throttle()
            req = urllib.request.Request(API_ROOT + path, data=body, method="POST")
            req.add_header("X-API-Key", self.api_key)
            req.add_header("Content-Type", "application/json")
            # 契约：仅客户端自行重试同一个非 GET 请求时复用同一个值，避免重复扣费
            req.add_header("Idempotency-Key", key)
            try:
                with urllib.request.urlopen(req, timeout=90) as resp:
                    raw = json.loads(resp.read().decode("utf-8"))
            except urllib.error.HTTPError as e:
                detail = ""
                try:
                    detail = e.read().decode("utf-8", "ignore")[:300]
                except Exception:
                    pass
                last_err = f"HTTP {e.code} {detail}"
                if e.code in (429, 500, 502, 503, 504):
                    time.sleep(1.5 * (attempt + 1))
                    continue
                raise ApiError(last_err)
            except (urllib.error.URLError, TimeoutError, json.JSONDecodeError) as e:
                last_err = str(e)
                time.sleep(1.0 * (attempt + 1))
                continue

            code = raw.get("code")
            self.ledger.record(raw.get("consumption"), raw.get("balance"), path)
            if code != "OK":
                raise ApiError(f"接口返回 code={code} requestId={raw.get('requestId')}")
            return raw.get("data") or {}
        raise ApiError(f"请求失败（已重试 {self.retries} 次）：{last_err}")


class ApiError(Exception):
    pass


# --------------------------------------------------------------------------
# 接口调用层
# --------------------------------------------------------------------------

def fetch_suggestions(client, query):
    """接口 23：搜一搜推荐词。返回推荐词列表（不含查询词本身）。"""
    data = client.post(PATHS["suggestions"], {"query": query})
    words, seen = [], set()
    for item in (data.get("items") or []):
        # 契约仅声明 items 为数组，未逐一声明子字段；实测每项含 word，防御式读取
        w = item.get("word") if isinstance(item, dict) else (item if isinstance(item, str) else None)
        if not w or not isinstance(w, str):
            continue
        w = w.strip()
        if w and w not in seen:
            seen.add(w)
            words.append(w)
    return words


def fetch_search(client, query, sort="hot", limit=10, publish_time="any"):
    """接口 14：搜一搜文章。返回标准化文章条目列表。"""
    data = client.post(PATHS["search"], {
        "query": query, "sort": sort, "limit": limit,
        "publishTime": publish_time, "scope": "any",
    })
    items = []
    for raw in (data.get("items") or []):
        url = raw.get("doc_url") or raw.get("url")
        if not url or not ARTICLE_URL_RE.match(url):
            continue  # 只保留契约声明格式的公众号文章链接，其余跳过避免浪费
        items.append({
            "title": (raw.get("title") or "").strip(),
            "account": (_get(raw, "source", "title") or "").strip(),
            "doc_url": url,
            "timestamp": raw.get("timestamp"),
            "desc": (raw.get("desc") or "").strip(),
            "display_read": _display_read(raw),
        })
    return items


def _display_read(item):
    """从搜索结果里提取页面展示的阅读文本（如「6.2万」），属展示值非精确值。"""
    for tag in (_get(item, "source", "tag") or []):
        if not isinstance(tag, dict):
            continue
        m = re.match(r"^\s*阅读\s*(\S+)\s*$", str(tag.get("title") or ""))
        if m:
            return m.group(1)
    return None


def fetch_metrics(client, url):
    """接口 1：文章互动数据。失败返回 None。"""
    try:
        data = client.post(PATHS["metrics"], {"url": url})
    except ApiError:
        return None
    return {
        "url": data.get("url") or url,
        "read_num": data.get("readNum"),
        "read_capped": bool(data.get("readCapped")),
        "read_text": data.get("readText") or "",
        "like_num": data.get("likeNum"),
        "old_like_num": data.get("oldLikeNum"),
        "share_num": data.get("shareNum"),
        "collect_num": data.get("collectNum"),
        "comment_num": data.get("commentNum"),
        "interaction_num": data.get("interactionNum"),
        "rates": data.get("ratesBps") if isinstance(data.get("ratesBps"), dict) else {},
        "title": (data.get("title") or "").strip(),
        "account_name": (data.get("accountName") or "").strip(),
    }


def fetch_content_analysis(client, url):
    """
    接口 3（format=analysis）：内容统计 + 媒体统计。失败返回 None。

    不改用接口 30（文章完整报告）的原因：实测两者返回的 content / media 与
    接口 30 的 contentAnalysis / mediaSummary 字段完全一致，
    而接口 3 单价 ¥0.008、接口 30 单价 ¥0.063，前者只有 1/8。
    本 skill 只缺内容规格，不需要接口 30 打包的 article / engagement 等冗余字段。
    """
    try:
        data = client.post(PATHS["content"], {"url": url, "format": "analysis"})
    except ApiError:
        return None
    ca = data.get("content") if isinstance(data.get("content"), dict) else {}
    ms = data.get("media") if isinstance(data.get("media"), dict) else {}
    return {
        "character_count": ca.get("characterCount"),
        "paragraph_count": ca.get("paragraphCount"),
        "estimated_read_minutes": ca.get("estimatedReadMinutes"),
        "image_count": ms.get("imageCount"),
        "video_count": ms.get("videoCount"),
    }


def fetch_hot_words(client):
    """
    接口 20（query 留空）：搜一搜实时热搜榜。返回 [{rank, word}]。

    契约只声明了 query / data / source，`items` 与 `groups` 是实测补充，防御式读取。
    `items[].id` 格式为 "{排名}-hotscore-{热词}"，可直接取排名。
    """
    data = client.post(PATHS["guide"], {"query": ""})
    words, seen = [], set()
    for item in (data.get("items") or []):
        if not isinstance(item, dict):
            continue
        w = (item.get("word") or "").strip()
        if not w or w in seen:
            continue
        seen.add(w)
        rank = None
        m = re.match(r"^(\d+)-", str(item.get("id") or ""))
        if m:
            rank = int(m.group(1))
        words.append({"rank": rank, "word": w})
    words.sort(key=lambda x: (x["rank"] is None, x["rank"] or 0))
    return words


def fetch_account_articles(client, account, pages=3, limit=20):
    """
    接口 4：公众号历史文章。`account` 为文章链接或 gh_ 开头的原始 ID，二选一。
    逐页取到 pages 页或 hasMore=false 为止，返回 (账号资料, 文章列表)。
    """
    if ARTICLE_URL_RE.match(account):
        id_key, id_val = "url", account
    elif GHID_RE.match(account):
        id_key, id_val = "ghid", account
    else:
        raise ApiError(f"无法识别的公众号标识：{account}（需为文章链接或 gh_ 开头的原始 ID）")

    out, seen = [], set()
    offset = 0
    info = {}
    for _ in range(max(1, pages)):
        body = {id_key: id_val, "offset": offset, "limit": max(1, min(limit, 20))}
        data = client.post(PATHS["account_articles"], body)
        if not info and isinstance(data.get("account"), dict):
            info = data["account"]
        items = data.get("items") or []
        if not items:
            break
        for raw in items:
            url = raw.get("url") or raw.get("canonicalUrl")
            if not url:
                continue
            key = raw.get("sn") or url
            if key in seen:
                continue
            seen.add(key)
            out.append({
                "title": (raw.get("title") or "").strip(),
                "url": url,
                "publish_timestamp": raw.get("publishTimestamp"),
                "idx": raw.get("idx"),
                "copyright_stat": raw.get("copyrightStat"),
                "content_type": raw.get("contentType"),
                "author": (raw.get("author") or "").strip(),
            })
        if not data.get("hasMore"):
            break
        nxt = data.get("nextOffset")
        if not isinstance(nxt, int) or nxt <= offset:
            break
        offset = nxt
    return info, out


# 主题聚类用的轻量停用词；只做粗筛，不追求分词精度
STOPWORDS = set("""的 了 是 在 和 与 及 或 就 都 而 其 这 那 有 没有 什么 怎么 为什么
如何 一个 一种 一些 可以 需要 应该 我们 你们 他们 自己 之 中 上 下 第 最 更 很 太 也 还
再 又 只 才 不 没 别 让 把 被 给 从 到 对 为 年 月 日 期 篇 个 位 名 岁 元 万 亿
""".split())


# 主题标签的首尾清洗字符与虚词（用于剔除被截断的碎片）
PHRASE_TRIM = " \t\r\n!！?？.。,，、;；:：()（）[]【】<>《》\"'“”‘’@#$%^&*+-_=~/\\|"
FRAGMENT_TAILS = set("的了是在和与及就都而其这那有个把被给从到对为让向使等将已会能要上下中")


def _extend_phrase(seed, titles):
    """
    以 seed 为核心，在包含它的所有标题里向左右逐字扩展，返回最长公共串。

    这是解决滑动窗口碎片的关键：窗口切出的「儿园游戏实践」在各标题里位置不同，
    但向左右扩展后会自然长回完整的「幼儿园游戏实践探索与理论成果精选」。
    遇到标题间字符不一致（包括标点）就停，因此不会跨标点粘连。
    """
    cur = seed
    seen = {cur}
    while True:
        idxs = []
        for t in titles:
            i = t.find(cur)
            if i < 0:
                return cur
            idxs.append(i)
        # 先试左扩展
        if all(i > 0 for i in idxs):
            lefts = {t[i - 1] for t, i in zip(titles, idxs)}
            if len(lefts) == 1:
                nxt = lefts.pop() + cur
                if nxt not in seen:
                    seen.add(nxt)
                    cur = nxt
                    continue
        # 再试右扩展
        if all(i + len(cur) < len(t) for t, i in zip(titles, idxs)):
            rights = {t[i + len(cur)] for t, i in zip(titles, idxs)}
            if len(rights) == 1:
                nxt = cur + rights.pop()
                if nxt not in seen:
                    seen.add(nxt)
                    cur = nxt
                    continue
        return cur


def _ngram_topics(clean_titles, raw_titles, ngram, top_n, min_count):
    counter = Counter()
    doc_hits = {}
    for i, ct in enumerate(clean_titles):
        for seg in ct.split():
            if len(seg) < min(ngram):
                continue
            for n in range(ngram[0], ngram[1] + 1):
                for j in range(len(seg) - n + 1):
                    g = seg[j:j + n]
                    if g in STOPWORDS:
                        continue
                    counter[g] += 1
                    doc_hits.setdefault(g, set()).add(i)

    items = [(g, c) for g, c in counter.items() if c >= min_count]
    items.sort(key=lambda x: (-len(doc_hits.get(x[0], ())), -x[1]))
    items = items[:200]  # 只在高频候选里做扩展，控制开销

    merged = {}
    for g, c in items:
        ds = doc_hits[g]
        if len(ds) < 2:
            continue  # 只在一篇里出现的不算主题
        phrase = _extend_phrase(g, [raw_titles[i] for i in ds]).strip(PHRASE_TRIM)
        if len(phrase) < 2 or len(phrase) > 18:
            continue  # 过长多半是整句标题，不是主题
        if phrase[0] in FRAGMENT_TAILS or phrase[-1] in FRAGMENT_TAILS:
            continue  # 以虚词开头/结尾的通常是被截掉的碎片
        if phrase.isdigit():
            continue  # 纯数字（年份、期数）不构成主题
        if phrase not in merged or len(ds) > len(merged[phrase][1]):
            merged[phrase] = (c, ds)

    ranked = sorted(merged.items(), key=lambda kv: (-len(kv[1][1]), -kv[1][0], -len(kv[0])))
    picked = []
    for phrase, _v in ranked:
        if any(p in phrase or phrase in p for p in picked):
            continue
        picked.append(phrase)
        if len(picked) >= top_n:
            break
    return [{"topic": p, "count": merged[p][0], "docs": len(merged[p][1])} for p in picked]


def extract_topics(titles, top_n=12, min_count=2):
    """
    从标题里提取高频主题标签。
    没有第三方分词库：n-gram 找种子 → 最长公共串扩展 → 包含关系去重。
    够用，但不追求分词精度。
    """
    raw = [t or "" for t in (titles or [])]
    clean = [re.sub(r"[^\u4e00-\u9fa5A-Za-z0-9]+", " ", t) for t in raw]
    picked = _ngram_topics(clean, raw, (3, 6), top_n, min_count)
    if len(picked) < max(3, top_n // 2):
        picked = _ngram_topics(clean, raw, (2, 6), top_n, min_count)
    return picked


def parse_account(spec):
    """
    解析 --account 参数，支持两种写法：
        "https://mp.weixin.qq.com/s?..."              纯链接，名称留空
        "广东教育传媒|https://mp.weixin.qq.com/s?..."  顺手给号起个名
    返回 (名称或 None, 链接或 ghid)。
    """
    raw = (spec or "").strip()
    if "|" in raw and not raw.startswith("http"):
        name, _, rest = raw.partition("|")
        if name.strip() and rest.strip():
            return name.strip(), rest.strip()
    return None, raw


# 注：接口 16（公众号资料）实测对多数账号返回空 accountName（2026-08-29 实测两个教育号均为空），
# 因此不自动调用它取名字，改由调用方用「名称|链接」的写法显式命名，省下 ¥0.03/号。


# --------------------------------------------------------------------------
# 评分模型（本地启发式，非平台指标）
# --------------------------------------------------------------------------

def batch_norm(value_map, floor=0.1, ceil=0.9):
    """
    批次内相对归一：把本批候选词的某个正数指标按 log10 拉开到 [floor, ceil]。

    不用固定的绝对区间，是因为不同领域的阅读/互动水位可能相差几个数量级
    （实测同批次阅读中位数可低至 445，硬编码 1000~100000 会把多数词压成 0，失去区分度）。
    用户要的是「这批词里哪个相对更蓝海」，属于批内排序问题。

    防御：若批内极差不足 2 倍（log10 跨度 < 0.3），说明差异不可信，一律给中性值 0.5，
    避免把噪声放大成虚假的分数差距。
    """
    vals = {k: v for k, v in value_map.items()
            if isinstance(v, (int, float)) and not isinstance(v, bool) and v > 0}
    if len(vals) < 2:
        return {k: 0.5 for k in vals}
    logs = {k: math.log10(v) for k, v in vals.items()}
    lo, hi = min(logs.values()), max(logs.values())
    if hi - lo < 0.3:
        return {k: 0.5 for k, v in vals.items()}
    return {k: floor + (ceil - floor) * (logs[k] - lo) / (hi - lo) for k, v in vals.items()}


def compute_stats(word, rank_score, articles):
    """汇总单个候选词的原始观测值，不做归一化。"""
    capped = [a for a in articles if a.get("metrics") and a["metrics"].get("read_capped")]
    valid = [a for a in articles
             if a.get("metrics") and isinstance(a["metrics"].get("read_num"), (int, float))
             and not a["metrics"].get("read_capped")]
    reads = [a["metrics"]["read_num"] for a in valid]
    med_read = median(reads)
    enags = [_get(a["metrics"], "rates", "engagement") for a in valid]
    med_eng = median([e for e in enags if isinstance(e, (int, float))])

    now = time.time()
    stamps = [a.get("timestamp") for a in articles if a.get("timestamp")]
    fresh = None
    if stamps:
        recent = sum(1 for t in stamps if (now - int(t)) <= FRESH_DAYS * 86400)
        fresh = recent / len(stamps)

    accounts = [a.get("account") for a in articles if a.get("account")]
    conc = None
    if accounts:
        conc = 1.0 - (len(set(accounts)) / len(accounts))
    big_share = (sum(1 for r in reads if r >= 10000) / len(reads)) if reads else None

    return {
        "word": word,
        "rank_score": round(rank_score, 3),
        "sample_count": len(articles),
        "valid_count": len(valid),
        "capped_count": len(capped),
        "median_read": med_read,
        "median_engagement_bps": med_eng,
        "fresh_ratio": fresh,
        "account_concentration": conc,
        "big_share": big_share,
        "articles": articles,
    }


def apply_scoring(stats_list):
    """
    需求热度 = 100 × (0.35×词位次 + 0.40×互动热度 + 0.25×新鲜度)
        词位次   —— 该词在搜索联想结果中的相对位置，越靠前说明联想越常见（0~1）
        互动热度 —— 样本互动率基点中位数，批内 log 相对归一
        新鲜度   —— 近 90 天文章占比
    竞争度 = 100 × (0.50×头部水位 + 0.30×账号集中度 + 0.20×大号占比)
        头部水位 —— 样本阅读中位数，批内 log 相对归一
        账号集中度 —— 1 − 不同账号数/样本数，越高说明被少数号把持
        大号占比 —— 阅读 ≥ 1 万 的样本占比
    机会分 = 需求热度 − 竞争度，越高越蓝海。

    证据充分度（独立于评分之外单独呈现）：
        上面三个分数只反映「样本呈现出的形态」，不反映「这个形态有多可信」。
        实测：同样的阅读量与互动率，2 篇和 12 篇样本会算出完全一样的机会分。
        因此单独给出 evidence_n / evidence_level / confidence，并另算一个
        trusted = 机会分 × 可信系数，用于排序，避免 2 篇样本的词凭运气占据榜首。
        机会分本身不做修改，保持「需求 − 竞争」的定义纯粹可审计。
    """
    level_n = batch_norm({i: s["median_read"] for i, s in enumerate(stats_list)})
    heat_n = batch_norm({i: s["median_engagement_bps"] for i, s in enumerate(stats_list)})
    for i, s in enumerate(stats_list):
        demand = 100.0 * (
            0.35 * s["rank_score"]
            + 0.40 * heat_n.get(i, 0.5)
            + 0.25 * (s["fresh_ratio"] if s["fresh_ratio"] is not None else 0.5))
        supply = 100.0 * (
            0.50 * level_n.get(i, 0.5)
            + 0.30 * (s["account_concentration"] if s["account_concentration"] is not None else 0.5)
            + 0.20 * (s["big_share"] if s["big_share"] is not None else 0.0))
        s["demand"] = round(demand, 1)
        s["supply"] = round(supply, 1)
        s["opportunity"] = round(demand - supply, 1)

        n = int(s.get("valid_count") or 0)
        conf = min(1.0, n / 6.0)          # 6 篇视为证据充分，之下线性衰减
        s["evidence_n"] = n
        s["confidence"] = round(conf, 3)
        s["evidence_level"] = "高" if n >= 6 else ("中" if n >= 3 else "低")
        # 可信系数最低 0.45：证据再弱也不把分数抹平，只是往中性压
        s["trusted"] = round((demand - supply) * (0.45 + 0.55 * conf), 1)
    return stats_list


def score_word(word, rank_score, articles):
    """单词评分（供自检等场景使用；批量场景请直接 compute_stats + apply_scoring）。"""
    return apply_scoring([compute_stats(word, rank_score, articles)])[0]


def evidence_text(s):
    """
    证据充分度的展示文案。

    机会分只说明「样本呈现出的形态」，不说明「这个形态有多可信」——
    实测同样的阅读量与互动率，2 篇和 12 篇样本会算出完全一样的机会分。
    所以证据必须单独摆出来，证据不足时顺便给出可信分，提醒别把运气当结论。
    """
    n = int(s.get("evidence_n", s.get("valid_count") or 0))
    lv = s.get("evidence_level") or ("高" if n >= 6 else ("中" if n >= 3 else "低"))
    txt = f"证据 {n} 篇 · {lv}"
    if lv != "高":
        tr = s.get("trusted")
        if tr is None:
            tr = round(s["opportunity"] * (0.45 + 0.55 * min(1.0, n / 6.0)), 1)
        txt += f"（可信分 {tr:+.1f}）"
    return txt, lv


def evidence_html(s):
    txt, lv = evidence_text(s)
    cls = {"高": "ev-hi", "中": "ev-mid", "低": "ev-lo"}.get(lv, "ev-mid")
    return f'<div class="ev {cls}">{esc(txt)}</div>'


# --------------------------------------------------------------------------
# 趋势快照：跨运行对比（本地 JSON，不引数据库）
# --------------------------------------------------------------------------

SNAPSHOT_KEEP = 24          # 每个种子词最多保留的快照次数


def load_snapshot(path):
    """读取历史快照。文件不存在或格式损坏都返回空字典，不阻断主流程。"""
    if not path or not os.path.exists(path):
        return {}
    try:
        with open(path, encoding="utf-8") as f:
            data = json.load(f)
    except (OSError, ValueError):
        return {}
    return data if isinstance(data, dict) else {}


def apply_trend(words, snap, seed):
    """
    与上一次快照对比，给每个词挂上 trend 字段，并返回本次应写入的记录。

    首次运行没有历史时，趋势标记为「首次出现」，不编造任何变化量——
    没有对比基准就不给数字，这是趋势功能最容易造假的地方。
    """
    hist = [h for h in (snap.get(seed) or []) if isinstance(h, dict)]
    prev = (hist[-1].get("words") if hist else {}) or {}
    now = datetime.now().strftime("%m-%d %H:%M")
    rec = {"date": now, "words": {}}

    for s in words:
        w = s["word"]
        cur = {
            "opportunity": s.get("opportunity"),
            "demand": s.get("demand"),
            "supply": s.get("supply"),
            "median_read": s.get("median_read"),
            "median_engagement_bps": s.get("median_engagement_bps"),
            "valid_count": s.get("valid_count"),
            "sample_count": s.get("sample_count"),
        }
        rec["words"][w] = cur
        p = prev.get(w)
        if not p:
            s["trend"] = {"is_new": True, "history_n": len(hist) + 1}
            continue
        def _d(k):
            a, b = cur.get(k), p.get(k)
            if isinstance(a, (int, float)) and isinstance(b, (int, float)):
                return round(a - b, 1)
            return None
        s["trend"] = {
            "is_new": False,
            "prev_date": hist[-1].get("date"),
            "history_n": len(hist) + 1,
            "d_opportunity": _d("opportunity"),
            "d_demand": _d("demand"),
            "d_supply": _d("supply"),
            "d_read": _d("median_read"),
            "d_engagement": _d("median_engagement_bps"),
            "d_articles": _d("sample_count"),
        }
    return rec


def save_snapshot(path, snap, seed, rec):
    """把本次记录追加进快照并落盘，超出保留上限的旧记录丢弃。"""
    hist = [h for h in (snap.get(seed) or []) if isinstance(h, dict)]
    hist.append(rec)
    snap[seed] = hist[-SNAPSHOT_KEEP:]
    try:
        d = os.path.dirname(os.path.abspath(path))
        if d:
            os.makedirs(d, exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            json.dump(snap, f, ensure_ascii=False, indent=1)
        return True
    except OSError as e:
        print(f"      ! 快照写入失败：{e}", file=sys.stderr)
        return False


def trend_text(s):
    """趋势展示文案。返回 (文案, 样式类)；无趋势数据时返回 (None, None)。"""
    t = s.get("trend")
    if not t:
        return None, None
    if t.get("is_new"):
        n = t.get("history_n", 1)
        if n <= 1:
            return "首次扫描，暂无趋势基准", "tr-new"
        return f"新出现的词（已扫描 {n} 次）", "tr-new"
    # 只列真正发生变化的维度，避免出现「机会分 +0.0」这种噪音
    parts = []
    d = t.get("d_opportunity")
    if isinstance(d, (int, float)) and abs(d) >= 0.05:
        parts.append(f"机会分 {d:+.1f}")
    dr = t.get("d_read")
    if isinstance(dr, (int, float)) and abs(dr) >= 1:
        parts.append(f"阅读 {int(dr):+d}")
    da = t.get("d_articles")
    if isinstance(da, (int, float)) and abs(da) >= 1:
        parts.append(f"样本 {int(da):+d}")
    if not parts:
        return f"较 {t.get('prev_date', '上次')} 无变化", "tr-flat"
    cls = "tr-up" if (d or 0) > 0 else ("tr-down" if (d or 0) < 0 else "tr-flat")
    return f"较 {t.get('prev_date', '上次')}：{' · '.join(parts)}", cls


def trend_html(s):
    txt, cls = trend_text(s)
    if not txt:
        return ""
    return f'<div class="ev {cls}">{esc(txt)}</div>'


def _as_list(v):
    """把 AI 洞察里的字段统一成列表：字符串按换行或分号切，列表原样过。"""
    if not v:
        return []
    if isinstance(v, str):
        return [x.strip(" 　·-") for x in re.split(r"[\n；;]+", v) if x.strip(" 　·-")]
    return [str(x).strip() for x in v if str(x).strip()]


def build_matrix_svg(words, colors, qlabel):
    """
    机会矩阵散点图，生成为内联 SVG。

    刻意不用 Chart.js：报告是本地文件，一旦依赖 CDN，离线打开、预览面板的 CSP、
    或一处 JS 报错都会让整张图变成空白，而且失败时没有兜底。
    SVG 是静态产物，渲染不依赖脚本，导出 PDF、打印、转发都不会掉内容。
    """
    W, H = 1000, 500
    ml, mr, mt, mb = 62, 28, 24, 56
    pw, ph = W - ml - mr, H - mt - mb

    def sx(v):
        return ml + (max(0.0, min(100.0, float(v))) / 100.0) * pw

    def sy(v):
        return mt + (1 - max(0.0, min(100.0, float(v))) / 100.0) * ph

    md = median([s["demand"] for s in words]) or 50.0
    ms = median([s["supply"] for s in words]) or 50.0

    parts = [f'<svg viewBox="0 0 {W} {H}" width="100%" height="auto" role="img" '
             f'xmlns="http://www.w3.org/2000/svg" style="display:block;max-width:100%;">'
             f'<title>候选词机会矩阵</title>'
             f'<desc>横轴竞争度、纵轴需求热度，气泡大小代表有效样本数，'
             f'虚线为需求与竞争的中位数分界，共 {len(words)} 个候选词。</desc>']

    # 象限底色：蓝海（高需求低竞争）在左上，冷淡区（低需求低竞争）在左下
    quad_rects = [
        (ml, mt, sx(ms) - ml, sy(md) - mt, "blue"),            # 左上：需求高 竞争低
        (sx(ms), mt, ml + pw - sx(ms), sy(md) - mt, "amber"),  # 右上：需求高 竞争高
        (ml, sy(md), sx(ms) - ml, mt + ph - sy(md), "gray"),   # 左下：需求低 竞争低
        (sx(ms), sy(md), ml + pw - sx(ms), mt + ph - sy(md), "red"),  # 右下
    ]
    for x0, y0, w0, h0, q in quad_rects:
        if w0 > 0 and h0 > 0:
            parts.append(f'<rect x="{x0:.1f}" y="{y0:.1f}" width="{w0:.1f}" '
                         f'height="{h0:.1f}" fill="{colors[q]}" fill-opacity="0.05"/>')

    # 网格与刻度
    for v in (0, 25, 50, 75, 100):
        gy = sy(v)
        parts.append(f'<line x1="{ml}" y1="{gy:.1f}" x2="{ml + pw}" y2="{gy:.1f}" '
                     f'stroke="rgba(128,128,128,.18)" stroke-width="1"/>')
        parts.append(f'<text x="{ml - 10}" y="{gy + 4:.1f}" text-anchor="end" '
                     f'font-size="11" fill="#888780">{v}</text>')
        gx = sx(v)
        parts.append(f'<line x1="{gx:.1f}" y1="{mt}" x2="{gx:.1f}" y2="{mt + ph}" '
                     f'stroke="rgba(128,128,128,.18)" stroke-width="1"/>')
        parts.append(f'<text x="{gx:.1f}" y="{mt + ph + 18}" text-anchor="middle" '
                     f'font-size="11" fill="#888780">{v}</text>')

    # 中位数分界（虚线）—— 四象限就是按它切的
    parts.append(f'<line x1="{sx(ms):.1f}" y1="{mt}" x2="{sx(ms):.1f}" y2="{mt + ph}" '
                 f'stroke="#B4B2A9" stroke-width="1" stroke-dasharray="5 4"/>')
    parts.append(f'<line x1="{ml}" y1="{sy(md):.1f}" x2="{ml + pw}" y2="{sy(md):.1f}" '
                 f'stroke="#B4B2A9" stroke-width="1" stroke-dasharray="5 4"/>')

    # 坐标轴标题
    parts.append(f'<text x="{ml + pw / 2:.1f}" y="{H - 12}" text-anchor="middle" '
                 f'font-size="12" fill="#5F5E5A">竞争度 →</text>')
    parts.append(f'<text x="14" y="{mt + ph / 2:.1f}" text-anchor="middle" '
                 f'font-size="12" fill="#5F5E5A" '
                 f'transform="rotate(-90 14 {mt + ph / 2:.1f})">需求热度 →</text>')

    # 气泡：半径随有效样本数变化，与图例说明一致
    placed = []
    for s in words:
        x, y = sx(s["supply"]), sy(s["demand"])
        r = 5 + min(s.get("valid_count") or 0, 10) * 1.1
        c = colors[s["quadrant"]]
        tip = (f'{esc(s["word"])}｜{esc(qlabel[s["quadrant"]])}｜'
               f'需求 {s["demand"]:.0f} / 竞争 {s["supply"]:.0f} / 机会分 '
               f'{s["opportunity"]:+.1f} / 有效样本 {s.get("valid_count", 0)} 篇')
        parts.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r:.1f}" fill="{c}" '
                     f'fill-opacity="0.38" stroke="{c}" stroke-width="1.4">'
                     f'<title>{tip}</title></circle>')
        placed.append((x, y, r, s["word"], c))

    # 标签：右 → 左 → 上 → 下依次尝试，都冲突就放弃（气泡仍可悬浮查看）
    boxes = []
    for x, y, r, label, c in placed:
        tw = len(label) * 11.5 + 4
        for dx, dy, anchor in ((r + 6, 4, "start"), (-r - 6, 4, "end"),
                               (0, -r - 6, "middle"), (0, r + 14, "middle")):
            lx, ly = x + dx, y + dy
            x0 = lx - tw if anchor == "end" else (lx - tw / 2 if anchor == "middle" else lx)
            box = (x0, ly - 11, tw, 14)
            if all(not (box[0] < b[0] + b[2] and b[0] < box[0] + box[2]
                        and box[1] < b[1] + b[3] and b[1] < box[1] + box[3])
                   for b in boxes):
                boxes.append(box)
                parts.append(f'<text x="{lx:.1f}" y="{ly:.1f}" text-anchor="{anchor}" '
                             f'font-size="11.5" fill="{c}">{esc(label)}</text>')
                break

    parts.append("</svg>")
    return "".join(parts)


def pick_angle(stats):
    """按互动结构给出切入角度建议（本地启发式，基于契约的 ratesBps 子项）。"""
    share = 0.0
    collect = 0.0
    like = 0.0
    n = 0
    for a in stats["articles"]:
        m = a.get("metrics")
        if not m:
            continue
        n += 1
        r = m.get("rates") or {}
        share += r.get("share") or 0
        collect += r.get("collect") or 0
        like += (r.get("like") or 0) + (r.get("oldLike") or 0)
    if n == 0:
        return "样本不足，无法判断"
    parts = {"share": share, "collect": collect, "like": like}
    total = sum(parts.values())
    if total <= 0:
        return "互动结构均衡，可自由选题"
    top = max(parts, key=parts.get)
    if top == "share":
        return "分享率领先 → 自带转发属性，适合清单 / 观点 / 避坑类"
    if top == "collect":
        return "收藏率领先 → 读者倾向留存，适合攻略 / 资料 / 步骤类"
    return "点赞率领先 → 情绪共鸣强，适合故事 / 经历 / 态度类"


# --------------------------------------------------------------------------
# 主流程
# --------------------------------------------------------------------------

def collect_candidates(client, seed, expand, extra_words):
    """返回 [(word, rank_score)]。种子词位次记 1.0。"""
    cands = [(seed, 1.0)]
    seen = {seed}
    lvl1 = fetch_suggestions(client, seed)
    for i, w in enumerate(lvl1):
        if w in seen:
            continue
        seen.add(w)
        # 推荐词位次：越靠前分越高
        cands.append((w, max(0.0, 1.0 - i / max(len(lvl1), 1))))
    if expand >= 2:
        freq = Counter()
        def _one(w):
            try:
                return fetch_suggestions(client, w)
            except ApiError:
                return []
        with ThreadPoolExecutor(max_workers=4) as pool:
            for words in pool.map(_one, lvl1):
                for w in words:
                    if w not in seen:
                        freq[w] += 1
        for w, _c in freq.most_common(extra_words):
            seen.add(w)
            cands.append((w, 0.35))
    return cands


def build_dataset(client, seed, args):
    if getattr(args, "seeds", None):
        # 外部已经给好候选词（热点模式转译后的结果），跳过推荐词扩散
        seeds = [s.strip() for s in args.seeds.split(",") if s.strip()]
        cands = [(w, max(0.0, 1.0 - i / max(len(seeds), 1))) for i, w in enumerate(seeds)]
        print(f"[1/4] 使用外部传入的 {len(cands)} 个候选词（跳过推荐词扩散）", flush=True)
    else:
        print(f"[1/4] 扩散候选词：种子词「{seed}」", flush=True)
        cands = collect_candidates(client, seed, args.expand, args.extra_words)
    print(f"      候选词 {len(cands)} 个", flush=True)

    print(f"[2/4] 抓取每个词的搜一搜结果（每词最多 {args.per_word} 篇）", flush=True)
    def _search(item):
        word, rank = item
        try:
            arts = fetch_search(client, word, sort=args.sort,
                                limit=min(args.per_word, 50),
                                publish_time=args.publish_time)
        except ApiError as e:
            print(f"      ! 「{word}」搜索失败：{e}", file=sys.stderr)
            arts = []
        return word, rank, arts

    word_articles = []
    with ThreadPoolExecutor(max_workers=4) as pool:
        for word, rank, arts in pool.map(_search, cands):
            word_articles.append((word, rank, arts[:args.per_word]))
    total_arts = sum(len(a) for _w, _r, a in word_articles)
    print(f"      命中文章 {total_arts} 篇", flush=True)

    print("[3/4] 批量取文章公开互动数据", flush=True)
    targets = [(wi, ai, art) for wi, (_w, _r, arts) in enumerate(word_articles)
               for ai, art in enumerate(arts)]
    def _metrics(t):
        wi, ai, art = t
        return wi, ai, fetch_metrics(client, art["doc_url"])
    done = 0
    with ThreadPoolExecutor(max_workers=4) as pool:
        for wi, ai, m in pool.map(_metrics, targets):
            word_articles[wi][2][ai]["metrics"] = m
            done += 1
            if done % 20 == 0:
                print(f"      已取 {done}/{len(targets)}", flush=True)
    ok = sum(1 for _w, _r, arts in word_articles for a in arts
             if a.get("metrics") and a["metrics"].get("read_num") is not None)
    print(f"      有效互动样本 {ok} 篇", flush=True)

    print("[4/4] 计算机会分", flush=True)
    scored = apply_scoring([compute_stats(w, r, arts)
                            for w, r, arts in word_articles if arts])
    scored.sort(key=lambda s: (-s.get("trusted", s["opportunity"]), -s["demand"]))

    md, ms = median([s["demand"] for s in scored]), median([s["supply"] for s in scored])
    for s in scored:
        s["quadrant"] = quadrant(s, md, ms)

    if args.deep > 0:
        top = scored[:DEEP_TOP_WORDS]
        print(f"      对 Top {len(top)} 蓝海词各采样 {args.deep} 篇内容规格", flush=True)
        for s in top:
            # 取该词下阅读最高的若干篇作为采样对象（阅读最高的篇最能代表"爆款长什么样"）
            ranked = [a for a in s["articles"]
                      if a.get("metrics")
                      and isinstance(a["metrics"].get("read_num"), (int, float))
                      and not a["metrics"].get("read_capped")]
            if not ranked:
                ranked = s["articles"]
            ranked = sorted(ranked, key=lambda a: (a["metrics"] or {}).get("read_num") or 0,
                            reverse=True)[:args.deep]
            results = [fetch_content_analysis(client, a["doc_url"]) for a in ranked]
            results = [r for r in results if r]
            if results:
                # 多篇取中位数，避免单篇偶然性（实测单篇跨度可达 1462~3266 字）
                s["deep"] = {
                    "character_count": median([r["character_count"] for r in results]),
                    "paragraph_count": median([r["paragraph_count"] for r in results]),
                    "estimated_read_minutes": median([r["estimated_read_minutes"] for r in results]),
                    "image_count": median([r["image_count"] for r in results]),
                    "sample_size": len(results),
                }
    return {
        "seed": seed,
        "cost": {"total": client.ledger.total, "balance": client.ledger.balance,
                 "calls": client.ledger.calls},
        "generated_at": datetime.now(timezone.utc).astimezone().strftime("%Y-%m-%d %H:%M"),
        "params": {
            "sort": args.sort, "publish_time": args.publish_time,
            "per_word": args.per_word, "expand": args.expand,
        },
        "words": scored,
        "median_demand": md, "median_supply": ms,
        "total_articles": total_arts,
    }


def quadrant(s, md, ms):
    hi_d = s["demand"] >= (md if md is not None else 0)
    hi_s = s["supply"] >= (ms if ms is not None else 0)
    if hi_d and not hi_s:
        return "blue"      # 高需求低竞争 —— 蓝海
    if hi_d and hi_s:
        return "amber"     # 高需求高竞争 —— 主战场
    if not hi_d and hi_s:
        return "red"       # 低需求高竞争 —— 红海
    return "gray"          # 低需求低竞争 —— 冷淡区


# --------------------------------------------------------------------------
# 模式 C：账号驱动（接口 4 历史文章 + 接口 1 互动数据 + 本地主题聚类）
# --------------------------------------------------------------------------

def cross_gaps(packs):
    """找出「某个号在高频做、其他号完全没碰过」的主题，即内容缺口。"""
    if len(packs) < 2:
        return []
    gaps = []
    for i, p in enumerate(packs):
        others = [q for j, q in enumerate(packs) if j != i]
        for t in p["topics"][:10]:
            missing = []
            for q in others:
                hit = any(t["topic"] in (x.get("title") or "") for x in q["articles"])
                if not hit:
                    missing.append(q["name"])
            if missing:
                gaps.append({"topic": t["topic"], "count": t["count"],
                             "docs": t["docs"], "owner": p["name"],
                             "missing_in": missing})
    gaps.sort(key=lambda g: (-g["docs"], -g["count"]))
    return gaps[:15]


def build_account_dataset(client, accounts, args):
    print(f"[1/3] 抓取 {len(accounts)} 个账号的历史文章", flush=True)
    packs = []
    for idx, spec in enumerate(accounts, 1):
        alias, acc = parse_account(spec)
        try:
            info, arts = fetch_account_articles(client, acc, pages=args.pages, limit=20)
        except ApiError as e:
            print(f"      ! 抓取失败：{e}", file=sys.stderr)
            continue
        arts = arts[:args.max_articles]
        name = alias or (info.get("accountName") or "").strip() or f"账号 {idx}"
        print(f"      {name}：{len(arts)} 篇", flush=True)
        packs.append({"account": info, "input": acc, "name": name, "articles": arts})
    if not packs:
        return None

    print("[2/3] 批量取互动数据", flush=True)
    for p in packs:
        arts = p["articles"]
        with ThreadPoolExecutor(max_workers=4) as pool:
            for a, m in zip(arts, pool.map(lambda x: fetch_metrics(client, x["url"]), arts)):
                a["metrics"] = m
        print(f"      {p['name']}：已取 {len(arts)} 篇", flush=True)

    print("[3/3] 主题聚类与缺口比对", flush=True)
    for p in packs:
        valid = [a for a in p["articles"]
                 if a.get("metrics") and isinstance(a["metrics"].get("read_num"), (int, float))]
        reads = [a["metrics"]["read_num"] for a in valid]
        engs = [_get(a["metrics"], "rates", "engagement") for a in valid]
        p["valid_count"] = len(valid)
        p["median_read"] = median(reads)
        p["median_engagement_bps"] = median([e for e in engs if isinstance(e, (int, float))])
        p["topics"] = extract_topics([a["title"] for a in p["articles"]], top_n=args.topics)
        p["top_articles"] = sorted(valid, key=lambda a: -(a["metrics"].get("read_num") or 0))[:6]
    return {
        "mode": "account",
        "accounts": packs,
        "gaps": cross_gaps(packs),
        "cost": {"total": client.ledger.total, "balance": client.ledger.balance,
                 "calls": client.ledger.calls},
        "generated_at": datetime.now(timezone.utc).astimezone().strftime("%Y-%m-%d %H:%M"),
        "params": {"pages": args.pages, "max_articles": args.max_articles, "topics": args.topics},
        "total_articles": sum(len(p["articles"]) for p in packs),
    }


ACCOUNT_EXTRA_CSS = """
.acct{background:#fff;border:1px solid rgba(0,0,0,.07);border-radius:12px;padding:16px 18px}
.acct-h{display:flex;justify-content:space-between;align-items:baseline;gap:10px}
.acct-n{font-size:15px;font-weight:600}
.acct-s{font-size:12px;color:#5F5E5A;white-space:nowrap}
.acct-m{font-size:12px;color:#5F5E5A;margin:6px 0 10px}
.acct-m b{font-weight:500;color:#2C2C2A}
.tags{display:flex;flex-wrap:wrap;gap:6px;margin-bottom:12px}
.tag{background:#EEEDFE;color:#3C3489;border-radius:6px;padding:3px 8px;font-size:12px}
.tag i{font-style:normal;color:#7F77DD;margin-left:4px;font-size:11px}
"""


def build_account_html(ds, ledger, md_text, summary=None):
    css = CSS + ACCOUNT_EXTRA_CSS      # CSS 定义在本文件后段，此处拼接避免模块级依赖顺序问题
    js = JS_COPY + ACCOUNT_EXTRA_JS
    packs = ds["accounts"]
    cards = ""
    for p in packs:
        tags = "".join(f'<span class="tag">{esc(t["topic"])}<i>{t["docs"]}</i></span>'
                       for t in p["topics"]) or '<span class="meta">主题样本不足</span>'
        tops = ""
        for a in p.get("top_articles") or []:
            m = a["metrics"]
            tops += (f'<li><a href="{esc(m.get("url") or a["url"])}" target="_blank" rel="noopener">'
                     f'{esc(a["title"] or "（无标题）")}</a>'
                     f'<div class="meta">阅读 {esc(fmt_num(m.get("read_num")))}'
                     f' · 互动 {esc(fmt_num(m.get("interaction_num")))}'
                     f' · {esc(iso_date(a.get("publish_timestamp")) or "时间未知")}</div></li>')
        tops = tops or '<li class="meta">未取到有效互动样本</li>'
        cards += f"""<div class="acct">
  <div class="acct-h"><div class="acct-n">{esc(p['name'])}</div>
    <div class="acct-s">{p['valid_count']}/{len(p['articles'])} 篇有效</div></div>
  <div class="acct-m">阅读中位数 <b>{esc(fmt_num(p.get('median_read')))}</b>
    　互动率 <b>{esc(fmt_num(p.get('median_engagement_bps')))}</b> bps</div>
  <div class="tags">{tags}</div>
  <ul class="refs">{tops}</ul>
</div>"""

    hero = (f'<div class="hero"><div class="k">AI 结论</div>'
            f'<div class="v">{esc(summary["headline"])}</div></div>'
            if summary and summary.get("headline") else "")
    insight = (f'<h2>怎么读这份版图</h2><div class="panel insight">{md_paras(summary["verdict"])}</div>'
               if summary and summary.get("verdict") else "")
    # 推进顺序放在缺口表之后：先看到空位在哪，再谈先补哪个
    seq = (f'<h2>推进顺序</h2><div class="panel insight">{md_paras(summary["sequence"])}</div>'
           if summary and summary.get("sequence") else "")

    gaps = ""
    if ds.get("gaps"):
        rows = "".join(
            f'<tr><td data-v="{esc(g["topic"])}"><b>{esc(g["topic"])}</b></td>'
            f'<td data-v="{esc(g["owner"])}">{esc(g["owner"])}</td>'
            f'<td class="n" data-v="{g["docs"]}">{g["docs"]}</td>'
            f'<td data-v="{esc("、".join(g["missing_in"]))}">'
            f'{esc("、".join(g["missing_in"]))}</td></tr>' for g in ds["gaps"])
        gaps = f"""<h2>内容缺口</h2>
<div class="panel"><p class="sub" style="margin:0 0 12px">
下面是「某个号在高频做、其他号完全没碰过」的主题，按覆盖篇数排序。
这些就是最直接可补的空位。</p>
<table><thead><tr><th onclick="sortTable(0)">主题</th>
<th onclick="sortTable(1)">谁在做</th>
<th class="n" onclick="sortTable(2)">覆盖篇数</th>
<th onclick="sortTable(3)">谁没做</th></tr></thead>
<tbody id="alltb">{rows}</tbody></table></div>{seq}"""

    return f"""<!DOCTYPE html>
<html lang="zh-CN"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>内容版图 · {len(packs)} 个账号</title>
<style>{css}</style></head><body><div class="wrap">
<h1>内容版图 · {len(packs)} 个账号</h1>
<p class="sub">{esc(ds['generated_at'])} · 每号最多 {ds['params']['max_articles']} 篇
 · 每号主题标签 {ds['params']['topics']} 个</p>
{hero}
<div class="cards">
  <div class="card"><div class="k">账号</div><div class="v">{len(packs)}</div></div>
  <div class="card"><div class="k">文章</div><div class="v">{ds['total_articles']}</div></div>
  <div class="card"><div class="k">发现缺口</div><div class="v">{len(ds.get('gaps') or [])}</div></div>
  <div class="card"><div class="k">本次消费</div><div class="v">¥{ledger.total:.4f}</div></div>
  <div class="card"><div class="k">账户余额</div><div class="v">¥{ledger.balance if ledger.balance is not None else '—'}</div></div>
</div>
{insight}
<h2>各账号内容版图</h2>
<div class="grid">{cards}</div>
{gaps}
<h2>选题清单</h2>
<div class="panel">
  <button class="btn" id="copybtn" onclick="copyMd()">复制清单 (Markdown)</button>
  <pre id="mdraw" style="display:none">{esc(md_text)}</pre>
</div>
<h2>方法与说明</h2>
<div class="note">
主题标签由标题的 2–4 字 n-gram 统计得出（本地朴素做法，未使用分词库），
标签后的数字是覆盖的文章篇数，数字越大说明这个主题在该号越稳定。<br>
「内容缺口」判定为字符串包含匹配，属于粗筛，可能存在包含关系造成的误判，
建议结合标签与文章标题人工确认。<br>
互动率取样本中位数的整数基点（互动/阅读×10000）；阅读被展示上限截断的样本不参与中位数计算。<br>
数据采集自公众号公开历史文章与文章公开互动数据，主题聚类为本地启发式结果，非平台官方分类。
</div>
</div>
<script>{js}</script></body></html>"""


ACCOUNT_EXTRA_JS = """
function sortTable(n){
  var tb=document.getElementById('alltb'),rows=[].slice.call(tb.rows);
  var asc=tb.getAttribute('data-asc')!=='1';
  rows.sort(function(a,b){
    var x=a.cells[n].getAttribute('data-v'),y=b.cells[n].getAttribute('data-v');
    var fx=parseFloat(x),fy=parseFloat(y);
    if(!isNaN(fx)&&!isNaN(fy))return asc?fx-fy:fy-fx;
    return asc?String(x).localeCompare(String(y),'zh'):String(y).localeCompare(String(x),'zh');
  });
  rows.forEach(function(r){tb.appendChild(r)});
  tb.setAttribute('data-asc',asc?'1':'0');
}
"""


def build_account_markdown(ds, ledger, summary=None):
    lines = [f"# 内容版图 · {len(ds['accounts'])} 个账号", "",
             f"- 生成时间：{ds['generated_at']}",
             f"- 文章总数：{ds['total_articles']} 篇",
             f"- 本次消费：¥{ledger.total:.4f}"
             f"｜余额：¥{ledger.balance if ledger.balance is not None else '—'}", ""]
    if summary:
        if summary.get("headline"):
            lines += [f"> **{summary['headline']}**", ""]
        if summary.get("verdict"):
            lines += [summary["verdict"], ""]
    for p in ds["accounts"]:
        lines += [f"## {p['name']}", "",
                  f"- 文章 {len(p['articles'])} 篇（有效 {p['valid_count']} 篇）"
                  f"｜阅读中位数 {fmt_num(p.get('median_read'))}"
                  f"｜互动率中位数 {fmt_num(p.get('median_engagement_bps'))} bps",
                  "- 高频主题：" + ("、".join(
                      f"{t['topic']}({t['docs']})" for t in p["topics"]) or "样本不足"),
                  "", "表现最好的文章："]
        for a in (p.get("top_articles") or [])[:5]:
            m = a["metrics"]
            lines.append(f"- [{a['title'] or '（无标题）'}]({m.get('url') or a['url']})"
                         f"｜阅读 {fmt_num(m.get('read_num'))}"
                         f"｜互动 {fmt_num(m.get('interaction_num'))}")
        lines.append("")
    if ds.get("gaps"):
        lines += ["## 内容缺口", "",
                  "| 主题 | 谁在做 | 覆盖篇数 | 谁没做 |", "| --- | --- | --- | --- |"]
        for g in ds["gaps"]:
            lines.append(f"| {g['topic']} | {g['owner']} | {g['docs']} "
                         f"| {'、'.join(g['missing_in'])} |")
        lines.append("")
    return "\n".join(lines)


# --------------------------------------------------------------------------
# 输出：Markdown
# --------------------------------------------------------------------------

def build_markdown(ds, ledger, summary=None):
    lines = [
        f"# 选题雷达 · {ds['seed']}",
        "",
        f"- 生成时间：{ds['generated_at']}",
        f"- 候选词：{len(ds['words'])} 个｜扫描文章：{ds['total_articles']} 篇",
        f"- 本次消费：¥{ledger.total:.4f}｜余额：¥{ledger.balance if ledger.balance is not None else '—'}",
        "",
    ]
    if summary:
        if summary.get("headline"):
            lines += [f"> **{summary['headline']}**", ""]
        if summary.get("verdict"):
            lines += [summary["verdict"], ""]
        for p in (summary.get("picks") or []):
            lines += [f"### {p.get('word', '')}" + (f"（{p['tag']}）" if p.get("tag") else ""), ""]
            if p.get("why"):
                lines += [f"- 为什么：{p['why']}", ""]
            if p.get("action"):
                lines += [f"- 怎么做：{p['action']}", ""]
            titles = p.get("titles") or []
            if titles:
                lines += ["- 标题参考："] + [f"  {i}. {t}" for i, t in enumerate(titles, 1)] + [""]
        if summary.get("avoid"):
            lines += ["## 别碰这些", ""]
            for a in summary["avoid"]:
                lines.append(f"- **{a.get('word', '')}**：{a.get('reason', '')}")
            lines.append("")
        if summary.get("sequence"):
            lines += ["## 推进顺序", "", summary["sequence"], ""]
        lines += ["---", ""]
    lines += [
        "## 蓝海选题 Top 10",
        "",
        "| # | 选题词 | 机会分 | 可信分 | 证据 | 需求 | 竞争 | 头部阅读中位数 | 建议切入角度 |",
        "| --- | --- | --- | --- | --- | --- | --- | --- | --- |",
    ]
    for i, s in enumerate(ds["words"][:10], 1):
        ev, _lv = evidence_text(s)
        lines.append(
            f"| {i} | {s['word']} | {s['opportunity']:+.1f} | "
            f"{s.get('trusted', s['opportunity']):+.1f} | {ev} | {s['demand']:.0f} | "
            f"{s['supply']:.0f} | {fmt_num(s['median_read'])} | {pick_angle(s)} |")
    lines += ["", "## 参考爆文", ""]
    for s in ds["words"][:10]:
        arts = [a for a in s["articles"] if a.get("metrics")][:3]
        if not arts:
            continue
        lines.append(f"### {s['word']}")
        for a in arts:
            m = a["metrics"]
            read = f"{fmt_num(m['read_num'])}{'+' if m['read_capped'] else ''}" \
                if m.get("read_num") is not None else (a.get("display_read") or "—")
            lines.append(f"- [{a['title'] or '（无标题）'}]({m.get('url') or a['doc_url']})"
                         f"｜{a.get('account') or '—'}｜阅读 {read}｜互动 {fmt_num(m.get('interaction_num'))}")
        lines.append("")
    lines += [
        "---",
        "",
        "机会分 = 需求热度 − 竞争度，为本地启发式评分，非平台官方指标，仅用于排序参考。",
        "机会分只反映样本呈现出的形态，不反映形态的可信程度——同样的阅读量与互动率下，"
        "2 篇和 12 篇样本会算出完全一样的机会分。",
        "因此另列「可信分」= 机会分 ×（0.45 + 0.55 × 有效样本数/6），默认按可信分排序；"
        "证据等级为「低」（<3 篇）的词请先补样本再下结论。",
        "数据来源：微信搜一搜公开结果与文章公开互动数据。阅读被微信展示上限截断的样本不参与均值计算。",
    ]
    return "\n".join(lines)


# --------------------------------------------------------------------------
# 输出：HTML
# --------------------------------------------------------------------------

CSS = """
*{box-sizing:border-box}
body{margin:0;padding:32px 20px 60px;background:#F7F6F3;color:#2C2C2A;
 font-family:-apple-system,BlinkMacSystemFont,"PingFang SC","Microsoft YaHei",system-ui,sans-serif;
 font-size:14px;line-height:1.65}
.wrap{max-width:1120px;margin:0 auto}
h1{font-size:24px;font-weight:600;margin:0 0 6px}
h2{font-size:17px;font-weight:600;margin:36px 0 14px}
.sub{color:#5F5E5A;font-size:13px;margin:0 0 22px}
.cards{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:12px;margin-bottom:8px}
.card{background:#fff;border:1px solid rgba(0,0,0,.07);border-radius:10px;padding:14px 16px}
.card .k{font-size:12px;color:#5F5E5A;margin-bottom:4px}
.card .v{font-size:22px;font-weight:600;line-height:1.2}
.panel{background:#fff;border:1px solid rgba(0,0,0,.07);border-radius:12px;padding:18px 20px}
.chartbox{width:100%}
.chartbox svg{height:auto}
.legend{display:flex;flex-wrap:wrap;gap:16px;font-size:12px;color:#5F5E5A;margin:0 0 12px 18px}
.legend span{display:flex;align-items:center;gap:5px}
.dot{width:10px;height:10px;border-radius:50%;display:inline-block}
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(330px,1fr));gap:14px}
.topic{background:#fff;border:1px solid rgba(0,0,0,.07);border-radius:12px;padding:16px 18px;
 border-left:4px solid #639922}
.topic.amber{border-left-color:#EF9F27}
.topic.red{border-left-color:#E24B4A}
.topic.gray{border-left-color:#B4B2A9}
.topic .head{display:flex;justify-content:space-between;align-items:flex-start;gap:10px}
.topic .word{font-size:16px;font-weight:600}
.topic .score{font-size:20px;font-weight:600;color:#0F6E56;white-space:nowrap}
.topic.amber .score{color:#854F0B}
.topic.red .score{color:#A32D2D}
.topic.gray .score{color:#5F5E5A}
.bars{display:flex;gap:14px;font-size:12px;color:#5F5E5A;margin:8px 0 12px}
.bar{flex:1}
.bar .track{height:5px;background:#F1EFE8;border-radius:3px;margin-top:4px;overflow:hidden}
.bar .fill{height:100%;border-radius:3px}
.f-d{background:#378ADD}.f-s{background:#EF9F27}
.angle{background:#F1EFE8;border-radius:6px;padding:8px 10px;font-size:12px;color:#444441;margin-bottom:12px}
.refs{list-style:none;padding:0;margin:0;font-size:13px}
.refs li{padding:7px 0;border-top:1px solid rgba(0,0,0,.06)}
.refs li:first-child{border-top:none}
.refs a{color:#185FA5;text-decoration:none}
.refs a:hover{text-decoration:underline}
.meta{color:#5F5E5A;font-size:12px;margin-top:5px}
table{width:100%;border-collapse:collapse;font-size:13px}
th,td{padding:9px 10px;text-align:left;border-bottom:1px solid rgba(0,0,0,.06)}
th{cursor:pointer;color:#5F5E5A;font-weight:500;font-size:12px;white-space:nowrap;user-select:none}
th:hover{color:#2C2C2A}
td.n{text-align:right;font-variant-numeric:tabular-nums}
.btn{background:#fff;border:1px solid rgba(0,0,0,.18);border-radius:8px;padding:8px 14px;
 font-size:13px;cursor:pointer;font-family:inherit;color:#2C2C2A}
.btn:hover{background:#F1EFE8}
.note{background:#fff;border:1px solid rgba(0,0,0,.07);border-radius:12px;padding:16px 20px;
 font-size:12px;color:#5F5E5A;line-height:1.8}
.badge{display:inline-block;font-size:11px;padding:1px 7px;border-radius:20px;
 background:#F1EFE8;color:#5F5E5A;margin-left:6px}
.ev{font-size:11px;color:#5F5E5A;margin:-2px 0 9px}
.ev-hi{color:#3B6D11}
.ev-mid{color:#854F0B}
.ev-lo{color:#A32D2D}
.tr-new{color:#185FA5}
.tr-up,.tr-down,.tr-flat{color:#5F5E5A}
.hero{background:#EEEDFE;border:1px solid #CECBF6;border-radius:12px;padding:18px 22px;margin-bottom:20px}
.hero .k{font-size:12px;color:#534AB7;margin-bottom:6px;letter-spacing:.06em}
.hero .v{font-size:18px;font-weight:600;color:#26215C;line-height:1.55}
.insight{font-size:13.5px;line-height:1.9;color:#444441}
.insight p{margin:0 0 10px}
.insight p:last-child{margin:0}
.advice{background:#E1F5EE;border:1px solid #9FE1CB;border-radius:8px;padding:11px 13px;
 margin:0 0 12px;font-size:12.5px;line-height:1.75;color:#085041}
.advice b{font-weight:500;color:#0F6E56}
.advice ol{margin:6px 0 0;padding-left:18px}
.advice li{margin-bottom:3px}
.advice ol.ol{margin-top:9px;border-top:1px dashed #9FE1CB;padding-top:9px}
.warn{background:#FCEBEB;border:1px solid #F7C1C1;border-radius:8px;padding:10px 13px;
 margin-bottom:10px;font-size:13px;line-height:1.7;color:#791F1F}
.warn:last-child{margin-bottom:0}
.warn b{font-weight:500;color:#A32D2D}
"""

JS_COPY = """
function copyMd(){
  var t=document.getElementById('mdraw').textContent;
  navigator.clipboard.writeText(t).then(function(){
    var b=document.getElementById('copybtn');b.textContent='已复制';
    setTimeout(function(){b.textContent='复制选题清单 (Markdown)';},1800);
  });
}
function sortTable(n){
  var tb=document.getElementById('alltb'),rows=[].slice.call(tb.rows);
  var asc=tb.getAttribute('data-asc')!=='1';
  rows.sort(function(a,b){
    var x=a.cells[n].getAttribute('data-v'),y=b.cells[n].getAttribute('data-v');
    var fx=parseFloat(x),fy=parseFloat(y);
    if(!isNaN(fx)&&!isNaN(fy))return asc?fx-fy:fy-fx;
    return asc?String(x).localeCompare(String(y),'zh'):String(y).localeCompare(String(x),'zh');
  });
  rows.forEach(function(r){tb.appendChild(r)});
  tb.setAttribute('data-asc',asc?'1':'0');
}
"""


def build_html(ds, ledger, md_text, summary=None):
    words = ds["words"]
    top = words[:10]
    pick_map = {p.get("word"): p for p in ((summary or {}).get("picks") or [])}

    def paras(text):
        # 先转义再还原 **加粗**，避免 esc 把标签吃掉
        out = []
        for p in str(text or "").split("\n\n"):
            p = p.strip()
            if not p:
                continue
            p = esc(p)
            p = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", p)
            out.append(f"<p>{p}</p>")
        return "".join(out)

    hero = (f'<div class="hero"><div class="k">AI 结论</div>'
            f'<div class="v">{esc(summary["headline"])}</div></div>'
            if summary and summary.get("headline") else "")
    insight = (f'<h2>怎么读这张图</h2><div class="panel insight">{paras(summary["verdict"])}</div>'
               if summary and summary.get("verdict") else "")
    avoid = ""
    if summary and summary.get("avoid"):
        items = "".join(f'<div class="warn"><b>{esc(a.get("word", ""))}</b>　'
                        f'{esc(a.get("reason", ""))}</div>' for a in summary["avoid"])
        avoid = f'<h2>别碰这些</h2><div class="panel">{items}</div>'
    seq = (f'<h2>推进顺序</h2><div class="panel insight">{paras(summary["sequence"])}</div>'
           if summary and summary.get("sequence") else "")
    colors = {"blue": "#639922", "amber": "#EF9F27", "red": "#E24B4A", "gray": "#888780"}
    qlabel = {"blue": "蓝海 · 高需求低竞争", "amber": "主战场 · 高需求高竞争",
              "red": "红海 · 低需求高竞争", "gray": "冷淡区 · 低需求低竞争"}

    matrix = build_matrix_svg(words, colors, qlabel) if words else ""

    cards = ""
    for i, s in enumerate(top, 1):
        refs = ""
        for a in [x for x in s["articles"] if x.get("metrics")][:3]:
            m = a["metrics"]
            if m.get("read_num") is None:
                read = (a.get("display_read") or "—") + ("（展示值）" if a.get("display_read") else "")
            else:
                read = fmt_num(m["read_num"]) + ("+" if m["read_capped"] else "")
            refs += (f'<li><a href="{esc(m.get("url") or a["doc_url"])}" target="_blank" '
                     f'rel="noopener">{esc(a["title"] or "（无标题）")}</a>'
                     f'<div class="meta">{esc(a.get("account") or "未标注公众号")}'
                     f' · 阅读 {esc(read)} · 互动 {esc(fmt_num(m.get("interaction_num")))}'
                     f' · {esc(iso_date(a.get("timestamp")) or "时间未知")}</div></li>')
        if not refs:
            refs = '<li class="meta">该词下未取到有效文章样本</li>'

        deep = ""
        if s.get("deep"):
            d = s["deep"]
            parts = []
            if d.get("character_count"):
                parts.append(f"约 {fmt_num(d['character_count'])} 字")
            if d.get("paragraph_count"):
                parts.append(f"{fmt_num(d['paragraph_count'])} 段")
            if d.get("image_count"):
                parts.append(f"{fmt_num(d['image_count'])} 图")
            if d.get("estimated_read_minutes"):
                parts.append(f"读完约 {d['estimated_read_minutes']} 分钟")
            if parts:
                n = d.get("sample_size") or 1
                src = "中位数" if n > 1 else "单篇"
                deep = (f'<div class="angle">头部样本内容规格（{n} 篇头部文章{src}）：'
                        + esc(" / ".join(parts)) + '</div>')

        advice = ""
        pick = pick_map.get(s["word"])
        if pick:
            bits = []
            if pick.get("why"):
                bits.append(f"<b>机会原因</b>　{esc(pick['why'])}")
            if pick.get("audience"):
                bits.append(f"<b>目标读者</b>　{esc(pick['audience'])}")
            if pick.get("angle"):
                bits.append(f"<b>推荐角度</b>　{esc(pick['angle'])}")
            if pick.get("competition"):
                bits.append(f"<b>竞争程度</b>　{esc(pick['competition'])}")
            # 证据与参考内容取自实际采集结果，不由 AI 生成——避免编造样本量
            bits.append(f"<b>证据充分度</b>　{esc(evidence_text(s)[0])}"
                        f"　参考内容 {s['valid_count']}/{s['sample_count']} 篇")
            if pick.get("action"):
                bits.append(f"<b>具体怎么做</b>　{esc(pick['action'])}")
            titles = _as_list(pick.get("titles"))
            if titles:
                bits.append("<b>建议标题</b><ol class=\"ti\">"
                            + "".join(f"<li>{esc(t)}</li>" for t in titles) + "</ol>")
            outline = _as_list(pick.get("outline"))
            if outline:
                bits.append("<b>内容大纲</b><ol class=\"ol\">"
                            + "".join(f"<li>{esc(t)}</li>" for t in outline) + "</ol>")
            if bits:
                advice = f'<div class="advice">{"<br>".join(bits)}</div>'

        cards += f"""<div class="topic {s['quadrant']}">
  <div class="head"><div class="word">{i}. {esc(s['word'])}
    <span class="badge">{esc(qlabel[s['quadrant']])}</span></div>
    <div class="score">{s['opportunity']:+.1f}</div></div>
  {evidence_html(s)}
  {trend_html(s)}
  <div class="bars">
    <div class="bar">需求热度 {s['demand']:.0f}
      <div class="track"><div class="fill f-d" style="width:{max(2, s['demand']):.0f}%"></div></div></div>
    <div class="bar">竞争度 {s['supply']:.0f}
      <div class="track"><div class="fill f-s" style="width:{max(2, s['supply']):.0f}%"></div></div></div>
  </div>
  <div class="angle">{esc(pick_angle(s))}</div>
  {deep}
  {advice}
  <ul class="refs">{refs}</ul>
</div>"""

    rows = ""
    for i, s in enumerate(words, 1):
        rows += (f'<tr><td data-v="{i}">{i}</td>'
                 f'<td data-v="{esc(s["word"])}">{esc(s["word"])}</td>'
                 f'<td class="n" data-v="{s["opportunity"]}">{s["opportunity"]:+.1f}</td>'
                 f'<td class="n" data-v="{s.get("trusted", s["opportunity"])}">'
                 f'{s.get("trusted", s["opportunity"]):+.1f}</td>'
                 f'<td class="n" data-v="{s["demand"]}">{s["demand"]:.0f}</td>'
                 f'<td class="n" data-v="{s["supply"]}">{s["supply"]:.0f}</td>'
                 f'<td class="n" data-v="{s["median_read"] or 0}">{fmt_num(s["median_read"])}</td>'
                 f'<td class="n" data-v="{s["valid_count"]}">{s["valid_count"]}/{s["sample_count"]}</td>'
                 f'<td data-v="{esc(qlabel[s["quadrant"]])}">{esc(qlabel[s["quadrant"]])}</td></tr>')

    valid_total = sum(s["valid_count"] for s in words)
    capped_total = sum(s["capped_count"] for s in words)
    legend = "".join(
        f'<span><i class="dot" style="background:{colors[k]}"></i>{qlabel[k]}</span>'
        for k in ["blue", "amber", "red", "gray"])

    return f"""<!DOCTYPE html>
<html lang="zh-CN"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>选题雷达 · {esc(ds['seed'])}</title>
<style>{CSS}</style></head><body><div class="wrap">
<h1>选题雷达 · {esc(ds['seed'])}</h1>
<p class="sub">{esc(ds['generated_at'])} · 排序方式 {esc(ds['params']['sort'])}
 · 时间范围 {esc(ds['params']['publish_time'])} · 每词采样 {ds['params']['per_word']} 篇</p>
{hero}
<div class="cards">
  <div class="card"><div class="k">候选词</div><div class="v">{len(words)}</div></div>
  <div class="card"><div class="k">扫描文章</div><div class="v">{ds['total_articles']}</div></div>
  <div class="card"><div class="k">有效互动样本</div><div class="v">{valid_total}</div></div>
  <div class="card"><div class="k">本次消费</div><div class="v">¥{ledger.total:.4f}</div></div>
  <div class="card"><div class="k">账户余额</div><div class="v">¥{ledger.balance if ledger.balance is not None else '—'}</div></div>
</div>

<h2>机会矩阵</h2>
<div class="panel">
  <div class="legend">{legend}<span>气泡大小 = 有效样本数</span></div>
  <div class="chartbox">{matrix}</div>
</div>
{insight}

<h2>蓝海选题 Top {len(top)}</h2>
<div class="grid">{cards}</div>
{avoid}
{seq}

<h2>全量候选词</h2>
<div class="panel"><table><thead><tr>
  <th onclick="sortTable(0)">#</th><th onclick="sortTable(1)">选题词</th>
  <th onclick="sortTable(2)">机会分</th><th onclick="sortTable(3)">可信分</th>
  <th onclick="sortTable(4)">需求</th><th onclick="sortTable(5)">竞争</th>
  <th onclick="sortTable(6)">阅读中位数</th>
  <th onclick="sortTable(7)">有效样本</th><th onclick="sortTable(8)">象限</th>
</tr></thead><tbody id="alltb">{rows}</tbody></table></div>

<h2>选题清单</h2>
<div class="panel">
  <button class="btn" id="copybtn" onclick="copyMd()">复制选题清单 (Markdown)</button>
  <pre id="mdraw" style="display:none">{esc(md_text)}</pre>
</div>

<h2>方法与说明</h2>
<div class="note">
机会分 = 需求热度 − 竞争度，均为本地启发式评分，<b>非平台官方指标</b>，只用于排序参考。<br>
<b>机会分只说明样本呈现出的形态，不说明这个形态有多可信。</b>实测同样的阅读量与互动率下，
2 篇与 12 篇样本会算出完全一样的机会分——因此证据充分度单独呈现：<br>
・证据等级 = 有效样本数 ≥6 篇为「高」、3–5 篇为「中」、&lt;3 篇为「低」；<br>
・可信分 = 机会分 ×（0.45 + 0.55 × 有效样本数/6），<b>默认排序按可信分</b>，
证据不足的词会被往中性压，避免仅凭 2 篇样本的运气占据榜首；<br>
・机会分本身不做修改，保持「需求 − 竞争」的定义纯粹可审计。看到「低」证据的词，
请先补样本再下结论，不要直接采信分数。<br>
需求热度 = 词在搜索联想中的位次 × 0.35 + 样本互动率（互动/阅读基点）中位数对数归一 × 0.40 + 近 {FRESH_DAYS} 天文章占比 × 0.25。<br>
竞争度 = 头部阅读中位数 × 0.50 + 账号集中度 × 0.30 + 阅读≥1万样本占比 × 0.20。<br>
其中阅读中位数采用<b>批内对数相对归一</b>：不同领域阅读水位差异极大（实测同批次可低至 445），
硬编码绝对区间会让多数词被压成 0 而失去区分度；若批内极差不足 2 倍则取中性值，避免把噪声放大成虚假分差。<br>
样本中被微信展示上限截断的阅读数（本次 {capped_total} 篇）只标注不参与均值，避免污染计算；
阅读、互动等字段均取自文章公开数据，展示值（如「6.2万」）与精确整数分列标注。<br>
数据采集自微信搜一搜公开结果与文章公开互动数据，仅反映该词当下的公开检索结果，不代表全平台真实需求量。
</div>
</div>
<script>{JS_COPY}</script></body></html>"""


# --------------------------------------------------------------------------
# 输出：Excel（手写最小 xlsx = zip + XML，保持零第三方依赖）
# --------------------------------------------------------------------------

def _xesc(s):
    return (str(s).replace("&", "&amp;").replace("<", "&lt;")
            .replace(">", "&gt;").replace('"', "&quot;"))


def _col_name(idx):
    """0 -> A，25 -> Z，26 -> AA。"""
    name = ""
    idx += 1
    while idx:
        idx, r = divmod(idx - 1, 26)
        name = chr(65 + r) + name
    return name


def _safe_sheet_name(name, used):
    """xlsx 表名：≤31 字符，且不能含 []:*?/\\"""
    bad = set('[]:*?/\\')
    clean = "".join("_" if ch in bad else ch for ch in str(name))[:31] or "Sheet"
    base, i = clean, 1
    while clean in used:
        suffix = f"_{i}"
        clean = base[:31 - len(suffix)] + suffix
        i += 1
    used.add(clean)
    return clean


_X_STYLES = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
             '<styleSheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main">'
             '<fonts count="2"><font><sz val="11"/><name val="Calibri"/></font>'
             '<font><b/><sz val="11"/><name val="Calibri"/></font></fonts>'
             '<fills count="2"><fill><patternFill patternType="none"/></fill>'
             '<fill><patternFill patternType="gray125"/></fill></fills>'
             '<borders count="1"><border><left/><right/><top/><bottom/><diagonal/></border></borders>'
             '<cellStyleXfs count="1"><xf numFmtId="0" fontId="0" fillId="0" borderId="0"/></cellStyleXfs>'
             '<cellXfs count="2"><xf numFmtId="0" fontId="0" fillId="0" borderId="0" xfId="0"/>'
             '<xf numFmtId="0" fontId="1" fillId="0" borderId="0" xfId="0" applyFont="1"/></cellXfs>'
             '<cellStyles count="1"><cellStyle name="Normal" xfId="0" builtinId="0"/></cellStyles>'
             '<dxfs count="0"/><tableStyles count="0" '
             'defaultTableStyle="TableStyleMedium2" defaultPivotStyle="PivotStyleLight16"/>'
             '</styleSheet>')


def _sheet_xml(rows):
    """rows：二维列表，元素可为 str / int / float / None。首行按表头加粗。"""
    out = ['<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
           '<worksheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main">'
           '<sheetData>']
    for ri, row in enumerate(rows, 1):
        if not row:
            continue
        out.append(f'<row r="{ri}">')
        for ci, v in enumerate(row):
            if v is None or v == "":
                continue
            ref = f"{_col_name(ci)}{ri}"
            style = ' s="1"' if ri == 1 else ""
            if isinstance(v, bool):
                v = "是" if v else "否"
            if isinstance(v, (int, float)) and not isinstance(v, bool):
                out.append(f'<c r="{ref}"{style}><v>{v}</v></c>')
            else:
                out.append(f'<c r="{ref}"{style} t="inlineStr">'
                           f'<is><t xml:space="preserve">{_xesc(v)}</t></is></c>')
        out.append("</row>")
    out.append("</sheetData></worksheet>")
    return "".join(out)


def write_xlsx(path, sheets):
    """
    sheets：[(表名, 二维数据), ...]，写成 xlsx。

    不用 openpyxl 是为了守住「仅依赖标准库」这条底线——一个 skill 不该让使用者
    先装环境才能导出表格。xlsx 本质是 zip 包 + 若干 XML，标准库足够。
    """
    import zipfile
    used = set()
    names = [_safe_sheet_name(n, used) for n, _ in sheets]

    ct = ['<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
          '<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">'
          '<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>'
          '<Default Extension="xml" ContentType="application/xml"/>'
          '<Override PartName="/xl/workbook.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet.main+xml"/>'
          '<Override PartName="/xl/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.styles+xml"/>']
    for i in range(1, len(sheets) + 1):
        ct.append(f'<Override PartName="/xl/worksheets/sheet{i}.xml" '
                  f'ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.worksheet+xml"/>')
    ct.append("</Types>")

    wb = ['<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
          '<workbook xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main" '
          'xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships"><sheets>']
    rels = ['<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
            '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">']
    for i, nm in enumerate(names, 1):
        wb.append(f'<sheet name="{_xesc(nm)}" sheetId="{i}" r:id="rId{i}"/>')
        rels.append(f'<Relationship Id="rId{i}" Type="http://schemas.openxmlformats.org/'
                    f'officeDocument/2006/relationships/worksheet" Target="worksheets/sheet{i}.xml"/>')
    wb.append("</sheets></workbook>")
    rels.append(f'<Relationship Id="rId{len(names) + 1}" Type="http://schemas.openxmlformats.org/'
                f'officeDocument/2006/relationships/styles" Target="styles.xml"/>')
    rels.append("</Relationships>")

    root_rels = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
                 '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
                 '<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/'
                 '2006/relationships/officeDocument" Target="xl/workbook.xml"/></Relationships>')

    d = os.path.dirname(os.path.abspath(path))
    if d:
        os.makedirs(d, exist_ok=True)
    with zipfile.ZipFile(path, "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr("[Content_Types].xml", "".join(ct))
        z.writestr("_rels/.rels", root_rels)
        z.writestr("xl/workbook.xml", "".join(wb))
        z.writestr("xl/_rels/workbook.xml.rels", "".join(rels))
        z.writestr("xl/styles.xml", _X_STYLES)
        for i, (_n, rows) in enumerate(sheets, 1):
            z.writestr(f"xl/worksheets/sheet{i}.xml", _sheet_xml(rows))
    return path


def _cost_sheets_rows(ledger):
    """费用明细。只呈现真实累计值，不按预计调用数反推。"""
    name_of = {v: k for k, v in PATHS.items()}
    rows = [["接口", "调用次数", "消费金额(元)", "占比"]]
    if ledger.by_path:
        for p, rec in sorted(ledger.by_path.items(), key=lambda x: -x[1]["cost"]):
            share = (rec["cost"] / ledger.total * 100) if ledger.total else 0.0
            rows.append([name_of.get(p, p), rec["calls"], round(rec["cost"], 4),
                         f"{share:.1f}%"])
    rows.append([])
    rows.append(["合计调用次数", ledger.calls, round(ledger.total, 4), "100%"])
    rows.append(["账户余额", "", ledger.balance if ledger.balance is not None else "—", ""])
    rows.append([])
    rows.append(["说明", "消费金额取自每次接口响应里的 consumption 字段累加，"
                        "不按预计调用数估算；空结果与失败重试不产生费用。"])
    return rows


def build_keyword_sheets(ds, ledger, summary=None):
    """关键词模式的 Excel 工作表。"""
    words = ds.get("words") or []
    qlabel = {"blue": "蓝海 · 高需求低竞争", "amber": "主战场 · 高需求高竞争",
              "red": "红海 · 低需求高竞争", "gray": "冷淡区 · 低需求低竞争"}

    s1 = [["#", "选题词", "机会分", "可信分", "证据等级", "有效样本", "总样本",
           "象限", "需求热度", "竞争度", "阅读中位数", "互动率(bps)", "切入角度", "趋势"]]
    for i, s in enumerate(words, 1):
        ev, lv = evidence_text(s)
        tr = trend_text(s)[0] or ""
        s1.append([i, s["word"], s["opportunity"], s.get("trusted", s["opportunity"]),
                   lv, s.get("valid_count"), s.get("sample_count"),
                   qlabel.get(s["quadrant"], s["quadrant"]), s["demand"], s["supply"],
                   s.get("median_read"), s.get("median_engagement_bps"),
                   pick_angle(s), tr.replace("较 ", "").replace("：", " ")])

    s2 = [["选题词", "联想位次", "总样本", "有效样本", "截断样本",
           "近90天文章占比", "账号集中度", "阅读≥1万占比", "不同账号数"]]
    for s in words:
        accs = len({a.get("account") for a in s["articles"] if a.get("account")})
        fr = s.get("fresh_ratio")
        s2.append([s["word"], s.get("rank_score"), s.get("sample_count"),
                   s.get("valid_count"), s.get("capped_count"),
                   round(fr, 3) if isinstance(fr, (int, float)) else "",
                   round(s["account_concentration"], 3)
                   if isinstance(s.get("account_concentration"), (int, float)) else "",
                   round(s["big_share"], 3) if isinstance(s.get("big_share"), (int, float)) else "",
                   accs])

    s3 = [["选题词", "文章标题", "公众号", "阅读", "互动", "互动率(bps)",
           "分享率", "收藏率", "点赞率", "发布时间", "链接"]]
    for s in words:
        for a in s["articles"]:
            m = a.get("metrics") or {}
            if not m:
                s3.append([s["word"], a.get("title") or "（无标题）",
                           a.get("account") or "", "", "", "", "", "", "",
                           iso_date(a.get("publish_timestamp")) or "",
                           a.get("doc_url") or ""])
                continue
            r = m.get("rates") or {}
            read = (f'{m["read_num"]}+' if m.get("read_capped")
                    else (m.get("read_num") if m.get("read_num") is not None
                          else (a.get("display_read") or "")))
            s3.append([s["word"], a.get("title") or "（无标题）", a.get("account") or "",
                       read, m.get("interaction_num"), r.get("engagement"),
                       r.get("share"), r.get("collect"), r.get("like"),
                       iso_date(a.get("publish_timestamp")) or "",
                       m.get("url") or a.get("doc_url") or ""])

    s4 = [["选题词", "标签", "机会原因", "目标读者", "推荐角度", "竞争程度",
           "具体怎么做", "建议标题", "内容大纲"]]
    picks = (summary or {}).get("picks") or []
    if picks:
        for p in picks:
            s4.append([p.get("word", ""), p.get("tag", ""), p.get("why", ""),
                       p.get("audience", ""), p.get("angle", ""), p.get("competition", ""),
                       p.get("action", ""),
                       " / ".join(_as_list(p.get("titles"))),
                       "\n".join(f"{i}. {t}" for i, t in enumerate(_as_list(p.get("outline")), 1))])
    else:
        s4.append(["（未注入 AI 洞察）", "", "用 --summary 传入洞察 JSON 后，"
                   "本表会填充机会卡明细。"])

    s5 = [["选题词", "快照日期", "机会分", "需求热度", "竞争度",
           "阅读中位数", "互动率(bps)", "有效样本", "总样本"]]
    hist = (ds.get("snapshot_history") or {}).get(ds.get("seed") or "") or []
    for h in hist:
        for w, v in (h.get("words") or {}).items():
            s5.append([w, h.get("date", ""), v.get("opportunity"), v.get("demand"),
                       v.get("supply"), v.get("median_read"),
                       v.get("median_engagement_bps"), v.get("valid_count"),
                       v.get("sample_count")])
    if len(s5) == 1:
        s5.append(["（暂无历史快照）", "", "用 --snapshot 指定快照文件，"
                   "每次运行会自动追加，下次即可看到趋势。"])

    return [("选题机会", s1), ("关键词信号", s2), ("文章样本", s3),
            ("机会卡", s4), ("趋势快照", s5), ("费用明细", _cost_sheets_rows(ledger))]


def build_account_sheets(ds, ledger, summary=None):
    """账号模式的 Excel 工作表。"""
    packs = ds.get("accounts") or []

    s1 = [["账号", "采集篇数", "有效篇数", "阅读中位数", "互动率(bps)", "高频主题"]]
    for p in packs:
        s1.append([p.get("name", ""), len(p.get("articles") or []),
                   p.get("valid_count"), p.get("median_read"),
                   p.get("median_engagement_bps"),
                   " / ".join(f'{t["topic"]}({t["docs"]})' for t in (p.get("topics") or []))])

    s2 = [["账号", "主题标签", "覆盖篇数", "出现次数"]]
    for p in packs:
        for t in (p.get("topics") or []):
            s2.append([p.get("name", ""), t.get("topic", ""),
                       t.get("docs"), t.get("count")])

    s3 = [["账号", "文章标题", "阅读", "互动", "互动率(bps)", "发布时间", "链接"]]
    for p in packs:
        for a in (p.get("articles") or []):
            m = a.get("metrics") or {}
            r = m.get("rates") or {}
            s3.append([p.get("name", ""), a.get("title") or "（无标题）",
                       m.get("read_num"), m.get("interaction_num"), r.get("engagement"),
                       iso_date(a.get("publish_timestamp")) or "",
                       m.get("url") or a.get("doc_url") or ""])

    s4 = [["主题", "谁在做", "覆盖篇数", "谁没做"]]
    for g in (ds.get("gaps") or []):
        s4.append([g.get("topic", ""), g.get("owner", ""), g.get("docs"),
                   "、".join(g.get("missing_in") or [])])
    if len(s4) == 1:
        s4.append(["（未发现缺口）", "", "传入 2 个以上账号才会做交叉对比。"])

    s5 = [["结论", (summary or {}).get("headline", "（未注入 AI 洞察）")],
          ["怎么读这份版图", (summary or {}).get("verdict", "")],
          ["推进顺序", (summary or {}).get("sequence", "")]]

    return [("账号概览", s1), ("主题标签", s2), ("文章样本", s3),
            ("内容缺口", s4), ("AI 洞察", s5), ("费用明细", _cost_sheets_rows(ledger))]


# --------------------------------------------------------------------------
# 离线自检
# --------------------------------------------------------------------------

SELF_TEST_DATA = {
    "suggestions": {"items": [{"word": "少儿编程有必要学吗"}, {"word": "少儿编程自学"},
                              {"word": "少儿编程怎么选"}, {"word": "少儿编程哪个机构好"},
                              {"word": "少儿编程入门教程"}]},
}


def self_test_dataset():
    """构造一份不联网的假数据，跑通评分与渲染全链路。"""
    now = int(time.time())
    seeds = [("少儿编程", 1.0, 62000, 300, 0.8, 4),
             ("少儿编程有必要学吗", 0.8, 18000, 520, 0.9, 3),
             ("少儿编程自学", 0.6, 3200, 260, 0.5, 5),
             ("少儿编程怎么选", 0.4, 24000, 410, 0.7, 3),
             ("少儿编程哪个机构好", 0.2, 51000, 180, 0.6, 4),
             ("少儿编程入门教程", 0.0, 900, 640, 1.0, 2)]
    stats = []
    for word, rank, base_read, eng, fresh, nacc in seeds:
        arts = []
        for i in range(8):
            capped = (i == 0 and base_read > 50000)
            read = 100001 if capped else max(120, int(base_read * (1.6 - i * 0.16)))
            arts.append({
                "title": f"{word} 相关第 {i+1} 篇", "account": f"示例账号{(i % nacc) + 1}",
                "doc_url": f"https://mp.weixin.qq.com/s?__biz=TEST&mid={i}&idx=1&sn=abc{i}",
                "timestamp": now - int((1 - fresh) * 200 + i * 7) * 86400,
                "desc": "", "display_read": None,
                "metrics": {
                    "url": f"https://mp.weixin.qq.com/s?__biz=TEST&mid={i}&idx=1&sn=abc{i}",
                    "read_num": read, "read_capped": capped, "read_text": "10万+" if capped else "",
                    "like_num": 30, "old_like_num": 60, "share_num": int(read * eng / 10000 * 0.7),
                    "collect_num": int(read * eng / 10000 * 0.2), "comment_num": None,
                    "interaction_num": int(read * eng / 10000),
                    "rates": {"engagement": eng, "share": int(eng * 0.7), "collect": int(eng * 0.2),
                              "like": int(eng * 0.05), "oldLike": int(eng * 0.05), "comment": 0},
                    "title": "", "account_name": "",
                },
            })
        stats.append(compute_stats(word, rank, arts))
    words = apply_scoring(stats)
    words.sort(key=lambda s: (-s.get("trusted", s["opportunity"]), -s["demand"]))
    md, ms = median([s["demand"] for s in words]), median([s["supply"] for s in words])
    for s in words:
        s["quadrant"] = quadrant(s, md, ms)
    return {"seed": "少儿编程（自检示例）",
            "generated_at": datetime.now(timezone.utc).astimezone().strftime("%Y-%m-%d %H:%M"),
            "params": {"sort": "hot", "publish_time": "any", "per_word": 8, "expand": 1},
            "words": words, "median_demand": md, "median_supply": ms,
            "total_articles": sum(s["sample_count"] for s in words)}


# --------------------------------------------------------------------------
# 入口
# --------------------------------------------------------------------------

def main():
    p = argparse.ArgumentParser(
        description="选题雷达：三种模式 —— 关键词驱动 / 热点驱动 / 账号驱动，"
                    "输出机会矩阵或内容版图与选题清单")
    p.add_argument("--api-key", default=os.environ.get("MANGE_API_KEY"),
                   help="曼格云 API Key；也可设环境变量 MANGE_API_KEY")
    p.add_argument("--seed", help="[关键词模式] 种子关键词")
    p.add_argument("--seeds", help="[关键词模式] 逗号分隔的多个种子词，"
                                   "直接作为候选词分析，不再做推荐词扩散（热点模式转译后用）")
    # ---- 热点模式 ----
    p.add_argument("--hot", action="store_true",
                   help="[热点模式] 拉取搜一搜实时热搜榜并输出词表，不做分析"
                        "（转译交给 Agent，再用 --seeds 跑分析）")
    # ---- 账号模式 ----
    p.add_argument("--account", action="append", metavar="URL_OR_GHID",
                   help="[账号模式] 公众号文章链接或 gh_ 开头的原始 ID，可多次传入对比多个号")
    p.add_argument("--pages", type=int, default=3, help="[账号模式] 每个号最多抓几页（每页≤20 篇）")
    p.add_argument("--max-articles", type=int, default=40, help="[账号模式] 每个号最多分析多少篇")
    p.add_argument("--topics", type=int, default=10, help="[账号模式] 每个号输出几个主题标签")
    p.add_argument("--sort", default="hot", choices=["comprehensive", "latest", "hot"])
    # 默认半年：既保证样本充足，又让「新鲜度」维度保留区分度（any 下样本多为旧文）
    p.add_argument("--publish-time", default="halfYear", choices=["any", "day", "week", "halfYear"])
    p.add_argument("--per-word", type=int, default=8, help="每个词抓取的文章数 1-50，默认 8")
    p.add_argument("--expand", type=int, default=1, choices=[1, 2],
                   help="1=只用一级推荐词；2=再扩散一级（更全，成本更高）")
    p.add_argument("--extra-words", type=int, default=15, help="expand=2 时额外纳入的二级词数量")
    p.add_argument("--deep", type=int, default=3,
                   help=f"对 Top {DEEP_TOP_WORDS} 个蓝海词各采样几篇内容规格（多篇取中位数），0 关闭")
    p.add_argument("--rate", type=float, default=DEFAULT_RATE, help="每秒请求数上限，默认 4")
    p.add_argument("--output", help="HTML 报告输出路径（热点模式可省略）")
    p.add_argument("--markdown", help="Markdown 副本输出路径")
    p.add_argument("--excel", help="Excel 工作簿输出路径（.xlsx，多 Sheet，零第三方依赖）")
    p.add_argument("--json", help="原始数据 JSON 输出路径")
    p.add_argument("--from-json", help="复用已采集的 JSON 数据重新渲染报告，不调用接口、不扣费")
    p.add_argument("--summary", help="AI 洞察 JSON 文件路径（由 Agent 读数据后生成，见 SKILL.md）")
    p.add_argument("--snapshot", help="趋势快照文件路径：每次运行追加本次结果，下次运行自动对比上次")
    p.add_argument("--self-test", action="store_true", help="离线自检，不联网不扣费")
    args = p.parse_args()

    if args.per_word < 1 or args.per_word > 50:
        p.error("--per-word 需在 1-50 之间")

    summary = None
    if args.summary:
        with open(args.summary, encoding="utf-8") as f:
            summary = json.load(f)
        print(f"已载入 AI 洞察：{args.summary}")

    # ---------- 热点模式：只拉榜不做分析，转译交给 Agent ----------
    if args.hot:
        if not args.api_key:
            p.error("缺少 API Key：用 --api-key 传入，或设置环境变量 MANGE_API_KEY")
        ledger = CostLedger()
        client = Client(args.api_key, rate=args.rate, ledger=ledger)
        try:
            words = fetch_hot_words(client)
        except ApiError as e:
            print(f"错误：{e}", file=sys.stderr)
            return 2
        payload = {
            "mode": "hot",
            "generated_at": datetime.now(timezone.utc).astimezone().strftime("%Y-%m-%d %H:%M"),
            "cost": {"total": ledger.total, "balance": ledger.balance, "calls": ledger.calls},
            "words": words,
        }
        if args.json:
            os.makedirs(os.path.dirname(os.path.abspath(args.json)) or ".", exist_ok=True)
            with open(args.json, "w", encoding="utf-8") as f:
                json.dump(payload, f, ensure_ascii=False, indent=1)
            print(f"已写入：{os.path.abspath(args.json)}")
        print(f"\n搜一搜实时热搜榜 {len(words)} 条（本次消费 ¥{ledger.total:.4f}）：")
        for w in words:
            print(f"  {w['rank']}. {w['word']}")
        print("\n提示：热词多为新闻事件，直接搜样本少、时效强。"
              "请先转译成可长期搜索的选题词，再用 --seeds 跑完整分析。")
        return 0

    if args.from_json:
        # 复用已采集的数据重新渲染（用于反复打磨 AI 总结，不重复调用接口）
        print(f"[复用模式] 读取已有数据 {args.from_json}，不会发起任何网络请求。")
        with open(args.from_json, encoding="utf-8") as f:
            ds = json.load(f)
        ledger = CostLedger()
        cost = ds.get("cost") or {}
        ledger.total = cost.get("total", 0.0)
        ledger.balance = cost.get("balance")
        ledger.calls = cost.get("calls", 0)
    elif args.self_test:
        print("[自检模式] 使用内置示例数据，不会发起任何网络请求，不消耗额度。")
        ds = self_test_dataset()
        ledger = CostLedger()
        ledger.total, ledger.balance, ledger.calls = 0.0, 0.0, 0
    elif args.account:
        if not args.api_key:
            p.error("缺少 API Key：用 --api-key 传入，或设置环境变量 MANGE_API_KEY")
        ledger = CostLedger()
        client = Client(args.api_key, rate=args.rate, ledger=ledger)
        try:
            ds = build_account_dataset(client, args.account, args)
        except ApiError as e:
            print(f"错误：{e}", file=sys.stderr)
            return 2
        if not ds:
            print("未取到任何账号数据，请检查传入的文章链接或 ghid 是否正确。", file=sys.stderr)
            return 1
    else:
        if not args.seed and not args.seeds:
            p.error("缺少输入：用 --seed 传单个种子词，或 --seeds 传多个词（逗号分隔）")
        if not args.api_key:
            p.error("缺少 API Key：用 --api-key 传入，或设置环境变量 MANGE_API_KEY")
        ledger = CostLedger()
        client = Client(args.api_key, rate=args.rate, ledger=ledger)
        seed = args.seed or (args.seeds.split(",")[0].strip() if args.seeds else "")
        try:
            ds = build_dataset(client, seed, args)
        except ApiError as e:
            print(f"错误：{e}", file=sys.stderr)
            return 2
        if not ds["words"]:
            print("未取到任何候选词样本，请更换种子词后重试。", file=sys.stderr)
            return 1

    # ---------- 趋势快照：对比上次 → 渲染 → 落盘 ----------
    # 只有真实采集过（--from-json / --self-test 不算）才写入，避免重复渲染污染历史。
    if args.snapshot and ds.get("mode") != "account" and ds.get("words"):
        snap = load_snapshot(args.snapshot)
        rec = apply_trend(ds["words"], snap, ds.get("seed") or "")
        # 存进 ds 供 Excel「趋势快照」表取用；含本次这条，否则表里会缺最新一次
        seed_key = ds.get("seed") or ""
        hist = {k: [h for h in v if isinstance(h, dict)]
                for k, v in snap.items() if isinstance(v, list)}
        hist.setdefault(seed_key, [])
        hist[seed_key] = (hist[seed_key] + [rec])[-SNAPSHOT_KEEP:]
        ds["snapshot_history"] = hist
        fresh = not (args.from_json or args.self_test)
        n_hist = len([h for h in (snap.get(ds.get("seed") or "") or []) if isinstance(h, dict)])
        if fresh:
            if save_snapshot(args.snapshot, snap, ds.get("seed") or "", rec):
                print(f"趋势快照：{args.snapshot}"
                      f"（{ds.get('seed')} 第 {n_hist + 1} 次，保留最近 {SNAPSHOT_KEEP} 次）")
        elif n_hist:
            print(f"趋势对比：已载入 {ds.get('seed')} 的历史快照 {n_hist} 次，不写入新记录")

    is_account = ds.get("mode") == "account"
    if is_account:
        md_text = build_account_markdown(ds, ledger, summary)
        html = build_account_html(ds, ledger, md_text, summary)
    else:
        md_text = build_markdown(ds, ledger, summary)
        html = build_html(ds, ledger, md_text, summary)

    if not args.output:
        p.error("缺少 --output HTML 输出路径")
    os.makedirs(os.path.dirname(os.path.abspath(args.output)) or ".", exist_ok=True)
    with open(args.output, "w", encoding="utf-8") as f:
        f.write(html)
    if args.markdown:
        with open(args.markdown, "w", encoding="utf-8") as f:
            f.write(md_text)
    if args.excel:
        try:
            if is_account:
                sheets = build_account_sheets(ds, ledger, summary)
            else:
                sheets = build_keyword_sheets(ds, ledger, summary)
            write_xlsx(args.excel, sheets)
            print(f"Excel：{os.path.abspath(args.excel)}"
                  f"（{len(sheets)} 个 Sheet：{' / '.join(n for n, _ in sheets)}）")
        except (OSError, ValueError) as e:
            print(f"      ! Excel 导出失败：{e}", file=sys.stderr)
    if args.json:
        with open(args.json, "w", encoding="utf-8") as f:
            json.dump(ds, f, ensure_ascii=False, indent=1, default=str)

    print()
    if is_account:
        print(f"账号 {len(ds['accounts'])} 个｜文章 {ds['total_articles']} 篇"
              f"｜发现缺口 {len(ds.get('gaps') or [])} 处")
        for pack in ds["accounts"]:
            print(f"  - {pack['name']}：{pack['valid_count']}/{len(pack['articles'])} 篇有效"
                  f"，阅读中位数 {fmt_num(pack.get('median_read'))}"
                  f"，主题 {len(pack['topics'])} 个")
    else:
        print(f"候选词 {len(ds['words'])} 个｜扫描文章 {ds['total_articles']} 篇")
        print("\n蓝海选题 Top 5：")
        for i, s in enumerate(ds["words"][:5], 1):
            print(f"  {i}. {s['word']}  机会分 {s['opportunity']:+.1f} "
                  f"(需求 {s['demand']:.0f} / 竞争 {s['supply']:.0f})")
    print(f"\n本次消费 ¥{ledger.total:.4f}｜余额 ¥{ledger.balance if ledger.balance is not None else '—'}")
    print(f"HTML 报告：{os.path.abspath(args.output)}")
    if args.markdown:
        print(f"Markdown：{os.path.abspath(args.markdown)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
