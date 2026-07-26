#!/usr/bin/env python3
"""DramaLex · exam_map.py — CEFR 与主流英语考试的分数量表

用途：把抽象的 B1/B2 翻译成用户熟悉的「雅思 X–X / 托福 X–X / 四六级」区间，
让难度档位与每个单词的级别更具参考性、更直观。
分数均为常见对照区间，非官方精确边界，已在展示处标注"约"。

来源：IELTS / TOEFL iBT / 中国大学英语四六级(CET-4/6) 的通用 CEFR 对照。
"""
# CEFR -> 各考试常见分数区间（约）。None 表示该考试通常不覆盖此档。
CEFR_EXAM = {
    'A1': {
        'ielts': '—（＜4.0）',
        'toefl': '0–31',
        'cet': '—（低于四级）',
    },
    'A2': {
        'ielts': '3.0–3.5',
        'toefl': '32–41',
        'cet': '—（接近四级）',
    },
    'B1': {
        'ielts': '4.0–5.0',
        'toefl': '42–71',
        'cet': 'CET-4（四级）',
    },
    'B2': {
        'ielts': '5.5–6.5',
        'toefl': '72–94',
        'cet': 'CET-6（六级）',
    },
    'C1': {
        'ielts': '7.0–8.0',
        'toefl': '95–120',
        'cet': '专四/专八水平',
    },
    'C2': {
        'ielts': '8.5–9.0',
        'toefl': '110–120',
        'cet': '专八优秀',
    },
}

# 反向：考试分数 -> CEFR 档位（用于学前诊断按分数定位档位）。
# 边界取保守（低）侧，避免高估导致材料过难。
# 元组语义：(阈值, 该阈值【之下】区间对应的档位)
#   雅思: <3.0→A1 · 3.0–3.5→A2 · 4.0–5.0→B1 · 5.5–6.5→B2 · 7.0–8.0→C1 · ≥8.5→C2
_IELTS_BANDS = [(3.0, 'A1'), (4.0, 'A2'), (5.5, 'B1'), (7.0, 'B2'), (8.5, 'C1')]
#   托福: <32→A1 · 32–41→A2 · 42–71→B1 · 72–94→B2 · 95–109→C1 · ≥110→C2
_TOEFL_BANDS = [(32, 'A1'), (42, 'A2'), (72, 'B1'), (95, 'B2'), (110, 'C1')]
_CET_BANDS = [('四级', 'B1'), ('六级', 'B2'), ('专四', 'C1'), ('专八', 'C2')]

# 展示顺序与中文名
EXAM_ORDER = [('ielts', '雅思'), ('toefl', '托福'), ('cet', '四六级')]


def exam_label(cefr):
    """返回如 '雅思4.0–5.0 · 托福42–71 · 四六级CET-4（四级）' 的字符串；cefr 无效返回 ''。"""
    m = CEFR_EXAM.get(cefr)
    if not m:
        return ''
    parts = []
    for key, cn in EXAM_ORDER:
        v = m.get(key)
        if v:
            parts.append(f"{cn}{v}")
    return ' · '.join(parts)


def exam_tag(cefr):
    """紧凑标注，用于单词卡角标：'雅思4–5/托福42–71/CET-4'。"""
    m = CEFR_EXAM.get(cefr)
    if not m:
        return ''
    out = []
    if m.get('ielts'):
        out.append(f"雅思{m['ielts']}")
    if m.get('toefl'):
        out.append(f"托福{m['toefl']}")
    if m.get('cet') and m['cet'] != '—（低于四级）':
        out.append(m['cet'])
    return '/'.join(out)


def suggest_line(cefr):
    """难度建议行：'B1（约 雅思4.0–5.0 · 托福42–71 · 四六级CET-4）'。"""
    lab = exam_label(cefr)
    if lab:
        return f"{cefr}（约 {lab}）"
    return cefr


def cefr_from_ielts(score):
    """雅思分数 -> CEFR（保守低侧）。<3.0 → A1。"""
    try:
        s = float(score)
    except (TypeError, ValueError):
        return None
    if s < 3.0:
        return 'A1'
    for lo, band in _IELTS_BANDS:
        if s < lo:
            return band
    return 'C2'


def cefr_from_toefl(score):
    """托福 iBT 分数 -> CEFR（保守低侧）。<32 → A1。"""
    try:
        s = float(score)
    except (TypeError, ValueError):
        return None
    if s < 32:
        return 'A1'
    for lo, band in _TOEFL_BANDS:
        if s < lo:
            return band
    return 'C2'


def cefr_from_cet(text):
    """四六级/专四专八文字 -> CEFR。识别 '四级/六级/专四/专八'。"""
    if not text:
        return None
    t = str(text)
    if '专八' in t:
        return 'C2'
    if '专四' in t:
        return 'C1'
    if '六级' in t or 'CET-6' in t:
        return 'B2'
    if '四级' in t or 'CET-4' in t:
        return 'B1'
    return None


def diagnose_from_exam(ielts=None, toefl=None, cet=None):
    """由任一/多个考试分数反推 CEFR。

    多条证据时取【最保守（最低）】档位，避免高估导致材料过难；
    返回 (cefr, 使用的证据列表)。无证据返回 (None, [])。
    """
    bands = []
    used = []
    if ielts is not None:
        b = cefr_from_ielts(ielts)
        if b:
            bands.append(b); used.append(f"雅思{ielts}")
    if toefl is not None:
        b = cefr_from_toefl(toefl)
        if b:
            bands.append(b); used.append(f"托福{toefl}")
    if cet:
        b = cefr_from_cet(cet)
        if b:
            bands.append(b); used.append(f"四六级{cet}")
    if not bands:
        return None, []
    order = ['A1', 'A2', 'B1', 'B2', 'C1', 'C2']
    # 最保守 = 在 order 中索引最小者
    best = min(bands, key=lambda x: order.index(x))
    return best, used


if __name__ == '__main__':
    for c in ('A1', 'A2', 'B1', 'B2', 'C1', 'C2'):
        print(c, '->', suggest_line(c))
    print('reverse ielts 6.5 ->', cefr_from_ielts(6.5))
    print('reverse toefl 90 ->', cefr_from_toefl(90))
    print('reverse cet 六级 ->', cefr_from_cet('CET-6'))
    print('diagnose ielts5.5/toefl80 ->', diagnose_from_exam(ielts=5.5, toefl=80))
