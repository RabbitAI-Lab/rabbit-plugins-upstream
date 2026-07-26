#!/usr/bin/env python3
"""DramaLex · estimate.py — 由字幕规模推导各学习材料数量（替代手写死值）

设计动机：
  原来 words 固定 15–30，但一部 2 小时电影约 14k 词、一集 22 分钟情景剧约 3k 词，
  二者「可学材料」量级差 4–5 倍，硬卡 30 个词对长片是荒谬的。
  这里用「每 15 分钟可消化目标词」作为容量锚点，按字幕时长 + 词汇密度 + 学习者档位，
  推导出 词汇 / 听力理解 / 听写 / 精读 / 完形 / 口语 / 写作 的合理数量。
  结果只是「建议上限」，agent 仍按真实教学价值取舍；用户可用 --word-cap 覆盖。

连续公式（10 分钟 ≠ 3 小时的关键）：
  per15 = 22 if new_ratio<0.45 else 28 if new_ratio<0.62 else 34   # 每 15 分钟可消化目标词（新词密度越高越多）
  word_cap = clamp( round(per15 * runtime_min / 15), 12, 260 )      # 与时长严格线性
  例：10 分钟 → ≈15 词；22 分钟 → ≈32 词；117 分钟(电影) → ≈158 词；180 分钟 → 260(封顶)
  低档位(A2)再 ×0.9；随后按价值分三层 core/expand/challenge，避免一次塞爆。
"""
import json, os, re


def _load_subtitle(path):
    if not path or not os.path.exists(path):
        return None
    try:
        data = json.load(open(path, encoding='utf-8'))
    except Exception:
        return None
    # parse_subtitles.py 产出 {episode, lines:[{start,end,text,...}], ...}
    # 也兼容 {segments:[...]} / {subtitles:[...]} / 纯 list
    if isinstance(data, list):
        return data
    if isinstance(data, dict):
        for k in ('lines', 'segments', 'subtitles'):
            if isinstance(data.get(k), list):
                return data[k]
    return None


def _runtime_min(segs):
    """从最后一条字幕的 end 估算时长（秒）。支持 'HH:MM:SS,mmm' / 浮点秒 / ms。"""
    last = None
    for s in segs:
        e = s.get('end')
        if e is None:
            continue
        last = e
    if last is None:
        return 0.0
    # 字符串时间戳
    if isinstance(last, str):
        last = last.strip().replace(',', '.')
        m = re.match(r'(\d+):(\d+):(\d+(?:\.\d+)?)', last)
        if m:
            h, mi, se = (int(m.group(1)), int(m.group(2)), float(m.group(3)))
            return (h * 3600 + mi * 60 + se) / 60.0
        try:
            return float(last) / 60.0  # 假定 ms
        except ValueError:
            return 0.0
    if isinstance(last, (int, float)):
        return float(last) / 60.0 if last > 1000 else float(last)  # >1000 视为秒
    return 0.0


def _word_stats(segs):
    toks = []
    for s in segs:
        t = s.get('text', '')
        if not t:
            continue
        toks += re.findall(r"[A-Za-z]+(?:['-][A-Za-z]+)*", t)
    n = len(toks)
    uniq = len(set(w.lower() for w in toks)) if toks else 0
    if not n:
        return 0, 0, 0.0
    avg_len = sum(len(w) for w in toks) / n
    # 低频词占比（出现仅 1 次的词 / 总词）近似「新词密度」
    from collections import Counter
    freq = Counter(w.lower() for w in toks)
    hapax = sum(1 for w, c in freq.items() if c == 1)
    new_ratio = hapax / uniq if uniq else 0.0
    return n, uniq, new_ratio


def estimate_counts(subtitle_json=None, text=None, runtime_min=0.0, uni=None, cefr='auto'):
    """返回推荐数量 dict（均为建议上限）。

    输入优先级：subtitle_json 文件 > text 字符串 > 仅用 runtime_min/uni 兜底。
    """
    segs = _load_subtitle(subtitle_json) if subtitle_json else None
    if text and not segs:
        toks = re.findall(r"[A-Za-z]+(?:['-][A-Za-z]+)*", text)
        segs = [{'text': text, 'start': 0, 'end': max(1, len(toks) / 130.0 * 60)}]

    # 空字幕防护：解析出 0 行时必须显式报错，避免下游建立在空数据上、静默给最小词量
    if not segs:
        return {
            'error': 'subtitle_empty',
            'runtime_min': 0, 'words_total': 0, 'uniq': 0, 'new_ratio': 0.0,
            'word_cap': 0, 'listening_comprehension': 0, 'listening_dictation': 0,
            'annotated_annotations': 0, 'annotated_cloze': 0,
            'tasks_speaking': 0, 'tasks_writing': 0,
        }

    words_total, uniq, new_ratio = 0, 0, 0.0
    rt = runtime_min
    if segs:
        rt = _runtime_min(segs) or rt
        words_total, uniq, new_ratio = _word_stats(segs)

    # 时长兜底
    if rt <= 0:
        rt = max(1.0, words_total / 130.0)  # 130 wpm 口语估算

    # ---- 容量锚点：每 15 分钟可消化目标词 ----
    per15 = 22 if new_ratio < 0.45 else 28 if new_ratio < 0.62 else 34
    cap = int(round(per15 * rt / 15.0))
    # 档位微调（诚实：低档不减数量，仅让 agent 标挑战★/在产出任务里跳过 C1）
    if cefr in ('A2',):
        cap = int(round(cap * 0.9))
    cap = max(12, min(cap, 260))  # 下限与上限护栏（长片可达 200+，而非 30）

    # ---- 长片分层：一部 2 小时电影的可学词远多于 30，按价值分三层呈现 ----
    core = max(8, round(cap * 0.5))       # 核心：最高频/最高价值，优先掌握
    expand = max(4, round(cap * 0.3))     # 扩展：巩固用
    challenge = max(0, cap - core - expand)  # 挑战：低频/高阶，量力
    tiers = {'core': core, 'expand': expand, 'challenge': challenge}

    # ---- 各材料按 cap 比例派生 ----
    comprehension = max(4, min(round(cap / 4), 30))
    dictation = max(4, min(round(cap / 5), 24))
    annotations = max(4, min(round(cap / 3), 32))
    cloze = max(3, min(round(cap / 6), 18))
    speaking = max(2, min(3 + cap // 40, 8))
    writing = max(2, min(2 + cap // 50, 6))

    return {
        'runtime_min': round(rt, 1),
        'words_total': words_total,
        'uniq': uniq,
        'new_ratio': round(new_ratio, 3),
        'word_cap': cap,
        'tiers': tiers,
        'listening_comprehension': comprehension,
        'listening_dictation': dictation,
        'annotated_annotations': annotations,
        'annotated_cloze': cloze,
        'tasks_speaking': speaking,
        'tasks_writing': writing,
    }


def render_bullets(est):
    """把 estimate 渲染成交接单用的要点行。"""
    t = est.get('tiers', {})
    tier_line = (
        f"- **长片分层（避免一次塞 200 词）**：核心 `{t.get('core')}` · 扩展 `{t.get('expand')}` · 挑战 `{t.get('challenge')}`"
        if t else ""
    )
    long_film_note = (
        "（⚠️ 长片/电影：词量随时长放大，一部 2 小时电影建议挖 **120–200** 词并分层，绝非 30 词）"
        if est.get('runtime_min', 0) >= 60 else ""
    )
    formula = (
        f"- **词量公式（连续，随时长线性）**：`word_cap = clamp(round(per15 × 时长/15), 12, 260)`，"
        f"其中 `per15` 由新词密度取 22/28/34。即 10 分钟≈15 词、22 分钟≈32 词、"
        f"117 分钟电影≈158 词、180 分钟封顶 260 —— **10 分钟和 3 小时绝不会都是 30 词**。"
    )
    lines = [
        f"- 估算时长 ≈ **{est['runtime_min']} 分钟** · 总词 {est['words_total']} · 去重 {est['uniq']} · 新词密度 {est['new_ratio']}",
        formula,
        f"- 建议目标词/语块 `word_cap ≈ {est['word_cap']}`（用户可用 `--word-cap` 覆盖，作为软上限，按价值取舍）{long_film_note}",
        tier_line,
        f"- 听力理解 ≈ **{est['listening_comprehension']}** · 听写 ≈ **{est['listening_dictation']}**",
        f"- 精读标注 ≈ **{est['annotated_annotations']}** · 完形 ≈ **{est['annotated_cloze']}**",
        f"- 口语 ≈ **{est['tasks_speaking']}** · 写作 ≈ **{est['tasks_writing']}**",
        "- 精读标注并非只讲单词：务必挖掘 grammar/pattern/collocation/discourse/pronunciation 等「非单词」语言知识点（见 schema）。",
        "- 以上为「建议上限」，请按真实教学价值取舍，勿为凑数塞低质项。",
    ]
    return lines


def suggest_cefr(subtitle_json=None, text=None):
    """由字幕词汇密度/平均词长反推本集大概水平，作为 --cefr 的默认值建议。

    依据（经验映射，仅建议、不强制）：新词密度越高、平均词越长 → 越难。
      new_ratio<0.45 且 avg_len<4.3  → A2
      new_ratio<0.60 且 avg_len<4.8  → B1
      new_ratio<0.70 或  avg_len<5.3  → B2
      否则                          → C1
    """
    segs = _load_subtitle(subtitle_json) if subtitle_json else None
    if text and not segs:
        segs = [{'text': text}]
    if not segs:
        return 'B1'
    _, _, new_ratio = _word_stats(segs)
    # 平均词长
    toks = []
    for s in segs:
        toks += re.findall(r"[A-Za-z]+(?:['-][A-Za-z]+)*", s.get('text', ''))
    avg_len = (sum(len(w) for w in toks) / len(toks)) if toks else 4.5
    if new_ratio < 0.45 and avg_len < 4.3:
        return 'A2'
    if new_ratio < 0.60 and avg_len < 4.8:
        return 'B1'
    if new_ratio < 0.70 or avg_len < 5.3:
        return 'B2'
    return 'C1'


if __name__ == '__main__':
    import sys
    p = sys.argv[1] if len(sys.argv) > 1 else None
    e = estimate_counts(subtitle_json=p)
    print(json.dumps(e, ensure_ascii=False, indent=2))
