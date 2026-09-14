#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""六条已确认口径（caliber v2, 定稿 2026-09-12, 永久生效）

本模块是**唯一口径来源**。任何报告生成、过滤、评分都必须从这里取值，
不得在别处硬编码。口径变更时必须同时：
  1. 修改本文件并升级 CALIBER_VERSION；
  2. 全量重算所有历史结论（口径变更会使结论不可比）；
  3. 在报告首页显式写出当前口径版本。

口径 v2 与 v1 的三点差异（必须记录）：
  * 口径③ 净利润增长率：v1 用**年度**同比 → v2 用**半年**（最新中报年内同比）
  * 口径④ 单年亏损：v1 视为一票否决 → v2 降级为**减分项**（仅连续两年年报亏损才否决）
  * 口径⑥ 新增 **L2.5 基础可交易性校验**独立层（原先混在 L3 一票否决里）
"""

from __future__ import annotations

CALIBER_VERSION = "v2"
CALIBER_CONFIRMED_ON = "2026-09-12"

# ---------------------------------------------------------------- 口径①
# 国企央企背景 = **偏好项**，不是硬门槛。
# v1 曾把它当门槛，导致「民企 → 0 只」的假警报。
SOE_BACKGROUND_IS_GATE = False
SOE_BACKGROUND_IS_PREFERENCE = True
SOE_SCORE_BONUS = 6.0          # 命中控股股东/实控人为国企央企时的加分

# ---------------------------------------------------------------- 口径②
# 新兴科技成长优先：在同等技术形态下，新兴产业/科技成长股优先。
EMERGING_TECH_FIRST = True
EMERGING_TECH_BONUS = 8.0      # 命中六大新兴支柱 / 六大未来产业时的加分

# ---------------------------------------------------------------- 口径③
# 净利润增长率采用**半年口径**（最新中报年内同比），不是年度同比。
PROFIT_GROWTH_CALIBER = "half_year"      # "half_year" | "annual"
PROFIT_GROWTH_FIELD = "NPParentCompanyYOY_Q"   # 单季同比；中报累计同比用 NPParentCompanyYOY
PROFIT_GROWTH_FIELD_INTERIM = "NPParentCompanyYOY"

# 增速红线（量化）：
#   硬线：中报同比 <= 0  → 直接排除
#   减分项：中报同比 > 0 但 < 上一年度增速的 50% → 重大减分
GROWTH_HARD_LINE = 0.0
GROWTH_PENALTY_RELATIVE_LINE = 0.50      # 框架自定的默认值，非市场共识
GROWTH_PENALTY_SCORE = 15.0

# ---------------------------------------------------------------- 口径④
# 单年亏损 = 减分项；连续两年年报亏损 = 一票否决。
SINGLE_YEAR_LOSS_IS_VETO = False
TWO_CONSECUTIVE_LOSSES_IS_VETO = True
SINGLE_YEAR_LOSS_SCORE = 10.0

# ---------------------------------------------------------------- 口径⑤
# 「链」形态主题（如「算力网」「机器人产业链」）默认**跳过 L1 否决权**，
# 行业层只做定性描述，不因行业分位高而直接否决其中的个股。
CHAIN_THEME_SKIPS_L1_VETO = True

# 「链」形态主题名单（可扩展）
CHAIN_THEMES = (
    "算力网", "新一代通信网", "机器人链", "低空经济链",
    "半导体产业链", "新能源车产业链", "锂电池产业链", "光伏产业链",
)

# ---------------------------------------------------------------- 口径⑥
# 新增「基础可交易性校验」独立层 L2.5，位置在 L2 与 L3 之间。
TRADABILITY_LAYER = "L2.5"

# 可交易性否决条件（命中任一即剔除，且**不计入** L3 一票否决统计）
NOTRADE_RULES = (
    "已退市 / 退市整理期",
    "ST / *ST",
    "停牌",
    "净资产为负（PB < 0）",
    "上市未满 60 个交易日",
    "近 20 交易日均成交额 < 3000 万元（流动性不足）",
)

# ---------------------------------------------------------------- 层定义
LAYERS = ("L1行业", "L2个股", "L2.5可交易", "L3基本面")

# 分层技术阈值
RANK_LOW_THRESHOLD = 25.0     # 历史分位低于 25% 视为「超低位」
VR_THRESHOLD = 1.0            # 额比 >= 1.0 视为「放量」
DISPERSION_ALERT = 60.0       # 个股分位离散度 >= 60pp = 内部严重分化

# 口径变更使结论不可比 —— 报告必须报告的敏感度
SENSITIVITY_MUST_REPORT = True
SENSITIVITY_TOLERANCE_STOCKS = 1   # ±1 只以内算可接受，但仍须写明


def describe() -> str:
    """人类可读的口径摘要，供报告首页直接引用。"""
    return (
        f"口径版本 {CALIBER_VERSION}（{CALIBER_CONFIRMED_ON} 定稿，永久生效）\n"
        f"  ① 国企央企背景：{'硬门槛' if SOE_BACKGROUND_IS_GATE else '偏好项（非门槛）'}\n"
        f"  ② 产业偏好：{'新兴科技成长优先' if EMERGING_TECH_FIRST else '无偏好'}\n"
        f"  ③ 净利润增长率：{'半年口径（最新中报年内同比）' if PROFIT_GROWTH_CALIBER == 'half_year' else '年度口径'}\n"
        f"     硬线 中报同比 <= {GROWTH_HARD_LINE:.0%} → 排除；"
        f"减分 中报同比 > 0 但 < 上年度的 {GROWTH_PENALTY_RELATIVE_LINE:.0%}\n"
        f"  ④ 单年亏损：{'一票否决' if SINGLE_YEAR_LOSS_IS_VETO else '减分项'}；"
        f"连续两年年报亏损 = {'否决' if TWO_CONSECUTIVE_LOSSES_IS_VETO else '不否决'}\n"
        f"  ⑤ 「链」形态主题：{'跳过 L1 否决权（行业层仅定性）' if CHAIN_THEME_SKIPS_L1_VETO else '不跳过'}\n"
        f"  ⑥ 基础可交易性校验：作为独立层 {TRADABILITY_LAYER}（位于 L2 与 L3 之间）\n"
    )


def is_chain_theme(name: str) -> bool:
    """判断主题名是否属于「链」形态（口径⑤）。"""
    if not name:
        return False
    return any(k in name for k in CHAIN_THEMES)


if __name__ == "__main__":
    print(describe())
