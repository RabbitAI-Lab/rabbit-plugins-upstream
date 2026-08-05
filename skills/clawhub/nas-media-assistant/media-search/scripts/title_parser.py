#!/usr/bin/env python3
"""资源标题解析器（稳定核心，与网站无关）。

把任意资源标题串解析成标准 JSON。信息全部从标题文本本身提取，
不依赖任何网页结构——网页会失效，但磁力名/文件名携带的信息始终在。

支持场景命名(scene) + 中文资源命名，例如:
  消失的人[国语配音/中文字幕].Vanishing.Point.2026.2160p.YK.WEB-DL.H.265.HDR.DTS5.1-PandaQT 2.42GB

用法:
  python3 title_parser.py '<标题串>'

设计原则: 网页抓取是脆弱的外围，标题解析才是稳定的核心。
标题串内嵌了 90% 有用信息(分辨率/编码/音频/字幕/年份/大小/来源/发行组)，
与具体网站无关。任何字段提取不到则为空，绝不抛异常。
"""
import re

# ---------- 清晰度 ----------
_RESOLUTION_RE = re.compile(
    r"(?<![a-zA-Z])(4320p|2160p|1440p|1080p|720p|576p|480p|4k|8k)(?![a-zA-Z])", re.I)

# ---------- 来源 ----------
_SOURCE_PATTERNS = [
    r"UHD\.?Blu-?Ray", r"Blu-?Ray", r"BluRay", r"BDRip", r"BRRip",
    r"REMUX", r"WEB-?DL", r"WEBRip", r"WEB-?Cap", r"WEB-?RIP",
    r"HDTV", r"DVDRip", r"DVDScr", r"HD-?DVD", r"HDTC",
    r"\bTC\b", r"\bTS\b", r"\bCAM\b", r"\bR5\b",
]
_SOURCE_RE = re.compile(r"(?<![a-zA-Z])(" + "|".join(_SOURCE_PATTERNS) + r")(?![a-zA-Z])", re.I)

# ---------- 编码 ----------
_CODEC_RE = re.compile(
    r"(?<![a-zA-Z])(x265|H\.?265|HEVC|x264|H\.?264|AVC|AV1|VP9|VC-?1|MPEG-?2|DivX|XviD)(?![a-zA-Z])", re.I)

# ---------- 音频 ----------
_AUDIO_PATTERNS = [
    r"DTS-?HD\.?MA", r"DTS-?HD\.?HRA", r"DTS-?HD", r"DTS-?X",
    r"TrueHD\.?Atmos", r"TrueHD", r"Atmos",
    r"E-?AC-?3", r"DDP[A5\.]+", r"DD\+?", r"AC-?3",
    r"DTS\d?\.?\d?", r"\bDTS\b", r"AAC\d?\.?\d?", r"\bAAC\b",
    r"\bFLAC\b", r"\bLPCM\b", r"DD\d?\.?\d?",
]
_AUDIO_RE = re.compile(r"(?<![a-zA-Z])(" + "|".join(_AUDIO_PATTERNS) + r")(?![a-zA-Z])", re.I)

# ---------- HDR / 杜比 ----------
_HDR_RE = re.compile(
    r"(?<![a-zA-Z])(HDR10\+|HDR10|HDR|Dolby\.?Vision|DoVi|DVProfile|DV)(?![a-zA-Z])", re.I)

# ---------- 年份 ----------
_YEAR_RE = re.compile(r"(?<!\d)(19\d{2}|20\d{2})(?!\d)")

# ---------- 单集标记 ----------
# 单集文件名: 标题-NN.mp4 / 标题.NN.mkv / EP01 / E01 / 第NN集（整季搜索时应降权）
_SINGLE_EP_RE = re.compile(
    r"[\s.\-_](?:E[Pp]?\s?(\d{1,3})|第(\d{1,3})[集话話期]|(\d{1,3}))"
    r"(?=\s*\.(?:mp4|mkv|avi|ts|rmvb|wmv|flv|mov|m2ts)$|\s*$)", re.I)

# ---------- 集数统计（全季资源，用于大小合理性判定）----------
# 全N集 / 共N集 / [全N集]：标识整季资源总集数，用于按集均大小评估是否过大
_EPISODE_COUNT_RE = re.compile(r"(?:全|共)\s*(\d{1,3})\s*集")

# ---------- 高码标记（高码版/高码，文件偏大；NAS 空间有限需适度降权）----------
_HIGH_BITRATE_RE = re.compile(r"高码", re.I)

# ---------- 大小 ----------
_SIZE_RE = re.compile(r"(\d[\d.]*)\s*(TiB|GiB|MiB|KiB|TB|GB|MB|KB|T|G|M)\b", re.I)

# ---------- 噪声 token（从 title_en 去除：位深/声道/容器/SxxExx 等）----------
_NOISE_RE = re.compile(
    r"\b(\d+bit|Hi10P|SDR|Hybrid|Dual|DualAudio|REMASTERED|Remastered)\b"
    r"|\b(\d\.\d|7\.1|5\.1|2\.0|1\.0|6CH|2CH)\b"
    r"|\b(mp4|mkv|avi|rmvb|wmv|flv|mov|m2ts|iso)\b"
    r"|\b[Ss]\d{1,2}[Ee]\d{1,3}\b|\b[Ss]\d{1,2}\b|\b[Ee]\d{1,3}\b",
    re.I)

# ---------- 中文平台标记（WEB-DL 国内源常见）----------
_PLATFORMS = {
    "YK": "优酷", "IQ": "爱奇艺", "TX": "腾讯视频", "MG": "芒果TV",
    "BJK": "哔哩哔哩", "KK": "快手", "HKT": "HKT",
}
_PLATFORM_RE = re.compile(
    r"(?<=[.\[-])(" + "|".join(_PLATFORMS.keys()) + r")(?=[.\]\s])", )

# ---------- 音轨语言 ----------
_LANG_AUDIO = [
    (r"国英", ["国语", "英语"]),
    (r"国粤英", ["国语", "粤语", "英语"]),
    (r"国粤", ["国语", "粤语"]),
    (r"国语配音", ["国语"]),
    (r"国语双音轨", ["国语"]),
    (r"国语版", ["国语"]),
    (r"国语", ["国语"]),
    (r"粤语", ["粤语"]),
    (r"英语", ["英语"]),
    (r"英文", ["英语"]),
    (r"日语", ["日语"]),
    (r"韩语", ["韩语"]),
    (r"原声", ["原声"]),
    (r"原版", ["原声"]),
]

# ---------- 字幕（含 CHS/CHT 简写）----------
_SUBTITLE = [
    (r"CHS/?CHT|CHT/?CHS", ["简体", "繁体"]),
    (r"\bCHS\b", ["简体"]),
    (r"\bCHT\b", ["繁体"]),
    (r"\bGB\b", ["简体"]),
    (r"\bBIG5\b", ["繁体"]),
    (r"简繁英.*字幕|简繁英双语", ["简体", "繁体", "英语"]),
    (r"简繁英", ["简体", "繁体", "英语"]),
    (r"简繁", ["简体", "繁体"]),
    (r"简体", ["简体"]),
    (r"繁体", ["繁体"]),
    (r"繁英", ["繁体", "英语"]),
    (r"简英", ["简体", "英语"]),
    (r"中英双字", ["中文", "英语"]),
    (r"中英双语", ["中文", "英语"]),
    (r"中文字幕", ["中文"]),
    (r"中字", ["中文"]),
    (r"双语", ["双语"]),
    (r"特效字幕", ["特效字幕"]),
    (r"内嵌字幕", ["内嵌"]),
    (r"内封字幕", ["内封"]),
]

# ---------- 低质 ----------
_LOWQ_RE = re.compile(
    r"(?<![a-zA-Z.])ts(?![a-zA-Z])|(?<![a-zA-Z])hdts(?![a-zA-Z])"
    r"|(?<![a-zA-Z])(?:hd)?(?:cam|tc)(?![a-zA-Z])"
    r"|枪版|枪影|抢先版|预告版|样片"
    r"|(?<![a-zA-Z.])sample(?![a-zA-Z])|(?<![a-zA-Z.])trailer(?![a-zA-Z])"
    r"|预告片|(?<![a-zA-Z.])dvdscr(?![a-zA-Z])|(?<![a-zA-Z.])workprint(?![a-zA-Z])", re.I)

_SIZE_MULT = {
    "TB": 10**12, "TIB": 2**40, "T": 10**12,
    "GB": 10**9, "GIB": 2**30, "G": 10**9,
    "MB": 10**6, "MIB": 2**20, "M": 10**6,
    "KB": 10**3, "KIB": 2**10,
}

# 裸单位（中文资源圈常用 G/M/T 表 GB/MB/TB）归一化为带 B 形式，保证 size_human 输出一致
_SIZE_NORM = {"T": "TB", "G": "GB", "M": "MB"}


def parse_size(text):
    """从任意文本提取文件大小，返回 (size_bytes:int, size_human:str)。

    供 aggregator 复用：标题内嵌大小优先，页面提供大小兜底。
    """
    m = _SIZE_RE.search(str(text))
    if not m:
        return 0, ""
    val = float(m.group(1))
    raw_unit = m.group(2)
    unit = raw_unit.upper()
    disp = _SIZE_NORM.get(unit, raw_unit)  # 裸 G/M/T -> GB/MB/TB；其余保留原大小写
    return int(val * _SIZE_MULT[unit]), f"{m.group(1)}{disp}"


def _norm_codec(m):
    v = m.upper().replace(".", "")
    if v in ("X265", "H265", "HEVC"):
        return "H.265" if v != "HEVC" else "HEVC"
    if v in ("X264", "H264", "AVC"):
        return "H.264" if v != "AVC" else "AVC"
    return m


def _norm_audio(m):
    return re.sub(r"\s+", "", m, flags=re.I).replace(".-", ".")


def _norm_source(v):
    v = v.lower().replace(".", "").replace("-", "")
    table = {"webdl": "WEB-DL", "webrip": "WEBRip", "webcap": "WEB-Cap",
             "bluray": "BluRay", "blurray": "BluRay", "bdrip": "BDRip",
             "brrip": "BRRip", "hdtv": "HDTV", "dvdrip": "DVDRip",
             "dvdscr": "DVDScr", "remux": "REMUX", "uhdbluray": "UHD BluRay"}
    return table.get(v, v.upper())


def _extract_title_cn(s):
    """提取中文标题：跳过开头的 [站点标签] 前缀，取 CJK 连续段（含标点/数字/空格）。"""
    # 跳过开头的 [xxx] 站点/组标签 + 空白
    rest = re.sub(r"^\s*\[[^\]]*\]\s*", "", s)
    # CJK 起始，后跟 CJK/中文标点/数字/空格/间隔号，遇 . 或 [ 或 ASCII 字母停止
    m = re.match(r"([\u4e00-\u9fff][\u4e00-\u9fff·：、，！？0-9\s]*)", rest)
    if m:
        return m.group(1).strip()
    return ""


def _extract_title_en(s, release_group):
    """提取英文标题：取年份之前的 ASCII token，去除中文/括号/平台码/噪声。

    策略（稳定核心）：scene 命名为 Title.Year.Resolution... ，年份之前即标题。
    无年份时回退为「移除所有已知元数据 token 后的剩余」。
    """
    # 找年份位置
    ym = _YEAR_RE.search(s)
    seg = s[:ym.start()] if ym else s
    # 去除中文段、括号内容、平台码
    seg = re.sub(r"[\u4e00-\u9fff·：、，！？\s]+", " ", seg)
    seg = re.sub(r"\[[^\]]*\]", " ", seg)
    for code in _PLATFORMS:
        seg = re.sub(rf"(?<![a-zA-Z]){code}(?![a-zA-Z])", " ", seg)
    # 切分为 token
    toks = []
    for t in re.split(r"[.\s]+", seg):
        t = t.strip("-")
        if not t or len(t) < 1:
            continue
        toks.append(t)
    # 去除发行组 token（大小写无关）与噪声 token
    rg = release_group.lower() if release_group else ""
    cleaned = []
    for t in toks:
        if rg and t.lower() == rg:
            continue
        if _NOISE_RE.fullmatch(t):
            continue
        if t.isdigit():
            continue
        cleaned.append(t)
    return " ".join(cleaned)


def parse(text):
    """把资源标题串解析为标准 JSON dict。

    Returns: raw/title/title_cn/title_en/year/resolution/source/codec/audio/
             hdr/language/subtitle/release_group/platform/size_bytes 等字段。
    任何字段提取不到则为空串/空列表，绝不抛异常。
    """
    s = str(text).strip()
    out = {"raw": s}

    # 大小
    sb, sh = parse_size(s)
    out["size_bytes"] = sb
    out["size_human"] = sh

    # 年份
    ym = _YEAR_RE.search(s)
    out["year"] = ym.group(1) if ym else ""

    # 分辨率（标准化: 4k->2160p, 8k->4320p，保证去重指纹与评分一致）
    rm = _RESOLUTION_RE.search(s)
    _res_raw = rm.group(1).lower() if rm else ""
    out["resolution"] = {"4k": "2160p", "8k": "4320p"}.get(_res_raw, _res_raw)

    # 来源
    sm = _SOURCE_RE.search(s)
    out["source"] = _norm_source(sm.group(1)) if sm else ""

    # 编码
    cm = _CODEC_RE.search(s)
    out["codec"] = _norm_codec(cm.group(1)) if cm else ""

    # 音频
    am = _AUDIO_RE.search(s)
    out["audio"] = _norm_audio(am.group(1)) if am else ""

    # HDR / 杜比：扫描全部标记，DV 优先（DV 通常含 HDR）
    hdr_tokens = _HDR_RE.findall(s)
    if any(re.match(r"(DV|DoVi|Dolby)", t, re.I) for t in hdr_tokens):
        out["hdr"] = "Dolby Vision"
    elif any(re.match(r"HDR", t, re.I) for t in hdr_tokens):
        out["hdr"] = "HDR"
    else:
        out["hdr"] = ""

    # 平台标记
    out["platform"] = ""
    pm = _PLATFORM_RE.search(s)
    if pm:
        code = pm.group(1)
        out["platform"] = f"{code}({_PLATFORMS[code]})"

    # 中文标题
    out["title_cn"] = _extract_title_cn(s)

    # 发行组：去掉大小后，最后一个 - 之后
    gtext = _SIZE_RE.sub("", s).strip().rstrip(".- ")
    gm = re.search(r"-([A-Za-z0-9&]+)$", gtext)
    out["release_group"] = gm.group(1) if gm else ""

    # 英文标题
    out["title_en"] = _extract_title_en(s, out["release_group"])

    # 主标题
    if out["title_cn"] and out["title_en"]:
        out["title"] = f"{out['title_cn']} / {out['title_en']}"
    else:
        out["title"] = out["title_cn"] or out["title_en"]

    # 音轨语言 / 字幕：扫描所有方括号（含 [国语配音] 与 [CHS]）
    brackets = re.findall(r"\[([^\]]+)\]", s)
    lang_field = " ".join(brackets) if brackets else s
    langs = set()
    for pat, vals in _LANG_AUDIO:
        if re.search(pat, lang_field):
            langs.update(vals)
    out["language"] = sorted(langs)

    subs = set()
    for pat, vals in _SUBTITLE:
        if re.search(pat, lang_field):
            subs.update(vals)
    out["subtitle"] = sorted(subs)
    out["language_label"] = "/".join(out["language"] + out["subtitle"]) if (out["language"] or out["subtitle"]) else ""

    # 低质标记
    out["is_low_quality"] = bool(_LOWQ_RE.search(s))

    # 单集检测（整季搜索时降权，不删除：用户可能确实要单集）
    _em = _SINGLE_EP_RE.search(s)
    out["is_single_episode"] = bool(_em)
    out["episode"] = next((g for g in _em.groups() if g), "") if _em else ""

    # 集数统计（全N集，用于大小合理性判定；0 表示未知/非整季）
    _ecm = _EPISODE_COUNT_RE.search(s)
    out["episode_count"] = int(_ecm.group(1)) if _ecm else 0

    # 高码标记（高码版/高码，体积偏大；size 未知时轻度降权）
    out["is_high_bitrate"] = bool(_HIGH_BITRATE_RE.search(s))

    # 质量标签聚合
    tags = []
    if out["hdr"]:
        tags.append(out["hdr"])
    if out["resolution"] in ("2160p", "4320p"):
        tags.append("4K")
    if out["source"] == "REMUX":
        tags.append("REMUX")
    out["quality_tags"] = tags
    return out


def main():
    import sys, json
    if len(sys.argv) < 2:
        print(json.dumps({"error": "用法: title_parser.py '<标题串>'"}))
        sys.exit(1)
    print(json.dumps(parse(sys.argv[1]), ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
