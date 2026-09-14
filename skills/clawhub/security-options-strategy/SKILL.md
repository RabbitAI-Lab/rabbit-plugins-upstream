---
name: Options Strategy Master
slug: security-options-strategy
description: AI-powered options strategy master for China market — covers options pricing, Greeks calculation, strategy analysis (covered call, protective put, spreads, straddles), and volatility trading. Built for options traders and risk managers. Keywords: options strategy, options pricing, Greeks, volatility trading, China options, covered call, protective put, iron condor, 50ETF期权, 沪深300期权, 期权策略, 波动率交易, BS定价, Delta, Gamma, Vega, Theta, 期权组合, 备兑开仓, 保护性看跌.
version: "3.0.2"
---

# Options Strategy Master / 期权策略大师

> **English:** AI-powered options strategy master — covers options pricing, Greeks calculation, multi-leg strategies, and volatility trading. Built for options traders and risk managers.
>
> **中文:** 期权策略大师——覆盖期权定价、Greeks计算、多腿策略分析、波动率交易。适用：期权交易者、风险管理人。

---


### 证券监管最新动态 [2026-09-13更新]

| 动态类型 | 内容摘要 | 影响范围 | 交易/风控侧应对动作 | 优先级 |
|---------|---------|---------|-----------------|-------|
| 程序化交易 | 程序化交易报告与异常交易监控要求持续落地，期权策略的自动化报单需纳入报送口径 | 策略执行与报备流程 | 策略上线前登记报备信息，保留参数取值与触发条件说明 | 高 |
| 持仓限额 | 交易所对期权持仓限额与大户报告执行趋严 | 多腿组合与义务仓规模 | 组合建仓前测算单合约/单账户限额占用 | 高 |
| 保证金管理 | 极端行情下交易所可动态调整保证金比例 | 义务仓与卖出价差策略 | 按保证金比例上浮 20%/35%/50% 三档情景预留资金 | 高 |
| 投资者适当性 | 期权权限分级（一级/二级/三级）需与策略动作严格匹配 | 客户开户与策略推荐 | 推荐策略前核验权限等级与交易经验 | 高 |
| 量化共振 | A股量化资金占比维持高位，期权对冲与现货量化存在联动 | 波动率结构与基差 | 建立量化资金流与 IV 的联动观察指标 | 中 |
| 波动率制度 | 场内期权做市与品种机制持续完善，曲面结构变化加快 | 波动率交易与套利研究 | 每周更新曲面快照，跟踪偏斜结构漂移 | 中 |

> **数据截止**: 2026-09-13 | 来源：证监会、沪深交易所、中证协、行业公开信息
> **声明**: 以上动态供参考，具体以官方最新发布为准

**动态解读示例（两类高频场景）**

- **场景A｜义务仓保证金预留不足**：某账户卖出宽跨式，按常态保证金率测算占用 12 万元并接近满仓建仓；交易所因波动率抬升将保证金比例上浮 30% → 追加保证金缺口约 3.6 万元，触发被动平仓。**改进动作**：建仓前按"保证金上浮 20%/35%/50%"三档情景测算，常态占用控制在可用资金的 60% 以内。
- **场景B｜适当性权限错配**：客户仅有一级权限（备兑开仓/买入开仓），业务人员却按"卖出开仓"设计策略 → 委托被拒并触发适当性核查。**改进动作**：策略推荐前先做"权限等级 × 策略动作"匹配检查（见下方权责矩阵）。

## Industry Pain Points / 行业痛点

| Pain Point / 痛点 | Impact / 影响 | Solution / 本Skill解决方案 | 量化基线（示例） | 责任岗 |
|------------------|-------------|------------------------|---------------|-------|
| **定价复杂** | BS 模型参数选择困难，理论价与市场价偏差大 | 参数解释+敏感性分析 | 理论价与市场价偏差 ≤1.5% 视为可接受 | 量化研究 |
| **希腊字母难懂** | Delta/Gamma/Vega 混淆，对冲比例算错 | 可视化 Greeks 图形 | 组合 \|Delta\| ≤5%，Gamma 集中度可控 | 交易员 |
| **策略选择困难** | 不知道用什么策略应对当前市场 | 情景化策略推荐 | 按"方向 × IV 分位"二维矩阵择策略 | 投资经理 |
| **保证金占用** | 资金效率低，极端行情被追保 | 最优保证金管理 | 常态保证金占用 ≤可用资金 60% | 风控 |
| **风险敞口不清晰** | 极端行情爆仓，回撤失控 | 实时风险监控+预警 | 单策略最大亏损 ≤账户权益 3% | 风控 |
| **权限与适当性错配** | 推荐策略超出客户权限，委托被拒 | 权限等级×策略动作匹配检查 | 建仓前 100% 完成权限核验 | 合规/运营 |
| **组合限额不清** | 多腿跨合约占用，超限被动减仓 | 单合约/单账户限额测算表 | 单合约持仓 ≤限额 80% | 交易/风控 |

**策略权责矩阵（示例）**

| 环节 | 输出物 | 责任岗 | 复核岗 | 留痕要求 |
|-----|-------|-------|-------|---------|
| 参数确定 | 无风险利率、波动率、分红率取值说明 | 量化研究 | 投资经理 | 参数来源与取值日期 |
| 策略选择 | 策略建议书（含适用行情、最大亏损、盈亏比） | 投资经理 | 风控 | 建议书版本号 |
| 下单前检查 | 权限、限额、保证金"三查"记录 | 交易员 | 合规 | 三查签字或系统日志 |
| 持仓监控 | Greeks 与保证金日报 | 风控 | 部门负责人 | 异常处置记录 |
| 到期处理 | 行权/放弃/平仓决议 | 交易员 | 风控 | 决议留档 |

---

## Trigger Keywords / 触发关键词

**English Triggers:** options strategy, options pricing, Greeks, volatility trading, China options, covered call, protective put, spread trading, straddles, collars

**中文触发词（优先）：** 期权策略 / 期权定价 / 希腊字母 / Delta / Gamma / Vega / 备兑开仓 / 保护性看跌 / 价差策略 / 跨式策略 / 勒式策略 / 波动率交易 / 50ETF期权 / 沪深300期权 / 期权开户 / 期权权限 / 权利仓 / 义务仓 / 做市商 / 波动率曲面

---

## Core Capabilities / 核心能力

### 1. Options Pricing Engine / 期权定价引擎

```python
import numpy as np
from scipy.stats import norm

class OptionsPricer:
    """期权定价引擎"""
    
    @staticmethod
    def black_scholes(S, K, T, r, sigma, option_type='call'):
        """
        Black-Scholes期权定价
        Args:
            S: 标的资产价格
            K: 行权价
            T: 到期时间（年）
            r: 无风险利率
            sigma: 波动率
            option_type: 'call' 或 'put'
        """
        if T <= 0:
            if option_type == 'call':
                return max(S - K, 0)
            else:
                return max(K - S, 0)
        
        d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
        d2 = d1 - sigma * np.sqrt(T)
        
        if option_type == 'call':
            price = S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
            delta = norm.cdf(d1)
        else:
            price = K * np.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)
            delta = norm.cdf(d1) - 1
        
        # Greeks计算
        gamma = norm.pdf(d1) / (S * sigma * np.sqrt(T))
        vega = S * norm.pdf(d1) * np.sqrt(T) / 100  # 每1%波动率变化
        theta_call = (-S * norm.pdf(d1) * sigma / (2 * np.sqrt(T)) - 
                     r * K * np.exp(-r * T) * norm.cdf(d2)) / 365
        theta_put = (-S * norm.pdf(d1) * sigma / (2 * np.sqrt(T)) + 
                    r * K * np.exp(-r * T) * norm.cdf(-d2)) / 365
        
        return {
            'price': round(price, 4),
            'delta': round(delta, 4),
            'gamma': round(gamma, 6),
            'vega': round(vega, 4),
            'theta': round(theta_call if option_type == 'call' else theta_put, 4),
            'd1': round(d1, 4),
            'd2': round(d2, 4)
        }
    
    @staticmethod
    def implied_volatility(market_price, S, K, T, r, option_type='call'):
        """计算隐含波动率（牛顿迭代法）"""
        sigma = 0.3  # 初始猜测
        
        for _ in range(100):
            bs_price = OptionsPricer.black_scholes(S, K, T, r, sigma, option_type)['price']
            vega = OptionsPricer.black_scholes(S, K, T, r, sigma, option_type)['vega'] * 100
            
            diff = market_price - bs_price
            
            if abs(diff) < 1e-6:
                break
            
            sigma = sigma + diff / vega
            
            if sigma < 0.01 or sigma > 5:
                return None
        
        return round(sigma * 100, 2)  # 返回百分比
```

#### 1.1 Worked Example / 定价结果解读示例

**输入**：50ETF 现价 2.800 元，行权价 2.850 元，剩余 30 天，无风险利率 1.80%，波动率 20%，看涨期权。

| 输出项 | 示例取值 | 含义 | 解读要点 |
|-------|---------|------|---------|
| price | 0.0256 | BS 理论价 | 与市场价偏差 >1.5% 需回查参数口径 |
| delta | 0.3892 | 标的价格每涨 1 元，期权价约涨 0.39 元 | 也可近似读作"到期为实值的概率" |
| gamma | 2.4103 | Delta 随标的变化的速率 | 平值附近最大，临近到期急剧放大 |
| vega | 0.0031 | 波动率每升 1 个百分点引起权利金变化 | 30 天短期期权 Vega 通常偏小 |
| theta | −0.0018 | 每日时间损耗 | 买方注意：横盘也在亏钱 |
| d1 / d2 | 0.0854 / 0.0160 | 中间变量 | 可用于核对计算是否出错 |

**手算校验（供复核使用）**：d1 = [ln(2.800/2.850) + (0.018 + 0.5×0.2²)×(30/365)] ÷ (0.2×√(30/365)) ≈ 0.085；d2 = d1 − 0.2×√(30/365) ≈ 0.016。若 d1、d2 符号与预期相反，最常见原因是利率被误填为百分数（应为 0.018 而不是 1.8）。

**参数敏感性对照（其他条件不变）**

| 变量变动 | 看涨期权理论价 | 变化幅度 | 提示 |
|---------|-------------|---------|------|
| 波动率 20% → 25% | 0.0256 → 0.0316 | +23.4% | 波动率对短期期权定价影响显著 |
| 剩余期限 30 → 60 天 | 0.0256 → 0.0389 | +52.0% | 时间价值大致随 √T 增长 |
| 标的价格 2.800 → 2.850 | 0.0256 → 0.0421 | +64.5% | 平值处 Delta 约 0.5，价格弹性最大 |
| 无风险利率 1.8% → 3.0% | 0.0256 → 0.0276 | +7.8% | 利率因素对短期期权影响相对最小 |

#### 1.2 Implied Volatility Edge Cases / 隐含波动率求解的常见失败情形

| 情形 | 现象 | 原因 | 处理方式 |
|-----|------|------|---------|
| 迭代不收敛 | 返回 None，sigma 跑出区间 | 市场价严重偏离理论价（深度实值或临近到期） | 改用二分法，或直接标记为异常报价 |
| 深度实值合约 IV 异常高 | 30 天深实值看涨 IV 报 45% | 流动性差，买卖价差在权利金中占比过高 | 用买价与卖价分别求 IV，取区间中值 |
| 临近到期 IV 剧烈跳动 | 剩余 2 天合约 IV 单日 +15pp | 时间极短，标的小幅波动即放大 IV | 剔除剩余 ≤3 天的合约后再算曲面 |
| 同日结果不一致 | 同一合约两个 IV | 无风险利率口径不同（1.8% vs 3.0%） | 曲面计算统一利率口径并记录取值日期 |

**示例**：某 50ETF 看涨期权市场价 0.0300 元，BS 理论价 0.0256 元 → 反解出的隐含波动率约 23.1%，高于当前 20% 的参考波动率约 3.1 个百分点，说明市场为该合约定价了额外的波动率溢价（解读时应同时检查当日是否有事件驱动）。

### 2. Options Strategy Analysis / 期权策略分析

```python
class OptionsStrategy:
    """期权策略分析"""
    
    STRATEGIES = {
        "covered_call": {
            "name": "备兑开仓",
            "description": "持有标的+卖出看涨期权",
            "use_case": "预期横盘/小幅上涨，想增加收益",
            "max_profit": "股价 - 行权价 + 权利金",
            "max_loss": "无限（理论上）"
        },
        "protective_put": {
            "name": "保护性看跌",
            "description": "持有标的+买入看跌期权",
            "use_case": "担心下跌，想锁定损失",
            "max_profit": "无限",
            "max_loss": "行权价 - 股价 + 权利金"
        },
        "bull_call_spread": {
            "name": "牛市看涨价差",
            "description": "买入低行权价看涨+卖出高行权价看涨",
            "use_case": "看涨但涨幅有限",
            "max_profit": "行权价差 - 净权利金",
            "max_loss": "净权利金"
        },
        "bear_put_spread": {
            "name": "熊市看跌价差",
            "description": "买入高行权价看跌+卖出低行权价看跌",
            "use_case": "看跌但跌幅有限",
            "max_profit": "行权价差 - 净权利金",
            "max_loss": "净权利金"
        },
        "straddle": {
            "name": "跨式策略",
            "description": "同时买入同行权价的看涨+看跌",
            "use_case": "预期大幅波动但方向不明",
            "max_profit": "无限（上涨）或标的 - 行权价（下跌）",
            "max_loss": "两倍权利金"
        },
        "strangle": {
            "name": "勒式策略",
            "description": "买入高行权价看涨+低行权价看跌",
            "use_case": "预期大幅波动但方向不明（成本低于跨式）",
            "max_profit": "无限",
            "max_loss": "两倍权利金"
        },
        "iron_condor": {
            "name": "铁鹰策略",
            "description": "卖出价差+买入更宽价差保护",
            "use_case": "预期标的在一定范围内波动",
            "max_profit": "净权利金",
            "max_loss": "两个价差幅度 - 净权利金"
        }
    }
    
    def analyze_strategy(self, strategy_name: str, 
                        underlying_price: float,
                        params: dict) -> dict:
        """分析策略损益"""
        if strategy_name not in self.STRATEGIES:
            return {"error": "未知策略"}
        
        strategy = self.STRATEGIES[strategy_name]
        analysis = {
            "strategy": strategy["name"],
            "description": strategy["description"],
            "use_case": strategy["use_case"]
        }
        
        # 计算不同标的价格下的盈亏
        price_range = np.linspace(
            underlying_price * 0.7,
            underlying_price * 1.3,
            100
        )
        
        pnl_curve = self._calculate_pnl(strategy_name, price_range, params)
        
        # 关键指标
        breakeven = self._find_breakeven(pnl_curve, price_range)
        max_profit = self._find_max_profit(pnl_curve, price_range)
        max_loss = self._find_max_loss(pnl_curve, price_range)
        
        return {
            **analysis,
            "breakeven": round(breakeven, 2),
            "max_profit": round(max_profit, 2),
            "max_loss": round(max_loss, 2),
            "profit_table": {
                "大幅下跌(-20%)": round(self._pnl_at_price(strategy_name, 
                    underlying_price * 0.8, params), 2),
                "小幅下跌(-10%)": round(self._pnl_at_price(strategy_name, 
                    underlying_price * 0.9, params), 2),
                "横盘(0%)": round(self._pnl_at_price(strategy_name, 
                    underlying_price, params), 2),
                "小幅上涨(+10%)": round(self._pnl_at_price(strategy_name, 
                    underlying_price * 1.1, params), 2),
                "大幅上涨(+20%)": round(self._pnl_at_price(strategy_name, 
                    underlying_price * 1.2, params), 2)
            }
        }
```

#### 2.1 Strategy Selection Matrix / 策略选择矩阵

| 市场观点 | IV 分位 <20%（偏便宜） | IV 分位 20%-80%（中性） | IV 分位 >80%（偏贵） |
|---------|--------------------|---------------------|------------------|
| 明确看涨 | 买入看涨 / 牛市看涨价差 | 牛市看涨价差 | 卖出看跌价差 |
| 温和看涨 | 备兑开仓 | 备兑开仓 | 卖出看跌价差 |
| 看横盘 | 卖出宽跨式（须留足保证金） | 铁鹰策略 | 铁鹰策略 |
| 温和看跌 | 熊市看跌价差 | 熊市看跌价差 | 卖出看涨价差 |
| 明确看跌 | 买入看跌 / 熊市看跌价差 | 保护性看跌 | 保护性看跌 |
| 方向不明、预期大幅波动 | 买入跨式 / 勒式 | 买入勒式 | 暂不建仓，等 IV 回落 |

> **使用规则**：先按"方向"锁定行，再按"IV 分位"锁定列。IV 分位应对同一合约近 250 个交易日的历史序列计算，而非用全市场平均波动率代替。

#### 2.2 Multi-leg Parameter Comparison / 多腿策略参数对照（示例）

| 策略 | 腿数 | 净权利金方向 | 保证金占用 | 最大亏损 | 适用 IV 环境 |
|-----|-----|-----------|-----------|---------|------------|
| 备兑开仓 | 2 | 收取 | 现货端已占用，期权端不额外占用 | 标的跌至 0（现货端亏损） | IV 偏高 |
| 保护性看跌 | 2 | 支出 | 现货端已占用 | 行权价差 + 权利金 | IV 偏低 |
| 牛市看涨价差 | 2 | 支出 | 买方结构，无义务仓保证金 | 净权利金 | 任意 |
| 熊市看跌价差 | 2 | 支出 | 买方结构，无义务仓保证金 | 净权利金 | 任意 |
| 买入跨式 / 勒式 | 2 | 支出 | 买方结构，无义务仓保证金 | 两腿权利金合计 | IV 偏低 |
| 铁鹰策略 | 4 | 收取 | 按卖出腿价差差额计 | 价差宽度 − 净权利金 | IV 偏高 |

#### 2.3 P&L Table Reading / 损益表解读示例

**输入**：标的现价 2.900 元；牛市看涨价差，买入行权价 3.000 元（权利金 0.0500），卖出行权价 3.200 元（权利金 0.0200）；净支出 0.0300 元。

| 情景 | 到期标的价 | 组合到期价值 | 单组盈亏 | 解读 |
|-----|----------|-----------|--------|------|
| 大幅下跌 −20% | 2.320 | 0 | −0.0300 | 亏损封顶于净权利金，继续下跌不再扩大 |
| 小幅下跌 −10% | 2.610 | 0 | −0.0300 | 两腿均为虚值，全部权利金损失 |
| 横盘 0% | 2.900 | 0 | −0.0300 | 未突破低行权价，仍为最大亏损 |
| 小幅上涨 +10% | 3.190 | 0.1900 | +0.1600 | 接近高行权价，收益趋近上限 |
| 大幅上涨 +20% | 3.480 | 0.2000 | +0.1700 | 已达最大盈利，再涨不再增加 |

- **盈亏平衡点** = 3.000 + 0.0300 = 3.0300 元（标的需上涨约 4.5% 才开始盈利）。
- **最大盈利** = (3.200 − 3.000) − 0.0300 = 0.1700 元；**盈亏比** ≈ 5.7 : 1。
- **常见误读**：把"最大盈利 0.1700 元"读成"收益率 170%"，实际应以净支出 0.0300 元为分母计算收益率，且须说明该收益需持有至到期并满足标的价格条件才成立。
- **选择提示**：若预期涨幅仅 3%，该结构难以覆盖盈亏平衡点，可考虑改用更低行权价组合或直接买入看涨。

### 3. Volatility Trading / 波动率交易

#### 3.1 Framework / 波动率交易框架

| 步骤 | 输入 | 输出 | 判断依据 |
|-----|------|------|---------|
| 1. 求 IV 曲面 | 各合约市场价、标的价、剩余期限、利率 | 各行权价隐含波动率曲线 | 剔除剩余 ≤3 天与当日无成交合约 |
| 2. 算 IV 分位 | 同合约近 250 个交易日 IV 序列 | IV Rank / IV Percentile | >80% 偏贵，<20% 偏便宜 |
| 3. 看偏斜结构 | 虚值看跌 IV 与平值 IV 之差 | Skew 值 | 负偏斜扩大说明尾部避险需求上升 |
| 4. 对比已实现波动率 | 标的近 20/60 日已实现波动率 | IV − RV 差值 | 差值 >5pp 时可研究卖出波动率结构 |
| 5. 决策与风控 | 上述指标 + 保证金余量 | 交易或等待 | 保证金占用超阈值则放弃，不做例外 |

#### 3.2 Volatility Smile Analysis / 波动率微笑分析

```python
def analyze_volatility_smile(option_chain: dict) -> dict:
    """
    分析波动率微笑曲面，识别相对高估/低估的合约（供研究参考）
    输入 option_chain: {行权价: 市场价}
    """
    # 计算各行权价的隐含波动率
    iv_curve = {
        strike: calculate_iv(option_price, spot, strike, days_to_expiry, r)
        for strike, option_price in option_chain.items()
    }
    
    # 波动率偏斜分析
    atm_iv = iv_curve[get_atm_strike(spot)]
    skew = {
        otm_put_10: atm_iv - iv_curve[otm_put_10],
        otm_call_10: iv_curve[otm_call_10] - atm_iv
    }
    
    return {
        "iv_curve": iv_curve,
        "atm_volatility": round(atm_iv, 2),
        "skew": skew,
        "iv_rank": compute_iv_rank(atm_iv, iv_history_250d),
        "rv_gap": round(atm_iv - realized_vol_20d, 2),
        "reading": "IV 偏高，研究卖出波动率结构" if iv_rank > 80
                   else ("IV 偏低，研究买入波动率结构" if iv_rank < 20
                         else "IV 中性，暂不做波动率方向性判断")
    }
```

#### 3.3 Reading Examples / 曲面结果解读示例（三类典型形态）

| 曲面形态 | IV Rank | Skew（虚值看跌 IV − 平值 IV） | IV − RV | 解读 | 研究方向（示例） |
|---------|---------|--------------------------|---------|------|-------------|
| 平坦型 | 45%（中位） | −1.2pp（轻微负偏） | +0.8pp | 市场定价中性，无显著错价 | 不交易波动率，回归方向性策略 |
| 陡峭负偏 | 72%（偏高） | −6.5pp（避险需求旺） | +4.1pp | 尾部保护被抢贵，整体 IV 抬升 | 研究买入看跌价差替代直接买保险 |
| 双峰型 | 88%（高位） | 虚值看涨 IV 反超平值 3pp | +9.3pp | 情绪推动上端 IV 虚高 | 研究卖出虚值看涨的价差结构 |

**示例测算**：平值 IV 24.5%，标的近 20 日已实现波动率 15.2%，差值 +9.3pp；同合约 IV Rank 88% → 结论为"波动率定价偏贵"，可研究卖出波动率结构，但须同步确认两点：① 保证金占用是否 ≤60%；② 未来两周是否有政策会议、指数调仓等可能推高实际波动的事件。

#### 3.4 Common Misreadings / 三类常见误读

- **把高 IV 当成"必跌"**：IV 高只说明市场为不确定性付费，不指示方向；卖出波动率在单边趋势中会连续亏损。
- **只看平值 IV 做决策**：曲面偏斜往往比平值 IV 更有信息量；负偏斜扩大时单纯卖出平值期权，风险收益并不对称。
- **忽略期限匹配**：用 20 日已实现波动率去对比 90 天期权的 IV 会系统性失真，两者期限应大体一致（如 20 日 RV 对近月合约、60 日 RV 对季月合约）。

---

## Quick Command Templates / 快速指令模板

**期权定价：**
```
计算50ETF期权定价：
- 标的价格：2.8元
- 行权价：2.85元
- 到期日：30天后
- 波动率：20%
- 类型：看涨期权
```

**分析策略：**
```
分析牛市看涨价差策略：
- 买入行权价：3.0元，权利金：0.05元
- 卖出行权价：3.2元，权利金：0.02元
- 标的现价：2.9元
```

**波动率曲面分析：**
```
分析当前50ETF期权波动率曲面：
- 标的现价：2.800元
- 合约序列：行权价 2.70/2.75/2.80/2.85/2.90/2.95，剩余 30 天
- 需要输出：IV 曲线、平值 IV、偏斜值、近 250 日 IV 分位、与 20 日已实现波动率的差值
- 同时给出是否存在相对高估/低估合约的提示
```

**组合 Greeks 汇总：**
```
汇总以下组合的 Greeks 敞口：
- 持有 50ETF 现货 10000 份
- 卖出 3.000 行权价看涨 10 张（剩 30 天）
- 买入 2.700 行权价看跌 5 张（剩 30 天）
需要输出：组合 Delta / Gamma / Vega / Theta，并说明 Delta 是否落在 ±5% 目标区间内
```

**压力情景测算：**
```
对上述组合做压力情景测算：
1. 标的 −10%、IV +8pp
2. 标的 −5%、IV +4pp
3. 标的持平、IV −5pp（注意 Theta）
4. 标的 +5%、IV −3pp
每档输出预估损益与保证金占用变化，并标注是否需要追加保证金
```

---

## Risk Control Checklist / 风控与合规检查清单

| 检查项 | 依据/说明 | 通过标准 |
|-------|---------|---------|
| 交易权限核验 | 期权权限分级与策略动作需匹配 | 权限等级覆盖策略全部腿 |
| 适当性匹配 | 客户风险等级与产品风险等级一致 | 无越级推荐 |
| 持仓限额测算 | 单合约、单账户与组合限额 | 建仓后占用 ≤限额 80% |
| 保证金压力测算 | 按比例上浮 20%/35%/50% 三档 | 三档情景下均无需追保 |
| 最大亏损约束 | 单策略最大亏损 | ≤账户权益 3% |
| Greeks 敞口监控 | Delta/Gamma/Vega/Theta 日报 | 敞口处于预设阈值内 |
| 参数与决议留痕 | 参数来源、策略建议书、下单前检查记录 | 全流程可回溯 |
| 免责表述 | 研究结果仅供参考，不构成投资建议 | 每份输出均含声明 |

---

## Disclaimer

Options trading involves substantial risk and is not suitable for all investors. Losses can exceed initial investment. This skill is for educational purposes only and does not constitute investment advice.
