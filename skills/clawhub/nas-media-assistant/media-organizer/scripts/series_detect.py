#!/usr/bin/env python3
"""series_detect.py - 媒体归档决策辅助（纯逻辑，不查网络）。

解耦后 media-organizer 不再内嵌任何 TMDB 查询。需要的元数据由编排器调用
media-lookup 取回归一化 JSON，经 organize_media.py 的 --metadata 注入进来。
本模块只接收已注入的元数据 dict，做"是否系列 / 是否动画 / 是否衍生剧"的决策。

归一化 JSON 形态（media-lookup 产出）：
  movie: {"media_type":"movie","title":..,"year":..,"collection":"合集名"或null,
          "genres":["动画","喜剧",..],"source":"tmdb"|"douban_fallback"}
  tv:    {"media_type":"tv","title":..,"year":..,"collection":null,
          "seasons":[{"season":"S01","name":"第一季","year":"2014","episode_count":n},..],
          "genres":[..],"source":..}
"""

_COLLECTION_SUFFIXES = (
    " Collection", " Series", " collection", " series",
    "（系列）", "(系列)", "系列",
    "（合集）", "(合集)", "合集",
)


def series_from_collection(collection_name):
    """collection 名（如 'Zootopia Collection'）-> 系列文件夹名（如 '疯狂动物城（系列）'）。

    循环剥离所有已知后缀，统一为 `XX（系列）` 格式。无 collection 返回 None。
    归一化 JSON 的 collection 字段只是名字字符串（不含成员列表），故仅做命名归一。
    """
    if not collection_name:
        return None
    name = str(collection_name).strip()
    changed = True
    while changed:
        changed = False
        for suffix in _COLLECTION_SUFFIXES:
            if name.endswith(suffix):
                name = name[: -len(suffix)].strip()
                changed = True
                break
    if not name:
        return None
    return f"{name}（系列）"


def is_animated(genres):
    """判断 genres 列表是否含动画。

    归一化 JSON 的 genres 是名字列表（如 ["动画","喜剧"]），检测是否含「动画」/「Animation」。
    返回 True(动画) / False(非动画) / None(无 genres，无法判断)。
    """
    if not genres:
        return None
    for g in genres:
        gs = str(g).strip().lower()
        if gs in ("动画", "animation", "anime"):
            return True
    # 有 genres 但不含动画
    return False


def detect_spinoff(title, year, full_entry, base_entry):
    """判断标题是否为某母剧的衍生剧/主题剧。

    参数：
      title:       完整标题（如「灵魂摆渡·十年」）
      year:        衍生剧年份（可能为空）
      full_entry:  完整标题的注入元数据条目（须为 tv 才可能是衍生剧）；None 表示未注入
      base_entry:  中点基名（如「灵魂摆渡」）的注入元数据条目；None 表示未注入

    返回：
      {"is_spinoff": True, "base_name":.., "base_year":..} 确认衍生剧；
      {"is_spinoff": False}            确定不是（非 tv / 基名过短 / 非中点分隔 / 母剧不存在）；
      {"is_spinoff": False, "need":"base_show_lookup",
       "reason":"疑似衍生剧，需确认母剧与首播年"}  无法判定，需补全元数据。
    """
    # 必须是 tv 才走衍生剧路径（电影·副标题不算）
    if full_entry and full_entry.get("media_type") != "tv":
        return {"is_spinoff": False}

    parts = title.split("·", 1)
    if len(parts) != 2:
        return {"is_spinoff": False}
    base_name = parts[0].strip()
    sub_title = parts[1].strip()
    if not sub_title or len(base_name) < 3:
        # 基名 <3 字符多为译名中点（哈利·波特），不是系列分隔
        return {"is_spinoff": False}

    if base_entry is None:
        # 缺母剧元数据 -> 无法确认，请求补全
        return {"is_spinoff": False, "need": "base_show_lookup",
                "reason": f"疑似衍生剧，需确认母剧「{base_name}」是否为剧集及其首播年",
                "base_name": base_name}

    # 母剧须为 tv
    if base_entry.get("media_type") != "tv":
        return {"is_spinoff": False}

    base_year = str(base_entry.get("year") or "")[:4]
    # 衍生剧首播年应 >= 母剧首播年（衍生在原剧之后）
    if year and base_year and int(year) < int(base_year):
        return {"is_spinoff": False}  # 母剧比衍生还晚 -> 误匹配

    return {
        "is_spinoff": True,
        "base_name": base_name,
        "base_year": base_year,
        "spinoff_title": title,
        "spinoff_year": year,
        "suggested_season": "S00",
    }
