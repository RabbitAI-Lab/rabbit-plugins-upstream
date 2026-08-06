#!/usr/bin/env python3
"""ffprobe_info.py — 从媒体文件提取 [信息] 标签。

当下载文件名中不含 [信息] 标签时，用 ffprobe（或 mediainfo 回退）分析文件内容，
提取音轨/字幕/分辨率/编码信息，构造命名规范要求的 [信息] 标签。

核心设计：
  - 国内压制组常把语言信息写在轨道 title 字段（如「国语」「上译国配」「简体中文」），
    而非标准 language 标签。本脚本同时解析 language 标签与 title 文本，优先 title（更准确）。
  - 双引擎：优先 ffprobe（大多数 NAS 含 ffmpeg 已预装），不可用时回退 mediainfo。

输出：
  {"info_tag": "国英多音轨+简繁中字幕", "release_tag": "1080p.x264.AC3.5.1", "all_found": true}
"""
import json
import os
import subprocess
import sys

# ---- 语言映射：ISO 639 / 英文名 -> 中文 ----
LANG_MAP = {
    "chi": "国语", "zho": "国语", "chinese": "国语", "cmn": "国语",
    "eng": "英语", "english": "英语", "und": "",
    "yue": "粤语", "cantonese": "粤语",
    "jpn": "日语", "japanese": "日语",
    "kor": "韩语", "korean": "韩语",
    "fra": "法语", "fre": "法语", "french": "法语",
    "tha": "泰语", "viet": "越南语", "rus": "俄语",
}

# ---- 编码映射 ----
VIDEO_CODEC_MAP = {
    "hevc": "x265", "h265": "x265",
    "h264": "x264", "avc": "x264",
    "av1": "av1", "vp9": "vp9", "mpeg4": "mpeg4", "mpeg2video": "mpeg2",
}
AUDIO_CODEC_MAP = {
    "dts": "DTS", "dts-hd ma": "DTS-HDMA", "dts_hd_ma": "DTS-HDMA", "dts-hd hra": "DTS-HD HRA",
    "truehd": "TrueHD", "true_hd": "TrueHD",
    "ac3": "AC3", "eac3": "EAC3", "ec3": "EAC3",
    "aac": "AAC", "mp3": "MP3", "mp2": "MP2", "flac": "FLAC", "opus": "Opus",
    "pcm": "PCM", "alac": "ALAC",
}

# ---- 分辨率映射（按 height 阈值，从高到低匹配） ----
RESOLUTION_MAP = [
    (2160, "2160p"), (1440, "1440p"), (1080, "1080p"),
    (720, "720p"), (576, "576p"), (480, "480p"),
]

# ---- 音轨 title 中的语言关键词（长串优先，避免误匹配） ----
AUDIO_TITLE_LANGS = [
    ("粤语配音", "粤语"), ("粤语", "粤语"), ("粤配", "粤语"), (" cantonese", "粤语"),
    ("国语配音", "国语"), ("国语", "国语"), ("国配", "国语"), ("中文配音", "国语"),
    ("上译", "国语"), ("八一", "国语"), ("长译", "国语"), ("北影", "国语"),
    ("日语", "日语"), ("日文", "日语"), (" japanese", "日语"),
    ("韩语", "韩语"), ("韩文", "韩语"),
    ("英语", "英语"), ("英文", "英语"), ("原声", "英语"), (" original", "英语"),
    ("法语", "法语"), ("泰语", "泰语"), ("俄语", "俄语"), ("德语", "德语"),
]


def _run_ffprobe(path):
    """调用 ffprobe 提取 JSON 格式的流信息。失败返回 None。"""
    try:
        cmd = ["ffprobe", "-v", "quiet", "-print_format", "json",
               "-show_streams", "-show_format", path]
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
        if result.returncode != 0:
            return None
        return json.loads(result.stdout)
    except (FileNotFoundError, subprocess.TimeoutExpired, json.JSONDecodeError):
        return None


def _run_mediainfo(path):
    """ffprobe 不可用时回退到 mediainfo，返回统一格式的流列表。"""
    try:
        cmd = ["mediainfo", "--Output=JSON", path]
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
        if result.returncode != 0:
            return None
        return json.loads(result.stdout)
    except (FileNotFoundError, subprocess.TimeoutExpired, json.JSONDecodeError):
        return None


def _normalize_lang(lang_code):
    """ISO 639 语言码 -> 中文名（如 'chi' -> '国语'）。无法识别返回空串。"""
    if not lang_code:
        return ""
    code = lang_code.lower().strip()
    base = code.split("-")[0].split("_")[0]
    return LANG_MAP.get(base, LANG_MAP.get(code, ""))


def _langs_from_title(title):
    """从轨道 title 文本推断语言（国内压制组常把语言写在 title 里）。
    返回去重的语言列表，如 ['国语', '英语']。"""
    if not title:
        return []
    low = title.lower()
    found = []
    for kw, lang in AUDIO_TITLE_LANGS:
        if kw.lower() in low and lang not in found:
            found.append(lang)
    return found


def _sub_kinds_from_title(title):
    """从字幕 title 推断字幕种类。
    返回 (kinds_set, has_effect)：kinds 含 '简'/'繁'/'英'/'中'，has_effect 标记特效字幕。"""
    kinds = set()
    effect = False
    if not title:
        return kinds, effect
    low = title.lower()
    if "特效" in title or "特效字幕" in title:
        effect = True
    if "繁" in title or "cht" in low or "traditional" in low:
        kinds.add("繁")
    if "简" in title or "chs" in low or "simplified" in low:
        kinds.add("简")
    if "英" in title or "eng" in low or "english" in low:
        kinds.add("英")
    if not kinds and ("中" in title or "chs" in low or "cht" in low or "chinese" in low):
        kinds.add("中")
    return kinds, effect


def _get_resolution(height):
    """视频高度 -> 分辨率标签（如 1080 -> '1080p'）。"""
    for h, label in RESOLUTION_MAP:
        if height >= h:
            return label
    return ""


def _check_atmos(audio_streams):
    """检测音轨是否含 Dolby Atmos（从 title 文本匹配）。"""
    for s in audio_streams:
        title = (s.get("tags", {}).get("title") or "").lower()
        if "atmos" in title or "dolby atmos" in title:
            return True
    return False


def _parse_mediainfo_streams(mi_data):
    """将 mediainfo JSON 转为与 ffprobe 一致的 streams 列表。"""
    tracks = mi_data.get("media", {}).get("track", [])
    streams = []
    for t in tracks:
        st = {}
        if t.get("@type") == "Video":
            st["codec_type"] = "video"
            st["codec_name"] = t.get("Format", "").lower().replace(" ", "")
            h = t.get("Height", "0").replace(" ", "")
            st["height"] = int(h) if h else 0
        elif t.get("@type") == "Audio":
            st["codec_type"] = "audio"
            st["codec_name"] = t.get("Format", "").lower()
            ch = t.get("Channels", "0")
            st["channels"] = int(ch) if ch else 0
            lang = t.get("Language", "")
            st["tags"] = {"language": lang} if lang else {}
            title = t.get("Title", "")
            if title:
                st.setdefault("tags", {})["title"] = title
        elif t.get("@type") == "Text":
            st["codec_type"] = "subtitle"
            lang = t.get("Language", "")
            st["tags"] = {"language": lang} if lang else {}
            title = t.get("Title", "")
            if title:
                st.setdefault("tags", {})["title"] = title
        if st:
            streams.append(st)
    return streams


def extract_info(path):
    """主入口：从媒体文件提取 [信息] 标签。

    流程：ffprobe -> mediainfo 回退 -> 解析音频/字幕/视频信息 -> 构造标签。
    返回 dict：info_tag(音轨+字幕)、release_tag(分辨率+编码+声道)、all_found、details。
    """
    if not os.path.exists(path):
        return {"error": "file not found: " + path, "info_tag": "未标注",
                "release_tag": "", "all_found": False}

    # 双引擎获取流信息
    data = _run_ffprobe(path)
    if data:
        streams = data.get("streams", [])
    else:
        mi_data = _run_mediainfo(path)
        if not mi_data:
            return {"error": "ffprobe and mediainfo unavailable", "info_tag": "未标注",
                    "release_tag": "", "all_found": False}
        streams = _parse_mediainfo_streams(mi_data)

    video_streams = [s for s in streams if s.get("codec_type") == "video"]
    audio_streams = [s for s in streams if s.get("codec_type") == "audio"]
    sub_streams = [s for s in streams if s.get("codec_type") == "subtitle"]

    # ---- 音频信息：language 标签 + title 文本双解析 ----
    audio_langs = []
    audio_codecs = set()
    for s in audio_streams:
        tags = s.get("tags", {})
        lang = _normalize_lang(tags.get("language", ""))
        title = tags.get("title", "") or ""
        title_langs = _langs_from_title(title)
        # 优先 title 解析（更准确），回退 language 标签
        for lg in (title_langs or ([lang] if lang else [])):
            if lg and lg not in audio_langs:
                audio_langs.append(lg)
        # 编码检测：codec_name + title 文本双重匹配
        codec = s.get("codec_name", "").lower()
        if codec in AUDIO_CODEC_MAP:
            audio_codecs.add(AUDIO_CODEC_MAP[codec])
        tlow = title.lower()
        if "dts-hd ma" in tlow or "dts_hd_ma" in tlow:
            audio_codecs.add("DTS-HDMA")
        if "truehd" in tlow:
            audio_codecs.add("TrueHD")
        if "atmos" in tlow:
            audio_codecs.add("Atmos")

    if _check_atmos(audio_streams):
        audio_codecs.add("Atmos")

    # 音轨标签：>=3 种语言 -> "国粤英多音轨"，2种 -> "国英多音轨"，1种 -> "国语"
    if len(audio_langs) >= 3:
        audio_tag = "".join(audio_langs[:3]) + "多音轨"
    elif len(audio_langs) == 2:
        audio_tag = "".join(audio_langs) + "多音轨"
    elif len(audio_langs) == 1:
        audio_tag = audio_langs[0]
    else:
        audio_tag = ""

    # ---- 字幕信息：title 文本解析为主，language 标签为辅 ----
    sub_kinds = set()
    has_effect = False
    for s in sub_streams:
        tags = s.get("tags", {})
        title = tags.get("title", "") or ""
        lang = _normalize_lang(tags.get("language", ""))
        kinds, effect = _sub_kinds_from_title(title)
        sub_kinds |= kinds
        has_effect = has_effect or effect
        if not kinds and lang:
            sub_kinds.add(lang)

    # 字幕标签：简繁英 -> 简繁英字幕，简繁 -> 简繁中字幕，中英 -> 中英字幕...
    if {"简", "繁", "英"} <= sub_kinds:
        sub_tag = "简繁英字幕"
    elif {"简", "繁"} <= sub_kinds:
        sub_tag = "简繁中字幕"
    elif ("英" in sub_kinds) and (sub_kinds & {"简", "繁", "中", "国语"}):
        sub_tag = "中英字幕"
    elif "英" in sub_kinds:
        sub_tag = "英文字幕"
    elif sub_kinds & {"简", "繁", "中", "国语"}:
        sub_tag = "中文字幕"
    else:
        sub_tag = ""
    if has_effect and sub_tag and "特效" not in sub_tag:
        sub_tag = "特效" + sub_tag

    # ---- 构造 [信息] 第一段：音轨+字幕 ----
    parts = []
    if audio_tag:
        parts.append(audio_tag)
    if sub_tag:
        parts.append(sub_tag)
    info_tag = "+".join(parts) if parts else "未标注"

    # ---- 构造 [信息] 第二段：发布信息（分辨率.编码.声道） ----
    release_parts = []
    resolution = ""
    if video_streams:
        v = video_streams[0]
        resolution = _get_resolution(v.get("height", 0))
    if resolution:
        release_parts.append(resolution)
    if video_streams:
        vcodec = video_streams[0].get("codec_name", "").lower()
        if vcodec in VIDEO_CODEC_MAP:
            release_parts.append(VIDEO_CODEC_MAP[vcodec])
    # 取最高质量音频编码（优先级排序）
    for ac in ["DTS-HDMA", "TrueHD", "Atmos", "DTS", "EAC3", "AC3", "AAC", "MP3", "MP2"]:
        if ac in audio_codecs:
            release_parts.append(ac)
            break
    # 声道数：6ch -> 5.1，8ch -> 7.1
    channels = audio_streams[0].get("channels", 0) if audio_streams else 0
    if channels in (6, 8):
        release_parts.append(str(channels - 1) + ".1")

    release_tag = ".".join(release_parts)

    return {
        "info_tag": info_tag,
        "release_tag": release_tag,
        "all_found": True,
        "details": {
            "audio_languages": audio_langs,
            "audio_codecs": list(audio_codecs),
            "subtitle_kinds": sorted(sub_kinds),
            "has_effect_sub": has_effect,
            "resolution": resolution,
            "video_codec": video_streams[0].get("codec_name", "") if video_streams else "",
            "audio_channels": channels,
            "has_atmos": _check_atmos(audio_streams),
        },
    }


def main():
    """CLI 入口：ffprobe_info.py <媒体文件路径>"""
    if len(sys.argv) < 2:
        print(json.dumps({"error": "用法: ffprobe_info.py <媒体文件路径>"}))
        sys.exit(1)
    print(json.dumps(extract_info(sys.argv[1]), ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
