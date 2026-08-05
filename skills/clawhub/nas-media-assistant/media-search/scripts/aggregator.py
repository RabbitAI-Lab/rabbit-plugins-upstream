#!/usr/bin/env python3
"""网页候选聚合: 富集(标题解析) + 去重 + 评分 + 排序 + 硬过滤（链路1·网页磁力）。

设计原则: 网页抓取是脆弱的外围，标题解析才是稳定的核心。
parser 只负责把页面上的原始文本抓下来（标题串 + 链接），本聚合器调用
title_parser 把标题串解析成结构化字段（年份/分辨率/编码/音轨/字幕/大小...），
再统一去重、评分、排序。网页源失效换站时，只要还能拿到标题串，信息提取逻辑不变。

用法:
  aggregator.py '<候选JSON>' [query_title] [query_year]
候选JSON 可为调度器输出的 {"candidates":[...]} 或直接为 [...]。

输出排序后候选 JSON 列表（附带 excluded 列表）。
"""
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import title_parser  # noqa: E402  稳定核心

# 清晰度权重表（来自解析后的 resolution 字段）
QUALITY_WEIGHT = {
    "4320p": 120, "8k": 120, "2160p": 100, "4k": 100,
    "1440p": 85,
    "1080p": 80,
    "720p": 60,
    "576p": 40, "480p": 30,
}

# 来源加分（解析后的 source 字段）
SOURCE_BONUS = {
    "UHD BluRay": 15, "BluRay": 10, "REMUX": 12,
    "WEB-DL": 5, "WEBRip": 3, "HDTV": 0, "DVDRip": -5,
}

# 音频加分（按优先级降序，取首个命中，避免重复计分）
AUDIO_BONUS_TABLE = [
    (r"TrueHD.*Atmos|Atmos", 6, "Atmos"),
    (r"TrueHD", 5, "TrueHD"),
    (r"DTS-?HD\.?MA|DTSHDMA", 5, "DTS-HD MA"),
    (r"DTS-?X|DTSX", 5, "DTS-X"),
    (r"DTS-?HD|DTSHD", 4, "DTS-HD"),
    (r"FLAC", 4, "FLAC"),
    (r"LPCM", 3, "LPCM"),
    (r"DTS", 3, "DTS"),
    (r"E-?AC-?3|DDP", 2, "E-AC3"),
    (r"AC-?3", 2, "AC3"),
    (r"AAC", 1, "AAC"),
]

# 编码加分
CODEC_BONUS = {"H.265": 4, "HEVC": 4, "AV1": 5, "H.264": 1, "AVC": 1}

# CJK 统一表意文字范围
_CJK_START = ord("\u4e00")
_CJK_END = ord("\u9fff")


def _is_cjk(ch):
    """判断字符是否为 CJK 汉字。"""
    return _CJK_START <= ord(ch) <= _CJK_END


def normalize_title(t):
    """归一化标题用于去重指纹：去广告前缀 + 去分隔符。"""
    t = str(t).lower()
    # 去掉开头的广告/发布站前缀 [xxx] / 【xxx】（如 [BBTTBA.COM]、【高清影视之家发布...】）
    t = re.sub(r"^(?:\[[^\]]*\]|【[^】]*】)\s*", "", t)
    return re.sub(r"[\s.\-_·]", "", t)


def enrich(c):
    """用 title_parser 富集候选：解析标题串，合并所有结构化字段。

    网页已有字段（url/link_type/seeders/detail_url/credibility/source_id）不被覆盖；
    标题内嵌大小优先，页面提供 size 原文兜底。
    """
    if "error" in c:
        return c
    parsed = title_parser.parse(c.get("title", ""))
    for k, v in parsed.items():
        if k == "raw":
            continue
        c.setdefault(k, v)
    # 大小兜底：标题无大小则用页面 size 原文解析
    if not c.get("size_bytes") and c.get("size"):
        sb, sh = title_parser.parse_size(c["size"])
        if sb:
            c["size_bytes"] = sb
            c["size_human"] = sh
    return c


def fingerprint(c):
    """去重指纹: 标题 + 年份 + 分辨率。年份/分辨率来自 title_parser 解析。"""
    return f"{normalize_title(c.get('title',''))}|{c.get('year','')}|{c.get('resolution','')}"


def is_low_quality(c):
    """低质资源（枪版/样片/预告等），由 title_parser 解析判定。"""
    return bool(c.get("is_low_quality"))


def dedup(candidates):
    """按指纹去重，合并多源信息到 alt_sources。"""
    seen = {}
    for c in candidates:
        if "error" in c:
            continue
        fp = fingerprint(c)
        if fp not in seen:
            seen[fp] = dict(c)
        else:
            existing = seen[fp]
            existing.setdefault("alt_sources", []).append(c.get("source_id"))
            # 保留更优的链接类型（magnet/direct 优先于 playpage）
            if c.get("link_type") in ("magnet", "direct", "torrent") and \
               existing.get("link_type") == "playpage":
                existing["url"] = c.get("url", existing.get("url", ""))
                existing["link_type"] = c["link_type"]
    return list(seen.values())


def _audio_bonus(audio):
    """从解析后的音频字段提取加分（取首个命中，大小写无关）。"""
    a = str(audio)
    for pat, pts, label in AUDIO_BONUS_TABLE:
        if re.search(pat, a, re.I):
            return pts, label
    return 0, ""


def _lang_bonus(language, subtitle):
    """语言/字幕加分。"""
    bonus, tags = 0, []
    langs = language or []
    subs = subtitle or []
    if len(langs) >= 3:
        bonus += 12; tags.append("三语")
    elif len(langs) == 2:
        bonus += 8; tags.append("双语")
    if "特效字幕" in subs:
        bonus += 6; tags.append("特效字幕")
    if "简体" in subs and "繁体" in subs:
        bonus += 5; tags.append("简繁")
    if subs and bonus == 0:
        bonus += 2; tags.append("字幕")
    return bonus, tags


def _title_relevance(candidate, query_title, query_year=""):
    """检查候选与查询标题的相关性，返回相关度 0.0~1.0。

    对解析后的 title_cn / title_en / 原始 title 三者分别匹配，取最大值。
    匹配策略：
    - 精确匹配（归一化后完全相同）-> 1.0
    - 子串匹配且后续为非 CJK 字符 -> 1.0
    - 子串匹配但后续为 CJK 字符（功夫->功夫梦）-> 年份相同0.9否则0.5
    - 前缀匹配（续集）-> 0.8
    - 弱相关 -> 0.3
    """
    if not query_title:
        return 1.0
    cand_year = str(candidate.get("year", ""))
    best = 0.3
    for field in ("title_cn", "title_en", "title"):
        cand_title = candidate.get(field, "")
        if not cand_title:
            continue
        r = _match_one(cand_title, query_title, cand_year, query_year)
        if r > best:
            best = r
            if best >= 1.0:
                break
    return best


def _match_one(candidate_title, query_title, candidate_year, query_year):
    """单标题字段的匹配逻辑。"""
    cn = normalize_title(candidate_title)
    qt = normalize_title(query_title)
    if not qt:
        return 1.0
    if cn == qt:
        return 1.0
    idx = cn.find(qt)
    if idx >= 0:
        after_pos = idx + len(qt)
        if after_pos >= len(cn):
            return 1.0
        next_char = cn[after_pos]
        if _is_cjk(next_char):
            # CJK 边界：可能不同电影（功夫->功夫梦）或系列成员
            if query_year and candidate_year:
                return 0.9 if query_year == candidate_year else 0.5
            return 0.6
        return 1.0
    # 前缀匹配（续集：疯狂动物城->疯狂动物城2）
    if len(qt) >= 2:
        prefix = qt[:max(2, len(qt) // 2)]
        if prefix in cn:
            return 0.8
    return 0.3


# ---------- 大小合理性（NAS 空间有限，过大资源降权）----------
# 按分辨率/类型给出集均或总大小的合理区间。超出区间线性降权，远超则重罚。
# 设计意图: 适合才是最重要的--不是信息最全的最高分，而是大小合理的优先。
_SIZE_BANDS = {
    # key: (is_4k, is_tv) -> (ideal_gb, soft_gb)
    # 理想区间内不罚；超出线性降至 0.7；远超则重罚下限 0.5。
    # 设计依据: NAS 可用 3TB，剧集占用比电影更敏感(单剧占 7%+ 不可接受)。
    (True,  True):  (2.5, 5.0),    # 4K 剧集 集均 GB（5GB/集×40集=200GB 过大）
    (True,  False): (50.0, 100.0), # 4K 电影 总 GB
    (False, True):  (1.2, 2.5),    # 1080p 剧集 集均 GB
    (False, False): (20.0, 40.0),  # 1080p 电影 总 GB
}


def _size_factor(c, query_type=""):
    """大小合理性因子 0.5~1.0。

    - 大小未知: 高码版轻度降权(0.9)，其余不罚(1.0)
    - 已知大小: 按集均(剧集)/总大小(电影)与分辨率合理区间线性降权，远超则重罚
    """
    size_bytes = c.get("size_bytes", 0) or 0
    res = str(c.get("resolution", "")).lower()
    is_4k = res in ("2160p", "4320p", "8k")

    # 判定剧集: 查询类型为 tv，或标题解析出集数 > 1
    ep_count = c.get("episode_count", 0) or 0
    is_tv = query_type == "tv" or ep_count > 1

    if not size_bytes:
        return 0.9 if c.get("is_high_bitrate") else 1.0

    gb = size_bytes / 1e9
    # 剧集按集均大小评估；未知集数则按总大小粗估（is_tv 仍取剧集档）
    if is_tv and ep_count > 0:
        gb = gb / ep_count
    elif is_tv:
        gb = gb / 40.0  # 未知集数的剧集，按 40 集粗估集均

    ideal, soft = _SIZE_BANDS.get((is_4k, is_tv), (1.0, 3.0))
    if gb <= ideal:
        return 1.0
    if gb <= soft:
        # 线性从 1.0 降到 0.7
        return round(1.0 - 0.3 * (gb - ideal) / (soft - ideal), 3)
    # 远超合理上限: 重罚，越大越低，下限 0.5
    return round(max(0.5, 0.7 - 0.1 * (gb - soft) / max(ideal, 0.5)), 3)


def score(c, query_title="", query_year="", query_type=""):
    """质量评分 = (清晰度+来源+音频+HDR+语言+编码+做种) × 可信度 × 可用性 × 相关度 × 大小合理性。

    所有加分项均来自 title_parser 解析后的结构化字段，不再对原始标题做正则。
    大小合理性(size_factor): NAS 空间有限，过大/高码资源降权，适合优先。
    """
    # 清晰度权重
    res = str(c.get("resolution", "")).lower()
    q = QUALITY_WEIGHT.get(res, 50)

    # 来源加分
    src = c.get("source", "")
    q += SOURCE_BONUS.get(src, 0)

    # 音频加分
    audio_pts, audio_label = _audio_bonus(c.get("audio", ""))
    q += audio_pts

    # HDR / 杜比加分
    hdr = c.get("hdr", "")
    if hdr == "Dolby Vision":
        q += 8
    elif hdr == "HDR":
        q += 6

    # 编码加分
    q += CODEC_BONUS.get(c.get("codec", ""), 0)

    # 语言/字幕加分
    lang_pts, lang_tags = _lang_bonus(c.get("language", []), c.get("subtitle", []))
    q += lang_pts

    # 做种加分（对数缩放）
    seeders = c.get("seeders", 0) or 0
    seeder_bonus = min(8, (seeders // 20)) if seeders > 0 else 0
    q += seeder_bonus

    # 可信度
    credibility = c.get("credibility", 0.8)

    # 可用性：磁力/直链最易下载 > 种子页(论坛可能需登录/积分) > 播放页
    link_type = c.get("link_type", "")
    availability = {"magnet": 1.0, "direct": 1.0, "torrent": 0.92,
                    "playpage": 0.5}.get(link_type, 0.85)

    # 标题相关度
    relevance = _title_relevance(c, query_title, query_year) if query_title else 1.0

    # seeder_bonus 已含在 q 中
    raw = q * credibility * availability * relevance
    # 单集资源降权（整季搜索时排在整季之后，不删除：用户可能确实要单集）
    if c.get("is_single_episode"):
        raw *= 0.5
    # 大小合理性: NAS 空间有限，过大/高码资源降权，适合优先
    raw *= _size_factor(c, query_type)
    result = round(raw, 2)

    # 信息标签
    tags = []
    if audio_label:
        tags.append(audio_label)
    tags.extend(lang_tags)
    if hdr:
        tags.append(hdr)
    if src == "REMUX":
        tags.append("REMUX")
    if c.get("is_high_bitrate"):
        tags.append("高码")
    if tags:
        c["info_tags"] = tags
    c["quality_score"] = result
    return result


def aggregate(candidates, query_title="", query_year="", query_type="", top_n=0, min_relevance=0.0):
    """聚合：富集 -> 硬过滤 -> 去重 -> 评分 -> 相关度过滤 -> 排序 -> Top-N。

    Args:
        candidates: 原始候选列表（fetcher 输出，仅含 title/url/link_type 等原始字段）
        query_title: 查询标题，用于标题相关度过滤
        query_year: 查询年份，用于年份消歧
        query_type: 查询类型(movie/tv)，用于大小合理性判定
        top_n: 取前 N 条，0 表示不限制
        min_relevance: 最低相关度阈值，低于此值的候选排除（0 表示不过滤）

    Returns:
        dict: {"candidates": [...排序后候选], "excluded": [...被过滤的链接]}
    """
    excluded = []

    # 1. 富集：标题解析（稳定核心）
    enriched = [enrich(c) for c in candidates]

    # 2. 硬过滤：错误候选 + 低质资源
    filtered = []
    for c in enriched:
        if "error" in c:
            excluded.append({"url": c.get("url", ""), "reason": "error",
                             "source_id": c.get("source_id", "")})
            continue
        if is_low_quality(c):
            excluded.append({"url": c.get("url", ""), "reason": "low_quality",
                             "title": c.get("title", "")})
            continue
        filtered.append(c)

    # 3. 去重
    uniq = dedup(filtered)

    # 4. 评分
    for c in uniq:
        score(c, query_title, query_year, query_type)

    # 5. 相关度过滤
    if query_title and min_relevance > 0:
        kept = []
        for c in uniq:
            relevance = _title_relevance(c, query_title, query_year)
            if relevance >= min_relevance:
                kept.append(c)
            else:
                excluded.append({"url": c.get("url", ""), "reason": "low_relevance",
                                  "title": c.get("title", "")})
        uniq = kept

    # 6. 排序
    uniq.sort(key=lambda x: x.get("quality_score", 0), reverse=True)

    # 7. Top-N 限制
    if top_n > 0 and len(uniq) > top_n:
        uniq = uniq[:top_n]

    return {"candidates": uniq, "excluded": excluded}


def main():
    if len(sys.argv) < 2:
        print(json.dumps({"error": "用法: aggregator.py '<候选JSON>' [query_title] [query_year]"}))
        sys.exit(1)
    data = json.loads(sys.argv[1])
    query_title = sys.argv[2] if len(sys.argv) > 2 else ""
    query_year = sys.argv[3] if len(sys.argv) > 3 else ""
    query_type = sys.argv[4] if len(sys.argv) > 4 else ""
    if isinstance(data, dict):
        candidates = data.get("candidates", [])
        query_obj = data.get("query", {})
        query_title = query_title or query_obj.get("title", "")
        query_year = query_year or str(query_obj.get("year", ""))
        query_type = query_type or query_obj.get("type", "")
    else:
        candidates = data
    result = aggregate(candidates, query_title, query_year, query_type)
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
