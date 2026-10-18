#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""classify_life.py - 终身寿险形态判定 + 杠杆率测算（SKILL.md §六 路由 / §7.18）。

★ 为什么需要这个脚本
──────────────────────────────────────────────────────────────
都叫「终身寿险」，但「定额终身寿（杠杆寿）」和「增额终身寿」是两种完全不同的东西：

  定额终身寿  保额恒定（如终身 100 万），钱主要被拿去买身故保障，
             现金价值几十年才回本，IRR 长期在 0~1%。
             → **算 IRR 意义不大，主看杠杆率**（保额÷保费 = 性价比）。
             把它的 IRR 当成评价指标，会把「保障型产品」误判成「收益差的产品」。

  增额终身寿  保额与现金价值按复利逐年递增，本质是中长期储蓄，
             → 按储蓄理财类做 总利益 / IRR / 回本 全套分析（§7）。

本脚本先做形态判定，再按形态输出该看的指标，避免「用 IRR 评价杠杆寿」这类口径错误。

用法
──────────────────────────────────────────────────────────────
  # 从 extract.py 的抽取结果自动判（推荐）
  python classify_life.py --extract 德华安顾.json
  python classify_life.py --extract 信美.json --sum-assured 1000000

  # 多品一次性判定 + 横向杠杆对比
  python classify_life.py --extract A.json B.json C.json --compare

  # 手喂数据（计划书只有图片表、需要人工录入时）
  python classify_life.py --policy hand.json
"""
import argparse
import json
import os
import re
import sys
import unicodedata

W = 68

# ---------------------------------------------------------------- 文本归一化


def dedup_cjk(s):
    """去掉中文文本层「逐字重复」伪影：保保单单年年年度度 → 保单年度。"""
    out = []
    for ch in s:
        if out and ch == out[-1] and ("一" <= ch <= "鿿"):
            continue
        out.append(ch)
    return "".join(out)


def norm(x):
    """NFKC 还原康熙部首（⾦ U+2FA6 → 金），去空白，去逐字重复。"""
    if x is None:
        return ""
    s = unicodedata.normalize("NFKC", str(x))
    s = re.sub(r"\s+", "", s)
    return dedup_cjk(s)


def to_float(v):
    if v is None:
        return 0.0
    if isinstance(v, bool):
        return 0.0
    if isinstance(v, (int, float)):
        return float(v)
    s = str(v).strip().replace(",", "").replace("，", "").replace("¥", "").replace("元", "")
    if not s:
        return 0.0
    try:
        return float(s)
    except ValueError:
        return 0.0


def fmt(v, dec=0):
    return f"{v:,.{dec}f}"


# ---------------------------------------------------------------- 列定位

# 附加责任识别词：命中即视为「有条件给付」的附加险（意外/猝死/交通工具等）
EXTRA_KWS = ("意外", "猝死", "交通", "客运", "航空", "自驾", "电梯", "自然灾害", "伤残")
# 无条件附加识别词：命中视为「任何身故/全残都额外给」的附加责任
UNCOND_KWS = ("额外", "特别", "关爱", "特别关爱", "额外关爱")

# ★ 场景互斥：航空意外、动车意外、自驾意外……这些是**互斥的出险场景**，
#   不可能同时发生。把所有附加责任无条件加总会严重虚增峰值赔付。
SUB_SCENES = {
    "航空意外": ("航空", "飞机", "民航"),
    "动车高铁意外": ("动车", "列车", "高铁", "轨道交通", "铁路"),
    "客运交通意外": ("客运", "交通工具", "营运", "公共汽车", "轮船"),
    "自驾意外": ("自驾", "驾驶", "私家车"),
    "电梯意外": ("电梯",),
    "自然灾害": ("自然灾害", "地震", "洪水", "台风"),
    "猝死": ("猝死", "猝"),
    "疾病身故": ("疾病",),
}
# 通用意外：只写「意外」而不指定具体场景 → 适用于**所有**意外子场景
GENERAL_ACCIDENT = "意外"


# ★ 上位概念：有些公司的责任是「打包」的，一条覆盖多个具体场景——
#   「客运交通工具意外」通常包含飞机、火车（含动车高铁）、轮船、营运客车，
#   应该同时计入航空意外、动车高铁意外、客运交通意外三个场景。
#   实测德华安顾就是这样；若按单一场景归类，会让它在航空/动车场景的赔付
#   从 250 万/200 万 少算成 150 万/100 万，**在矩阵里被严重低估**。
#   必须**先于** SUB_SCENES 匹配，否则「客运」二字会先命中客运交通意外这一个格子。
UPPER_SCENES = {
    "交通工具": ["客运交通意外", "航空意外", "动车高铁意外", "自驾意外"],
    "公共交通": ["客运交通意外", "航空意外", "动车高铁意外"],
}


def scene_of(header):
    """判断一条附加责任覆盖哪些出险场景。

    返回 (场景列表, 是否为有条件附加)：
      ([], False)                          → 无条件附加（任何身故/全残都给）
      (["通用意外"], True)                  → 只含「意外」未指定子场景，适用所有意外场景
      (["航空意外"], True)                  → 该子场景专属
      (["航空意外","动车意外",...], True)    → 上位概念，同时覆盖多个场景
    """
    for kws, scenes in UPPER_SCENES.items():
        if kws in header:
            return list(scenes), True
    for name, kws in SUB_SCENES.items():
        if any(k in header for k in kws):
            return [name], True
    if GENERAL_ACCIDENT in header:
        return ["通用意外"], True
    return [], False


def _is_accident(scene):
    return bool(scene) and "意外" in scene


# ★ 出险情景「极端性」分类：决定峰值赔付要不要打「极端小概率」注解。
#   用户要求：最高赔付不能只给一个数字，必须注解它由哪几部分组成、是否极端。
#   互斥关系：航空/动车/自驾同属交通意外，互相排斥；交通意外与猝死、一般身故亦互斥
#   （现实中只能发生一种，峰值只是『单一最有利情景』而非可叠加总额）。
SCENE_EXTREME = {
    "一般身故/全残": ("常规", "最常见的身故/全残，绝大多数理赔属此情景"),
    "猝死": ("特定（非意外）", "需满足条款定义的猝死条件；与交通意外互斥"),
    "其他意外身故": ("意外（一般）", "泛指非交通类意外身故"),
    "客运交通意外": ("交通意外", "与航空/动车/自驾同属交通意外，互相排斥"),
    "自驾意外": ("交通意外", "与航空/动车/客运同属交通意外，互相排斥"),
    "航空意外": ("极端小概率", "空难，发生概率极低"),
    "动车高铁意外": ("极端小概率", "动车/高铁事故，发生概率极低"),
    "自然灾害": ("极端小概率", "地震/洪水/台风等，发生概率低且地域性强"),
}


# 出险情景清单（用于「情景 × 产品」赔付矩阵）
# (显示名, 场景标签)；标签 None = 一般身故（不加任何有条件附加）
SCENE_LIST = [
    ("一般身故/全残", None),
    ("猝死", "猝死"),
    ("其他意外身故", "通用意外"),
    ("客运交通意外", "客运交通意外"),
    ("航空意外", "航空意外"),
    ("动车高铁意外", "动车高铁意外"),
]


def _stack(base, uncond_vals, cond_items, tag):
    """累加「出险情景 tag」下应得的各项附加责任。

    cond_items: [(列名, 金额, 场景列表)]
    叠加规则：
      - 场景列表直接包含 tag → 计入
      - 场景列表为「通用意外」且 tag 本身是意外类场景 → 计入
        （信美「意外身故 15 万」就属于这种，航空/动车/其他意外都该给）
      - 猝死、疾病身故不是意外类，不叠「通用意外」
    """
    extra = 0.0
    for _, val, scs in cond_items:
        if tag in scs:
            extra += val
        elif "通用意外" in scs and _is_accident(tag):
            extra += val
    return base + uncond_vals + extra


def scene_pay(base, uncond_vals, cond_items, tag):
    """算出险情景 tag 下的总赔付（互斥场景不叠加，见 peak_by_scene 说明）。"""
    if tag is None:
        return base + uncond_vals
    return _stack(base, uncond_vals, cond_items, tag)


def peak_by_scene(base, uncond_vals, cond_items):
    """按场景叠加算「最高身故赔付」，避免把互斥场景加在一起。

    ★ 早期版本 d_max = 主责任 + 所有附加责任之和，
      会同时叠加上「航空意外 100 万」与「动车意外 100 万」——
      但一个人不可能既死于航空事故又死于动车事故。
      实测信美新版：虚报 425 万 / 8.36 倍，正确应为 315 万 / 6.20 倍，
      **虚高 35%**，足以让一款产品错误地登顶对比榜首。

    叠加规则（互斥情景只取其一）：
      一般身故   = 主 + 无条件附加
      通用意外   = 主 + 无条件 + 通用意外附加
      猝死       = 主 + 无条件 + 猝死附加（猝死不属意外，不叠意外附加）
      各子场景   = 主 + 无条件 + 通用意外附加 + 该子场景专属
    峰值 = 上述各情景最大值；返回 (金额, 情景名, 构成明细)。

    ★★ 构成明细用于「注解」而非「数字」：峰值由哪几部分组成、是否极端小概率，
      都必须在报告里写出来，不能只给一个孤零零的最高赔付数字。
    """
    def build_comp(tag):
        comp = [("一般身故/全残保险金", base)]
        if uncond_vals:
            comp.append(("无条件附加（任何身故/全残额外给）", uncond_vals))
        for hdr, val, scs in cond_items:
            if val <= 0:
                continue
            if tag in scs:
                comp.append((hdr, val))
            elif "通用意外" in scs and _is_accident(tag):
                comp.append((hdr, val))
        return comp

    comps = {}
    for lb, tag in SCENE_LIST:
        comps[lb] = build_comp(tag)
    best_lb = max(comps, key=lambda k: sum(v for _, v in comps[k]))
    comp = comps[best_lb]
    return sum(v for _, v in comp), best_lb, comp
# 主身故责任：只认这几种「纯」写法，不含额外/意外等修饰
MAIN_DEATH_KWS = ("身故保险金", "身故或全残保险金", "身故/全残保险金", "身故给付", "全残保险金")


class Col:
    """演示表的一列（已抽取为数值序列）。"""

    def __init__(self, idx, header, vals):
        self.idx = idx
        self.header = header
        self.vals = vals

    @property
    def nums(self):
        return [v for v in self.vals if v > 0]

    @property
    def constant(self):
        n = self.nums
        return len(n) >= 3 and max(n) == min(n)

    def __repr__(self):
        return f"<Col {self.idx} {self.header[:18]}>"


def find_demo_table(data):
    """挑出最可能是利益演示表的 table。

    ★ 与 build_policy.py 不同：杠杆寿的表演示表可能**没有**「现金价值」列
      （或现价为空），但一定有「身故/全残保险金」之类的保障列，
      所以这里把保障类关键词也算进候选分，否则定额寿会「找不到演示表」。
    """
    pages = data.get("data", {}).get("pages", []) if data.get("kind") == "pdf" else []
    cands = []
    for p in pages:
        for tb in p.get("tables", []):
            if len(tb) < 5:      # 噪声碎片过滤：真实演示表必然 ≥5 个保单年度
                continue
            flat = " ".join(norm(c) for r in tb for c in r)
            score = 0
            if "保单年度" in flat or (len(tb) > 1 and re.search(r"^\d+$", norm(tb[1][0]))):
                score += 2
            for kw in ("现金价值", "生存总利益", "总利益", "身故", "全残", "保险金",
                       "养老年金", "累积红利"):
                if kw in flat:
                    score += 1
            if score >= 2:
                cands.append((score, tb))
    if not cands:
        # docx 结构：tables 平铺在 data.tables
        for tb in data.get("data", {}).get("tables", []):
            if len(tb) < 5:
                continue
            flat = " ".join(norm(c) for r in tb for c in r)
            score = sum(1 for kw in ("现金价值", "身故", "保单年度", "保险金") if kw in flat)
            if score >= 2:
                cands.append((score, tb))
    if not cands:
        return None
    cands.sort(key=lambda x: (-x[0], -len(x[1]), -max((len(r) for r in x[1]), default=0)))
    return cands[0][1]


def header_of(tb, i, rows_start):
    """拼接表头区该列的所有文字（合并单元格还原：跨列表头只在首格有值）。"""
    toks = []
    for r in range(max(0, rows_start)):
        if i < len(tb[r]):
            t = norm(tb[r][i])
            if t:
                toks.append(t)
    # 合并单元格右向填充：表头行里本列为空时，沿用同一行左侧最近的非空表头
    return "".join(toks)


def locate(tb):
    """定位演示表的各类列。返回 (rows_start, dict)。"""
    ncol = max(len(r) for r in tb)
    # 数据起始行：首行含 ≥2 个纯数字单元格即数据行（合并表头会让表头行没有纯数字）
    start = 0
    for i, r in enumerate(tb):
        cnt = sum(1 for c in r if re.fullmatch(r"[\d,，.]+", norm(c)) and norm(c))
        if cnt >= 2:
            start = i
            break
    headers = []
    for i in range(ncol):
        h = header_of(tb, i, start) if start else norm(tb[0][i] if i < len(tb[0]) else "")
        headers.append(h)

    cols = {}
    for i, h in enumerate(headers):
        vals = []
        for r in tb[start:]:
            vals.append(to_float(r[i]) if i < len(r) else 0.0)
        cols[i] = Col(i, h, vals)

    def pick(kws, exclude=()):
        for i, c in cols.items():
            if any(k in c.header for k in kws) and not any(k in c.header for k in exclude):
                return c
        return None

    def pick_all(kws, exclude=()):
        return [c for c in cols.values()
                if any(k in c.header for k in kws) and not any(k in c.header for k in exclude)]

    res = {}
    res["year"] = pick(["保单年度"]) or pick(["年度"], exclude=("年龄", "年末年龄"))
    res["age"] = pick(["年龄"])
    res["prem"] = pick(["当年保费", "期交保费", "年交保费", "年度保险费", "当年保险费",
                        "每年保费", "当年度保险费", "保险费", "保费"],
                       exclude=("累计", "合计", "总保费", "首年"))
    res["cum_prem"] = pick(["累计保费", "累计保险费", "累计所交保费", "累计已交保费",
                            "累计应交保费", "所交保费", "累计保费合计"])
    res["cv"] = pick(["现金价值", "退保金"], exclude=("红利", "万能"))
    # 主身故责任：必须「不含」附加/意外等修饰词
    res["death"] = pick(MAIN_DEATH_KWS, exclude=EXTRA_KWS + UNCOND_KWS)
    # 附加责任
    # ★ 附加责任候选词必须比「身故/全残」宽：实测「猝死关爱保险金」这种列名
    #   一个「身故」字样都没有，只按身故/全残筛会把整条附加责任漏掉，
    #   导致峰值赔付少算（德华安顾实测少算 10 万猝死责任）。
    res["extra_cond"] = pick_all(
        ("身故", "全残", "猝死", "意外", "关爱", "交通", "客运", "航空",
         "自驾", "电梯", "自然灾害", "疾病"),
        exclude=("现金价值", "保费", "红利", "年度", "年龄"))
    res["sa"] = pick(["有效保险金额", "基本保额", "保险金额", "身故保额"],
                     exclude=("现金价值", "红利"))
    if res["death"] is not None:
        res["extra_cond"] = [c for c in res["extra_cond"]
                             if c.idx != res["death"].idx
                             and any(k in c.header for k in EXTRA_KWS + UNCOND_KWS)]
    else:
        res["extra_cond"] = []
    # 无条件附加（任何身故都额外给）：含「额外/关爱」但不含「意外/交通/猝死」
    res["extra_uncond"] = [c for c in res["extra_cond"]
                           if any(k in c.header for k in UNCOND_KWS)
                           and not any(k in c.header for k in EXTRA_KWS)]

    # 年度行过滤：去掉年度为 0 的行（表头残留）
    if res["year"] is not None:
        keep = [k for k, v in enumerate(res["year"].vals) if v > 0]
        for k, c in res.items():
            if isinstance(c, Col):
                c.vals = [c.vals[k] for k in keep]
            elif isinstance(c, list):
                for cc in c:
                    cc.vals = [cc.vals[k] for k in keep]
    return start, res


# ---------------------------------------------------------------- 形态判定


def judge(name, prems, death, cv, sa, back_year=None):
    """定额终身寿 vs 增额终身寿 判定。返回 (形态, 置信度, 证据列表)。

    判据按可靠性加权；主判据是**主身故/全残保险金列是否恒定**——
    定额寿的保额终身不变，增额寿的身故赔付随现价/保额逐年递增，这条几乎不会错。
    """
    ev, s_ding, s_zeng = [], 0, 0
    nn = norm(name)

    # ① 主身故赔付列是否恒定（决定性）
    if death is not None and len(death.nums) >= 3:
        if death.constant:
            s_ding += 3
            ev.append(("✓", f"主身故/全残赔付列全期恒定 = {fmt(death.nums[0])}"
                            f"（定额终身寿的决定性特征）"))
        else:
            s_zeng += 3
            ev.append(("✓", f"主身故/全残赔付列逐年递增 {fmt(death.nums[0])} → "
                            f"{fmt(death.nums[-1])}（增额终身寿的决定性特征）"))

    # ② 有效保额/基本保额列是否递增
    if sa is not None and len(sa.nums) >= 3:
        if sa.constant:
            s_ding += 2
            ev.append(("✓", f"基本保额列恒定 = {fmt(sa.nums[0])}"))
        else:
            s_zeng += 2
            ev.append(("✓", f"保额列逐年递增 {fmt(sa.nums[0])} → {fmt(sa.nums[-1])}"))

    # ③ 产品名
    if "增额" in nn:
        s_zeng += 2
        ev.append(("✓", "产品名含「增额」"))
    elif "终身" in nn:
        ev.append(("·", "产品名不含「增额」（弱信号，不少增额寿产品名也不带）"))

    # ★ 判据④⑤ 依赖「首年现价 / 年交保费」与「回本速度」，这两条对**趸交**完全不成立：
    #   趸交一次性交清，首年现价天然接近甚至超过已交保费、回本天然在第 1 年，
    #   若照常计分会把趸交的定额传承型产品推成「增额寿」
    #   （实测 chengrao.json：趸交 100 万保 500 万，依据栏出现
    #    「身故列恒定→定额」与「首年现价 258%、第 1 年回本→增额」的自相矛盾证据）。
    pay_years = sum(1 for p in prems if p > 0)
    single = pay_years <= 1
    if single:
        ev.append(("·", "趸交（一次交清）→ 首年现价占比与回本速度两条判据不适用，已跳过"))

    # ④ 首年现价 / 年交保费（增额寿首年现价通常占保费 20%~80%，定额寿极低）
    #    ★ 现价列缺失（全 0）时必须跳过，不能把「首年现价 0」当成定额寿的证据——
    #      那是用缺失数据冒充证据，会让置信度虚高
    #      （实测信美无现价数据，却被判出「首年现价占比 0.0%」的"证据"）。
    has_cv = cv is not None and any(v > 0 for v in cv.vals)
    if has_cv and prems and not single:
        p0 = prems[0] if prems[0] > 0 else (prems[1] if len(prems) > 1 else 0)
        if p0 > 0 and cv.vals:
            r = cv.vals[0] / p0
            if r < 0.15:
                s_ding += 1
                ev.append(("✓", f"首年现价 {fmt(cv.vals[0])} 仅为年交保费 {fmt(p0)} 的 "
                                f"{r*100:.1f}%（增额寿通常 20%~80%）"))
            elif r > 0.5:
                s_zeng += 1
                ev.append(("✓", f"首年现价 {fmt(cv.vals[0])} 达年交保费的 {r*100:.1f}%"))

    # ⑤ 现价回本速度
    if back_year and not single:
        if back_year <= 15:
            s_zeng += 1
            ev.append(("✓", f"现价第 {back_year} 年即回本（增额寿典型节奏）"))
        elif back_year >= 30:
            s_ding += 1
            ev.append(("✓", f"现价回本在第 {back_year} 年（增额寿通常 ≤15 年）"))

    # ⑥ 末年现价 vs 身故保额 —— **只作佐证，不参与计分**
    #    原因：增额寿的身故赔付 = max(现价, 保额)，后期现价反超后两者同样趋近，
    #    年末现价/保额 落在 1.0 附近只是巧合（实测 5万趸交.json 命中的是增额寿），
    #    早期版本给它加了定额分，直接把增额寿推向误判。
    if cv is not None and death is not None and cv.vals and death.nums and death.constant:
        end_cv, sa0 = cv.vals[-1], death.nums[0]
        if sa0 > 0 and 0.8 <= end_cv / sa0 <= 1.05:
            ev.append(("·", f"末年现价 {fmt(end_cv)} 收敛于保额 {fmt(sa0)}"
                            f"（佐证：保额终身未增长）"))

    if s_ding > s_zeng:
        shape, gap = "定额终身寿（杠杆寿）", s_ding - s_zeng
    elif s_zeng > s_ding:
        shape, gap = "增额终身寿（储蓄型）", s_zeng - s_ding
    else:
        shape, gap = "无法判定（需人工确认）", 0
    conf = "高" if gap >= 4 else ("中" if gap >= 2 else "低")
    if shape.startswith("无法"):
        conf = "—"
        ev.append(("!", "可用判据不足或证据势均力敌，**不要自动路由**，须人工看条款确认"))
        # 说清楚缺什么，否则使用者只知道「判不出来」，不知道该补什么数据
        missing = []
        if death is None or len(getattr(death, "nums", []) or []) < 3:
            missing.append("身故/全残保险金列（★ 决定性判据）")
        if sa is None:
            missing.append("基本保额或有效保险金额列")
        if cv is None or not cv.vals:
            missing.append("现金价值列（不影响形态判定，但现价/IRR/回本无法计算）")
        if not any(p > 0 for p in prems):
            missing.append("保费列")
        if missing:
            ev.append(("!", "本表未能定位到：" + "、".join(missing)
                       + "。可用 `--sum-assured` 指定保额，或手工构造 policy.json 重跑。"))
    elif gap < 4:
        ev.append(("!", "置信度非「高」，建议在报告里写明判定依据，"
                        "或向用户确认后再下结论"))
    return shape, conf, ev


# ---------------------------------------------------------------- 杠杆率


def leverage(name, prems, death_all, death_base, death_max, cv, n_year, sa, extra_names,
             peak_scenes=None):
    """杠杆率全套指标。death_* 均为「各保单年度末」的序列。"""
    out = {}
    total = sum(p for p in prems if p > 0)
    out["total_prem"] = total
    p0 = prems[0] if prems[0] > 0 else (prems[1] if len(prems) > 1 else 0)
    out["annual_prem"] = p0
    out["pay_years"] = sum(1 for p in prems if p > 0)

    sa0 = sa if sa else (death_base[0] if death_base else 0)
    out["sum_assured"] = sa0

    if p0 > 0 and sa0:
        out["lev_first"] = sa0 / p0
    if total > 0 and sa0:
        out["lev_total"] = sa0 / total
        out["cost_per_10k"] = total / (sa0 / 10000.0)
    if total > 0 and death_max:
        mx = max(death_max)
        out["death_peak"] = mx
        out["lev_peak"] = mx / total
        out["peak_year"] = death_max.index(mx) + 1
        out["peak_scene"] = peak_scenes.get(out["peak_year"], "—")
    return out


def back_year_of(prems, cv_vals, years=None):
    """现价 ≥ 累计已交保费 的最早年度；无则 None。

    ★ 保费列定位失败时（prems 全 0）必须直接返回 None。
      早期版本没做这层保护：累计保费全为 0，而「现价 ≥ 0」恒成立，
      于是**任何产品都会被判成「第 1 年即回本」**，进而把增额寿的证据喂给定额寿判定
      （实测 chengrao.json 依据栏同时出现「身故列恒定→定额」和
      「第 1 年回本→增额」两条自相矛盾的证据）。

    ★★ years：演示表常常**只给抽样年度**（实测德华安顾鑫传家只给 1–15、25、35、45、
      55、65、70，共 21 行）。此时「第 i 个数据点」≠「第 i 年」，
      若返回 i+1 会把第 35 年的数据报成「第 17 年」（实测报出「第 17 年回本、
      年龄 70 岁」这种自相矛盾的输出）。故优先返回 years[i] 这个真实年度。
    """
    if not any(p > 0 for p in prems):
        return None
    cum, acc = [], 0.0
    for p in prems:
        acc += p
        cum.append(acc)
    n = min(len(cum), len(cv_vals))
    for i in range(n):
        if cv_vals[i] >= cum[i] - 1e-6 and cv_vals[i] > 0:
            if years and i < len(years):
                return int(years[i])
            return i + 1
    return None


# ---------------------------------------------------------------- 单品分析


def analyze(src, sum_assured=None, quiet=False):
    """src 可以是 extract.json 路径，也可以是手工 policy.json 路径。"""
    with open(src, encoding="utf-8") as f:
        d = json.load(f)

    if "kind" in d and "data" in d:                       # extract.py 产出
        # ★ PDF 的正文在 data.pages[].text 里，不在 paragraphs（那是 docx 结构）。
        #   只翻 paragraphs 的话 PDF 产品名永远是文件名，报告里没法看。
        texts = list(d.get("data", {}).get("paragraphs", []))
        for pg in d.get("data", {}).get("pages", []):
            t = pg.get("text", "")
            if t:
                texts.extend(ln for ln in t.splitlines() if ln.strip())
        name = None
        for p in texts[:120]:
            if "终身" in p or "两全" in p or "年金" in p:
                name = p.strip()[:60]
                break
        if name is None:
            for p in texts[:40]:
                if "保险" in p and len(p.strip()) < 60:
                    name = p.strip()
                    break
        tb = find_demo_table(d)
        if tb is None:
            return None, f"[跳过] {src}: 未找到利益演示表"
        _, c = locate(tb)
        prems = [v for v in c["prem"].vals] if c["prem"] else []
        # ★ 保费列兜底：很多计划书只给「累计保费」不给「当年保费」，
        #   或列名写作「保险费/保费」被别的规则排除。此时用累计列做差分还原逐年保费，
        #   否则杠杆率全空（分母为 0），这个脚本就白跑了。
        if not any(p > 0 for p in prems) and c["cum_prem"]:
            cum = c["cum_prem"].vals
            prems = [cum[0]] + [cum[i] - cum[i - 1] for i in range(1, len(cum))]
        ncv = len(c["cv"].vals) if c["cv"] else 0
        years = ([int(v) for v in c["year"].vals] if c["year"]
                 else list(range(1, ncv + 1)) if ncv
                 else list(range(1, len(prems) + 1)))
        # ★ 年龄必须用表里的年龄列，不能拿「30 + 年度」硬推 ——
        #   被保人不是 30 岁时会整列错位，且无法显示真实投保年龄。
        ages = [int(v) for v in c["age"].vals] if c["age"] else []
        if ages and years:
            entry_age = ages[0] - years[0]
        else:
            entry_age = None
        cvv = c["cv"].vals if c["cv"] else []
        death = c["death"]
        extra = c["extra_cond"]
        sa_col = c["sa"]
        insured = ""
        for p in d.get("data", {}).get("paragraphs", []):
            m = re.search(r"被保[人险][：: ]*([^\t\n]{0,12})", p)
            if m:
                insured = m.group(1).strip()
                break
    else:                                                  # 手工 policy.json
        name = d.get("name") or os.path.basename(src)
        insured = d.get("insured", "")
        years = d.get("years") or list(range(1, len(d.get("premiums", [])) + 1))
        prems = [to_float(v) for v in d.get("premiums", [])]
        cvv = [to_float(v) for v in d.get("cv", d.get("cv_guaranteed", []))]
        if cvv and len(cvv) == len(prems) + 1:             # 0 基占位 [0, y1, y2...]
            cvv = cvv[1:]
        dv = d.get("death_benefit") or []
        # ★ 方便手工录入：定额终身寿的保额终身恒定，允许只写一个值自动铺满全期
        #   （写 75 遍 1000000 既啰嗦又容易数错）。
        if len(dv) == 1:
            _lens = [len(prems), len(cvv)] + \
                    [len(v) for v in (d.get("extra_death") or {}).values()]
            dv = dv * (d.get("years_count") or max(_lens) or 75)
        death = Col(-1, "身故保险金", [to_float(v) for v in dv]) if dv else None
        extra = [Col(-1, k, [to_float(v) for v in vs])
                 for k, vs in (d.get("extra_death") or {}).items()]
        sa_col = Col(-1, "保额", [to_float(d.get("sum_assured", 0))]) \
            if d.get("sum_assured") else None
        ages = d.get("ages") or []
        entry_age = d.get("entry_age")

    if sum_assured:
        sa_col = Col(-1, "保额", [float(sum_assured)])

    n = max([len(years)] + [len(prems)] + [len(cvv)] +
            ([len(death.vals)] if death else []) +
            [len(e.vals) for e in extra] or [0])

    def pad(seq):
        s = list(seq) + [0.0] * (n - len(seq))
        return s[:n]

    prems = pad(prems)
    cvv = pad(cvv)
    d_base = pad(death.vals) if death else [0.0] * n
    # 身故总赔付 = 主责任 + 无条件附加（任何身故/全残都额外给的）
    uncond = [e for e in extra
              if any(k in e.header for k in UNCOND_KWS)
              and not any(k in e.header for k in EXTRA_KWS)]
    d_all = [d_base[i] + sum(pad(e.vals)[i] for e in uncond) for i in range(n)]

    # ★ 峰值赔付按「场景叠加」而不是「所有附加责任加总」——
    #   互斥场景（航空 vs 动车）不能同时发生，见 peak_by_scene 的说明。
    cond = [(e, scene_of(e.header)) for e in extra
            if not (any(k in e.header for k in UNCOND_KWS)
                    and not any(k in e.header for k in EXTRA_KWS))]
    peak_scenes, peak_comp, d_max = {}, {}, []
    for i in range(n):
        uc = sum(pad(e.vals)[i] for e in uncond)
        items = [(e.header, pad(e.vals)[i], scs) for e, (scs, sub) in cond if sub]
        val, scene, comp = peak_by_scene(d_base[i], uc, items)
        d_max.append(val)
        peak_scenes[i + 1] = scene
        peak_comp[i + 1] = comp

    # 「出险情景 × 赔付」矩阵（第 1 年度各项附加责任均在有效期内）
    _uc0 = sum(pad(e.vals)[0] for e in uncond) if n else 0
    _items0 = [(e.header, pad(e.vals)[0], scs) for e, (scs, sub) in cond if sub]
    scenes = {}
    for _label, _tag in SCENE_LIST:
        scenes[_label] = scene_pay(d_base[0] if n else 0, _uc0, _items0, _tag)
    scenes["附加责任到期后"] = d_base[-1] if d_base else 0

    by = back_year_of(prems, cvv, years)
    shape, conf, ev = judge(name or src, prems, death if death else None,
                            Col(-1, "cv", cvv) if cvv else None, sa_col, by)
    lev = leverage(name or src, prems, d_all, d_base, d_max, cvv, n,
                   (sa_col.nums[0] if sa_col and sa_col.nums else None),
                   [e.header for e in extra], peak_scenes)
    # ★ 把峰值构成明细 + 极端性标签挂到杠杆指标上，供 show/compare 做注解
    lev["peak_scene"] = peak_scenes.get(lev.get("peak_year", 0), "—")
    lev["peak_comp"] = peak_comp.get(lev.get("peak_year", 0), [])
    lev["peak_extreme"] = SCENE_EXTREME.get(lev["peak_scene"], ("", ""))[0]

    ages = pad([float(a) for a in ages]) if ages else [
        (entry_age + i + 1) if entry_age is not None else 0.0 for i in range(n)]
    return {
        "name": name or os.path.basename(src), "insured": insured, "shape": shape,
        "conf": conf, "ev": ev, "lev": lev, "years": years, "prems": prems,
        "cv": cvv, "d_base": d_base, "d_all": d_all, "d_max": d_max,
        "back_year": by, "extra": [e.header for e in extra],
        "n": n, "ages": ages, "entry_age": entry_age, "scenes": scenes,
    }, None


def show(r):
    L = r["lev"]
    print("═" * W)
    print(" 终身寿险形态判定（SKILL.md §六 路由）")
    print("═" * W)
    print(f"产品：{r['name']}")
    print(f"被保人：{r['insured'] or '—'}　保额：{fmt(L['sum_assured']) if L.get('sum_assured') else '—'}"
          f"　交费：{L.get('pay_years', '—')} 年"
          f"　年交：{fmt(L.get('annual_prem', 0))}")
    print()
    print(f"【形态】{r['shape']}　　置信度：{r['conf']}")
    print("依据：")
    for mark, t in r["ev"]:
        print(f"  {mark} {t}")

    if r["shape"].startswith("定额"):
        print()
        print("→ 路由：按 §7.18 **杠杆寿**口径分析 ——")
        print("　主看杠杆率（保额÷保费 = 性价比）；现金价值与 IRR 仅作辅助，")
        print("　**不作为评价指标**（IRR 长期 0~1% 是杠杆寿的本来面目，不是产品差）。")
    elif r["shape"].startswith("增额"):
        print()
        print("→ 路由：按「七、储蓄理财类」做 总利益 / IRR / 回本 全套分析。")
    else:
        print()
        print("→ 路由：**暂停自动分析**，先向用户确认是定额还是增额。")

    # 杠杆率：定额寿是主指标，增额寿只是参考（它的卖点是现价增值不是身故杠杆）
    is_ding = r["shape"].startswith("定额")
    print()
    print("═" * W)
    if is_ding:
        print(" 杠杆率（★ 定额终身寿的核心性价比指标）")
    else:
        print(" 杠杆率（参考）—— 本产品判为" + r["shape"].split("（")[0] +
              "，卖点是现价增值，主看 IRR")
    print("═" * W)
    sa, total = L.get("sum_assured", 0), L.get("total_prem", 0)
    rows = [
        ("首年杠杆", f"{fmt(sa)} ÷ {fmt(L.get('annual_prem',0))} 年交",
         f"{L['lev_first']:.2f} 倍" if L.get("lev_first") else "—",
         "第 1 年的保障放大倍数"),
        ("总保费杠杆", f"{fmt(sa)} ÷ {fmt(total)} 总保费",
         f"{L['lev_total']:.2f} 倍" if L.get("lev_total") else "—",
         "★ 掏完所有钱后的放大倍数，横向可比"),
        ("峰值赔付杠杆", f"{fmt(L.get('death_peak',0))} ÷ {fmt(total)}",
         f"{L['lev_peak']:.2f} 倍" if L.get("lev_peak") else "—",
         f"最有利情景：{L.get('peak_scene','—')}（{L.get('peak_extreme') or '—'}；"
         f"第 {L.get('peak_year','—')} 年；互斥场景不叠加）"),
        ("单位保障成本", f"{fmt(total)} ÷ {sa/10000:.0f} 万元保额",
         f"{L['cost_per_10k']:,.0f} 元/万元" if L.get("cost_per_10k") else "—",
         "★ 每买 1 万元身故保障花多少，越低越划算"),
    ]
    print(f"{'指标':<14}{'算式':<34}{'结果':<14}")
    print("─" * W)
    for a, b, c, _ in rows:
        print(f"{a:<14}{b:<34}{c:<14}")
    print("─" * W)
    for a, _, _, d in rows:
        print(f"  · {a}：{d}")

    # ★ 峰值赔付构成注解：由哪几部分组成 + 是否极端小概率情景。
    #   用户明确要求：最高赔付不能只给数字，必须注解组成与极端性。
    if L.get("peak_comp") and L.get("death_peak"):
        comp = L["peak_comp"]
        print("─" * W)
        print(" 峰值赔付构成（★ 单一出险情景，互斥情景不可叠加）")
        print(f"   合计 {fmt(L['death_peak'])} =")
        for lbl, amt in comp:
            print(f"     · {lbl}：{fmt(amt)}")
        ex = L.get("peak_extreme", "") or "常规"
        print(f"   情景类别：{L.get('peak_scene','—')}（{ex}）")
        if ex == "极端小概率":
            print("   ⚠ 该峰值为极端小概率情景（如空难/动车事故），发生概率极低；")
            print("     不可据此判断产品日常杠杆，日常身故杠杆请看『总保费杠杆/一般身故赔付』。")

    if r["back_year"]:
        print(f"\n现价回本：第 {r['back_year']} 年（现价 ≥ 累计已交保费）")
    elif r["cv"] and any(r["cv"]):
        print("\n现价回本：持有期内未回本")

    # 逐年表：只有定额寿才列（增额寿按 §7 走 irr.py，列杠杆衰减没有意义）
    if not is_ding:
        print()
        print("─" * W)
        print(" 本产品不列逐年杠杆表 —— 增额终身寿请走标准储蓄理财链路：")
        print("   python build_policy.py <extract.json> --name <产品> --run")
        print("   或手工构造 policy 后 python irr.py --input policy.json")
        return

    if r["cv"] and any(r["cv"]):
        print()
        print("═" * W)
        print(" 逐年杠杆衰减与退保差额")
        print("═" * W)
        print(f"{'年度':>5}{'年龄':>6}{'累计保费':>12}{'一般身故赔付':>13}"
              f"{'杠杆':>9}{'现金价值':>12}{'退保差额':>12}")
        print("─" * W)
        # ★ 演示表常只给抽样年度（1–15、25、35…），此时「第 i 个数据点」≠「第 i 年」。
        #   必须按真实年度 r["years"] 取值，否则会把第 35 年（70 岁）的数据
        #   打印成「第 17 年、70 岁」这种自相矛盾的行（实测德华安顾鑫传家踩到）。
        yrs = [int(v) for v in (r.get("years") or [])]
        if len(yrs) != r["n"]:
            yrs = list(range(1, r["n"] + 1))
        want = sorted(set([1, 5, 10, 20, 30, 40, 50, 60, 70] +
                          ([r["back_year"]] if r["back_year"] else []) +
                          [yrs[-1] if yrs else r["n"]]))
        # 每个目标年度取「不超过它的最后一个实际数据点」，绝不插值
        shown = set()
        for y in want:
            idxs = [k for k, yy in enumerate(yrs) if yy <= y]
            if not idxs:
                continue
            i = idxs[-1]
            if yrs[i] in shown:      # 多个目标年度落在同一数据点上，只显示一次
                continue
            shown.add(yrs[i])
            acc = sum(r["prems"][:i + 1])
            dl = r["d_all"][i] or r["d_max"][i]
            cvv = r["cv"][i]
            lev = dl / acc if acc > 0 else 0
            age = int(r["ages"][i]) if i < len(r["ages"]) and r["ages"][i] else 0
            print(f"{yrs[i]:>5}{(str(age) if age else '—'):>6}{fmt(acc):>12}"
                  f"{fmt(dl):>13}{lev:>8.1f}x{fmt(cvv):>12}{fmt(acc-cvv):>12}")
        print("─" * W)
        print("  杠杆 = 当年一般身故赔付 ÷ 累计已交保费（随时间自然衰减，属正常现象）")
        print("  退保差额 = 累计已交保费 − 当年现金价值")
        print("    正数 → 若当年退保，比已交保费少拿回这么多（即保障的净花费）")
        print("    负数 → 退保能拿回的比已交保费还多（现价已超保费，但身故则按保额赔、二选一）")


# ---------------------------------------------------------------- 多品对比


def compare(rs):
    print()
    print("═" * W)
    print(f" 杠杆寿横向对比（{len(rs)} 款）　★ 主看杠杆，不看 IRR")
    print("═" * W)
    # ★ 产品名常常完全一样（同一产品的不同档位），用「#序号 + 年交保费」做列标签，
    #   表后再列完整名称对照，否则对比表两列同名、根本看不出谁是谁。
    short, full = [], []
    for i, r in enumerate(rs, 1):
        p = r["lev"].get("annual_prem", 0)
        short.append(f"#{i} {fmt(p)}")
        full.append(f"  #{i} = {r['name']}（{r['insured'] or '—'}，"
                    f"年交 {fmt(p)}，{r['shape'].split('（')[0]}）")
    print(f"{'指标':<16}" + "".join(f"{s:>15}" for s in short))
    print("─" * W)

    def row(label, fn, better=None, dec=0):
        """better: 'max' / 'min' / None → 给最优值打 ★，省得读者自己比大小。

        ★ 格式化与打星必须分开做：早期版本先打星（值变字符串），
        再统一格式化，结果带 ★ 的那格不走千分位，出现「26,500」与「23780.0 ★」并排。
        """
        raw, txt = [], []
        for r in rs:
            try:
                v = fn(r["lev"], r)
            except Exception:
                v = None
            raw.append(v)
            txt.append("—" if v is None else
                       (f"{v:,.{dec}f}" if isinstance(v, (int, float)) else str(v)))
        if better and len(rs) > 1:
            nums = [v for v in raw if isinstance(v, (int, float))]
            if nums and len(set(nums)) > 1:        # 全部相同就不打星，避免无意义标记
                best = max(nums) if better == "max" else min(nums)
                for i, v in enumerate(raw):
                    if v == best:
                        txt[i] = txt[i] + " ★"
        print(f"{label:<16}" + "".join(f"{t:>15}" for t in txt))

    row("形态", lambda L, r: r["shape"].split("（")[0])
    # ★ 缴费期必须单列：总保费 = 年交 × 缴费期，缴费期不同会让「总保费杠杆」
    #   天然失真（交得越久总保费越高、杠杆越低），这是数学必然不是产品优劣。
    row("缴费期(年)", lambda L, r: L.get("pay_years", 0))
    # 保费行不打星：保额/责任不同时「便宜」不代表划算，会被误读成推荐。
    row("年交保费", lambda L, r: L.get("annual_prem", 0))
    row("总保费", lambda L, r: L.get("total_prem", 0))
    row("保额", lambda L, r: L.get("sum_assured", 0))
    # 以下是已按保额归一化的指标，可直接打星
    row("首年杠杆(倍)", lambda L, r: L.get("lev_first"), "max", dec=2)
    row("总保费杠杆(倍)", lambda L, r: L.get("lev_total"), "max", dec=2)
    row("峰值杠杆(倍)", lambda L, r: L.get("lev_peak"), "max", dec=2)
    # 峰值情景：纯文本行，标注情景名 + 极端性，不打★（非数值指标）
    row("峰值情景", lambda L, r: (f"{L.get('peak_scene','—')}"
                                  + (f"（{L.get('peak_extreme')}）"
                                     if L.get("peak_extreme") else "")))
    row("单位成本(元/万)", lambda L, r: L.get("cost_per_10k"), "min")
    row("回本(年)", lambda L, r: r["back_year"] if r.get("back_year") else None, "min")
    print("─" * W)
    print("对照：")
    for f in full:
        print(f)
    print("─" * W)
    print("※ ★ = 该指标更优。年交保费/总保费越低越省，但**必须结合保额与附加责任一起看**，")
    print("  单看保费低没有意义（可能是保障缩水）。")
    print("※ 单位保障成本 = 总保费 ÷ 保额（万元）；总保费杠杆 = 保额 ÷ 总保费，两者互为倒数。")
    print("※ 只有形态一致（都是定额终身寿）才能直接比；混入增额寿须分开看。")
    # ★ 缴费期不一致告警：总保费杠杆会被缴费期长短直接扭曲
    pays = {r["lev"].get("pay_years") for r in rs}
    if len(pays) > 1:
        desc = "；".join(f"#{i} {r['lev'].get('pay_years')} 年"
                        for i, r in enumerate(rs, 1))
        print("─" * W)
        print(f"⚠ 缴费期不一致（{desc}）——总保费杠杆**不能直接比大小**。")
        print("  总保费 = 年交 × 缴费期：交得越久，总保费越高、总保费杠杆越低，")
        print("  这是数学必然，**不代表产品更差**（拉长缴费反而提高首年杠杆、")
        print("  降低每年缴费压力）。此时请重点看「首年杠杆 / 单位保障成本」，")
        print("  或把产品按缴费期分组后再比总保费杠杆。")
    print("─" * W)
    print(" 峰值赔付构成（★ 单一出险情景，互斥不可叠加；标签含「极端」= 小概率情景）")
    for i, r in enumerate(rs, 1):
        L = r["lev"]
        comp = L.get("peak_comp", [])
        if not comp or not L.get("death_peak"):
            continue
        parts = " + ".join(f"{lbl}{fmt(a)}" for lbl, a in comp)
        print(f"   #{i}（{r['name'][:14]}）：合计 {fmt(L['death_peak'])} = {parts}")
        if L.get("peak_extreme") == "极端小概率":
            print(f"       ⚠ {L['peak_scene']} 为极端小概率情景，"
                  f"日常身故杠杆请以『总保费杠杆』为准，勿据峰值判断性价比。")


def print_matrix(rs):
    """多品「出险情景 × 产品」赔付矩阵。

    ★ 这是杠杆寿对比里信息量最大的一张表：基本保额都是 100 万，
      但不同出险情景下实际赔付可能差 3 倍，只比保费和保额根本看不出来。
    """
    print()
    print("═" * W)
    print(" 出险情景 × 产品 赔付矩阵（元）")
    print("═" * W)
    print("  取第 1 保单年度（各项附加责任均在有效期内）；"
          "末行为附加责任全部到期后的赔付。")
    short = [f"#{i}" for i in range(1, len(rs) + 1)]
    print(f"{'出险情景':<18}" + "".join(f"{s:>13}" for s in short))
    print("─" * W)
    keys = [lb for lb, _ in SCENE_LIST] + ["附加责任到期后"]
    for k in keys:
        vals = []
        for r in rs:
            v = r.get("scenes", {}).get(k, 0)
            vals.append("—" if not v else f"{v:,.0f}")
        # 该情景下的最高赔付打 ★
        nums = [r.get("scenes", {}).get(k, 0) for r in rs]
        mx = max(nums) if nums else 0
        vals = [f"{v} ★" if nums[i] == mx and mx > 0 and len(set(nums)) > 1 else v
                for i, v in enumerate(vals)]
        print(f"{k:<18}" + "".join(f"{v:>13}" for v in vals))
    print("─" * W)
    print("  ★ = 该情景下赔付最高。重要注解：")
    print("  ① 所有『最高赔付』均为**单一出险情景**下的金额，**互斥情景不可叠加**——")
    print("     航空/动车/自驾同属交通意外，现实中只能发生其一；")
    print("     交通意外与猝死、一般身故亦互斥（一次身故只赔一种情景）。")
    print("     故峰值只是『单一最有利情景』，≠ 各项之和，不可当作可拿到的『总额』。")
    print("  ② 标记「极端」的情景（航空/动车高铁/自然灾害）发生概率极低；")
    print("     峰值杠杆高≠日常杠杆高，勿据极端情景判断产品性价比。")
    print("  ③ 各情景是否成立、猝死是否属意外，均以**保险合同条款**为准，此表为计划书口径推演。")


# ---------------------------------------------------------------- main


def main():
    ap = argparse.ArgumentParser(description="终身寿险形态判定 + 杠杆率测算")
    ap.add_argument("--extract", nargs="*", help="extract.py 产出的 JSON（可多个）")
    ap.add_argument("--policy", nargs="*", help="手工构造的 policy JSON（可多个）")
    ap.add_argument("--sum-assured", type=float, help="手工指定基本保额（抽取不到时用）")
    ap.add_argument("--compare", action="store_true", help="多品时输出横向对比表")
    ap.add_argument("--matrix", action="store_true",
                    help="多品时输出「出险情景 × 产品」赔付矩阵（★ 杠杆寿建议必出）")
    a = ap.parse_args()

    srcs = [(p, False) for p in (a.extract or [])] + [(p, True) for p in (a.policy or [])]
    if not srcs:
        ap.print_help()
        return 1

    rs = []
    for p, _ in srcs:
        if not os.path.exists(p):
            print(f"[错误] 文件不存在：{p}")
            continue
        r, err = analyze(p, a.sum_assured)
        if err:
            print(err)
            continue
        rs.append(r)
        show(r)
        print()

    if len(rs) > 1 and a.matrix:
        print_matrix(rs)
    if len(rs) > 1 and a.compare:
        compare(rs)

    # 形态不一致时给提示
    shapes = {r["shape"].split("（")[0] for r in rs}
    if len(rs) > 1 and len(shapes) > 1:
        print("⚠ 参与对比的产品形态不一致（" + "、".join(shapes) + "），"
              "**不能放在同一张杠杆表里直接比**，请在报告中分开说明。")
    return 0


if __name__ == "__main__":
    try:
        from _feedback_hook import install
        install()
    except Exception:
        pass
    main()
