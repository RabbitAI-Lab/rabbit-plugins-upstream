---
name: Bond Analysis Expert
slug: security-bond-analysis
description: AI-powered bond analysis expert for China market — covers bond valuation, yield analysis, duration/convexity calculation, credit spread analysis, and bond portfolio management. Built for fixed income analysts, bond traders, and portfolio managers. Keywords: bond analysis, yield curve, duration, convexity, credit spread, China bonds,利率债, 信用债, 国债, 企业债, 城投债, 债券估值, 收益率曲线, 久期, 凸性, 信用利差, 固收, 利率风险, 债券组合.
version: "3.0.2"
---

# Bond Analysis Expert / 债券分析专家

> **English:** AI-powered bond analysis expert — covers bond valuation, yield analysis, duration/convexity calculation, credit spread analysis, and bond portfolio management. Built for fixed income professionals.
>
> **中文:** 债券分析专家——覆盖债券估值、收益率分析、久期/凸性计算、信用利差分析、债券组合管理。适用：固收分析师、债券交易员、组合管理人。

---


### 证券监管最新动态 [2026-09-13更新]

| 动态类型 | 内容摘要 | 影响范围 | 固收侧应对动作 | 优先级 |
|---------|---------|---------|-------------|-------|
| 银行理财 | 理财"三清"（净值清晰、风险清晰、投向清晰）持续推进 | 理财资金的债券配置偏好 | 按期限与评级重估负债稳定性，相应调整组合久期 | 高 |
| 地方债务化解 | 一揽子化债安排持续落地，城投平台融资与偿债结构变化 | 城投债定价与估值 | 按区域财力与债务率分级，区分公开债与非标风险 | 高 |
| 债券市场统一执法 | 银行间与交易所市场信息披露、违约处置规则趋同 | 违约回收率与估值口径 | 建立违约处置流程台账，跟踪回收进度 | 高 |
| 信用风险 | 信用债内部分化加剧，弱资质主体再融资压力上升 | 信用利差分层 | 提高利差分位监控频率，弱资质主体加做压力测算 | 高 |
| 流动性 | 做市与报价机制完善，部分品种流动性分层明显 | 交易成本与冲击成本 | 按流动性分层设定单券持仓上限 | 中 |
| 可转债 | 可转债条款（修正、赎回、回售）执行与信息披露受关注 | 转债估值与条款风险 | 逐券登记条款触发条件，跟踪强赎公告 | 中 |

> **数据截止**: 2026-09-13 | 来源：证监会、NFRA、交易商协会、中证协、行业公开信息
> **声明**: 以上动态供参考，具体以官方最新发布为准

**动态解读示例（两类高频场景）**

- **场景A｜城投估值随政策预期波动**：某区域城投债在中性假设下按 AAA 利差定价；化债政策预期升温阶段，同区域利差两个交易日收窄 12bp，随后因财力数据不及预期又走阔 15bp。**解读**：政策预期驱动的利差波动不等于信用基本面改善，应跟踪区域一般公共预算收入、债务率与再融资滚续能力三项硬指标，而非只跟随消息面。
- **场景B｜转债强赎条款误判**：某转债正股在连续 30 个交易日中已有 15 个交易日收盘价高于转股价 130%，触及强赎条件。若仍按"转债无到期日、可长期持有"的思路配置 → 可能被按面值加当期利息强制赎回。**改进动作**：对可转债逐券登记条款触发进度，每周复核一次。

## Industry Pain Points / 行业痛点

| Pain Point / 痛点 | Impact / 影响 | Solution / 本Skill解决方案 | 量化基线（示例） |
|------------------|-------------|------------------------|---------------|
| **收益率计算复杂** | 多种收益率指标容易混淆 | 标准化收益率计算框架 | 全组合统一 YTM 口径并记录取值日期 |
| **信用分析耗时** | 发行主体众多，分析量大 | 模板化信用分析框架 | 主体入池前完成五项区域与财务核验 |
| **利率风险难测** | 久期/凸性概念抽象，估算误差大 | 可视化风险分析 | 利率变动 >50bp 必须计入凸性项 |
| **城投债信仰** | 城投刚兑预期与违约现实冲突 | 区域财政分析模型 | 按财力与债务率分级，弱区域不超组合 5% |
| **久期管理难** | 利率变动对组合影响大 | 久期匹配优化工具 | 组合久期偏离基准 ≤0.5 年 |
| **可转债条款复杂** | 强赎/修正/回售条款判断易遗漏 | 逐券条款登记与触发进度表 | 每周复核一次条款触发进度 |
| **估值口径不统一** | 全价净价、付息频率混用导致结果偏差 | 统一定价口径并留痕 | 全组合同一口径 + 记录取值日期 |

---

## Trigger Keywords / 触发关键词

**English Triggers:** bond analysis, yield curve, duration, convexity, credit spread, China bonds, fixed income, bond valuation, interest rate risk, credit risk

**中文触发词（优先）：** 债券分析 / 收益率曲线 / 久期 / 凸性 / 信用利差 / 中国债券 / 固收 / 债券估值 / 利率风险 / 信用风险 / 国债 / 企业债 / 城投债 / 金融债 / 可转债 / 债券回购 / 债券评级 / YTM / 即期收益率 / 到期收益率

---

## Core Capabilities / 核心能力

### 1. Bond Valuation Engine / 债券估值引擎

```python
import numpy as np
import pandas as pd

class BondAnalyzer:
    """债券分析引擎"""
    
    @staticmethod
    def calculate_price(face_value: float, coupon_rate: float, 
                       ytm: float, years: int, 
                       frequency: int = 2) -> float:
        """
        债券定价
        Args:
            face_value: 面值（元）
            coupon_rate: 年票面利率
            ytm: 到期收益率
            years: 剩余期限（年）
            frequency: 付息频率（1=年付，2=半年付）
        """
        n = years * frequency
        r_per_period = ytm / frequency
        c_per_period = (face_value * coupon_rate) / frequency
        
        # 现金流现值
        pv_coupons = sum([c_per_period / (1 + r_per_period) ** t 
                         for t in range(1, n + 1)])
        pv_face = face_value / (1 + r_per_period) ** n
        
        return pv_coupons + pv_face
    
    @staticmethod
    def calculate_ytm(price: float, face_value: float,
                     coupon_rate: float, years: float,
                     frequency: int = 2) -> float:
        """
        计算到期收益率（YTM）- 牛顿迭代法
        """
        n = years * frequency
        c = (face_value * coupon_rate) / frequency
        
        # 初始猜测
        ytm = coupon_rate
        
        for _ in range(100):
            pv = sum([c / (1 + ytm/frequency) ** t 
                     for t in range(1, n + 1)]) + face_value / (1 + ytm/frequency) ** n
            
            diff = price - pv
            
            # 导数（久期近似）
            duration = BondAnalyzer.calculate_duration(
                price, face_value, coupon_rate, ytm, years, frequency
            )
            dv = -duration / (1 + ytm/frequency) * diff
            
            ytm = ytm + diff / dv * 0.5
            
            if abs(diff) < 1e-6:
                break
        
        return ytm
    
    @staticmethod
    def calculate_duration(price: float, face_value: float,
                          coupon_rate: float, ytm: float,
                          years: float, frequency: int = 2) -> float:
        """
        计算久期（Macauley Duration）
        """
        n = int(years * frequency)
        c = (face_value * coupon_rate) / frequency
        r = ytm / frequency
        
        # 加权平均到期时间
        weighted_time = sum([t * c / (1 + r) ** t for t in range(1, n + 1)])
        weighted_time += n * face_value / (1 + r) ** n
        
        return weighted_time / price / frequency  # 转换为年
    
    @staticmethod
    def calculate_convexity(price: float, face_value: float,
                          coupon_rate: float, ytm: float,
                          years: float, frequency: int = 2) -> float:
        """
        计算凸性
        """
        n = int(years * frequency)
        c = (face_value * coupon_rate) / frequency
        r = ytm / frequency
        
        weighted_sq = sum([t * (t + 1) * c / (1 + r) ** (t + 2) 
                          for t in range(1, n + 1)])
        weighted_sq += n * (n + 1) * face_value / (1 + r) ** (n + 2)
        
        return weighted_sq / price / (frequency ** 2)
    
    @staticmethod
    def price_change_estimate(duration: float, convexity: float,
                             rate_change: float) -> dict:
        """
        利率变动对价格的影响估算
        """
        # 久期效应
        duration_effect = -duration * rate_change
        
        # 凸性效应
        convexity_effect = 0.5 * convexity * (rate_change ** 2)
        
        total_effect = duration_effect + convexity_effect
        
        return {
            "duration_effect": round(duration_effect * 100, 4),
            "convexity_effect": round(convexity_effect * 100, 4),
            "total_effect": round(total_effect * 100, 4),
            "approximate_new_price_pct": round((1 + total_effect) * 100, 4)
        }
```

#### 1.1 Worked Example / 估值结果解读示例

**输入**：面值 100 元，票面利率 4.00%，YTM 3.50%，剩余 5 年，年付。

| 指标 | 示例取值 | 含义 | 解读要点 |
|-----|---------|------|---------|
| price | 102.26 元 | 现金流现值合计 | 高于面值，因票息 4% > 市场利率 3.5% |
| Macaulay duration | 4.62 年 | 加权平均回款时间 | 票息越高、期限越短，久期越小 |
| Modified duration | 4.46 | 利率每变动 1 个百分点，价格反向变动约 4.46% | 风险度量的核心参数 |
| convexity | 24.1 | 久期自身的变动速率 | 凸性为正，利率大幅波动时对持有人有利 |
| DV01 | 0.0456 元/百元面值 | 利率每变动 1bp 的价格变动 | 组合层面即"每 bp 损益" |

**久期与凸性组合效应（利率上行/下行对照）**

| 利率变动 | 久期效应 | 凸性效应 | 合计 | 说明 |
|---------|--------|--------|------|------|
| +100bp | −4.46% | +0.12% | −4.34% | 凸性提供正向缓冲 |
| +50bp | −2.23% | +0.03% | −2.20% | 小幅变动时凸性影响很小 |
| −50bp | +2.23% | +0.03% | +2.26% | 收益率下行时价格涨得更多 |
| −100bp | +4.46% | +0.12% | +4.58% | 上涨幅度略大于同幅下跌 |

> **提示**：利率变动在 ±10bp 以内，仅用久期估算的误差通常在 1bp 价格量级，可以接受；超过 ±50bp 必须加入凸性项，否则会用久期线性外推、系统性夸大上行时的损失。

**常见计算错误（供复核）**

- **付息频率与期数不匹配**：半年付息债券 5 年应为 10 期、每期折现率取 YTM/2；直接用年付口径会使价格偏差约 0.1 元以上。
- **全价与净价混淆**：交易报价通常为净价，估值需用全价（净价 + 应计利息）；应计利息 = 票面利率 × 已过计息天数 ÷ 当期计息天数。
- **YTM 反算不收敛**：市场价与票面利率偏离过大时初值取值不佳，可先用"票面利率 ± 面值/价格修正项"构造更接近的初值，或改用二分法。

### 2. Credit Analysis Framework / 信用分析框架

```markdown
## 信用债分析模板

### 一、发债主体概况
| 项目 | 内容 |
|-----|------|
| 公司名称 | |
| 实际控制人 | |
| 主体评级 | |
| 行业分类 | |
| 主营业务 | |

### 二、财务分析
```python
CREDIT_ANALYSIS_RATIOS = {
    "盈利能力": {
        "毛利率": ">30%为优质",
        "净利率": ">15%为优质",
        "ROE": ">10%为优质"
    },
    "偿债能力": {
        "资产负债率": "<70%为稳健",
        "流动比率": ">1.5为稳健",
        "利息保障倍数": ">3倍为稳健"
    },
    "现金流": {
        "经营现金流/带息债务": ">15%为稳健",
        "经营现金流/资本支出": ">100%为稳健"
    }
}
```

#### 2.1 财务指标分层阈值（示例，供交叉验证）

| 指标 | 优质 | 稳健 | 关注 | 预警 | 说明 |
|-----|-----|-----|-----|-----|------|
| 资产负债率 | <55% | 55%-70% | 70%-80% | >80% | 行业差异大，重资产行业可适度放宽 |
| 流动比率 | >2.0 | 1.5-2.0 | 1.0-1.5 | <1.0 | 需结合速动比率一并观察 |
| 利息保障倍数 | >5 倍 | 3-5 倍 | 1.5-3 倍 | <1.5 倍 | 低于 1 倍说明经营利润不足以覆盖利息 |
| 经营现金流/带息债务 | >25% | 15%-25% | 8%-15% | <8% | 比利润指标更难粉饰 |
| 经营现金流/资本支出 | >150% | 100%-150% | 60%-100% | <60% | 长期低于 100% 说明依赖外部融资 |

#### 2.2 城投主体区域分析维度（示例）

| 维度 | 具体指标 | 数据来源 | 观察要点 |
|-----|---------|---------|---------|
| 财政实力 | 一般公共预算收入、税收占比、财政自给率 | 地方预算执行报告 | 关注收入质量而非总量 |
| 债务压力 | 地方政府债务率、城投有息债务/综合财力 | 公开统计与评级报告 | 计算口径需全市场统一 |
| 平台地位 | 平台层级、公益性业务占比、政府补助占比 | 募集说明书 | 层级越低、市场化业务越多，政府支持意愿越难判定 |
| 再融资能力 | 近 12 个月债券发行与到期规模、银行授信余额 | 发行公告 | 滚续能力是短期违约的直接决定因素 |
| 外部支持 | 上级政府财力、担保与救助记录 | 公开信息 | 关注是否已有非标违约先例 |

### 三、信用利差分析
```python
def analyze_credit_spread(bond_yield: float, treasury_yield: float,
                         rating: str) -> dict:
    """
    信用利差分析
    """
    spread = bond_yield - treasury_yield
    
    # 评级对应利差参考
    SPREAD_REFERENCE = {
        "AAA": 0.50,  # 50bp
        "AA+": 0.80,
        "AA": 1.20,
        "AA-": 1.50,
        "A+": 2.00,
        "A": 2.50
    }
    
    reference = SPREAD_REFERENCE.get(rating, 2.0)
    
    return {
        "credit_spread": round(spread * 100, 2),
        "reference_spread": reference,
        "relative_value": "低估" if spread < reference else "高估",
        "spread_premium": round((spread - reference) * 100, 2)
    }
```

#### 2.3 Spread Percentile Reading / 利差分位解读示例

| 利差绝对水平 | 近 3 年分位 | 评级 | 解读 | 研究结论（示例） |
|-----------|-----------|------|------|--------------|
| 62bp | 15%（低位） | AAA | 利差补偿不充分 | 相对价值偏低，考虑缩短久期或换券 |
| 118bp | 55%（中位） | AA+ | 与评级参考利差基本一致 | 无显著错价，按配置需求决策 |
| 265bp | 92%（高位） | AA | 利差含较高风险溢价 | 先排除个体风险（到期结构、负面舆情）再判断是否错价 |
| 430bp | 98%（极值） | AA- | 接近"准违约"定价 | 不属于相对价值机会，应进入风险名单复核 |

**示例测算**：某 AA+ 城投债 YTM 3.68%，同期限国债 2.50%，利差 118bp；评级参考利差 80bp → 溢价比参考高 38bp。若该主体近 12 个月发行与到期规模大体匹配、区域一般公共预算收入同比小幅增长，可初步判断 **38bp 溢价可能来自流动性与市场情绪而非基本面恶化**——但输出结论时应写成"需进一步核验"，并列出核验清单，而非直接给出交易方向判断。
```

### 3. Bond Portfolio Management / 债券组合管理

```python
class BondPortfolio:
    """债券组合管理"""
    
    def __init__(self):
        self.bonds = []
    
    def add_bond(self, bond: dict):
        """添加债券"""
        # 计算关键指标
        bond["price"] = self._calculate_bond_price(bond)
        bond["ytm"] = self._calculate_ytm(bond)
        bond["duration"] = self._calculate_duration(bond)
        bond["convexity"] = self._calculate_convexity(bond)
        bond["dv01"] = bond["duration"] * bond["price"] / 100 / 100  # 每bp变化
        
        self.bonds.append(bond)
    
    def portfolio_duration(self) -> float:
        """组合久期"""
        total_value = sum(b["market_value"] for b in self.bonds)
        weighted_duration = sum(
            b["duration"] * b["market_value"] for b in self.bonds
        ) / total_value
        return weighted_duration
    
    def portfolio_credit_breakdown(self) -> dict:
        """组合信用分布"""
        breakdown = {}
        for bond in self.bonds:
            rating = bond.get("rating", "Unknown")
            if rating not in breakdown:
                breakdown[rating] = {"count": 0, "value": 0}
            breakdown[rating]["count"] += 1
            breakdown[rating]["value"] += bond.get("market_value", 0)
        
        return breakdown
    
    def interest_rate_risk(self, rate_shock: float) -> dict:
        """利率风险分析"""
        port_duration = self.portfolio_duration()
        
        # 纯久期效应
        duration_pnl = -port_duration * rate_shock / 100
        
        # 凸性调整
        port_convexity = sum(
            b["convexity"] * b["market_value"] for b in self.bonds
        ) / sum(b["market_value"] for b in self.bonds)
        convexity_pnl = 0.5 * port_convexity * (rate_shock/100) ** 2
        
        return {
            "portfolio_duration": round(port_duration, 3),
            "rate_shock_bp": round(rate_shock * 100, 0),
            "duration_pnl_pct": round(duration_pnl * 100, 2),
            "convexity_pnl_pct": round(convexity_pnl * 100, 2),
            "total_pnl_pct": round((duration_pnl + convexity_pnl) * 100, 2)
        }
```

#### 3.1 Interest Rate Scenario Table / 利率情景损益示例

**输入**：组合规模 1,000 万元，组合久期 3.8 年，组合凸性 18.6。

| 情景 | 利率变动 | 久期损益 | 凸性调整 | 合计损益 | 说明 |
|-----|--------|--------|--------|--------|------|
| 大幅下行 | −50bp | +19.0 万 | +2.3 万 | +21.3 万 | 收益率下行阶段凸性放大收益 |
| 小幅下行 | −20bp | +7.6 万 | +0.4 万 | +8.0 万 | 常见情景 |
| 持平 | 0 | 0 | 0 | 0 | 仅有持有期票息收益 |
| 小幅上行 | +20bp | −7.6 万 | +0.4 万 | −7.2 万 | 凸性小幅缓冲 |
| 大幅上行 | +50bp | −19.0 万 | +2.3 万 | −16.7 万 | 凸性保护在上行时更明显 |

> **口径说明**：表中损益为价格变动损益，不含持有期票息收入。组合凸性为正时，上行情景的损失被部分抵消，下行收益被小幅放大——这就是"凸性偏好"的来源。

#### 3.2 Immunization / 久期免疫与负债匹配（示例）

| 负债特征 | 匹配方式 | 关键约束 | 复核频率 |
|---------|--------|---------|---------|
| 单一确定时点支付 | 单期免疫：组合久期 = 剩余期限 | 组合凸性应大于负债凸性 | 每季度 |
| 多期确定支付 | 多期免疫：现金流按期限分层匹配 | 每层久期与对应负债久期偏差 ≤0.2 年 | 每季度 |
| 不确定支取（如理财赎回） | 久期区间管理 + 流动性缓冲 | 保留 5%-10% 高流动性资产 | 每月 |
| 收益率曲线非平行变动 | 关键利率久期（KRD）管理 | 各关键期限敞口 ≤总敞口 30% | 每月 |

#### 3.3 Portfolio Review Checklist / 组合复核清单

| 检查项 | 阈值（示例） | 触发动作 |
|-------|-----------|---------|
| 组合久期偏离基准 | ±0.5 年以内 | 超出则再平衡 |
| 单一主体集中度 | ≤5% | 超限则减仓或专项说明 |
| 弱资质主体（AA 及以下）占比 | ≤15% | 超限须专项审批 |
| 高流动性资产占比 | ≥5% | 低于则补充 |
| 估值偏离中债估值 | ±30bp 以内 | 偏离需说明原因 |
| 到期滚续缺口 | 未来 3 个月到期 ≤可动用资金 | 存在缺口须提前安排 |

### 4. Convertible Bond Analysis / 可转债分析

```python
def analyze_convertible(convert_price: float, stock_price: float,
                        bond_floor: float, market_price: float) -> dict:
    """
    可转债关键指标测算（供研究参考）
    """
    conversion_value = 100 / convert_price * stock_price   # 每百元面值的转股价值
    premium_rate = (market_price - conversion_value) / conversion_value * 100
    downside_buffer = (market_price - bond_floor) / bond_floor * 100

    return {
        "conversion_value": round(conversion_value, 2),
        "conversion_premium_rate": round(premium_rate, 2),   # 转股溢价率
        "downside_buffer": round(downside_buffer, 2),        # 相对纯债价值的溢价比
        "reading": "转股溢价率偏高，股性偏弱" if premium_rate > 30 else "股性相对较强"
    }
```

| 指标 | 计算口径 | 解读要点 |
|-----|---------|---------|
| 转股价值 | 100 ÷ 转股价 × 正股价 | 与转债价格对比得出溢价率 |
| 转股溢价率 | (转债价 − 转股价值) ÷ 转股价值 | 越高说明股性越弱、对正股上涨越不敏感 |
| 纯债价值 | 按同评级同期限信用债 YTM 折现 | 构成转债的价格下限 |
| 双低值 | 转债价 + 转股溢价率 × 100 | 常用的相对估值筛选口径之一 |
| 条款触发进度 | 修正/赎回/回售条款的交易日计数 | 强赎触发后按面值加利息赎回，须重点关注 |

**示例**：某转债转股价 12.00 元，正股价 13.20 元，转债市场价 128.50 元，同评级纯债价值约 92 元。
- 转股价值 = 100 ÷ 12.00 × 13.20 = 110.00 元；
- 转股溢价率 = (128.50 − 110.00) ÷ 110.00 = 16.8%（股性相对较强）；
- 相对纯债价值的溢价比 = (128.50 − 92.00) ÷ 92.00 = 39.7%（保护垫较薄，正股下跌时回撤空间大）。

**条款风险提示**：当正股满足"连续 30 个交易日中至少 15 个交易日收盘价 ≥ 转股价 130%"时，多数转债条款将触发强赎条件。持有高溢价转债且已触发强赎的，需及时评估转股或卖出，否则可能被按面值加当期利息赎回。

---

## Risk Control Checklist / 风控与合规检查清单

| 检查项 | 依据/说明 | 通过标准 |
|-------|---------|---------|
| 估值口径统一 | 全价/净价、付息频率、应计利息规则 | 全组合统一并留痕 |
| 数据来源 | 中债估值等公开基准 | 记录取值日期与来源 |
| 评级一致性 | 外部评级与内部评级差异 | 差异超一档须专项说明 |
| 集中度管理 | 单一主体、单一区域、单一行业占比 | 均在预设阈值内 |
| 久期偏离 | 相对基准的久期偏离 | 处于允许区间 |
| 流动性分层 | 单券持仓相对日均成交 | 不超过预设上限 |
| 违约处置预案 | 违约债券处置流程与台账 | 有流程、有责任人 |
| 免责表述 | 分析结果仅供参考，不构成投资建议 | 每份输出均含声明 |

---

## Quick Command Templates / 快速指令模板

**债券定价：**
```
计算债券价格：
- 面值：100元
- 票面利率：4%
- 到期收益率：3.5%
- 剩余期限：5年
- 付息频率：年付
```

**久期分析：**
```
分析债券组合的久期风险：
- 组合总规模：1000万
- 利率上升50bp时的损益
```

**信用利差分析：**
```
分析信用利差：
- 债券YTM：3.68%
- 同期限国债收益率：2.50%
- 主体评级：AA+
需要输出：利差绝对值、对应评级参考利差、近3年利差分位、初步判断与需进一步核验清单
```

**可转债分析：**
```
分析可转债：
- 转股价：12.00元，正股价：13.20元
- 转债市场价：128.50元，同评级纯债价值约92元
输出转股价值、转股溢价率、相对纯债溢价比，并核验强赎条款触发进度
```

**城投主体复核：**
```
复核某城投主体信用状况：
- 区域：某地级市
- 需要维度：一般公共预算收入、债务率、平台层级、近12个月发行与到期规模
- 要求：给出分级判断与需进一步核验清单
```

---

## Disclaimer

Bond analysis involves various risks including interest rate risk and credit risk. This skill provides analysis tools for educational purposes only and does not constitute investment advice.
