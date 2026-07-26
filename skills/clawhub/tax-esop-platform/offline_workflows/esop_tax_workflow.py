#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
员工持股平台投资分回利润 · 税负测算对比闭环引擎（离线版，零依赖、纯标准库）
Version: v1.1.0 | Updated: 2026-07-23
Author: Joyxj2devs Team

设计要点
--------
- 本引擎为「有限公司型 vs 有限合伙企业型」两种持股平台组织形式的税负测算对比工具，
  对应服务端知识库 esop-platform-compliance.md §4.4 投资分回利润税负测算对比专项报告模板。
- 纯计算、无状态、不持久化任何企业私有数据；企业数据仅用于当次计算、不留存。
- 可在完全离线场景下由本技能直接调用，生成与专业知识库一致的「两组织形式税负对比」专业报告。
- 测算口径依据最新政策标准统一维护（企税法第26条 / 个税法 / 84号函 / 财税〔2000〕91号 /
  41号公告 / 财税〔2016〕36号 / 印花税法），详见 references/esop_rules.json（服务端）与下方常量。

使用方式（客户端）
----------------
- 在线时：由主技能调用云端知识库口径作答，本引擎作为结构化测算与成果报告输出底座。
- 离线时：直接调用 esop_report(metrics) 生成对比报告；或 `python esop_tax_workflow.py` 打印示例报告。

版本更新（v1.1.0）
---------------
- 新增交易结构层级表（§1.1）、员工取得利润方式对比表（§1.4）、各层级税种税率表（§2.1）、
  综合对比表（§2.4）、落地实施要点表（§4.3），报告结构与 docx 原报告完全对齐。
"""
from __future__ import annotations

VERSION = "1.1.0"

# ===== 公共政策税率常量（仅政策阈值，无企业数据） =====
RATE_CIT_GENERAL = 0.25          # 居民企业企业所得税一般税率
RATE_CIT_MICRO = 0.05            # 小型微利企业实际税负（延续至2027年底）
RATE_CIT_PREFER = 0.15           # 优惠地区企业所得税率
RATE_DIVIDEND_PIT = 0.20         # 利息、股息、红利所得个人所得税率（84号函穿透）
RATE_PARTNERSHIP_BUSINESS = 0.35 # 经营所得5%–35%超额累进上限（大额利得接近35%）
RATE_CIT_COMPANY_PLATFORM = 0.25 # 有限公司平台转让所得企业所得税率
STAMP_DUTY_RATE = 0.0005         # 股权转让书据印花税（非上市，产权转移书据0.05%）
VAT_EXEMPT_NOTE = "股息红利不征增值税；非上市股权转让非金融商品转让，不征增值税"


def _to_float(v, default=0.0):
    try:
        if v is None or v == "":
            return default
        return float(v)
    except (TypeError, ValueError):
        return default


# ===== 数据构建函数（静态，与 metrics 无关）=====

def build_structure_levels() -> list:
    """交易结构层级表（§1.1）：L0-L2 + 控制逻辑 + 税务属性。"""
    return [
        ["层级", "有限公司平台", "有限合伙平台"],
        ["L0 最终受益人", "员工（自然人股东）", "员工（有限合伙人LP，实控人可任执行事务合伙人GP）"],
        ["L1 持股平台", "有限责任公司（持股公司）", "有限合伙企业（GP+LP）"],
        ["L2 主体公司", "员工间接持股的运营公司", "同左"],
        ["控制逻辑", "同股同权，按出资比例表决", "GP执行事务、掌握控制权；LP出资享有收益"],
        ["税务属性", "独立法人，缴纳企业所得税", "穿透实体（先分后税），不缴企税"],
    ]


def build_earning_methods() -> list:
    """员工取得利润方式对比表（§1.4）：工资/奖金/分红/转让。"""
    return [
        ["取得方式", "支付方", "员工税种", "税率", "能否税前列支", "适用要点"],
        ["工资薪金", "主体公司", "个税（综合所得）", "3%–45%", "可扣除（减企税）",
         "需真实劳动关系；高收入者边际45%>20%，不如分红"],
        ["奖金", "主体公司", "个税（综合所得）", "3%–45%", "可扣除",
         "同工资；受合理性审核"],
        ["股息红利（平台→员工）", "持股平台", "个税（利息股息红利）", "20%", "不可扣除",
         "两种平台形式均为20%；高收入者更优"],
        ["股权转让所得（平台转让）", "持股平台", "经营所得(LLP)/企税+股息(有限公司)",
         "5%–35% 或 ≈40%", "—", "退出变现时产生，税负差异核心"],
    ]


def build_tax_rate_table() -> list:
    """各层级税种及适用税率表（§2.1）：7行×4列。"""
    return [
        ["层级/环节", "税种", "适用税率/处理", "依据"],
        ["主体公司·利润", "企业所得税", "一般25%；小微实际5%（2027年底前）；优惠地15%", "企税法+小微优惠"],
        ["主体公司→平台·股息", "企业所得税", "居民企业间免税（有限公司）；不征企税（合伙穿透）", "企税法第26条"],
        ["平台→员工·股息", "个人所得税", "20%（利息、股息、红利所得）", "个税法+84号函"],
        ["平台转让股权·利得（有限公司）", "企业所得税+个税", "企税25%+个人股息20% ≈ 综合40%", "企税法+个税法"],
        ["平台转让股权·利得（有限合伙）", "个人所得税（经营所得）", "5%–35%超额累进（查账征收）", "财税〔2000〕91号+41号公告"],
        ["股息/非上市股权转让", "增值税", "不征（股息非增值税范围；非上市股权非金融商品）", "财税〔2016〕36号"],
        ["股权转让书据", "印花税", "产权转移书据0.05%（非上市，双方）", "印花税法"],
        ["员工工资薪金", "个税+社保", "综合所得3%–45%+社保", "个税法"],
    ]


def build_comprehensive_compare() -> list:
    """综合对比表（§2.4）：7维度。"""
    return [
        ["维度", "有限公司平台", "有限合伙平台"],
        ["股息个税", "20%", "20%（84号函）"],
        ["转让所得税负", "≈40%（企税+股息）", "5%–35%（查账，大额≈35%）"],
        ["个税递延", "可留存递延", "先分后税，不可递延"],
        ["控制权安排", "同股同权", "GP掌权，LP分收益（钱权分离）"],
        ["设立/退出成本", "较高（法人）", "较低（合伙，工商变更简便）"],
        ["增值税", "不征（非上市股权）", "不征"],
        ["适合场景", "需递延、长期持有、资金沉淀", "股权激励、退出变现、控制集中"],
    ]


def build_implementation_steps() -> list:
    """落地实施要点表（§4.3）：5步动作+合规要点。"""
    return [
        ["步骤", "动作", "合规要点"],
        ["1 架构搭建", "设立平台并确权员工份额/股权",
         "签合伙协议/公司章程，明确收益分配与表决权"],
        ["2 主体入股", "平台受让或增资主体公司",
         "公允定价，留存交易凭证"],
        ["3 利润分配", "主体公司完税后代扣股息个税",
         "有限合伙严格按84号函20%申报"],
        ["4 退出安排", "转让按经营所得/企税合规缴税",
         "查账征收，禁核定；规范回购协议"],
        ["5 常态监控", "月度风险扫描+年度复核",
         "对照风险指标，留存同期资料"],
    ]


# ===== 核心测算 =====
def compute_dividend(P: float, r_c: float = RATE_CIT_GENERAL, r_d: float = RATE_DIVIDEND_PIT) -> dict:
    """股息分红环节：两种组织形式员工最终税负一致（均为企税 + 股息个税20%）。

    P   : 主体公司税前利润（单位：万元）
    r_c : 主体公司企业所得税率（默认 25%；小微 5%；优惠地 15%）
    r_d : 股息个税税率（默认 20%）
    """
    Tc = P * r_c
    Np = P - Tc
    Td = Np * r_d
    net = Np - Td
    rate = (Tc + Td) / P if P else 0.0
    return {
        "pretax_profit": round(P, 4),
        "corp_tax": round(Tc, 4),
        "after_tax_net_profit": round(Np, 4),
        "employee_pit": round(Td, 4),
        "employee_net": round(net, 4),
        "total_rate": round(rate, 4),
        "deferrable": False,
    }


def compute_transfer(G: float, r_e: float = RATE_CIT_COMPANY_PLATFORM,
                     r_b: float = RATE_PARTNERSHIP_BUSINESS,
                     r_d: float = RATE_DIVIDEND_PIT) -> dict:
    """股权转让（退出）环节：有限合伙经营所得35% < 有限公司企税+股息≈40%。

    G   : 平台转让主体公司股权利得（万元）
    r_e : 有限公司平台企业所得税率（默认 25%）
    r_b : 有限合伙经营所得税率（默认 35% 上限）
    r_d : 穿透个人股息税率（默认 20%）
    """
    Te1 = G * r_e
    Tp1 = (G - Te1) * r_d
    net_co = G - Te1 - Tp1
    rate_co = (Te1 + Tp1) / G if G else 0.0
    Tp2 = G * r_b
    net_lp = G - Tp2
    rate_lp = Tp2 / G if G else 0.0
    return {
        "gain": round(G, 4),
        "company_form": {
            "platform_tax": round(Te1, 4),
            "platform_tax_note": "企税25%",
            "pass_through_pit": round(Tp1, 4),
            "pass_through_pit_note": "再缴股息20%",
            "employee_net": round(net_co, 4),
            "total_rate": round(rate_co, 4),
        },
        "partnership_form": {
            "business_income_tax": round(Tp2, 4),
            "business_income_tax_note": "经营所得35%（查账）",
            "employee_net": round(net_lp, 4),
            "total_rate": round(rate_lp, 4),
        },
        "delta_rate": round(rate_co - rate_lp, 4),
        "partnership_saves": round((Te1 + Tp1) - Tp2, 4),
    }


# ===== 关键风险点（脱敏，不含内部来源）=====
ESOP_RISKS = [
    {"code": "ESOP-W1", "level": "高", "name": "留存也须缴税",
     "desc": "有限合伙\"先分后税\"，利润留平台未支付仍须当年缴个税，易漏报被追缴+滞纳金。"},
    {"code": "ESOP-W2", "level": "中", "name": "股息误用低税率",
     "desc": "不得将合伙股息红利错按\"经营所得5%–35%\"或已取消的核定征收申报，须严格按84号函20%。"},
    {"code": "ESOP-W3", "level": "高", "name": "名为合伙实为雇佣",
     "desc": "员工仅为雇员却通过平台\"分红\"，可能被重定为工资薪金（边际45%）+社保补缴；须确保真实持股身份。"},
    {"code": "ESOP-W4", "level": "高", "name": "核定征收违规",
     "desc": "2022年起权益性投资合伙企业一律查账征收，沿用旧核定政策存在重大补税风险。"},
    {"code": "ESOP-W5", "level": "中", "name": "代持与一致行动",
     "desc": "股权代持在税务上以名义股东为纳税人，争议时补税风险高；须确权并留存协议。"},
    {"code": "ESOP-W6", "level": "中", "name": "转让定价与实质",
     "desc": "平台与主体公司间服务、租赁等关联交易须公允并备同期资料；优惠地平台须满足实质性运营四要素。"},
    {"code": "ESOP-W7", "level": "中", "name": "离职回购税务",
     "desc": "员工退伙/转让份额按财产转让所得20%处理，须规范协议与付款路径，避免私户收款红线。"},
]

POLICY_REFS = [
    "《中华人民共和国企业所得税法》第26条——居民企业之间股息红利免税。",
    "《中华人民共和国个人所得税法》——利息股息红利所得20%；综合所得3%–45%；经营所得5%–35%。",
    "国税函〔2001〕84号——合伙企业对外投资分回股息红利，单独按\"利息、股息、红利所得\"20%由合伙人缴纳。",
    "财政部 税务总局公告2021年第41号——持有股权等权益性投资的合伙企业一律查账征收（2022-01-01起）。",
    "财税〔2016〕36号——股息红利不征增值税；非上市股权转让非金融商品转让，不征增值税。",
    "《中华人民共和国印花税法》——股权转让书据（非上市）按产权转移书据0.05%（双方）。",
    "小微企业所得税优惠（实际税负5%，延续至2027年底）——业务分拆须具真实商业实质。",
]


def esop_report(metrics: dict | None = None) -> dict:
    """生成「有限公司型 vs 有限合伙企业型」税负测算对比报告。

    metrics 字段（单位：万元）：
      P        : 主体公司税前利润（默认 1000）
      r_c      : 主体公司企税率（默认 0.25；可传 0.05/0.15）
      G        : 平台转让主体公司股权利得（默认 500；无退出传 0）
      r_e      : 有限公司平台企税率（默认 0.25）
      r_b      : 有限合伙经营所得税率（默认 0.35）
      r_d      : 股息个税（默认 0.20）
      company  : 企业名称（可选，用于报告抬头）
    返回结构化报告 dict（含 report_markdown 完整文本）。
    """
    m = metrics or {}
    P = _to_float(m.get("P"), 1000.0)
    r_c = _to_float(m.get("r_c"), RATE_CIT_GENERAL)
    G = _to_float(m.get("G"), 500.0)
    r_e = _to_float(m.get("r_e"), RATE_CIT_COMPANY_PLATFORM)
    r_b = _to_float(m.get("r_b"), RATE_PARTNERSHIP_BUSINESS)
    r_d = _to_float(m.get("r_d"), RATE_DIVIDEND_PIT)
    company = (m.get("company") or "").strip()

    div = compute_dividend(P, r_c, r_d)
    div_co = dict(div); div_co["deferrable"] = True
    div_lp = dict(div); div_lp["deferrable"] = False

    tr = compute_transfer(G, r_e, r_b, r_d) if G > 0 else None

    # 选型推荐
    if tr:
        primary = "有限合伙型企业" if tr["delta_rate"] >= 0 else "有限公司型企业"
        primary_reason = (
            f"股权转让环节有限合伙综合税负率 {tr['partnership_form']['total_rate']*100:.0f}% "
            f"低于有限公司 {tr['company_form']['total_rate']*100:.0f}%，个人到手多 "
            f"{tr['partnership_saves']:.0f} 万；且GP控制、设立退出简便。"
            if tr["delta_rate"] >= 0 else
            "当前参数下有限公司综合税负更优。"
        )
    else:
        primary = "有限公司型企业"
        primary_reason = "本次未设退出利得；若核心诉求为利润长期沉淀再投资、递延个人税负，建议有限公司。"

    recommendation = {
        "primary": primary,
        "primary_reason": primary_reason,
        "dual_platform": "实务可采用\"有限公司（长期/递延）+ 有限合伙（激励/退出）\"双平台架构，兼顾递延与低税负。",
        "advice": [
            "退出税负敏感型（看重变现落袋、控制集中）→ 选有限合伙：转让利得35% < 有限公司40%。",
            "递延需求型（利润沉淀再投资、不急于分配）→ 选有限公司：可留存不分配，个人股息个税递延。",
            "双平台组合：以有限公司持有长期资产/递延分红，以有限合伙承载员工激励与未来退出。",
            "工资与分红搭配：低收入员工多发工资（可扣企税、边际低）；高收入核心员工以分红为主（20%<45%）。",
            "合规底座：查账征收、留存同期资料、关联交易公允、优惠地满足实质性运营，杜绝核定违规与私户收款。",
        ],
    }

    data = {
        "topic": "esop",
        "engine_version": VERSION,
        "company": company,
        "input": {"P": P, "r_c": r_c, "G": G, "r_e": r_e, "r_b": r_b, "r_d": r_d},
        "structure_levels": build_structure_levels(),
        "earning_methods": build_earning_methods(),
        "tax_rate_table": build_tax_rate_table(),
        "dividend": {"company_form": div_co, "partnership_form": div_lp, "same": True,
                     "note": "股息分红环节两种形式员工最终税负一致（均企税+股息个税20%）。"},
        "transfer": tr,
        "comprehensive_compare": build_comprehensive_compare(),
        "recommendation": recommendation,
        "implementation_steps": build_implementation_steps(),
        "risks": ESOP_RISKS,
        "policy_refs": POLICY_REFS,
    }
    data["report_markdown"] = generate_report_markdown(data)
    return data


def _render_table(rows: list, bold_header: bool = True) -> str:
    """将二维行列表渲染为 Markdown 表格。"""
    if not rows:
        return ""
    out = []
    for ri, row in enumerate(rows):
        cells = [c for c in row]
        out.append("| " + " | ".join(cells) + " |")
        if ri == 0:
            out.append("| " + " | ".join("---" for _ in cells) + " |")
    return "\n".join(out)


def generate_report_markdown(d: dict) -> str:
    """依据计算结果生成与知识库 §4.4 一致的专业化完整报告（四章 + 附录）。"""
    co = d["dividend"]["company_form"]
    lp = d["dividend"]["partnership_form"]
    tr = d["transfer"]
    r = d["recommendation"]
    P = d["input"]["P"]
    G = d["input"]["G"]
    r_c = d["input"]["r_c"]
    Np = P - P * r_c
    Td = Np * 0.20
    net = Np - Td

    title = "# 员工持股平台投资分回利润税务分析对比专项报告\n"
    sub = ("> 适用场景：员工通过持股平台间接持有主体公司股权，在「主体公司税后利润分配至平台、"
           "平台再向员工分配（股息环节）」以及「平台转让主体公司股权退出（资本利得环节）」两类情形下，"
           "对比**有限公司型**与**有限合伙企业型**两种组织形式的税负差异，支撑平台选型、架构设计与退出筹划决策。\n")
    if d.get("company"):
        sub += f"> 测算主体：{d['company']}\n"

    # ============ 第一章 ============
    ch1 = "## 第一章 员工持股平台利润分配方案设计\n\n"

    ch1 += "### 1.1 两种组织形式与基本交易结构\n\n"
    ch1 += (
        "持股平台是员工间接持有主体公司股权的载体。员工不直接持有主体公司股权，"
        "而是通过持有\"平台\"的份额/股权，间接享有主体公司利润分配与资本增值。"
        "平台法律形式通常二选一：**有限责任公司（有限公司平台）**或**有限合伙企业（有限合伙平台）**。\n\n"
    )
    ch1 += _render_table(d["structure_levels"]) + "\n\n"

    ch1 += "### 1.2 形式一：有限公司持股平台 利润分配方案\n\n"
    ch1 += "路径：主体公司（缴企税后）→ 向有限公司平台分配股息（居民企业间免税）→ 有限公司平台向员工（自然人股东）分配股息（缴20%个税）。\n\n"
    ch1 += "步骤1 · 主体公司就税前利润缴纳企业所得税（一般25%，符合条件可享小微5%或优惠地15%）。\n"
    ch1 += "步骤2 · 税后净利润向有限公司平台分配股息。依《企业所得税法》第26条，居民企业之间的股息红利免税，平台收到时不缴企税。\n"
    ch1 += "步骤3 · 有限公司平台可\"留存不分配\"，将利润沉淀于平台用于再投资；仅在向员工实际分配时，员工缴20%股息红利个税（可递延）。\n"
    ch1 += "步骤4 · 员工以自然人股东身份取得股息，按\"利息、股息、红利所得\"缴20%个税；该分红不可在主体公司税前列支，亦不计入社保缴费基数。\n\n"
    ch1 += "**员工取得利润的具体方式**：本形式下员工只能以\"股东分红\"方式取得（20%个税）；平台本身不得向员工支付工资薪金的常规雇佣关系（除非员工确在平台任职）。\n\n"

    ch1 += "### 1.3 形式二：有限合伙企业持股平台 利润分配方案\n\n"
    ch1 += "路径：主体公司（缴企税后）→ 向有限合伙平台分配股息 → 穿透至员工合伙人，按\"利息、股息、红利所得\"缴20%个税（国税函〔2001〕84号）。\n\n"
    ch1 += "步骤1 · 主体公司缴纳企业所得税后，向有限合伙平台分配股息。\n"
    ch1 += "步骤2 · 有限合伙为穿透实体，本身不缴企税、不缴个税。其取得的股息红利，依84号函不并入经营所得，单独按\"利息、股息、红利所得\"20%由合伙人分别缴纳。\n"
    ch1 += "步骤3 · \"先分后税\"：即使利润留存在合伙企业未实际支付给员工，也须按员工应享份额于当年缴个税，无法像有限公司那样递延。\n"
    ch1 += "步骤4 · 员工（LP）取得收益按20%股息个税；实控人担任GP执行事务，掌握表决权，实现\"钱权分离\"（LP出钱分收益、GP掌控制权）。\n\n"
    ch1 += "**员工取得利润的具体方式**：分红（20%个税，84号函口径）；若未来平台转让主体公司股权，则按\"经营所得\"5%–35%缴税（详见第二章）。\n\n"

    ch1 += "### 1.4 员工取得利润的方式对比（工资 / 奖金 / 分红）\n\n"
    ch1 += "合规计划提示：对低收入员工以工资（可扣企税、边际税率低）为主；对高收入核心员工以分红（20%<45%）为主；工资与分红搭配可平衡现金流、社保基数与综合税负。\n\n"
    ch1 += _render_table(d["earning_methods"]) + "\n"

    # ============ 第二章 ============
    ch2 = "## 第二章 各层级税务分析与税负差异\n\n"

    ch2 += "### 2.1 各层级涉及的税种及适用税率\n\n"
    ch2 += _render_table(d["tax_rate_table"]) + "\n\n"

    ch2 += "### 2.2 股息分红环节：两种形式税负一致\n\n"
    ch2 += f"关键结论：在\"投资分回的利润\"（股息红利）环节，有限公司平台与有限合伙平台的员工最终税负**完全相同**——均为公司25%企税 + 个人20%股息个税，综合约40%。原因在于有限合伙取得的股息按84号函单独以20%股息个税穿透，无法借\"经营所得5%–35%\"降低股息税负。\n\n"
    ch2 += _render_table([
        ["对比项", "有限公司平台", "有限合伙平台"],
        [f"主体公司企税（{int(r_c*100)}%）", f"{co['corp_tax']:.0f}万", f"{lp['corp_tax']:.0f}万"],
        ["平台收股息企税", "免税（居民企业间）", "不征（穿透实体）"],
        ["员工股息个税（20%）", f"{co['employee_pit']:.0f}万", f"{lp['employee_pit']:.0f}万"],
        ["员工到手", f"{co['employee_net']:.0f}万", f"{lp['employee_net']:.0f}万"],
        ["综合税负率（对税前利润）", f"{co['total_rate']*100:.0f}%", f"{lp['total_rate']*100:.0f}%"],
        ["个税能否递延", "可（平台留存不分配）", "不可（先分后税）"],
    ]) + "\n\n"

    ch2 += "### 2.3 股权转让（退出）环节：有限合伙更优\n\n"
    ch2 += (
        "真正的税负差异出现在平台转让主体公司股权（资本利得）时。"
        + (f"假设转让利得{G:.0f}万元、主体公司已完税：\n\n" if G > 0 else "本次未设退出利得。\n\n")
    )
    if tr:
        ch2 += _render_table([
            ["对比项", "有限公司平台", "有限合伙平台"],
            ["平台层税负", f"企税25% = {tr['company_form']['platform_tax']:.0f}万", f"经营所得35%（查账）= {tr['partnership_form']['business_income_tax']:.0f}万"],
            ["分配/穿透后个人税负", f"再缴股息20% = {tr['company_form']['pass_through_pit']:.0f}万", "（已含在经营所得中）"],
            ["个人最终到手", f"{tr['company_form']['employee_net']:.0f}万", f"{tr['partnership_form']['employee_net']:.0f}万"],
            [f"综合税负率（对{tr['gain']:.0f}万利得）", f"{tr['company_form']['total_rate']*100:.0f}%", f"{tr['partnership_form']['total_rate']*100:.0f}%"],
            ["结论", "双重征税，税率确定", f"税负更低（大额利得省约{tr['delta_rate']*100:.0f}个百分点）"],
        ]) + "\n\n"
        ch2 += "> 注：有限合伙\"经营所得\"适用5%–35%超额累进，利得越大越接近35%上限；2021年41号公告已取消权益性投资合伙企业的核定征收，须查账征收，不得以\"核定低税率\"避税。\n\n"
    else:
        ch2 += "> 本次未设转让利得，跳过股权转让环节测算。\n\n"

    ch2 += "### 2.4 综合对比\n\n"
    ch2 += _render_table(d["comprehensive_compare"]) + "\n\n"

    ch2 += "### 2.5 关键税务风险点及合规注意事项\n\n"
    ch2 += "\n".join(f"⚠ **风险{i+1} · {x['name']}**：{x['desc']}" for i, x in enumerate(d["risks"])) + "\n"

    # ============ 第三章 ============
    ch3 = "## 第三章 具体数值测算示例\n\n"
    ch3 += "### 3.1 示例假设\n\n"
    micro_note = "（超过小微300万上限，适用25%企税）" if P >= 300 else "（可能符合小微实际5%税率）"
    ch3 += (
        f"主体公司年应纳税所得额 {P:.0f} 万元{micro_note}；"
        f"税后净利 {Np:.0f} 万元全部分配为股息；"
        + (f"另设平台转让主体公司股权产生利得 {G:.0f} 万元。员工为平台100%权益享有者。\n" if G > 0 else "本次未设退出利得。\n")
    )

    ch3 += "### 3.2 测算一：股息分红（税前利润1,000万）\n\n"
    ch3 += _render_table([
        ["环节", "有限公司平台", "有限合伙平台", "说明"],
        ["① 主体公司企税", f"{co['corp_tax']:.0f}万", f"{lp['corp_tax']:.0f}万", f"{P:.0f}×{int(r_c*100)}%"],
        ["② 平台收股息", "免税", "不征（穿透）", "居民企业间免税 / 合伙不征企税"],
        ["③ 员工个税", f"{co['employee_pit']:.0f}万", f"{lp['employee_pit']:.0f}万", f"{Np:.0f}×20%"],
        ["员工到手", f"{co['employee_net']:.0f}万", f"{lp['employee_net']:.0f}万", "税后净利−个税"],
        ["综合税负率", f"{co['total_rate']*100:.0f}%", f"{lp['total_rate']*100:.0f}%", f"({co['corp_tax']:.0f}+{co['employee_pit']:.0f})/{P:.0f}"],
    ]) + "\n\n"

    ch3 += "### 3.3 测算二：股权转让（利得500万）\n\n"
    if tr:
        ch3 += _render_table([
            ["环节", "有限公司平台", "有限合伙平台", "说明"],
            ["平台层税", f"{tr['company_form']['platform_tax']:.0f}万（企税25%）", f"{tr['partnership_form']['business_income_tax']:.0f}万（经营所得35%）", f"{tr['gain']:.0f}×25% / {tr['gain']:.0f}×35%"],
            ["穿透/分配税", f"{tr['company_form']['pass_through_pit']:.0f}万（股息20%）", "—", f"({tr['gain']:.0f}−{tr['company_form']['platform_tax']:.0f})×20%"],
            ["个人到手", f"{tr['company_form']['employee_net']:.0f}万", f"{tr['partnership_form']['employee_net']:.0f}万", "利得−税负"],
            ["综合税负率", f"{tr['company_form']['total_rate']*100:.0f}%", f"{tr['partnership_form']['total_rate']*100:.0f}%", f"200/500 / 175/500"],
        ]) + "\n\n"
    else:
        ch3 += "> 本次未设转让利得，跳过。\n\n"

    ch3 += "### 3.4 员工实际税负率汇总\n\n"
    rows34 = [
        ["场景", "有限公司平台", "有限合伙平台", "差异"],
        ["股息分红（对税前利润）", f"{co['total_rate']*100:.0f}%", f"{lp['total_rate']*100:.0f}%", "无差异"],
    ]
    if tr:
        rows34.append(["股权转让（对利得）", f"{tr['company_form']['total_rate']*100:.0f}%", f"{tr['partnership_form']['total_rate']*100:.0f}%", f"有限合伙省{tr['delta_rate']*100:.0f}个百分点"])
    rows34.append(["个税递延能力", "可递延", "不可递延", "有限公司占优"])
    ch3 += _render_table(rows34) + "\n"

    # ============ 第四章 ============
    ch4 = "## 第四章 专业税务合规计划建议与最优选择推荐\n\n"
    ch4 += "### 4.1 合规计划建议\n\n"
    ch4 += "\n".join(f"建议{i+1} · {a}" for i, a in enumerate(r["advice"])) + "\n\n"

    ch4 += "### 4.2 最优选择推荐\n\n"
    ch4 += (
        f"综合结论：对绝大多数以\"激励+退出\"为目标的员工持股平台，推荐优先采用「**{r['primary']}**」形式"
        f"——{r['primary_reason']}\n\n"
        f"但须明确权衡：{r['dual_platform']}\n"
    )

    ch4 += "### 4.3 落地实施要点\n\n"
    ch4 += _render_table(d["implementation_steps"]) + "\n"

    # ============ 附录 ============
    appx = "## 附录 政策依据清单\n\n"
    appx += "\n".join(f"- {p}" for p in d["policy_refs"]) + "\n"

    banner = "\n---\n\n> 📚 本报告由 **tax-policy-knowledge 财税知识库与技能矩阵** 生成\n"
    banner += "> 🔗 [点击查看并复制链接](https://skillhub.cn/skills/tax-policy-knowledge) · 觉得好用请点 ★ 收藏\n"
    banner += "> 有需求建议可加企鹅号 **1817694478** 或在评论区留言 · 有你的关注与支持是我们功能升级持续更新的最大动力！\n"

    return title + sub + "\n" + ch1 + ch2 + ch3 + ch4 + appx + banner


def _print_sample():
    print("=" * 64)
    print("员工持股平台投资分回利润 · 税负测算对比闭环引擎 v%s" % VERSION)
    print("=" * 64)
    sample = {"P": 1000, "r_c": 0.25, "G": 500, "company": "示例主体公司"}
    data = esop_report(sample)
    print(data["report_markdown"])
    print("\n[INFO] 结构化结果摘要：")
    print("  股息环节综合税负率：%.0f%%（两种形式一致）" % (data["dividend"]["company_form"]["total_rate"] * 100))
    if data["transfer"]:
        print("  股权转让环节：有限公司 %.0f%% vs 有限合伙 %.0f%%（省 %.0f 个百分点）" % (
            data["transfer"]["company_form"]["total_rate"] * 100,
            data["transfer"]["partnership_form"]["total_rate"] * 100,
            data["transfer"]["delta_rate"] * 100,
        ))
    print("  最优选择：%s" % data["recommendation"]["primary"])


if __name__ == "__main__":
    _print_sample()
