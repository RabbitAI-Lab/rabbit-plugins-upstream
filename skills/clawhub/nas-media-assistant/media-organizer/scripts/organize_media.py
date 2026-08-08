#!/usr/bin/env python3
"""organize_media.py - 批量媒体库整理器（media-organizer 规则）。

解耦说明：
  本工具不内嵌任何 TMDB 查询。需要元数据补全时，由编排器调用 media-lookup
  取回归一化 JSON 后经 --metadata 注入；自身策略无法确诊时输出 pending_lookup，
  由编排器补全元数据后带 --metadata 重试。已归档文件（规范命名+正确分类目录）
  默认跳过解析，--rescan 可强制重扫。

命名格式：
  电影(独立): 电影/电影名 (年份)/电影名 (年份) [信息].扩展名
  电影(系列): 电影/系列名（系列）/电影名 (年份) [信息].扩展名
  剧集(独立): 剧集/剧名 (年份)/剧名 - SXXEYY [信息].扩展名
  剧集(多季): 剧集/剧名/剧名·第N季/剧名 - SXXEYY [信息].扩展名
  剧集(主题): 剧集/剧名/剧名·主题(年份)/剧名·主题 - SXXEYY [信息].扩展名
  动漫:       动漫/动漫名 (年份)/Season XX/动漫名 - SXXEYY [信息].扩展名

三阶段处理：
  1. 逐文件解析 + 分类 + 系列检测(优先 series_registry curated 段 + media_cache.known 自扩充, 回退注入元数据 / 冒号/中点启发式)
  2. 剧集系列归组：单季->独立, 多季->格式2(第N季)/格式3(主题)
  3. 单成员系列自动降级为独立电影(避免单部电影误入系列文件夹)

用法:
  python3 organize_media.py /media/downloads/inbox            # 预演(默认)
  python3 organize_media.py /media/downloads/inbox --commit   # 实际移动
  python3 organize_media.py /media/movies --commit --no-ffprobe
  # 带元数据注入（编排器从 media-lookup 取回后传入）：
  python3 organize_media.py /media/downloads/inbox --commit --metadata-file /tmp/meta.json
"""
import argparse
import io
import json
import os
import re
import shutil
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from series_detect import series_from_collection, detect_spinoff, is_animated  # noqa: E402


# ==================== 常量 ====================

VIDEO_EXTS = {
    "mkv", "mp4", "ts", "avi", "m2ts", "mov", "wmv", "flv", "webm",
    "iso", "mpg", "mpeg", "rmvb", "rm",
}
# 跳过样本/预告/花絮/非视频文件
SKIP_PATTERNS = re.compile(
    r"(?i)(sample|预告|花絮|trailer|bonus|extra|\.nfo$|\.jpg$|\.png$|\.txt$|\.srt$|\.ass$|\.ssa$)"
)

# 集号正则（按优先级尝试）
EPISODE_RE = re.compile(r"(?<![A-Za-z0-9])[Ss](\d{1,2})[Ee](\d{1,3})(?:[Ee](\d{1,3}))?")  # S01E12
EPISODE_EONLY_RE = re.compile(r"(?<![A-Za-z0-9])[Ee][Pp]?(\d{1,3})(?![0-9])")            # E12 / Ep12
EPISODE_CN_RE = re.compile(r"第(\d{1,3}|[零一二三四五六七八九十百]+)集")                    # 第17集
EPISODE_BARE_RE = re.compile(r"(\D)(\d{1,3})(?=\.\w+$|$)")                                # 末尾裸数字: 夏娃01
EPISODE_LEADING_RE = re.compile(r"^(\d{1,3})[-_.\s]")                                     # 开头数字: 01-4K
EPISODE_SE_RE = re.compile(r"(?i)SE(\d{1,2})[.\s](\d{1,3})")                              # SE01.07

YEAR_RE = re.compile(r"[（(](\d{4})[)）]")
MIDDOT_RE = re.compile(r"(.+?)·(.+)")

KIND_DIR = {"movie": "电影", "tv": "剧集", "anime": "动漫"}

# 动漫关键词（用于剧集分流：含关键词的归入动漫而非剧集）
ANIME_HINTS = (
    "番", "动漫", "动画", "国漫", "火影", "海贼", "龙珠",
    "柯南", "鬼灭", "咒术", "间谍过家家",
)

# 剧场版/OVA/OAD/SP/番外 是单体电影格式，强制走电影路径（即使检测到裸数字集号）
MOVIE_FORMAT_KEYWORDS = ("剧场版", "OVA", "OAD", "SP", "特别篇", "番外")

# 仅含质量/压制组等无意义 token 的剧名（用于判断剧集文件名缺剧名）
JUNK_TITLE_RE = re.compile(
    r"(?i)^(HD|720P|1080P|2160P|4K|UHD|WEB|HDTV|蓝光|国|粤|英|中|双语|双字|"
    r"特效|简|繁|内嵌|外挂|压制|组|REMUX|BluRay|x264|x265|[\s.\-])+$"
)
SEASON_FOLDER_RE = re.compile(r"^(?:[Ss]\d{1,2}|[Ss]eason\s*\d{1,2})$")


# ==================== 中文数字辅助 ====================

_CN_DIGITS = "零一二三四五六七八九"


def _cn_to_int(s):
    """中文数字转 int: '十七'->17, '一百零八'->108, '十'->10, '三'->3。
    纯阿拉伯数字直接转。"""
    s = s.strip()
    if s.isdigit():
        return int(s)
    if s == "十":
        return 10
    if "十" in s:
        parts = s.split("十", 1)
        tens = _cn_to_int(parts[0]) if parts[0] else 1
        ones = _cn_to_int(parts[1]) if parts[1] else 0
        return tens * 10 + ones
    if "百" in s:
        parts = s.split("百", 1)
        hundreds = _cn_to_int(parts[0]) if parts[0] else 1
        remainder = parts[1]
        if remainder:
            if remainder.startswith("零"):
                return hundreds * 100 + _cn_to_int(remainder[1:])
            return hundreds * 100 + _cn_to_int(remainder)
        return hundreds * 100
    for i, c in enumerate(_CN_DIGITS):
        if s == c:
            return i
    try:
        return int(s)
    except ValueError:
        return 0


def _int_to_cn(n):
    """int 转中文季号: 1->一, 2->二, 10->十, 22->二十二。"""
    if n <= 0:
        return str(n)
    if n < 10:
        return _CN_DIGITS[n]
    if n == 10:
        return "十"
    if n < 20:
        return "十" + _CN_DIGITS[n % 10]
    if n % 10 == 0:
        return _CN_DIGITS[n // 10] + "十"
    return _CN_DIGITS[n // 10] + "十" + _CN_DIGITS[n % 10]


# ==================== 文件名解析 ====================

def split_ext(name):
    """拆分文件名为 (stem, ext)，ext 转小写无点。"""
    p = Path(name)
    return p.stem, p.suffix.lstrip(".").lower()


def extract_info_portion(stem):
    """从原始文件名提取 [信息] 段（首个 [ 到末个 ]，原样保留）。"""
    m = re.search(r"\[.*\]", stem)
    return m.group(0) if m else ""


def is_episode(s):
    """检测文件名中的集号，返回 (season, episode) 或 (None, None)。
    支持格式：S01E12, SE01.07, E12, 第17集, 第十季 076, 第3季 12。"""
    m = EPISODE_RE.search(s)
    if m:
        return int(m.group(1)), int(m.group(2))
    m = EPISODE_SE_RE.search(s)  # SE01.07 格式 (Season=1, Episode=7)
    if m:
        return int(m.group(1)), int(m.group(2))
    m = EPISODE_EONLY_RE.search(s)  # 仅集号 E12 (默认 Season 1)
    if m:
        return 1, int(m.group(1))
    m = EPISODE_CN_RE.search(s)  # 中文集号 第17集
    if m:
        return 1, _cn_to_int(m.group(1))
    # 中文季号+集号: 第十季 台配 076, 第3季 12
    m = re.search(r"第([零一二三四五六七八九十百\d]+)季.*?(\d{1,3})(?![0-9])", s)
    if m:
        ep = int(m.group(2))
        if 1 <= ep <= 999:
            return _cn_to_int(m.group(1)), ep
    return None, None


def _clean_title(t):
    """清洗标题：去书名号/广告前缀【...】、统一分隔符、去首尾空格。"""
    t = t.replace("《", "").replace("》", "")
    t = re.sub(r"【.*?】", "", t)          # 去广告前缀（如【高清影视之家发布 www.xxx.com】）
    t = re.sub(r"[._]", " ", t)
    t = re.sub(r"\s+", " ", t).strip()
    return t.strip(" --")


def _strip_quality_tail(title):
    """裁掉标题尾部的纯质量标记（1080p/BluRay/x265…），保留中文字符标题主体。"""
    m = re.search(
        r"\s+((?:\d{3,4}p|4K|UHD|HDR|BluRay|Blu-Ray|WEB-DL|WEBRip|HDTV|REMUX|"
        r"x264|x265|h264|h265|HEVC|10bit|DTS|TrueHD|Atmos|AC3|AAC|DV|Dolby)[\w.\- ]*)$",
        title, re.I)
    if m and len(title[:m.start()].strip()) >= 1:
        return title[:m.start()].strip()
    return title.strip()


def _extract_source_stem(stem, cn_title):
    """从原始文件名提取英文标题+质量信息部分，用于组合「中文标题.英文信息.ext」。
    去掉广告前缀【...】和开头的中文标题，保留英文标题和全部质量/信息标记。
    清洗后若为空（纯中文文件名无英文部分），返回空字符串。"""
    s = re.sub(r"【.*?】", "", stem)                       # 去广告前缀
    if cn_title:
        s = re.sub(rf"^{re.escape(cn_title)}[\s.]*", "", s)  # 去开头中文标题
    return s.strip(". ")


def parse_media(stem):
    """解析文件名，返回 (title, year, info_portion, season, episode)。
    剥离 [信息] 标签和集号后提取标题和年份。"""
    info_portion = extract_info_portion(stem)
    work = re.sub(r"\[[^\]]*\]", "", stem)
    sea, ep = is_episode(work)
    if sea is not None:
        work = re.sub(r"(?<![A-Za-z0-9])[Ss]\d{1,2}[Ee]\d{1,3}(?:[Ee]\d{1,3})?", "", work)
        work = re.sub(r"(?i)SE\d{1,2}[.\s]\d{1,3}", "", work)  # 剥离 SE01.07
        work = re.sub(r"(?<![A-Za-z0-9])[Ee][Pp]?\d{1,3}(?![0-9])", "", work)  # 剥离 Ep01/E01
    ym = YEAR_RE.search(work)
    year = ""
    if ym:
        year = ym.group(1)
        title_part = work[: ym.start()]
    else:
        toks = re.split(r"[._\s\-]+", work)
        ti = []
        for t in toks:
            if re.fullmatch(r"(19\d{2}|20\d{2})", t) and not year:
                year = t
                break
            ti.append(t)
        title_part = " ".join(ti)
    title = _strip_quality_tail(_clean_title(title_part))
    return title, year, info_portion, sea, ep


# ==================== 路径上下文 ====================

def looks_anime(stem, title):
    """检测文件名/标题是否含动漫关键词。"""
    return any(h in (stem + title) for h in ANIME_HINTS)


def folder_kind(abspath):
    """从文件路径推断分类：剧集/动漫/电影/None。"""
    s = str(abspath)
    if "剧集" in s or "电视剧" in s or "/tv/" in s or "/shows/" in s or "/剧/" in s:
        return "tv"
    if "动画" in s or "动漫" in s or "/anime/" in s or "/番/" in s:
        return "anime"
    if "电影" in s or "/movie" in s:
        return "movie"
    return None


def show_name_from_path(abspath):
    """剧集文件名不含剧名时（如 S01E01.HD1080P.中英双字...），从路径提取剧名。
    优先 Season 文件夹的父目录，其次带年份的父目录，最后分类目录下的父目录。"""
    _KIND_NAMES = {"电影", "剧集", "动画", "电视剧", "动漫"}
    p = Path(abspath)
    # 优先: Season 文件夹的父目录
    for parent in p.parents:
        if SEASON_FOLDER_RE.match(parent.name):
            show_folder = parent.parent.name
            cleaned = _clean_title(show_folder)
            cleaned = re.sub(r"\s*[（(]\d{4}[)）]\s*$", "", cleaned).strip()
            if cleaned and cleaned not in _KIND_NAMES:
                return cleaned
    # Fallback 1: 最近的带年份的父目录
    for parent in p.parents:
        if YEAR_RE.search(parent.name):
            cleaned = _clean_title(parent.name)
            cleaned = re.sub(r"\s*[（(]\d{4}[)）]\s*$", "", cleaned).strip()
            if cleaned and cleaned not in _KIND_NAMES:
                return cleaned
    # Fallback 2: 分类目录下的父目录（如 动画/蜡笔小新日语2016全集）
    for parent in p.parents:
        if parent.parent and parent.parent.name in _KIND_NAMES:
            cleaned = _clean_title(parent.name)
            cleaned = re.sub(
                r"(日语|国语|粤语|英语|中字|双语|全集|完整版|全季|合集|"
                r"高清|720p|1080p|2160p|4k|uhd|hdr|web.?dl|bluray).*",
                "", cleaned, flags=re.I)
            ym = re.search(r"(20\d{2}|19\d{2})", cleaned)
            if ym:
                cleaned = cleaned[:ym.start()].strip()
            if cleaned and cleaned not in _KIND_NAMES and len(cleaned) >= 2:
                return cleaned
    return ""


def _year_from_path(abspath):
    """从路径提取年份（Season 文件夹父目录优先，其次最近带年份的父目录）。"""
    p = Path(abspath)
    for parent in p.parents:
        if SEASON_FOLDER_RE.match(parent.name):
            ym = YEAR_RE.search(parent.parent.name)
            if ym:
                return ym.group(1)
            break
    for parent in p.parents:
        ym = YEAR_RE.search(parent.name)
        if ym:
            return ym.group(1)
    return ""


def _extract_season_from_path(abspath):
    """从路径中提取 Season 编号：Season 01 -> 1, S02 -> 2。"""
    p = Path(abspath)
    for parent in p.parents:
        m = re.match(r"^[Ss](\d{1,2})$", parent.name)
        if m:
            return int(m.group(1))
        m = re.match(r"^[Ss]eason\s*(\d{1,2})$", parent.name, re.I)
        if m:
            return int(m.group(1))
    return None


def title_is_junk(title):
    """文件名剥离集号后只剩质量/压制组 token，视为缺剧名。"""
    if not title:
        return True
    return bool(JUNK_TITLE_RE.fullmatch(title))


# ==================== [信息] 标签回退 ====================

def build_info_tag(info_portion, filepath, use_ffprobe=True):
    """四级回退：1 原始文件名 -> 2 ffprobe -> 3 [未标注]。
    use_ffprobe=False 时跳过 ffprobe（快速预演），直接回退 [未标注]。"""
    if info_portion:
        return info_portion, "原始文件名"
    if not use_ffprobe:
        return "[未标注]", "占位(未标注)"
    tag, ok = _ffprobe_info(filepath)
    if ok:
        return tag, "ffprobe"
    return "[未标注]", "占位(未标注)"


def _ffprobe_info(filepath):
    """调用 ffprobe_info.py 提取 [信息] 标签，返回 (tag_str, success)。"""
    try:
        import importlib
        ff = importlib.import_module("ffprobe_info")
        r = ff.extract_info(filepath)
        if not r or r.get("error"):
            return "", False
        info_tag = (r.get("info_tag") or "").strip()
        if not info_tag or info_tag == "未标注":
            return "", False
        tag = f"[{info_tag}]"
        rel = (r.get("release_tag") or "").strip()
        if rel:
            tag += f".[{rel}]"
        return tag, True
    except Exception:
        return "", False


# ==================== 系列检测 ====================

def _series_registry_path():
    """series_registry.json 路径：手工 curated 系列名册（随项目发布，read-only）。"""
    return os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                        "data", "series_registry.json")


def _media_cache_path():
    """media_cache.json 路径：运行时自扩充（known 段，gitignore）。"""
    return os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                        ".cache", "media_cache.json")


def _load_series_registry():
    """加载 curated 系列名册（Level 1a）。失败返回空列表。"""
    try:
        with io.open(_series_registry_path(), encoding="utf-8") as f:
            return json.load(f).get("series", []) or []
    except Exception:
        return []


def _load_media_cache():
    """加载运行时自扩充缓存（known 段）。失败返回空结构。"""
    try:
        with io.open(_media_cache_path(), encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return {"known": {}}


def _load_known():
    """加载 known 段（自扩充的 title->元数据 离线缓存）。"""
    return _load_media_cache().get("known", {}) or {}


def _match_known(title, known):
    """在 known 段按标题查找（精确+模糊）。返回 dict 或 None。"""
    if not known or not title:
        return None
    tl = title.strip().lower()
    for key in (title, tl):
        e = known.get(key)
        if e:
            return e
    for k, e in known.items():
        kl = k.lower()
        if kl == tl or tl in kl or kl in tl:
            return e
    return None


def _meta_lookup(meta, title):
    """在注入元数据索引中按标题查找归一化条目（精确+模糊）。返回 dict 或 None。"""
    if not meta or not title:
        return None
    tl = title.strip().lower()
    for key in (title, tl):
        e = meta.get(key)
        if e:
            return e
    for k, e in meta.items():
        kl = k.lower()
        if kl == tl or tl in kl or kl in tl:
            return e
    return None


def _series_from_path(abspath):
    """Level 0：检查文件是否已在系列文件夹内（如 哈利·波特（系列）/）。
    返回系列文件夹名或 None。优先于元数据查询，避免不必要的查找。"""
    for parent in Path(abspath).parents:
        name = parent.name
        if name.endswith("（系列）") or name.endswith("(系列)"):
            return name
    return None


def _strip_trailing_numeral(base):
    """剥离冒号基名尾部的续集编号（阿拉伯数字+空格，或中文数字）。"""
    base = re.sub(r"\s*\d+$", "", base)            # "僵尸先生2" / "电锯惊魂 8"
    base = re.sub(r"[零一二三四五六七八九十]+$", "", base)
    return base.strip()


def _check_registry(title, series_list):
    """在本地注册表中匹配标题。返回 (series_folder, source) 或 (None, None)。"""
    for entry in series_list:
        for pattern in entry.get("match_patterns", []):
            if pattern.lower() in title.lower() or title.lower() in pattern.lower():
                return entry.get("folder"), "本地注册表"
    return None, None


def _registry_member(title, series_list):
    """标题是否为某 series 的成员；返回 (series_folder, member_dict) 或 None。
    用于衍生剧离线确认（如「灵魂摆渡·十年」是「灵魂摆渡」系列的 tv 成员）。"""
    tl = title.strip()
    for entry in series_list:
        for m in entry.get("members", []):
            if (m.get("title") or "").strip() == tl:
                return entry.get("folder"), m
    return None


def detect_movie_series(title, year, meta, path_hint=None):
    """电影系列检测（四级）：0 文件夹 -> 1 注册表+known -> 2 注入 collection -> 3 启发式。
    返回 (series_folder, source)，独立电影返回 (None, "独立电影")。"""
    # Level 0: 已在系列文件夹内（路径检测，无网络）
    if path_hint:
        sf = _series_from_path(path_hint)
        if sf:
            return sf, "文件夹(系列)"
    # Level 1a: 本地注册表 series 段
    registry = _load_series_registry()
    if registry:
        folder, src = _check_registry(title, registry)
        if folder:
            return folder, src
    # Level 1b: .cache/media_cache.json 的 known 段（自扩充沉淀）
    known = _load_known()
    if known:
        ke = _match_known(title, known)
        if ke and ke.get("series_folder"):
            return ke["series_folder"], "本地缓存(known)"
    # Level 2: 注入元数据 collection（media-lookup 归一化 JSON 的 collection 字段）
    entry = _meta_lookup(meta, title)
    if entry:
        coll = entry.get("collection")
        if coll:
            sf = series_from_collection(coll)
            if sf:
                return sf, "元数据(合集)"
    # Level 3: 启发式（中点 -> 冒号）
    m = MIDDOT_RE.match(title)
    if m and len(m.group(1)) >= 3:
        return f"{m.group(1).strip()}（系列）", "启发式(中点)"
    if re.search(r"[：:]", title):
        base = _strip_trailing_numeral(re.split(r"[：:]", title, 1)[0].strip())
        if len(base) >= 3:
            return f"{base}（系列）", "启发式(冒号)"
    return None, "独立电影"


# ==================== 目标构建 ====================

def fmt_filename(title, year, info_str, ext, season=None, episode=None,
                 source_title=None, source_stem=None):
    """构造规范文件名。剧集含 SXXEYY，电影含 (年份)。
    当 source_title(英文解析标题) 与 title(中文元数据标题) 不同且 source_stem 非空时，
    组合为「中文标题.原始英文信息.ext」以保留全部质量/分辨率信息。"""
    safe_title = title.strip()
    if season is not None:
        s, e = f"{season:02d}", f"{(episode or 1):02d}"
        base = f"{safe_title} - S{s}E{e}"
        info = info_str if (info_str and info_str.strip()) else "[未标注]"
        return f"{base} {info}.{ext}"
    # 电影：中文标题与英文解析标题不同 -> 组合格式（信息全面）
    if (source_title and source_stem
            and source_title.strip().lower() != safe_title.lower()):
        return f"{safe_title}.{source_stem}.{ext}"
    base = f"{safe_title} ({year})" if year else f"{safe_title} (未知年份)"
    info = info_str if (info_str and info_str.strip()) else "[未标注]"
    return f"{base} {info}.{ext}"


def safe_name(name):
    """文件名安全化：替换非法字符。"""
    return re.sub(r'[\\/:\*\?"<>|]', "_", name).strip()


def resolve_episode_show(title, year, meta):
    """剧名保留源文件名；年份优先取注入元数据，缺失时保持原样。
    非必要不查：年份已有时不查元数据。"""
    st, sy = title, year
    if not sy:
        e = _meta_lookup(meta, st)
        if e and e.get("year"):
            sy = str(e["year"])[:4]
    return st, sy


def _resolve_tv_kind(stem, title, fkind, eff_title, year, meta):
    """剧集分类决策（三级）：关键词 -> 文件夹上下文 -> 注入元数据 genres 回退。
    返回 'anime'(动漫) 或 'tv'(剧集)。"""
    if looks_anime(stem, title):
        return "anime"
    if fkind == "anime":
        return "anime"
    if fkind == "tv":
        return "tv"
    # 无文件夹上下文，注入元数据 genres 回退（归一化 genres 名表含「动画」则归动漫）
    e = _meta_lookup(meta, eff_title or title)
    if e and is_animated(e.get("genres")) is True:
        return "anime"
    return "tv"


# ==================== 分类主逻辑 ====================

def classify(abspath, stem, ext, meta, no_ffprobe):
    """阶段一：解析 -> 分类 -> 系列检测，返回带目标路径的 plan dict。

    分类优先级：
      1. 剧场版/OVA/OAD/SP/番外 -> 强制电影路径（即使检测到集号）
      2. 衍生剧(·标题) -> 剧名·特别篇 衍生剧路径
      3. 有集号(SxxExx/裸数字) -> 剧集/动漫路径
      4. 无集号 -> 电影路径（含系列检测）

    衍生剧疑似但无元数据/注册表确认时，返回 status="pending_lookup"，
    由编排器调 media-lookup 补全后带 --metadata 重试。
    """
    title, year, info_portion, sea, ep = parse_media(stem)
    fkind = folder_kind(abspath)
    info_str, src = build_info_tag(info_portion, str(abspath), use_ffprobe=not no_ffprobe)
    series_folder = None
    is_spinoff = False
    status = "resolved"
    need_lookup = None
    src_stem_val = ""     # 清洗后的原始英文文件名（用于组合命名）
    src_title_val = ""    # 解析出的英文标题（与中文标题不同时非空）

    # 剧场版/OVA/OAD/SP/番外 强制走电影路径（即使检测到集号）
    is_movie_format = any(kw in title for kw in MOVIE_FORMAT_KEYWORDS)
    if is_movie_format:
        sea, ep = None, None

    # ---- 衍生剧(·标题)检测：注入元数据 > 注册表成员 > 否则 pending_lookup ----
    spin = None
    if "·" in title and fkind != "movie":
        full_entry = _meta_lookup(meta, title)
        mm = MIDDOT_RE.match(title)
        base_name = mm.group(1).strip() if (mm and len(mm.group(1)) >= 3) else ""
        base_entry = _meta_lookup(meta, base_name) if base_name else None
        spin = detect_spinoff(title, year, full_entry, base_entry)
        if not (spin and spin.get("is_spinoff")):
            # 元数据未确认 -> 退而查注册表成员（如「灵魂摆渡·十年」是已知 tv 成员）
            rm = _registry_member(title, _load_series_registry())
            if rm and (rm[1].get("type") == "tv" or not rm[1].get("type")):
                spin = {"is_spinoff": True, "base_name": _strip_series_suffix(rm[0]),
                        "base_year": str(rm[1].get("year", ""))[:4]}
            elif spin and spin.get("need"):
                need_lookup = {"title": title, "year": year, "media_type_hint": "tv",
                               "need": ["spinoff_check"], "reason": spin.get("reason", ""),
                               "extra_queries": [{"title": base_name, "media_type": "tv"}] if base_name else []}

    if spin and spin.get("is_spinoff"):
        kind = _resolve_tv_kind(stem, title, fkind, title, year, meta)
        is_spinoff = True
        sea, ep = 0, 1
        show_title = spin.get("base_name", title)
        show_year = spin.get("base_year", year)
        info_source = "元数据衍生剧" if (_meta_lookup(meta, title) or _meta_lookup(meta, show_title)) else "注册表衍生剧"
        fname = fmt_filename(title, show_year, info_str, ext, season=0, episode=1)
        special_folder = f"{show_title}·特别篇"
        rel = (f"{KIND_DIR[kind]}/{safe_name(show_title)}/"
               f"{safe_name(special_folder)}/{safe_name(fname)}")
    elif need_lookup:
        status = "pending_lookup"
        kind = _resolve_tv_kind(stem, title, fkind, title, year, meta)
        info_source = "待补全(衍生剧)"
        fname = fmt_filename(title, year, info_str, ext)
        rel = f"{KIND_DIR[kind]}/{safe_name(title)} ({year or '未知'})/{safe_name(fname)}"
    elif sea is not None and not is_movie_format:
        # ---- 有明确集号(SxxExx) -> 剧集/动漫 ----
        kind = _resolve_tv_kind(stem, title, fkind, title, year, meta)
        folder_season = _extract_season_from_path(abspath)
        if folder_season:
            sea = folder_season
        folder_show = show_name_from_path(abspath)
        eff_title = folder_show or title
        if not eff_title:
            parent_name = Path(abspath).parent.name
            cleaned = _clean_title(parent_name)
            pym = YEAR_RE.search(parent_name)
            if pym:
                year = pym.group(1)
                cleaned = re.sub(r"\s*[（(]\d{4}[)）]\s*$", "", cleaned).strip()
            elif year:
                eff_title = year
                year = ""
            if cleaned:
                eff_title = cleaned
        if not year:
            folder_year = _year_from_path(abspath)
            if folder_year:
                year = folder_year
        show_title, show_year = resolve_episode_show(eff_title, year, meta)
        em = bool(_meta_lookup(meta, eff_title))
        info_source = ("文件夹剧名" if folder_show else "文件名") + ("+元数据" if em else "")
        fname = fmt_filename(show_title, show_year, info_str, ext, season=sea, episode=ep)
        rel = f"{KIND_DIR[kind]}/{safe_name(show_title)} ({show_year or '未知'})/Season {sea:02d}/{safe_name(fname)}"
    elif fkind in ("tv", "anime") and not is_movie_format:
        # ---- 剧集目录下的裸数字集号回退 ----
        ep_num, bare_title = _detect_bare_episode(stem)
        if ep_num is not None and 1 <= ep_num <= 999:
            folder_show = show_name_from_path(abspath)
            sea_from_folder = _extract_season_from_path(abspath)
            sea = sea_from_folder or 1
            ep = ep_num
            eff_title = folder_show or bare_title or title
            kind = _resolve_tv_kind(stem, title, fkind, eff_title, year, meta)
            if not year:
                folder_year = _year_from_path(abspath)
                if folder_year:
                    year = folder_year
            show_title, show_year = resolve_episode_show(eff_title, year, meta)
            info_source = "裸数字集号" + (f"+Season{sea:02d}文件夹" if sea_from_folder else "")
            fname = fmt_filename(show_title, show_year, info_str, ext, season=sea, episode=ep)
            rel = f"{KIND_DIR[kind]}/{safe_name(show_title)} ({show_year or '未知'})/Season {sea:02d}/{safe_name(fname)}"
        else:
            series_folder, ssrc = detect_movie_series(title, year, meta, abspath)
            kind = "movie"
            info_source = ssrc
            fname = fmt_filename(title, year, info_str, ext)
            if series_folder:
                rel = f"电影/{safe_name(series_folder)}/{safe_name(fname)}"
            else:
                rel = f"电影/{safe_name(title)} ({year or '未知'})/{safe_name(fname)}"
    else:
        # ---- 无集号 -> 电影路径（含系列检测）----
        series_folder, ssrc = detect_movie_series(title, year, meta, abspath)
        # 查元数据：通过 original_title 可匹配到中文标题条目
        meta_entry = _meta_lookup(meta, title)
        display_title = title
        used_meta = False
        if meta_entry:
            meta_title = (meta_entry.get("title") or "").strip()
            if meta_title and meta_title.lower() != title.lower():
                display_title = meta_title
                src_stem_val = _extract_source_stem(stem, meta_title)
                src_title_val = title
            if meta_entry.get("year"):
                yr = str(meta_entry["year"])[:4]
                if yr and (not year or yr != year):
                    year = yr
                used_meta = True
        kind = "movie"
        info_source = ssrc + ("+元数据" if used_meta else "")
        fname = fmt_filename(display_title, year, info_str, ext,
                             source_title=src_title_val or None,
                             source_stem=src_stem_val or None)
        if series_folder:
            rel = f"电影/{safe_name(series_folder)}/{safe_name(fname)}"
        else:
            rel = f"电影/{safe_name(display_title)} ({year or '未知'})/{safe_name(fname)}"
        # 元数据有中文标题时，用中文标题替换 plan 的 title（影响显示/降级/缓存）
        if display_title != title:
            title = display_title

    return {
        "src": str(abspath), "title": title, "year": year, "kind": kind,
        "info_source": info_source, "info_str": info_str, "ext": ext,
        "season": sea, "episode": ep,
        "series": series_folder if series_folder else ("衍生剧S00" if is_spinoff else None),
        "status": status, "need_lookup": need_lookup,
        "_rel": rel,
        "_source_title": src_title_val,
        "_source_stem": src_stem_val,
    }


def _detect_bare_episode(stem):
    """检测剧集目录下的裸数字集号。
    尝试 4 种模式：末尾裸数字、纯数字文件名、开头数字、括号集号。
    返回 (episode_num, bare_title)，未检测到返回 (None, "")。"""
    ep_num = None
    bare_title = ""

    # 1) 末尾裸数字：标题+数字（夏娃01, 甄嬛传26）
    bare = EPISODE_BARE_RE.search(stem)
    if bare:
        ep_num = int(bare.group(2))
        bare_title = re.sub(r"\d{1,3}(?=\.\w+$|$)", "", stem)
        bare_title = re.sub(r"\[.*\]", "", bare_title)
        bare_title = _strip_quality_tail(_clean_title(bare_title))

    # 2) 纯数字文件名：01.mp4, 03.mp4（Season 文件夹提供季号和剧名）
    if ep_num is None:
        pure = re.match(r"^(\d{1,3})$", stem)
        if pure:
            ep_num = int(pure.group(1))
            bare_title = ""

    # 3) 开头数字：01-4K.高码率, 02.1080p（Season 文件夹提供季号）
    if ep_num is None:
        lead = EPISODE_LEADING_RE.match(stem)
        if lead:
            ep_num = int(lead.group(1))
            bare_title = re.sub(r"^\d{1,3}[-_.\s]", "", stem)
            bare_title = re.sub(r"\[.*\]", "", bare_title)
            bare_title = _strip_quality_tail(_clean_title(bare_title))

    # 4) 括号集号：[170], [02]（常见于字幕组命名 [组名][剧名][集号][规格]）
    if ep_num is None:
        bracket_nums = re.findall(r"\[(\d{1,3})\]", stem)
        for b in bracket_nums:
            n = int(b)
            if 1 <= n <= 999 and not (1900 <= n <= 2099):
                ep_num = n
                break
        if ep_num is not None:
            bare_title = _strip_quality_tail(_clean_title(
                re.sub(r"\[.*?\]", "", stem)))

    if ep_num is not None and ep_num > 999:
        # 裸数字过大（可能是年份/续集编号），不作为集号
        return None, ""

    return ep_num, bare_title


# ==================== 剧集系列归组 ====================

def _split_theme(title):
    """从标题中提取主题名。如果标题含「·」且基名>=3字，返回 (base, theme)。
    否则返回 (title, None)。用于区分：
      灵魂摆渡·十年 -> ('灵魂摆渡', '十年')  主题分隔
      后宫·甄嬛传 -> ('后宫·甄嬛传', None)  译名中点(基名<3字)
    """
    m = MIDDOT_RE.match(title)
    if m:
        base = m.group(1).strip()
        theme = m.group(2).strip()
        if len(base) >= 3 and len(theme) >= 2:
            if not _is_generic_season_name(theme, base):
                return base, theme
    return title, None


def _normalize_show_key(title):
    """归一化剧名用于分组：去书名号/年份后缀/空格/主题后缀，小写。"""
    t = title.replace("《", "").replace("》", "")
    t = re.sub(r"\s*[（(]\d{4}[)）]\s*$", "", t).strip()
    # 去主题后缀：灵魂摆渡·十年 -> 灵魂摆渡（使衍生剧与母剧归组）
    base, theme = _split_theme(t)
    if theme:
        t = base
    return t.lower()


def _get_season_names(show_title, meta):
    """从注入元数据读取季主题名。返回 {season_num: season_name} 或空 dict。
    跳过空名/S00/与剧名相同/通用季名。"""
    e = _meta_lookup(meta, show_title)
    if not e:
        return {}
    seasons = {}
    for s in e.get("seasons", []):
        sstr = s.get("season") or "S0"
        snum = int(sstr[1:]) if sstr.startswith("S") and sstr[1:].isdigit() else 0
        sname = (s.get("name") or "").strip()
        if snum <= 0 or not sname:
            continue
        if sname.lower() == show_title.lower():
            continue
        if _is_generic_season_name(sname, show_title):
            continue
        m = re.match(r"^第\s*[零一二三四五六七八九十\d]+\s*季\s*", sname)
        if m:
            stripped = sname[m.end():].strip()
            if stripped and not _is_generic_season_name(stripped, show_title):
                sname = stripped
            else:
                continue
        seasons[snum] = sname
    return seasons


def _is_generic_season_name(sname, show_title):
    """判断季名是否为通用名（非主题），应跳过不用于格式3。"""
    sl = sname.lower().strip()
    if sl in ("season 1", "season 2", "season 3", "season 4", "season 5",
              "season 6", "season 7", "season 8", "specials", "特别篇"):
        return True
    if sl == show_title.lower().strip():
        return True
    if re.match(r"^第\s*[零一二三四五六七八九十\d]+\s*季$", sname):  # 第N季
        return True
    if sname.isdigit():
        return True
    return False


def finalize_tv_shows(plans, tv_format="season", meta=None):
    """阶段 1.5：剧集系列归组后处理。

    按 show_title 分组，统计季数：
    - 单季 -> 独立格式: 剧集/剧名 (年份)/剧名 - SXXEYY [信息].ext
    - 多季 + 主题名(来自注入元数据) -> 格式3: 剧集/剧名/剧名·主题(年份)/剧名·主题 - SXXEYY [信息].ext
    - 多季无主题名 + tv_format=year -> 格式1: 剧集/剧名/剧名 (年份)/剧名 - SXXEYY [信息].ext
    - 多季无主题名 -> 格式2: 剧集/剧名/剧名·第N季/剧名 - SXXEYY [信息].ext
    - 衍生剧(特别篇) 不改，已由 classify() 处理

    跳过 pending_lookup / already_organized 的 plan。
    动漫同理（KIND_DIR["anime"] = "动漫"）。
    返回 (multi_count, single_count)。
    """
    tv_groups = {}
    for p in plans:
        if p["kind"] not in ("tv", "anime"):
            continue
        if p.get("series") == "衍生剧S00":
            continue  # 衍生剧不改
        if p.get("status") != "resolved":
            continue  # 跳过 pending_lookup / already_organized
        rel_parts = p["_rel"].split("/")
        if len(rel_parts) < 2:
            continue
        folder_name = rel_parts[1]
        show_title = re.sub(r"\s*[（(](?:\d{4}|未知)[)）]\s*$", "", folder_name).strip()
        show_title = show_title.replace("《", "").replace("》", "").strip()
        if not show_title:
            continue
        src_base, src_theme = _split_theme(show_title)
        if src_theme:
            show_title = src_base
        ym = YEAR_RE.search(folder_name)
        show_year = ym.group(1) if ym else p.get("year", "")

        show_key = _normalize_show_key(show_title)
        if show_key not in tv_groups:
            tv_groups[show_key] = {
                "plans": [], "seasons": set(), "show_title": show_title, "show_year": show_year,
                "source_themes": {},
            }
        tv_groups[show_key]["plans"].append(p)
        if src_theme and p.get("season") and p["season"] > 0:
            tv_groups[show_key]["source_themes"][p["season"]] = src_theme
        if p["season"] is not None and p["season"] > 0:
            tv_groups[show_key]["seasons"].add(p["season"])

    multi_count = 0
    single_count = 0
    for show_key, grp in tv_groups.items():
        seasons = sorted(grp["seasons"])
        show_title = grp["show_title"]
        show_year = grp["show_year"]
        is_multi = len(seasons) > 1

        if is_multi:
            multi_count += 1
            theme_map = dict(grp.get("source_themes", {}))
            meta_themes = _get_season_names(show_title, meta)
            for sn, tn in meta_themes.items():
                if sn not in theme_map:
                    theme_map[sn] = tn
            kind_dir = None
            for p in grp["plans"]:
                kind_dir = KIND_DIR.get(p["kind"], "剧集")
                break

            for p in grp["plans"]:
                sea = p["season"]
                if sea is None or sea <= 0:
                    continue
                s_str = f"{sea:02d}"
                e_str = f"{(p['episode'] or 1):02d}"
                info = p["info_str"] if p["info_str"] and p["info_str"].strip() else "[未标注]"

                if sea in theme_map:
                    theme = theme_map[sea]
                    season_year = _get_season_year(show_title, sea, meta)
                    fname = f"{show_title}·{theme} - S{s_str}E{e_str} {info}.{p['ext']}"
                    season_folder = (f"{show_title}·{theme} ({season_year})"
                                     if season_year else f"{show_title}·{theme}")
                    p["_rel"] = f"{kind_dir}/{safe_name(show_title)}/{safe_name(season_folder)}/{safe_name(fname)}"
                    p["info_source"] = p.get("info_source", "") + " | 格式3(主题)"
                elif tv_format == "year" and _get_season_year(show_title, sea, meta):
                    season_year = _get_season_year(show_title, sea, meta)
                    fname = f"{show_title} - S{s_str}E{e_str} {info}.{p['ext']}"
                    season_folder = f"{show_title} ({season_year})"
                    p["_rel"] = f"{kind_dir}/{safe_name(show_title)}/{safe_name(season_folder)}/{safe_name(fname)}"
                    p["info_source"] = p.get("info_source", "") + " | 格式1(年份)"
                else:
                    cn_season = _int_to_cn(sea)
                    fname = f"{show_title} - S{s_str}E{e_str} {info}.{p['ext']}"
                    season_folder = f"{show_title}·第{cn_season}季"
                    p["_rel"] = f"{kind_dir}/{safe_name(show_title)}/{safe_name(season_folder)}/{safe_name(fname)}"
                    p["info_source"] = p.get("info_source", "") + " | 格式2(第N季)"
        else:
            single_count += 1
            for p in grp["plans"]:
                sea = p["season"] or 1
                s_str = f"{sea:02d}"
                e_str = f"{(p['episode'] or 1):02d}"
                info = p["info_str"] if p["info_str"] and p["info_str"].strip() else "[未标注]"
                fname = f"{show_title} - S{s_str}E{e_str} {info}.{p['ext']}"
                kind_dir = KIND_DIR.get(p["kind"], "剧集")
                p["_rel"] = f"{kind_dir}/{safe_name(show_title)} ({show_year or '未知'})/{safe_name(fname)}"
                p["info_source"] = p.get("info_source", "") + " | 独立格式"

    return multi_count, single_count


def _get_season_year(show_title, season_num, meta):
    """从注入元数据读取指定季的年份。"""
    e = _meta_lookup(meta, show_title)
    if not e:
        return ""
    for s in e.get("seasons", []):
        sstr = s.get("season") or "S0"
        snum = int(sstr[1:]) if sstr.startswith("S") and sstr[1:].isdigit() else 0
        if snum == season_num:
            return str(s.get("year") or "")[:4]
    return ""


# ==================== 阶段二：降级 + 执行 ====================

def finalize_target(p, base, demote):
    """阶段二：按系列成员数决定最终目标。单成员系列降级为独立电影。"""
    if p.get("status") == "already_organized":
        p["rel"] = p["_rel"]
        p["target"] = str(base / p["rel"]) if p["_rel"] else str(p["src"])
        return p
    if demote and p["kind"] == "movie" and p["series"] and p["series"] != "衍生剧S00":
        fname = fmt_filename(p["title"], p["year"], p["info_str"], p["ext"],
                             source_title=p.get("_source_title") or None,
                             source_stem=p.get("_source_stem") or None)
        p["_rel"] = f"电影/{safe_name(p['title'])} ({p['year'] or '未知'})/{safe_name(fname)}"
        p["series"] = None
        p["info_source"] = "独立电影(单成员降级)"
    p["rel"] = p["_rel"]
    p["target"] = str(base / p["rel"])
    return p


def scan_videos(root):
    """遍历根目录，返回视频文件列表 [(abspath, stem, ext), ...]。

    自动跳过伪装文件(图片冒充视频扩展名): 这类文件非真正视频，绝不应归档入库；
    残留可用 --purge-junk 清理。判断依据文件头 magic(PNG/JPEG/GIF/BMP)，
    真正的 mkv/mp4/ts 等文件头不会与之冲突，无误判。
    """
    out = []
    for dirpath, _dirs, files in os.walk(root):
        for fn in files:
            if SKIP_PATTERNS.search(fn):
                continue
            stem, ext = split_ext(fn)
            if ext not in VIDEO_EXTS:
                continue
            fp = Path(dirpath) / fn
            if _looks_like_image(fp):  # 图片冒充视频 -> 跳过，交由 --purge-junk 清理
                continue
            out.append((fp, stem, ext))
    return out


def _move_file(src, tgt):
    """移动文件：同文件系统原子 mv，跨文件系统 cp+校验+rm。"""
    try:
        os.replace(src, tgt)
    except OSError:
        sz = src.stat().st_size
        shutil.copy2(str(src), str(tgt))
        if tgt.stat().st_size != sz:
            raise IOError("字节数校验失败")
        src.unlink()


def cleanup_empty_dirs(root):
    """移动后清理空目录（仅 root 之下，不删 root 自身）。"""
    removed = 0
    for dirpath, dirs, files in os.walk(root, topdown=False):
        if Path(dirpath) == Path(root):
            continue
        if not dirs and not files:
            try:
                os.rmdir(dirpath)
                removed += 1
            except OSError:
                pass
    return removed


# ==================== 无用文件清理（--purge-junk）====================
# 下载资源包常夹带广告图片/推广文本/站点nfo/伪装视频(图片冒充mkv)/sample，整理后残留下载目录。
_JUNK_IMG_EXTS = {"png", "jpg", "jpeg", "webp", "bmp", "gif"}
_JUNK_DOC_EXTS = {"nfo", "url", "htm", "html"}
# 推广特征：网址 或 广告词
_AD_URL_RE = re.compile(r"www\.|https?://|[.\s](com|net|org|xyz|cn|me|info|vip|top)\b", re.I)
_AD_WORD_RE = re.compile(
    r"请访问|无水印|高清电影|蓝光电影|蓝光原盘|影视之家|影视发布|"
    r"更多[\u4e00-\u9fff]{0,8}(?:电影|蓝光)|BT下载|磁力下载|迅雷下载|网址|官网|推广")
# 非正片视频标记
_SAMPLE_VIDEO_RE = re.compile(
    r"(?i)(?:^|[.\s\[\-])(sample|trailer|预告片?|花絮|bonus|extra|特典|菜单|promo)(?:[.\s\]\-]|$)")


def _looks_like_image(filepath):
    """读文件头判断是否图片（伪装成视频扩展名的图片）。"""
    try:
        with open(filepath, "rb") as f:
            head = f.read(4)
    except OSError:
        return False
    return head.startswith((b"\x89PNG", b"\xff\xd8\xff", b"GIF8", b"BM"))


def _classify_junk(fp, fn, ext):
    """返回无用文件原因字符串，非无用返回空串。

    识别: 广告图片 / 推广文本 / 站点 nfo / 伪装视频(图片冒充) / sample 预告花絮。
    字幕(.srt/.ass/.ssa) 与主视频一律保留。
    """
    # 广告图片: 图片扩展名 + 文件名含推广特征
    if ext in _JUNK_IMG_EXTS:
        return "广告图片" if (_AD_URL_RE.search(fn) or _AD_WORD_RE.search(fn)) else ""
    # 站点/推广文件: nfo/url/htm/html 在媒体下载包中恒为无用(场景发布信息/网页快捷方式)
    if ext in _JUNK_DOC_EXTS:
        return "站点/推广文件"
    # 推广文本 txt: 需含明确广告词才删(避免误删仅含单一网址的笔记/索引)
    if ext == "txt":
        try:
            content = Path(fp).read_text(encoding="utf-8", errors="ignore")[:4096]
        except OSError:
            content = ""
        return "推广文本" if _AD_WORD_RE.search(content) else ""
    # 视频扩展名: 伪装图片 / sample 预告花絮
    if ext in VIDEO_EXTS:
        if _looks_like_image(fp):
            return "伪装图片(视频扩展名)"
        if _SAMPLE_VIDEO_RE.search(fn):
            return "sample/预告/花絮"
        return ""
    return ""


def cleanup_junk_files(root, commit=False):
    """识别并删除无用文件，返回 [(abspath, reason), ...]。

    commit=False 只报告不删；commit=True 实际删除。
    在整理流程「移动视频后、清空目录前」调用，确保视频已迁出再清残留。
    """
    junk = []
    for dirpath, _dirs, files in os.walk(root):
        for fn in files:
            fp = Path(dirpath) / fn
            ext = split_ext(fn)[1].lower()
            reason = _classify_junk(fp, fn, ext)
            if reason:
                junk.append((str(fp), reason))
    if not junk:
        return []
    for fp, reason in junk:
        act = "删除" if commit else "将删(预演)"
        print(f"[清理] {act}: {Path(fp).name}  ({reason})")
    if commit:
        for fp, _ in junk:
            try:
                os.remove(fp)
            except OSError:
                pass
    return junk


def _build_meta_index(args):
    """从 --metadata(JSON 字符串) 或 --metadata-file 构建标题->归一化条目 索引。
    同时按 title(中文标题) 和 original_title(英文原名) 建索引，
    使文件名解析出的英文标题也能匹配到元数据条目。"""
    raw = None
    if getattr(args, "metadata_file", ""):
        with io.open(args.metadata_file, encoding="utf-8") as f:
            raw = json.load(f)
    elif getattr(args, "metadata", ""):
        raw = json.loads(args.metadata)
    if not raw:
        return {}
    entries = raw if isinstance(raw, list) else [raw]
    idx = {}
    for e in entries:
        if not isinstance(e, dict):
            continue
        t = (e.get("title") or "").strip()
        if t:
            idx[t] = e
            idx[t.lower()] = e
        ot = (e.get("original_title") or "").strip()
        if ot and ot not in idx:
            idx[ot] = e
            idx[ot.lower()] = e
    return idx


def _already_organized(abspath, stem):
    """文件是否已处于规范归档位置（规范命名 + 正确分类目录）。
    命中则跳过解析（已归档文件名自带 [信息]，无需 ffprobe/元数据）。"""
    kind = folder_kind(abspath)
    if kind == "movie":
        return bool(YEAR_RE.search(stem))
    if kind in ("tv", "anime"):
        return bool(EPISODE_RE.search(stem)) or bool(EPISODE_CN_RE.search(stem))
    return False


def _strip_series_suffix(folder):
    """系列文件夹名（XX（系列））-> 基名（XX）。"""
    if not folder:
        return ""
    f = folder.strip()
    for suf in ("（系列）", "(系列)"):
        if f.endswith(suf):
            return f[: -len(suf)].strip()
    return f


def _save_learned_series(plans):
    """将本次经注入元数据解析出的系列写回 .cache/media_cache.json 的 known 段（自扩充）。
    只记录 resolved 且使用了元数据的系列标题，从不查 TMDB。"""
    cache = _load_media_cache()
    known = cache.setdefault("known", {})
    if not isinstance(known, dict):
        known = {}
        cache["known"] = known
    changed = False
    for p in plans:
        if p.get("status") != "resolved":
            continue
        if "元数据" not in (p.get("info_source") or "") or not p.get("series"):
            continue
        t = (p.get("title") or "").strip()
        if not t or t in known:
            continue
        known[t] = {"year": p.get("year", ""), "kind": p.get("kind", ""),
                    "series_folder": p.get("series", ""), "source": "learned"}
        changed = True
    if changed:
        try:
            with io.open(_media_cache_path(), "w", encoding="utf-8") as f:
                json.dump(cache, f, ensure_ascii=False, indent=2)
        except Exception:
            pass
    return changed


def main():
    """CLI 主流程：扫描 -> 分类 -> 归组 -> 降级 -> 迁移。"""
    ap = argparse.ArgumentParser(description="批量媒体库整理器(media-organizer 规则)")
    ap.add_argument("root", help="待整理根目录(如 /media/downloads/inbox 或 /media/movies)")
    ap.add_argument("--base", default="/media/movies", help="影音库根(默认 /media/movies)")
    ap.add_argument("--commit", action="store_true", help="实际执行移动(默认只预演)")
    ap.add_argument("--overwrite", action="store_true", help="目标已存在时覆盖(默认跳过)")
    ap.add_argument("--report", default="", help="写入计划 JSON 到此文件")
    ap.add_argument("--no-ffprobe", action="store_true", help="跳过 ffprobe(快速预演,[信息]用[未标注])")
    ap.add_argument("--tv-format", choices=["season", "year"], default="season",
                    help="多季剧集文件夹格式: season=第N季(默认) | year=年份标注(需注入季年份)")
    ap.add_argument("--metadata", default="", help="注入元数据(JSON 数组, media-lookup 归一化结果)")
    ap.add_argument("--metadata-file", default="", help="注入元数据文件路径(同 --metadata)")
    ap.add_argument("--fast", action="store_true",
                    help="离线尽力而为,不输出 pending_lookup(快速预演)")
    ap.add_argument("--rescan", action="store_true",
                    help="不跳过已归档文件(强制重新解析整库)")
    ap.add_argument("--purge-junk", action="store_true",
                    help="删除无用文件(广告图片/推广文本/nfo/伪装视频/sample); 预演只报告, 配合 --commit 实际删除")
    args = ap.parse_args()

    root = Path(args.root).resolve()
    base = Path(args.base).resolve()
    meta = _build_meta_index(args)
    if args.fast:
        meta = {}
        print("[INFO] --fast 模式: 离线尽力而为(文件名+注册表+启发式+文件夹结构), 不输出 pending_lookup", file=sys.stderr)
    elif meta:
        n_meta = len(set(id(v) for v in meta.values())); print(f"[INFO] 已注入 {n_meta} 条元数据(来自 media-lookup)", file=sys.stderr)
    if not root.exists():
        print(f"[ERROR] 根目录不存在: {root}", file=sys.stderr)
        sys.exit(1)

    videos = scan_videos(root)
    print(f"[扫描] {root} 下视频文件 {len(videos)} 个", file=sys.stderr)

    # 阶段一：逐文件解析 + 系列检测（已归档文件默认跳过）
    plans, errors = [], 0
    skipped_organized = 0
    for abspath, stem, ext in videos:
        if not args.rescan and _already_organized(abspath, stem):
            try:
                rel = str(abspath.relative_to(base))
            except ValueError:
                rel = ""
            plans.append({"src": str(abspath), "title": "", "year": "", "kind": "movie",
                          "info_source": "已就位(规范路径)", "info_str": "", "ext": ext,
                          "season": None, "episode": None, "series": None,
                          "status": "already_organized", "need_lookup": None, "_rel": rel})
            skipped_organized += 1
            continue
        try:
            p = classify(abspath, stem, ext, meta, args.no_ffprobe)
            if args.fast and p["status"] == "pending_lookup":
                p["status"] = "resolved"
                p["need_lookup"] = None
                p["info_source"] = (p.get("info_source", "") or "") + "(fast降级)"
            plans.append(p)
        except Exception as e:
            print(f"[ERR] {Path(abspath).name}: {e}", file=sys.stderr)
            errors += 1
    if skipped_organized:
        print(f"[跳过] {skipped_organized} 个已归档文件(规范路径, --rescan 可重扫)", file=sys.stderr)

    # 阶段 1.5：剧集系列归组
    multi_tv, single_tv = finalize_tv_shows(plans, tv_format=args.tv_format, meta=meta)
    if multi_tv or single_tv:
        print(f"[剧集] 多季系列 {multi_tv} 部, 单季独立 {single_tv} 部", file=sys.stderr)

    # 阶段二：统计各系列成员数，单成员系列降级为独立电影
    series_counts = Counter(
        p["series"] for p in plans
        if p.get("series") and p["series"] != "衍生剧S00" and p.get("status") == "resolved"
    )
    demoted_set = {s for s, c in series_counts.items() if c < 2}
    if demoted_set:
        print(f"[降级] {len(demoted_set)} 个单成员系列将降级为独立电影: {sorted(demoted_set)}", file=sys.stderr)

    # 阶段三：确定最终目标 + 执行
    done, skipped = 0, 0
    pending = 0
    for p in plans:
        if p.get("status") == "pending_lookup":
            pending += 1
            print(f"[待补全] {p['title']} ({p['year']}) -> {p['need_lookup']['reason']}")
            print(f"      源: {p['src']}")
            continue
        finalize_target(p, base, p.get("series") in demoted_set)
        if p.get("status") == "already_organized":
            skipped += 1
            tag = "已就位"
        else:
            src_p, tgt_p = Path(p["src"]), Path(p["target"])
            if src_p.resolve() == tgt_p.resolve():
                skipped += 1
                tag = "已就位"
            elif tgt_p.exists() and not args.overwrite:
                skipped += 1
                tag = "目标已存在(跳过)"
            else:
                tag = "待移动" if not args.commit else "已移动"
                if args.commit:
                    tgt_p.parent.mkdir(parents=True, exist_ok=True)
                    try:
                        if tgt_p.exists() and args.overwrite:
                            tgt_p.unlink()
                        _move_file(src_p, tgt_p)
                        done += 1
                    except Exception as e:
                        print(f"[ERR 移动] {src_p} -> {tgt_p}: {e}", file=sys.stderr)
                        errors += 1
                        continue
        series = f" | 系列:{p['series']}" if p.get("series") else ""
        print(f"[{tag}] ({p['kind']}) {p['title']} ({p['year']}){series}")
        print(f"      源:   {p['src']}")
        if p.get("target"):
            print(f"      目标: {p['target']}")
        print(f"      信息来源: {p['info_source']}")

    # 自扩充：本次经元数据解析出的系列沉淀到 .cache/media_cache.json
    if args.commit and _save_learned_series(plans):
        print("[缓存] 本次新学系列已沉淀到 .cache/media_cache.json (known 段)", file=sys.stderr)

    # 阶段四：清理无用文件（--purge-junk 启用，须在移动视频后、清空目录前）
    purged = []
    if args.purge_junk:
        purged = cleanup_junk_files(root, commit=args.commit)
        if purged:
            print(f"[清理] 无用文件 {len(purged)} 个" +
                  ("(已删除)" if args.commit else "(预演,未删)"), file=sys.stderr)

    if args.commit:
        emptied = cleanup_empty_dirs(root)
        if emptied:
            print(f"[清理] 删除空目录 {emptied} 个", file=sys.stderr)

    if args.report:
        with io.open(args.report, "w", encoding="utf-8") as f:
            json.dump({"plans": plans, "summary": {
                "total": len(plans), "moved": done, "skipped": skipped, "errors": errors,
                "pending_lookup": pending, "already_organized": skipped_organized,
                "series_counts": dict(series_counts), "demoted": sorted(demoted_set),
                "junk_purged": len(purged),
            }}, f, ensure_ascii=False, indent=2)
        print(f"[报告] 已写入 {args.report}", file=sys.stderr)

    print(f"\n[汇总] 共 {len(plans)} | 移动 {done} | 跳过 {skipped} | 待补全 {pending} | 错误 {errors}"
          + ("  (预演模式,未改动文件)" if not args.commit else "  (已提交)"), file=sys.stderr)
    if pending and not args.fast:
        print("[提示] 存在待补全项: 请编排器调 media-lookup 取回元数据后, 带 --metadata / --metadata-file 重试", file=sys.stderr)


if __name__ == "__main__":
    main()
