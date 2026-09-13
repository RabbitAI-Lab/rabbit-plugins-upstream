---
name: Portfolio Risk Analysis Expert
slug: security-portfolio-risk
description: AI-powered portfolio risk analysis expert for China market — covers VaR calculation, stress testing, tail risk measurement, factor exposure analysis, and risk decomposition. Built for fund managers, risk analysts, and institutional investors. Keywords: portfolio risk, VaR, stress testing, risk decomposition, China A-share, factor risk, tail risk, 组合风险, 风险分析, VaR, 压力测试, 风险分解, 风险管理, 最大回撤, 夏普比率, 收益风险比, 资产配置, 风险预算.
version: "3.0.2"
---

# Portfolio Risk Analysis Expert / 组合风险分析专家

> **English:** AI-powered portfolio risk analysis expert — covers VaR calculation, stress testing, tail risk measurement, factor exposure, and risk attribution. Built for fund managers and risk analysts.
>
> **中文:** 组合风险分析专家——覆盖VaR计算、压力测试、尾部风险度量、因子敞口分析、风险归因。适用：基金经理、风险分析师、机构投资者。

---


### 证券监管最新动态 [2026-09-12更新]

| 动态类型 | 内容摘要 | 影响范围 | 风险侧应对动作 | 责任岗 | 优先级 |
|---------|---------|---------|--------------|-------|-------|
| 证券监管 | 2026年Q1：市场波动加剧，组合风险管理要求提升 | 组合风险模型需增加量化冲击和ESG风险维度 | 风险报告增设极端情景专项说明 | 风控 | 高 |
| 证券监管 | 量化资金共振风险增加，极端行情止损策略需更新 | 组合风险模型需增加量化冲击和ESG风险维度 | 压力测试新增流动性枯竭情景 | 风控 | 高 |
| 证券监管 | ESG投资分析要求扩大，组合风险需纳入ESG因素 | 组合风险模型需增加量化冲击和ESG风险维度 | 风险分解单列ESG敞口维度 | 风控 | 中 |
| 程序化交易 | 程序化交易报告与异常交易监控要求细化 | 极端行情下的流动性与波动归因 | 压力测试中区分程序化交易影响部分 | 风控 | 中 |
| 信息披露 | 上市公司信息披露质量监管强化 | 风险模型的财务输入数据 | 模型输入须标注报告期与数据来源 | 风控 | 高 |
| 估值与净值 | 净值化管理要求下风险指标披露趋严 | 产品风险报告与定期披露 | 波动率、回撤、VaR口径固定并留档 | 合规 | 高 |
| 投资者保护 | 风险揭示与适当性匹配要求提升 | 产品风险等级与客户匹配 | 风险报告附适当性匹配说明 | 合规 | 高 |
| 集中度管理 | 单一标的与单一行业集中度关注度提升 | 组合集中度指标 | 集中度阈值纳入日常监控与预警 | 风控 | 高 |

> **数据截止**: 2026-09-12 | 来源：证监会、交易所公开规则、行业公开信息
> **声明**: 以上动态供参考，具体以官方最新发布为准

**动态解读示例（四类高频场景）**

- **场景A｜流动性枯竭情景**：压力测试仅覆盖价格冲击，未考虑成交量萎缩 → 命中"量化共振风险"要求 → 新增"流动性降至50%+价格下跌20%"的复合情景，输出无法顺利减仓的敞口估算。
- **场景B｜ESG敞口单列**：风险分解仅按行业与因子拆分 → 命中"ESG风险维度"要求 → 在风险分解中增加ESG评级分布与高碳敞口占比。
- **场景C｜口径固定留档**：不同报告的波动率口径时而日频、时而月频 → 命中"口径固定披露"要求 → 统一为日频年化并在报告中标注计算口径与样本区间。
- **场景D｜集中度预警**：单标的市值占比升至18%未触发任何预警 → 命中"集中度监控"要求 → 设置单标的15%、单行业35%的预警线，超限自动进入整改流程。

## Industry Pain Points / 行业痛点

| Pain Point / 痛点 | Impact / 影响 | Solution / 本Skill解决方案 | 量化基线指标 / Baseline |
|------------------|-------------|------------------------|----------------------|
| **系统风险难预测** | 黑天鹅事件导致大幅回撤 | 极端情景压力测试+尾部风险分析 | 压力测试情景覆盖 ≥6类 |
| **因子敞口不清晰** | 不知道组合暴露在哪些风险上 | 因子归因模型+敞口分解 | 因子解释度 R² ≥0.7 |
| **回撤控制困难** | 持有人体验差，资金赎回压力 | 动态回撤监控+预警机制 | 最大回撤控制在预设阈值内 |
| **相关性突变** | 平时低相关的资产大跌时齐跌 | 相关性压力测试+分散化效果评估 | 压力情景下相关性假设上浮至0.7+ |
| **合规要求高** | 资管新规净值化要求 | 标准风险指标+监管报告 | 风险指标披露完整率 100% |
| **集中度超标** | 单一标的/行业权重过高 | 集中度监控阈值+预警 | 单标的≤15%、单行业≤35% |
| **尾部风险低估** | VaR未反映肥尾特征 | CVaR与修正VaR双口径 | 同时披露VaR与CVaR |
| **口径不一致** | 跨报告指标不可比 | 计算口径登记表 | 口径一致率 100% |

---

## Trigger Keywords / 触发关键词

**English Triggers:** portfolio risk, VaR, stress testing, risk decomposition, factor exposure, tail risk, risk attribution, China A-share, fund management, risk management

**中文触发词（优先）：** 组合风险 / 风险分析 / VaR / 压力测试 / 回撤控制 / 风险归因 / 因子敞口 / 尾部风险 / 风险分解 / 风险预警 / 资产配置 / 分散化 / 相关性分析 / 最大回撤 / 夏普比率 / 波动率 / 风险调整收益 / 风险预算 / VaR计算 / CVaR / ES

---

## Core Capabilities / 核心能力

### 1. VaR & Risk Metrics / VaR与风险指标

```python
import numpy as np
import pandas as pd
from scipy import stats

class PortfolioRiskAnalyzer:
    """组合风险分析引擎"""
    
    def __init__(self, returns: pd.DataFrame, weights: np.ndarray):
        """
        Args:
            returns: 收益率序列（列=资产，行=日期）
            weights: 资产权重向量
        """
        self.returns = returns
        self.weights = weights
        self.n_assets = len(weights)
    
    def calculate_var(self, confidence: float = 0.95, 
                      method: str = "historical") -> dict:
        """计算VaR（Value at Risk）"""
        portfolio_returns = (self.returns * self.weights).sum(axis=1)
        
        if method == "historical":
            var = np.percentile(portfolio_returns, (1 - confidence) * 100)
        elif method == "parametric":
            mu = portfolio_returns.mean()
            sigma = portfolio_returns.std()
            var = stats.norm.ppf(1 - confidence, mu, sigma)
        elif method == "modified":
            # Cornish-Fisher调整
            mu = portfolio_returns.mean()
            sigma = portfolio_returns.std()
            skew = stats.skew(portfolio_returns)
            kurt = stats.kurtosis(portfolio_returns)
            z = stats.norm.ppf(1 - confidence)
            z_cf = (z + (z**2 - 1) * skew / 6 + 
                   (z**3 - 3*z) * kurt / 24 - 
                   (2*z**3 - 5*z) * skew**2 / 36)
            var = mu + sigma * z_cf
        
        return {
            "var": round(var * 100, 2),  # 百分比
            "var_amount": round(var * 1000000, 2),  # 假设100万组合
            "confidence": confidence,
            "method": method,
            "interpretation": f"在{confidence*100}%置信度下，最大损失为{abs(var)*100:.2f}%"
        }
    
    def calculate_cvar(self, confidence: float = 0.95) -> dict:
        """计算CVaR（Conditional VaR / Expected Shortfall）"""
        portfolio_returns = (self.returns * self.weights).sum(axis=1)
        var = np.percentile(portfolio_returns, (1 - confidence) * 100)
        
        cvar = portfolio_returns[portfolio_returns <= var].mean()
        
        return {
            "cvar": round(cvar * 100, 2),
            "cvar_amount": round(cvar * 1000000, 2),
            "interpretation": f"超过VaR时的平均损失为{abs(cvar)*100:.2f}%"
        }
    
    def calculate_max_drawdown(self) -> dict:
        """计算最大回撤"""
        cumulative = (1 + self.returns @ self.weights).cumprod()
        running_max = cumulative.expanding().max()
        drawdown = (cumulative - running_max) / running_max
        
        max_dd = drawdown.min()
        max_dd_end = drawdown.idxmin()
        max_dd_start = cumulative[:max_dd_end].idxmax()
        
        return {
            "max_drawdown": round(max_dd * 100, 2),
            "peak_date": str(max_dd_start.date()),
            "trough_date": str(max_dd_end.date()),
            "recovery_date": None  # 需后续计算
        }
    
    def factor_risk_attribution(self, factor_returns: pd.DataFrame) -> dict:
        """因子风险归因"""
        portfolio_returns = self.returns @ self.weights
        
        # 回归分析
        X = factor_returns.values
        X = np.column_stack([np.ones(len(X)), X])
        y = portfolio_returns.values
        
        coeffs = np.linalg.lstsq(X, y, rcond=None)[0]
        residuals = y - X @ coeffs
        
        # 分解方差
        total_var = np.var(y)
        factor_var = np.var(X[:, 1:] @ coeffs[1:])
        specific_var = np.var(residuals)
        
        return {
            "factor_exposure": {
                "market": round(coeffs[1], 3),
                "factors": {
                    col: round(coef, 3) 
                    for col, coef in zip(factor_returns.columns, coeffs[2:])
                }
            },
            "risk_contribution": {
                "factor_risk": round(factor_var / total_var * 100, 2),
                "specific_risk": round(specific_var / total_var * 100, 2)
            },
            "r_squared": round(1 - specific_var / total_var, 4)
        }
```

**VaR 三种方法对比（同一组合结果可能差异明显）**

| 方法 | 假设 | 适用场景 | 优点 | 局限 |
|------|------|---------|------|------|
| 历史模拟法 | 未来分布与历史一致 | 样本充足、分布未知 | 不依赖分布假设 | 依赖历史窗口，肥尾可能漏估 |
| 参数法（正态） | 收益率服从正态分布 | 快速估算、常规监控 | 计算快、易解释 | 低估极端损失 |
| 修正VaR（Cornish-Fisher） | 引入偏度与峰度 | 收益率非正态的市场 | 能反映肥尾特征 | 参数估计误差敏感 |

实践建议：日常监控用历史模拟法，风险报告同时披露修正VaR与CVaR；若三者差异超过30%，须在报告中说明原因。

**示例 1｜组合VaR手算与解读**

- 输入：组合日收益率序列近250个交易日，95%置信度。
- 历史模拟法：取第5百分位收益 = **−2.35%**，即"95%置信度下，单日最大损失约2.35%"。
- 组合规模1000万元 → VaR金额 = 1000万 × 2.35% = **23.5万元**。
- CVaR（超过VaR部分的均值）= **−3.62%** → 金额 **36.2万元**，说明极端日的平均损失比VaR更深。
- 解读要点：VaR回答"最多亏多少（在95%情形下）"，CVaR回答"突破之后平均亏多少"，二者必须同时披露。

**示例 2｜最大回撤解读与恢复期**

| 项目 | 数值 | 说明 |
|------|------|------|
| 最大回撤 | −18.6% | 峰值到谷底跌幅 |
| 峰值日期 | 2026-03-12 | 回撤起点 |
| 谷底日期 | 2026-05-28 | 回撤最深日 |
| 回撤持续天数 | 77天 | 下跌过程时长 |
| 是否已恢复 | 否（当前−9.4%） | 尚未回到前高 |
| 恢复所需时间 | 待观察 | 不应假设"必然恢复" |

解读要点：回撤分析要给出三件事——多深、多久、是否恢复；只报"最大回撤−18.6%"而不说恢复状态会误导持有人。

**风险指标口径登记表（避免跨报告不可比）**

| 指标 | 计算口径 | 频率 | 样本窗口 | 备注 |
|------|---------|------|---------|------|
| 年化波动率 | 日收益率标准差×√244 | 日 | 近1年 | 采用交易日244天 |
| 最大回撤 | 复权净值峰值到谷底 | 日 | 成立以来 | 标注峰值与谷底日期 |
| 夏普比率 | (年化收益−无风险利率)/年化波动率 | 月 | 近1年 | 无风险利率用1年期国债 |
| VaR | 历史模拟法，95% | 日 | 近250日 | 同时披露CVaR |
| 跟踪误差 | 相对基准超额收益标准差 | 周 | 近1年 | 标注基准指数 |

### 2. Stress Testing / 压力测试

```python
class StressTestScenarios:
    """压力测试情景库"""
    
    SCENARIOS = {
        "2015股灾重演": {
            "description": "假设上证指数单周下跌20%",
            "market_shock": -0.20,
            "sector_impacts": {
                "金融": -0.25,
                "房地产": -0.30,
                "消费": -0.15,
                "科技": -0.20,
                "医药": -0.10
            },
            "liquidity_shock": 0.5  # 流动性降至50%
        },
        
        "利率急升": {
            "description": "假设基准利率上调100bp",
            "rate_shock": 0.01,
            "bond_impact": -0.08,
            "equity_impact": -0.10,
            "bank_impact": -0.05
        },
        
        "人民币急贬": {
            "description": "假设USD/CNY一日升值5%",
            "fx_shock": 0.05,
            "export_related": -0.15,
            "import_related": 0.05,
            "domestic_consumer": -0.08
        },
        
        "黑天鹅-新冠": {
            "description": "类似2020年初疫情冲击",
            "market_shock": -0.12,
            "travel": -0.30,
            "retail": -0.20,
            "healthcare": 0.10,
            "online": 0.05
        },
        
        "流动性枯竭-量化踩踏": {
            "description": "成交额萎缩至五成，程序化交易减仓放大波动",
            "market_shock": -0.18,
            "liquidity_shock": 0.5,
            "sector_impacts": {
                "小市值": -0.28,
                "高换手": -0.32,
                "大盘蓝筹": -0.12,
                "红利低波": -0.08
            },
            "correlation_shift": 0.85,
            "notes": "分散化效果在此情景下显著减弱"
        },
        
        "利率下行-资产重定价": {
            "description": "基准利率下调50bp，利率敏感资产重估",
            "rate_shock": -0.005,
            "bond_impact": 0.04,
            "equity_impact": 0.06,
            "bank_impact": -0.03,
            "notes": "债券与红利资产受益，银行净息差承压"
        }
    }
    
    def run_stress_test(self, portfolio: dict, scenario: str) -> dict:
        """执行压力测试"""
        if scenario not in self.SCENARIOS:
            raise ValueError(f"Unknown scenario: {scenario}")
        
        s = self.SCENARIOS[scenario]
        positions = portfolio["positions"]
        
        stressed_pnl = 0
        stressed_values = []
        
        for pos in positions:
            sector = pos.get("sector", "general")
            weight = pos["weight"]
            
            # 根据情景调整
            if "sector_impacts" in s and sector in s["sector_impacts"]:
                shock = s["sector_impacts"][sector]
            else:
                shock = s.get("market_shock", -0.10)
            
            pos_stressed = weight * (1 + shock)
            stressed_values.append(pos_stressed)
            stressed_pnl += weight * shock
        
        total_value = sum(stressed_values)
        portfolio_stress_loss = total_value - 1  # 假设初始为1
        
        return {
            "scenario": scenario,
            "description": s["description"],
            "portfolio_loss": round(portfolio_stress_loss * 100, 2),
            "portfolio_value_after": round(total_value * 100, 2),
            "position_impacts": [
                {"name": pos["name"], "weight": pos["weight"], 
                 "shock": round(shock * 100, 2), "impact": "loss" if shock < 0 else "gain"}
                for pos, shock in zip(positions, 
                    [s.get("sector_impacts", {}).get(pos.get("sector", ""), 
                     s.get("market_shock", -0.10)) for pos in positions])
            ]
        }
```

**情景结果对照表（一次跑完所有情景，横向比较）**

| 情景 | 组合冲击 | 最受伤资产 | 相对受益资产 | 触发动作 |
|------|---------|-----------|------------|---------|
| 2015股灾重演 | −21.5% | 房地产、金融 | 医药 | 降仓、暂停加仓 |
| 利率急升100bp | −9.2% | 债券、权益、银行 | 现金类 | 缩短久期 |
| 人民币急贬5% | −7.8% | 进口相关、消费 | 出口相关 | 核查外汇敞口 |
| 黑天鹅-新冠 | −12.6% | 交运、零售 | 医药、线上 | 按行业再平衡 |
| 流动性枯竭-量化踩踏 | −19.4% | 小市值、高换手 | 红利低波 | 优先减仓低流动性标的 |
| 利率下行50bp | +4.1% | 银行 | 债券、红利资产 | 适度提升久期 |

**示例 1｜压力测试后的处置清单**

| 优先级 | 处置动作 | 触发条件 | 责任人 | 时限 |
|-------|---------|---------|-------|------|
| 1 | 降低整体仓位至60%以下 | 任一情景损失>15% | 投资经理 | T+1 |
| 2 | 减仓流动性最差标的 | 流动性情景损失>威胁阈值 | 交易 | T+1 |
| 3 | 暂停同向新增买入 | 集中度超限 | 投资经理 | 即时 |
| 4 | 补充现金缓冲 | 组合现金<5% | 投资经理 | T+2 |
| 5 | 出具情景专项说明 | 任一情景损失>10% | 风控 | T+3 |

**示例 2｜压力测试阈值设定（把结果变成规则）**

| 指标 | 正常区间 | 预警线 | 处置线 |
|------|---------|-------|-------|
| 单情景最大损失 | <10% | 10%-15% | >15% |
| 组合年化波动率 | <18% | 18%-25% | >25% |
| 单标的权重 | <10% | 10%-15% | >15% |
| 单一行业权重 | <25% | 25%-35% | >35% |
| 前三大标的合计 | <30% | 30%-40% | >40% |
| 压力情景下相关性 | <0.5 | 0.5-0.7 | >0.7 |

### 3. Risk Contribution Analysis / 风险贡献分析

```python
    def risk_contribution_by_asset(self) -> dict:
        """计算各资产风险贡献"""
        cov_matrix = self.returns.cov()
        portfolio_vol = np.sqrt(self.weights @ cov_matrix.values @ self.weights)
        
        # 边际风险贡献 (MCTR)
        mctr = (cov_matrix.values @ self.weights) / portfolio_vol
        
        # 风险贡献
        risk_contrib = self.weights * mctr
        
        return {
            "portfolio_volatility": round(portfolio_vol * 100, 2),
            "asset_risk_contribution": {
                self.returns.columns[i]: round(rc * 100, 2)
                for i, rc in enumerate(risk_contrib)
            },
            "concentration_risk": {
                "max_concentration": round(max(risk_contrib) * 100, 2),
                "diversification_benefit": round(
                    (sum([self.returns[col].std() * w 
                         for col, w in zip(self.returns.columns, self.weights)]) - 
                     portfolio_vol) * 100, 2)
            }
        }
```

**示例 1｜权重与风险贡献的错位（最容易忽视的风险）**

| 资产 | 权重 | 波动率 | 风险贡献 | 权重-风险差 | 结论 |
|------|------|-------|---------|-----------|------|
| 股票A | 30% | 32% | 42% | −12pct | 风险贡献显著高于权重，需减配 |
| 股票B | 20% | 20% | 14% | +6pct | 风险效率较高 |
| 债券C | 40% | 6% | 9% | +31pct | 起到稳定器作用 |
| 黄金ETF | 10% | 15% | 6% | +4pct | 分散化贡献明显 |
| **组合** | 100% | — | 71%（含相关项） | — | 组合波动率 14.2% |

解读要点：权重高不等于风险高——上例中权重30%的股票A贡献了42%的组合风险，是真正需要关注的对象；风险报告应同时展示权重与风险贡献两列，避免只看权重做决策。

**示例 2｜分散化效果评估**

| 场景 | 加权平均波动率 | 组合波动率 | 分散化收益 | 判断 |
|------|-------------|----------|-----------|------|
| 常态市场 | 18.5% | 14.2% | 4.3pct | 分散化有效 |
| 相关性上浮至0.7 | 18.5% | 17.1% | 1.4pct | 效果显著减弱 |
| 相关性上浮至0.85（踩踏情景） | 18.5% | 18.2% | 0.3pct | 几乎失效 |

解读要点：分散化在极端行情下会被显著削弱，"平时低相关"不能作为风险控制的唯一依据；报告须同时给出常态与压力情景下的分散化收益对比。

**示例 3｜风险预算分配（把风险额度当成资源）**

| 资产类别 | 风险预算 | 实际风险贡献 | 偏离 | 调整动作 |
|---------|---------|------------|-----|---------|
| 权益 | 50% | 71% | +21pct | 减配，或增加低波动品种 |
| 固收 | 30% | 18% | −12pct | 可适度提升久期 |
| 商品/黄金 | 10% | 6% | −4pct | 保持 |
| 现金 | 10% | 5% | −5pct | 保持 |

使用要点：风险预算与实际贡献偏离超过10pct即需调整；调整时应优先通过降低高波动资产权重实现，而非简单增加杠杆。

---

## Quick Command Templates / 快速指令模板

**组合风险评估：**
```
分析以下组合的风险：
- 总规模：1000万
- 持仓：[股票A 30%, 股票B 20%, 债券B 50%]
- 置信度：95%
```

**压力测试：**
```
执行"2015股灾重演"情景压力测试
```

**多情景横向比较：**
```
对以下组合跑全部压力情景，输出情景损失对照表、
最受伤资产、待触发处置动作与优先级：
- 持仓：[标的与权重]
- 组合规模：[X]万
```

**风险贡献与预算：**
```
计算以下组合各资产的风险贡献与风险预算偏离，
给出单标的≤15%、单行业≤35%的集中度检查结果与调整建议。
```

---

## Disclaimer

This skill provides risk analysis tools for educational purposes. Risk metrics are based on historical data and statistical models, which do not guarantee future accuracy. Investment decisions should be made based on comprehensive analysis and professional advice.
