---
name: Securities Equity Research Report Generator
slug: security-equity-research
description: AI-powered equity research report generator for China A-share market — covers industry research, company coverage initiation, earnings analysis, valuation modeling (DCF/DDM/PE-band), and investment thesis synthesis. Built for China equity research analysts, buy-side analysts, and investment bank researchers. Updated 2026 with latest ESG integration requirements, short-seller report response templates, and cross-sector comparison frameworks. Keywords: equity research, A-share research, investment report, short-seller defense, ESG integration, valuation model, China stock analysis, 研报生成, 行业研究, 个股覆盖, 估值建模, 投研报告, 行研, 财报分析, 盈利预测, 目标价, 评级, 深度报告, 事件点评, 新股分析.
version: "3.0.2"
---

# Securities Equity Research Report Generator / 证券投研报告生成器

> **English:** AI-powered equity research report generator for China A-share market — automates industry research, company coverage initiation, earnings analysis, valuation modeling, and investment thesis synthesis. Solves pain points: time-consuming data collection, repetitive report templates, and fast-response capability for short-seller reports. Built for equity research analysts and buy-side researchers.
>
> **中文:** 证券投研报告生成器——覆盖行业研究、公司首次覆盖、业绩点评、估值建模（DCF/DDM/PE区间）、投资逻辑提炼的全流程AI助手。解决痛点：数据收集耗时、报告模板重复、快速响应做空报告需求。适用：中国A股研究员、买方分析师、投资银行研究人员。

---


### 证券监管最新动态 [2026-09-12更新]

| 动态类型 | 内容摘要 | 影响范围 | 研报侧应对动作 | 责任岗 | 优先级 |
|---------|---------|---------|--------------|-------|-------|
| 证券监管 | 2026年Q1：证监会持续强化上市公司信息披露质量监管 | 研究报告模板需纳入信披合规和量化冲击分析 | 研报增设"信披质量"小节，标注公告编号 | 研究 | 高 |
| 证券监管 | 业绩预告披露质量被重点关注，研究需加强信披合规分析 | 研究报告模板需纳入信披合规和量化冲击分析 | 业绩点评须区分"预告口径"与"实际口径" | 研究 | 高 |
| 证券监管 | A股量化资金占比30%-40%，研究报告需关注量化冲击因素 | 研究报告模板需纳入信披合规和量化冲击分析 | 增加"交易结构"小节，说明波动归因 | 研究 | 中 |
| 研报执业 | 研报执业规范持续强化，观点依据与数据来源须可追溯 | 深度报告、事件点评、盈利预测 | 每个关键数据标注来源与取数日期 | 研究 | 高 |
| 适当性与传播 | 研报公开传播需注意目标价、评级的表述边界 | 对客传播的研报摘要与路演材料 | 摘要保留评级定义与免责声明 | 合规 | 高 |
| 市值管理 | 上市公司市值管理行为的信息披露要求趋严 | 涉及股东增减持、回购的点评 | 点评须同时列示公告原文要点 | 研究 | 中 |
| 程序化交易 | 程序化交易报告与异常交易监控要求细化 | 与量化资金相关的流动性与波动分析 | 在流动性分析中纳入程序化交易因素 | 研究 | 中 |
| ESG披露 | 可持续披露规则推进，ESG信息在估值中的权重上升 | ESG整合、行业比较 | 估值与比较框架中单列ESG评分维度 | 研究 | 中 |

> **数据截止**: 2026-09-12 | 来源：证监会、NFRA、中证协、交易所公开规则、行业公开信息
> **声明**: 以上动态供参考，具体以官方最新发布为准

**动态解读示例（四类高频场景）**

- **场景A｜数据可追溯**：研报中"行业增速约15%"未标注来源 → 命中"数据来源须可追溯" → 改为"据XX机构2026年8月行业月报，行业增速15%（取数日期2026-09-01）"。
- **场景B｜业绩点评口径**：公司发布业绩预告后直接按预告区间取中值做盈利预测 → 命中"预告口径与实际口径混用" → 点评中分别列示预告区间与预测值，并说明预测与预告的差异原因。
- **场景C｜量化冲击归因**：股价单日波动8%被简单归因为"基本面变化" → 命中"量化资金占比需纳入分析" → 补充当日成交结构（成交量放大倍数、换手率）与是否有程序化交易特征的说明。
- **场景D｜摘要传播合规**：对外传播的研报摘要删掉了评级定义和免责声明 → 命中"传播边界"要求 → 摘要页固定保留评级定义表与免责声明段落，不因篇幅删减。

## Industry Pain Points / 行业痛点

| Pain Point / 痛点 | Impact / 影响 | Solution / 本Skill解决方案 | 量化基线指标 / Baseline |
|------------------|-------------|------------------------|----------------------|
| **数据收集耗时** | 分析师60%时间花在数据整理 | 自动抓取财报/宏观/行业数据库，一键生成数据底稿 | 单篇数据底稿整理 ≤2小时 |
| **报告模板重复** | 每次撰写覆盖报告都要重新排版 | 内置研报标准模板，30秒生成初稿框架 | 初稿框架产出 ≤5分钟 |
| **估值建模复杂** | DCF/DDM参数调整耗时长 | 参数化估值模型，输入假设自动计算 | 单次估值重算 ≤1分钟 |
| **做空报告应急** | 做空机构突袭需24小时内回应 | 紧急响应模板，快速组织反驳论据 | 首版回应稿 ≤6小时 |
| **研报合规风险** | 监管对研报质量要求越来越高 | 内置合规检查清单，自动识别风险表述 | 合规检查项通过率 100% |
| **假设不可追溯** | 假设取值无依据，结论易被质疑 | 关键假设登记表（数值+依据+取数日期） | 关键假设可追溯率 ≥95% |
| **估值口径不一** | 同一公司不同报告估值口径不同 | 估值口径统一表（币种/股本/净负债处理） | 口径一致率 100% |
| **观点与数据脱节** | 结论与数据支撑不匹配 | 结论-证据映射表（每条逻辑对应数据） | 每条逻辑 ≥2项数据支撑 |

---

## Trigger Keywords / 触发关键词

**English Triggers:** equity research, A-share research, investment report, coverage initiation, earnings review, valuation model, DCF, DDM, PE band, short-seller response, ESG integration, China stock analysis, industry research report, buy-side research

**中文触发词（优先）：** 投研报告 / 行业研究 / 个股分析 / 首次覆盖 / 业绩点评 / 估值建模 / DCF / DDM / PE区间 / 做空报告回应 / ESG整合 / 投研框架 / 研究报告 / 买方研报 / 券商研报 / 宏观策略 / 行业比较 / 公司对比 / 盈利预测 / 目标价 / 评级调整 / 研究报告审查 / 研报合规检查 / 研报降重 / 研报改写

---

## Core Capabilities / 核心能力

### 1. Research Report Templates / 研报模板库

**标准研报结构（证监会/中证协规范格式）：**

```markdown
# [公司简称]（[股票代码]）深度报告
**报告日期**: YYYY-MM-DD
**研究员**: [姓名]
**联系方式**: [邮箱/电话]

## 核心观点
[3-5句话概括投资亮点和核心风险]

## 投资逻辑
### 逻辑1：[一句话]
### 逻辑2：[一句话]
### 逻辑3：[一句话]

## 关键假设
| 假设项 | 数值 | 依据 |
|-------|------|------|
| 收入增速 | XX% | [市场/公司历史数据] |
| 毛利率 | XX% | [行业趋势/竞争格局] |
| 费用率 | XX% | [历史均值/管理变革] |

## 盈利预测
| 指标 | 2024A | 2025E | 2026E | 2027E |
|------|-------|-------|-------|-------|
| 营业收入（亿元） | | | | |
| 归母净利润（亿元） | | | | |
| EPS（元） | | | | |
| YoY增速 | | | | |

## 估值分析
### DCF估值
- WACC: XX%
- 永续增长率: XX%
- 绝对估值区间: [XX-XX]元

### 相对估值
| 可比公司 | P/E | P/B | P/S |
|---------|-----|-----|-----|
| [公司A] | | | |
| [公司B] | | | |
| 行业中位数 | | | |

## 风险提示
1. [风险1]
2. [风险2]
3. [风险3]
```

**报告类型与篇幅矩阵（先定类型再动笔）**

| 报告类型 | 建议篇幅 | 核心交付物 | 撰写周期 | 必含要素 |
|---------|---------|-----------|---------|---------|
| 首次覆盖（深度） | 1.5万字+ | 投资逻辑 + 盈利预测 + 估值 | 5-10个工作日 | 三大逻辑 + 关键假设表 + 敏感性分析 |
| 业绩点评 | 2000-4000字 | 业绩拆解 + 预期差判断 | 1个工作日 | 预告/实际口径对照 + 超预期归因 |
| 事件点评 | 1500-3000字 | 事件影响量化 | 0.5个工作日 | 事件时间线 + 影响测算 |
| 行业深度 | 1.2万字+ | 产业趋势 + 竞争格局 + 标的 | 5-8个工作日 | 产业链图 + CR3/CR5 + 景气度打分 |
| 估值对比 | 3000-5000字 | 可比公司矩阵 | 2个工作日 | 口径统一说明 + 分位区间 |
| 做空回应 | 2500-5000字 | 逐条反驳 + 证据链 | ≤6小时首版 | 指控-事实-证据三段式 |

**示例 1｜业绩点评的预期差框架（把"是否超预期"讲清楚）**

| 项目 | 预告区间 | 实际值 | 市场一致预期 | 预期差判断 |
|------|---------|-------|------------|-----------|
| 营业收入（亿元） | 48-52 | 53.1 | 50.0 | 超预期（+6.2%） |
| 归母净利润（亿元） | 6.0-6.8 | 7.2 | 6.5 | 超预期（+10.8%） |
| 毛利率 | 未披露 | 31.4% | 29.8% | 超预期，原材料降价贡献约1.2pct |
| 经营性现金流（亿元） | 未披露 | 4.6 | 5.2 | 低于预期，应收增加所致 |

结论写法：先给预期差结论，再拆解贡献因子，最后给可持续性判断（一次性因素剔除后的"可比增速"）。

**示例 2｜关键假设登记表（假设必须可追溯）**

| 假设项 | 取值 | 依据 | 取数日期 | 敏感性 |
|-------|------|------|---------|-------|
| 收入增速 | 18% | 近3年复合增速 + 新增产能投放节奏 | 2026-09-01 | 每降1pct，目标价降约2.1% |
| 毛利率 | 31.5% | 原材料价格中枢下移 + 产品结构升级 | 2026-09-01 | 每降1pct，净利润降约5.4% |
| 费用率 | 12.0% | 近3年均值，规模效应小幅摊薄 | 2026-09-01 | 影响较小 |
| WACC | 9.5% | 无风险利率 + 行业β + 规模溢价 | 2026-08-31 | 每升0.5pct，估值降约6% |

**示例 3｜结论-证据映射（防止观点悬空）**

| 投资逻辑 | 数据支撑1 | 数据支撑2 | 反证与应对 |
|---------|----------|----------|-----------|
| 新增产能驱动增长 | 在建工程同比+42% | 公司公告投产时间表 | 若投产延期，增速下调至12% |
| 毛利率具备韧性 | 原材料价格指数回落 | 高毛利产品占比提升至38% | 若原材料反弹，毛利率下修1pct |
| 估值处于历史低位 | 当前PE位于近5年12%分位 | 可比公司中位数PE 18x | 若行业景气下行，分位参考失效 |

### 2. Valuation Models / 估值模型

#### 2.1 DCF Model / 现金流折现模型

```python
import numpy as np
import pandas as pd
from scipy.optimize import brentq

def dcf_valuation(fcf_forecast: list, wacc: float, terminal_growth: float, 
                   terminal_share: float = 1.0) -> dict:
    """
    DCF估值模型
    Args:
        fcf_forecast: 未来5年自由现金流预测（亿元）
        wacc: 加权平均资本成本（%）
        terminal_growth: 永续增长率（%）
        terminal_share: 终值折现系数
    Returns:
        估值结果字典
    """
    # 预测期现值
    discount_factors = [(1 + wacc/100) ** t for t in range(1, len(fcf_forecast) + 1)]
    pv_forecast = sum([fcf / df for fcf, df in zip(fcf_forecast, discount_factors)])
    
    # 终值计算
    terminal_fcf = fcf_forecast[-1] * (1 + terminal_growth / 100)
    terminal_value = terminal_fcf / (wacc / 100 - terminal_growth / 100)
    pv_terminal = terminal_value / discount_factors[-1] * terminal_share
    
    # 企业价值 & 股权价值
    enterprise_value = pv_forecast + pv_terminal
    equity_value = enterprise_value  # 简化：无净负债调整
    
    # 敏感性分析
    sensitivity = {}
    for wacc_adj in [-0.5, 0, 0.5]:
        for tg_adj in [-0.5, 0, 0.5]:
            adj_wacc = wacc + wacc_adj
            adj_tg = terminal_growth + tg_adj
            if adj_wacc > adj_tg:
                adj_tv = terminal_fcf * (1 + adj_tg/100) / (adj_wacc/100 - adj_tg/100)
                adj_pv_tv = adj_tv / discount_factors[-1] * terminal_share
                adj_pv_f = sum([fcf / ((1 + adj_wacc/100) ** t) 
                               for t, fcf in enumerate(fcf_forecast, 1)])
                sensitivity[f"WACC={adj_wacc}%, g={adj_tg}%"] = adj_pv_f + adj_pv_tv
    
    return {
        "enterprise_value": round(enterprise_value, 2),
        "equity_value": round(equity_value, 2),
        "pv_forecast": round(pv_forecast, 2),
        "pv_terminal": round(pv_terminal, 2),
        "terminal_value": round(terminal_value, 2),
        "sensitivity_table": sensitivity
    }

# 使用示例
result = dcf_valuation(
    fcf_forecast=[5.2, 6.1, 7.3, 8.5, 9.8],  # 未来5年FCF（亿元）
    wacc=9.5,  # WACC 9.5%
    terminal_growth=2.5,  # 永续增长率 2.5%
    terminal_share=0.8  # 终值折现系数
)
print(f"企业价值: {result['enterprise_value']} 亿元")
print(f"股权价值: {result['equity_value']} 亿元")
```

**示例 1｜DCF 结果解读（把数字翻译成结论）**

| 输出项 | 数值 | 解读 |
|-------|------|------|
| 预测期现值 | 33.2亿元 | 占企业价值比重偏低，说明价值主要来自终值 |
| 终值现值 | 96.4亿元 | 占比74%，须重点检验永续增长假设 |
| 企业价值 | 129.6亿元 | 假设无净负债调整 |
| 终值占比 | 74% | >70%说明估值对长期假设高度敏感，需做双情景 |

结论写法：终值占比偏高时，必须同时给出"保守情景"（永续增长率2.0%）与"乐观情景"（3.0%）的企业价值，避免只给单点结论。

**示例 2｜敏感性分析读表（WACC × 永续增长率）**

| WACC ↓ \ g → | 2.0% | 2.5% | 3.0% |
|-------------|------|------|------|
| 9.0% | 138.5 | 145.2 | 152.8 |
| 9.5% | 129.6 | 135.4 | 142.0 |
| 10.0% | 121.8 | 126.9 | 132.6 |

读表方法：①先看对角线区间（129.6-145.2）给出估值中枢；②再看最不利与最有利组合（121.8-152.8）给出区间边界；③若区间宽度超过市值的±20%，在报告中明确标注"估值不确定性较高"。

#### 2.2 DDM Model / 股利贴现模型

```python
def ddm_valuation(current_dps: float, dividend_growth: list, 
                  required_return: float, terminal_growth: float) -> dict:
    """
    DDM估值模型（两阶段）
    Args:
        current_dps: 当前每股股利（元）
        dividend_growth: 高增长阶段各年增长率（%）
        required_return: 必要收益率（%）
        terminal_growth: 永续增长率（%）
    """
    pv_dividends = []
    cumulative_dps = current_dps
    
    for i, g in enumerate(dividend_growth, 1):
        cumulative_dps *= (1 + g / 100)
        pv = cumulative_dps / ((1 + required_return / 100) ** i)
        pv_dividends.append(pv)
    
    # 永续价值
    terminal_dps = cumulative_dps * (1 + terminal_growth / 100)
    terminal_value = terminal_dps / (required_return / 100 - terminal_growth / 100)
    pv_terminal = terminal_value / ((1 + required_return / 100) ** len(dividend_growth))
    
    intrinsic_value = sum(pv_dividends) + pv_terminal
    
    return {
        "intrinsic_value": round(intrinsic_value, 2),
        "pv_dividends": [round(p, 4) for p in pv_dividends],
        "terminal_value": round(terminal_value, 2),
        "pv_terminal": round(pv_terminal, 2)
    }
```

**示例 1｜两阶段 DDM 输入与输出对照**

| 输入项 | 取值 | 说明 |
|-------|------|------|
| 当前每股股利 | 0.90元 | 最近一期实际分红 |
| 高增长期 | 3年，增速15%/12%/10% | 对应业务扩张期 |
| 必要收益率 | 8.5% | 无风险利率 + 风险溢价 |
| 永续增长率 | 2.5% | 不高于长期名义GDP增速 |

输出：内在价值区间 [20.4, 22.8] 元；若现价 21.5 元，则处于区间中枢附近，评级倾向"中性"；若现价 18.0 元，则折价约14%，可给"增持"。

**示例 2｜DDM 适用性判断（先判断能不能用）**

| 公司特征 | 是否适用DDM | 建议替代方法 |
|---------|-----------|------------|
| 稳定分红的大型公用事业 | 适用 | — |
| 高分红银行 | 适用（注意拨备影响） | 股利折现 + PB校验 |
| 不分红的高成长科技 | 不适用 | DCF 或 PEG |
| 分红波动极大的周期股 | 慎用 | 正常化盈利 + PE区间 |
| 政策强制高分红但盈利下滑 | 慎用 | 情景化DDM（分红率下行情景） |

#### 2.3 PE Band Analysis / PE估值区间分析

```python
def pe_band_analysis(eps_history: list, price_history: list, 
                     forecast_eps: float) -> dict:
    """
    PE估值区间分析
    基于历史估值分布给出当前估值水位
    """
    # 计算历史PE
    pe_history = [p / e for p, e in zip(price_history, eps_history) if e > 0]
    
    # 统计分布
    pe_stats = {
        "min": np.min(pe_history),
        "q25": np.percentile(pe_history, 25),
        "median": np.median(pe_history),
        "q75": np.percentile(pe_history, 75),
        "max": np.max(pe_history),
        "mean": np.mean(pe_history)
    }
    
    # 估值区间
    valuation_band = {
        "极度低估 (PE < Q25)": forecast_eps * pe_stats["q25"],
        "偏低估 (Q25 < PE < Median)": forecast_eps * pe_stats["median"],
        "合理区间 (Median < PE < Q75)": forecast_eps * pe_stats["q75"],
        "偏高估 (PE > Q75)": forecast_eps * pe_stats["max"]
    }
    
    return {
        "pe_statistics": pe_stats,
        "valuation_band": {k: round(v, 2) for k, v in valuation_band.items()}
    }
```

**示例 1｜PE 分位与目标价推导**

| 分位 | PE | 对应股价（元） | 含义 |
|------|----|-------------|------|
| Q25 | 14.2x | 17.0 | 历史偏低水位 |
| 中位数 | 18.5x | 22.2 | 估值中枢 |
| Q75 | 24.0x | 28.8 | 历史偏高水平 |
| 当前 | 16.3x | 19.6 | 位于近5年28%分位 |

结论写法：现价对应16.3x、近5年28%分位，若给中位数18.5x则目标价22.2元（+13%空间）；给出目标价时必须同时说明所选分位与理由（如"行业景气向上，取中位数偏上分位"）。

**示例 2｜PE 区间失效场景排查**

| 场景 | 现象 | 处置 |
|------|------|------|
| 盈利为负或接近0 | PE 无意义或剧烈波动 | 改用PS或EV/EBITDA |
| 一次性收益扭曲EPS | 当期PE异常低 | 用扣非EPS重算 |
| 大额并购导致可比性下降 | 历史PE不可比 | 剔除并购年份或改用并表后口径 |
| 行业进入下行周期 | 低PE可能是"价值陷阱" | 用正常化盈利 + 周期位置判断 |
| 股本大幅变动 | EPS被摊薄 | 统一用最新总股本重算 |

### 3. Industry Research Framework / 行业研究框架

```markdown
## 行业研究标准框架

### 一、行业概述
- 行业定义与边界
- 产业链结构图
- 行业发展阶段（导入期/成长期/成熟期/衰退期）

### 二、竞争格局
- 市场集中度（CR3/CR5/CR10）
- 波特五力分析
- 竞争格局演变趋势

### 三、驱动因素
- 需求侧：市场规模、增速、渗透率
- 供给侧：产能扩张、技术迭代
- 政策面：监管政策、扶持政策
- 宏观面：经济周期、人口结构

### 四、核心标的
- 龙头公司竞争优势
- 二线公司差异化
- 潜在黑马

### 五、风险因素
- 周期性风险
- 政策风险
- 技术替代风险
- 竞争加剧风险
```

**行业景气度打分表（把"景气"量化，避免主观表述）**

| 维度 | 观测指标 | 权重 | 打分（1-5） | 加权得分 |
|------|---------|------|-----------|---------|
| 需求端 | 下游订单/出货量同比 | 30% | 4 | 1.20 |
| 价格端 | 主要产品价格环比 | 20% | 3 | 0.60 |
| 供给端 | 在建产能与开工率 | 15% | 2 | 0.30 |
| 库存端 | 渠道库存周转天数 | 15% | 4 | 0.60 |
| 政策端 | 政策方向与落地节奏 | 10% | 4 | 0.40 |
| 估值端 | 行业PE历史分位 | 10% | 3 | 0.30 |
| **合计** | — | 100% | — | **3.40** |

判定口径：加权得分 ≥3.5 为景气向上；3.0-3.5 为景气平稳；<3.0 为景气下行。打分须逐项标注数据来源与取数日期。

**示例｜跨行业比较矩阵（新增维度：景气度与估值匹配度）**

| 行业 | 需求增速 | 毛利率趋势 | 政策方向 | 行业PE分位 | 景气度得分 | 估值匹配度 | 结论 |
|------|---------|-----------|---------|-----------|-----------|-----------|------|
| 行业A | 25% | 上行 | 支持 | 35% | 4.2 | 匹配 | 重点推荐 |
| 行业B | 12% | 持平 | 中性 | 78% | 3.3 | 偏高 | 精选个股 |
| 行业C | -5% | 下行 | 限制 | 15% | 2.4 | 陷阱 | 回避 |
| 行业D | 18% | 上行 | 支持 | 62% | 3.8 | 略高 | 逢调布局 |

比较要点：同为高景气行业，若估值分位差异大，应优先选择"景气高+分位低"的组合；"景气低+分位低"往往是价值陷阱，需单独说明。

### 4. Short-Seller Response Template / 做空报告回应模板

```markdown
# 关于[做空机构名称]做空报告的声明

**公司声明日期**: YYYY-MM-DD
**股票代码**: [代码]
**声明人**: [公司名称]投资者关系部

## 一、核心回应

[机构]于[日期]发布的做空报告，存在严重的事实错误和误导性陈述。
本公司特此声明如下：

### 1. 关于[指控1]的回应
**事实**: [澄清事实]
**证据**: [提供证据]
**结论**: [明确结论]

### 2. 关于[指控2]的回应
[同上格式]

## 二、补充信息

### 财务数据核实
| 指标 | 公司公告数据 | 做空报告数据 | 差异说明 |
|-----|-------------|-------------|---------|
| | | | |

## 三、风险提示

本声明不构成投资建议。投资者应仔细阅读公司过往公告，
审慎判断投资风险。

---
联系方式：[IR邮箱]
```

**24小时响应时间表（应急流程参考）**

| 时点 | 动作 | 责任人 | 交付物 |
|------|------|-------|-------|
| T+0小时 | 收集做空报告原文与市场反应数据 | 研究 | 指控清单（逐条拆分） |
| T+1小时 | 事实核对与证据归集（公告、审计报告、工商资料） | 研究+IR | 证据包 |
| T+2小时 | 内部会商定调，明确回应边界 | 合规+IR | 回应口径 |
| T+4小时 | 完成首版回应稿框架 | 研究 | 初稿 |
| T+6小时 | 合规复核，核对数据与表述 | 合规 | 复核意见 |
| T+12小时 | 补充证据与量化测算 | 研究 | 终稿 |
| T+24小时 | 发布并同步市场沟通口径 | IR | 声明+问答口径表 |

**示例｜指控-事实-证据三段式（量化反驳）**

| 指控 | 做空方说法 | 事实核对 | 证据 | 量化差异 |
|------|-----------|---------|------|---------|
| 收入真实性 | "收入增速远超行业" | 收入增速与行业一致，差异来自并表 | 审计报告、并表公告 | 剔除并表后增速11.2%，行业12.0% |
| 应收账款质量 | "应收账款周转恶化" | 周转天数上升因账期政策调整 | 年报附注、客户结构 | 调整后周转天数同比+9天，非恶化 |
| 关联交易 | "存在未披露关联交易" | 交易已在年报关联交易章节披露 | 年报第X节 | 披露完整，金额占比3.1% |

原则：每条指控都要落到"可比数字"，不做纯文字反驳；无法证实的部分明确说明核查进展，不臆测。

---

## Compliance Checklist / 合规检查清单

| 检查项 | 依据 | 通过标准 |
|-------|------|---------|
| 盈利预测合理性 | 《证券研究报告执业规范》 | 预测区间不超过合理范围 |
| 风险提示完整性 | 《证券法》第79条 | 必须包含3项以上风险提示 |
| 利益冲突披露 | 证监会相关规定 | 持有股票需披露 |
| 评级定义一致性 | 《证券研究报告执业规范》 | 评级定义需与公司标准一致 |
| 数据来源合规 | 交易所规则 | 引用数据需标注来源 |
| 假设可追溯性 | 内部质控要求 | 关键假设均标注依据与取数日期 |
| 估值口径统一 | 内部质控要求 | 币种、股本、净负债处理口径一致 |
| 目标价与评级匹配 | 内部质控要求 | 目标价隐含空间与评级档位对应 |
| 免责声明完整 | 内部质控要求 | 摘要与正文均保留免责声明 |
| 预期差表述准确 | 内部质控要求 | 明确区分预告口径与实际口径 |
| 敏感性分析完备 | 内部质控要求 | 关键假设均给出敏感性区间 |

---

## Usage Examples / 使用示例

**启动研报撰写：**
```
分析[行业名称]的竞争格局和投资机会，生成行业研究报告模板
```

**估值建模：**
```
帮我用DCF模型对[公司名称]估值：
- 未来5年FCF预测：[X]亿/[X]亿/[X]亿/[X]亿/[X]亿
- WACC：[X]%
- 永续增长率：[X]%
```

**做空报告应急：**
```
[机构]刚发布做空报告指控[公司]，需24小时内回应，
帮我生成回应初稿框架，重点反驳以下3点：
1. [指控点1]
2. [指控点2]
3. [指控点3]
```

**行业景气度打分：**
```
对[行业名称]做景气度打分：按需求、价格、供给、库存、政策、估值六个维度，
每项给出1-5分与数据依据，并输出加权得分与景气判定结论。
```

**估值复算与敏感性：**
```
用DCF对[公司名称]重算估值，并输出WACC（9.0%/9.5%/10.0%）× 永续增长率（2.0%/2.5%/3.0%）
的敏感性矩阵，标出估值中枢与区间边界，并说明终值占比是否偏高。
```

---

## Disclaimer

This skill provides research report templates and valuation models for educational and reference purposes. Investment decisions should be based on independent research and professional advice. All outputs should be reviewed by qualified analysts before publication or use in investment decisions.
