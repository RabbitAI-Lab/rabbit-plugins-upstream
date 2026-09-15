---
name: AI-Powered Stock Selection Engine
slug: security-stock-screening
description: AI-powered intelligent stock selection engine for China A-share market — covers quantitative factor screening, fundamental analysis ranking, technical signal detection, sector rotation analysis, and portfolio construction. Built for retail investors, fund managers, and quantitative analysts. Updated 2026 with latest factor models, short-seller vulnerability detection, and AI-enhanced stock screening. Keywords: stock selection, quantitative screening, factor investing, technical analysis, China A-share, stock picker, AI investing, 选股引擎, 量化选股, 因子投资, 技术分析, A股, 智能选股, 选股策略, 量化策略, AI选股, 股票筛选, 价值投资, 成长股, 短线选股.
version: "3.0.2"
---

# AI-Powered Stock Selection Engine / 智能选股引擎

> **English:** AI-powered intelligent stock selection engine for China A-share market — combines quantitative factor screening, fundamental analysis, technical signals, and sector rotation analysis. Solves pain points: information overload, emotional decision-making, and inconsistent stock picking criteria. Built for investors and analysts at all levels.
>
> **中文:** 智能选股引擎——整合量化因子筛选、基本面分析、技术信号检测、行业轮动分析的全流程选股工具。解决痛点：信息过载、情绪化决策、选股标准不统一。适用：各级投资者、基金经理、量化分析师。

---


### 证券监管最新动态 [2026-09-12更新]

| 动态类型 | 内容摘要 | 影响范围 | 选股侧应对动作 | 责任岗 | 优先级 |
|---------|---------|---------|--------------|-------|-------|
| 证券监管 | 2026年A股量化资金占比30%-40%，选股模型需考虑量化冲击 | 选股引擎需增加量化冲击识别和极端行情风控 | 模型输出附带流动性冲击提示与成交结构说明 | 研究 | 高 |
| 证券监管 | 2026年3月23日量化踩踏案例（单日蒸发4.29万亿），风控需加强 | 选股引擎需增加量化冲击识别和极端行情风控 | 引入集中度与拥挤度指标，作为风控前置条件 | 研究 | 高 |
| 证券监管 | 上证周线级别中枢震荡，2026年核心区间3200-4000点 | 选股引擎需增加量化冲击识别和极端行情风控 | 震荡区间内降低趋势类因子权重 | 研究 | 中 |
| 程序化交易 | 程序化交易报告与异常交易监控要求细化 | 与量化资金相关的流动性与波动分析 | 在流动性评估中单独列示程序化交易影响 | 研究 | 中 |
| 信息披露 | 财务信息披露质量监管持续强化 | 财报异常检测、因子取数 | 因子取数须标注报告期与公告编号 | 研究 | 高 |
| 市值管理 | 上市公司市值管理行为披露要求趋严 | 涉及回购、增减持的个股筛选 | 筛选中单列股东行为事件标签 | 研究 | 中 |
| 业绩预告 | 业绩预告披露质量受关注 | 事件驱动类选股 | 使用预告数据时区分预告口径与实际口径 | 研究 | 高 |
| 投资者保护 | 投顾与荐股类内容传播边界收紧 | 选股结果对外输出 | 输出结果保留风险提示与免责声明 | 合规 | 高 |

> **数据截止**: 2026-09-12 | 来源：证监会、交易所公开规则、行业公开信息
> **声明**: 以上动态供参考，具体以官方最新发布为准

**动态解读示例（四类高频场景）**

- **场景A｜量化冲击识别**：某标的近20日成交额中位数仅0.8亿元，模型给出买入信号 → 命中"流动性冲击"风险 → 输出中增加"预估冲击成本"，并提示单笔建仓不超过日均成交额的5%。
- **场景B｜拥挤度预警**：某板块因子暴露高度集中、机构持仓占比快速抬升 → 命中"踩踏风险" → 在风控前置条件中加入拥挤度阈值，超阈值则降低该板块权重。
- **场景C｜因子取数可追溯**：ROE取数未标注报告期 → 命中"取数须可追溯" → 因子表增加"报告期"与"公告编号"两列，便于回溯与复算。
- **场景D｜预告口径混用**：用业绩预告中值直接作为当年利润因子 → 命中"预告与实际口径混用" → 预告期数据单列"预告口径"标记，与实际披露数据分栏展示。

## Industry Pain Points / 行业痛点

| Pain Point / 痛点 | Impact / 影响 | Solution / 本Skill解决方案 | 量化基线指标 / Baseline |
|------------------|-------------|------------------------|----------------------|
| **信息过载** | A股5000+股票，无法逐一研究 | 多维度因子筛选，快速缩小范围 | 一次筛选候选池 ≤50只 |
| **情绪化决策** | 追涨杀跌，高买低卖 | 量化标准选股，避免主观干扰 | 交易决策中规则触发占比 ≥80% |
| **选股标准模糊** | 没有系统性方法论 | 完整选股框架+评分模型 | 每条选股逻辑可量化复现 |
| **财报造假风险** | 康美药业、瑞幸等案例警示 | 财报异常信号检测+预警 | 高风险标的排除率 100% |
| **行业轮动难把握** | 踏错节奏，板块轮动踏空 | 宏观+情绪+资金三维轮动模型 | 轮动判断命中率 ≥60% |
| **流动性陷阱** | 小市值标的无法顺利进出 | 流动性门槛+冲击成本估算 | 单笔建仓 ≤日均成交额5% |
| **拥挤度风险** | 机构持仓过度集中引发踩踏 | 拥挤度指标与阈值监控 | 超阈值板块权重自动下调 |
| **样本外失效** | 因子在样本内有效、样本外失效 | 分区间验证与滚动检验 | 样本外IC保持同向 ≥60%窗 |

---

## Trigger Keywords / 触发关键词

**English Triggers:** stock selection, quantitative screening, factor investing, fundamental analysis, technical analysis, China A-share, stock picker, AI investing, momentum stocks, value investing, growth stocks, sector rotation, portfolio construction

**中文触发词（优先）：** 选股 / 智能选股 / 量化选股 / 因子选股 / 基本面选股 / 技术面选股 / 价值投资 / 成长股 / 蓝筹股 / 小盘股 / 行业轮动 / 板块轮动 / 资金流向 / 北向资金 / 龙虎榜 / 涨停板 / 破净股 / 低估值 / 高成长 / 业绩超预期 / 财报选股 / 研报筛选 / AI选股 / 机器选股 / 组合构建 / 仓位管理 / 止损策略

---

## Core Capabilities / 核心能力

### 1. Quantitative Factor Screening / 量化因子筛选

```python
import pandas as pd
import numpy as np
from typing import List, Dict, Optional

class StockScreener:
    """智能选股引擎"""
    
    def __init__(self):
        self.factors = {
            # 估值因子
            "pe": {"name": "市盈率", "weight": 0.13, "direction": "low_better", "bounds": (0, 100)},
            "pb": {"name": "市净率", "weight": 0.10, "direction": "low_better", "bounds": (0, 10)},
            "ps": {"name": "市销率", "weight": 0.05, "direction": "low_better", "bounds": (0, 20)},
            "pcf": {"name": "市现率", "weight": 0.05, "direction": "low_better", "bounds": (0, 30)},
            
            # 成长因子
            "revenue_growth": {"name": "营收增速", "weight": 0.14, "direction": "high_better", "bounds": (-50, 100)},
            "profit_growth": {"name": "利润增速", "weight": 0.13, "direction": "high_better", "bounds": (-100, 200)},
            "gross_margin": {"name": "毛利率", "weight": 0.08, "direction": "high_better", "bounds": (0, 100)},
            
            # 质量因子
            "roe": {"name": "ROE", "weight": 0.10, "direction": "high_better", "bounds": (-20, 50)},
            "debt_ratio": {"name": "资产负债率", "weight": 0.05, "direction": "low_better", "bounds": (0, 100)},
            "current_ratio": {"name": "流动比率", "weight": 0.03, "direction": "high_better", "bounds": (0.5, 10)},
            
            # 动量因子
            "momentum_20d": {"name": "20日动量", "weight": 0.03, "direction": "high_better", "bounds": (-30, 50)},
            "momentum_60d": {"name": "60日动量", "weight": 0.01, "direction": "high_better", "bounds": (-50, 100)},
            
            # 股东回报因子
            "dividend_yield": {"name": "股息率", "weight": 0.05, "direction": "high_better", "bounds": (0, 8)},
            
            # 科创属性因子
            "rd_ratio": {"name": "研发投入占比", "weight": 0.05, "direction": "high_better", "bounds": (0, 30)}
        }
    
    def screen(self, stocks: pd.DataFrame, 
               criteria: Dict[str, tuple],
               min_score: float = 60) -> pd.DataFrame:
        """
        量化筛选主函数
        Args:
            stocks: 股票数据（含各因子列）
            criteria: 筛选条件 {因子名: (最小值, 最大值)}
            min_score: 最低综合评分
        Returns:
            符合条件的股票
        """
        result = stocks.copy()
        
        # Step 1: 硬性条件筛选
        for factor, (min_val, max_val) in criteria.items():
            if factor in result.columns:
                result = result[(result[factor] >= min_val) & (result[factor] <= max_val)]
        
        # Step 2: 因子打分
        result = self._factor_scoring(result)
        
        # Step 3: 综合评分排序
        result = result[result["综合评分"] >= min_score].sort_values("综合评分", ascending=False)
        
        return result
    
    def _factor_scoring(self, df: pd.DataFrame) -> pd.DataFrame:
        """因子打分（百分制）"""
        scores = pd.DataFrame(index=df.index)
        
        for factor, config in self.factors.items():
            if factor in df.columns:
                raw = df[factor].copy()
                min_val, max_val = config["bounds"]
                
                # 标准化到0-100
                normalized = (raw - min_val) / (max_val - min_val) * 100
                normalized = normalized.clip(0, 100)
                
                # 方向调整（部分因子越低越好）
                if config["direction"] == "low_better":
                    normalized = 100 - normalized
                
                scores[factor] = normalized * config["weight"]
        
        df["综合评分"] = scores.sum(axis=1)
        return df
```

**因子权重与方向一览（可直接核对权重合计）**

| 类别 | 因子 | 权重 | 方向 | 区间 |
|------|------|------|------|------|
| 估值 | 市盈率/市净率/市销率/市现率 | 0.13/0.10/0.05/0.05 | 越低越好 | 见配置 |
| 成长 | 营收增速/利润增速/毛利率 | 0.14/0.13/0.08 | 越高越好 | 见配置 |
| 质量 | ROE/资产负债率/流动比率 | 0.10/0.05/0.03 | 前三者高好、负债率低好 | 见配置 |
| 动量 | 20日/60日动量 | 0.03/0.01 | 越高越好 | 见配置 |
| 股东回报 | 股息率 | 0.05 | 越高越好 | 0-8% |
| 科创属性 | 研发投入占比 | 0.05 | 越高越好 | 0-30% |
| **合计** | — | **1.00** | — | — |

说明：权重合计必须为 1.00，新增因子时须同步下调其他因子权重；震荡市中可临时下调动量类因子权重（合计不超过0.05），以降低追高风险。

**示例 1｜单只标的打分手算（含低估值因子反向处理）**

| 因子 | 原始值 | 归一到0-100 | 方向调整后 | 权重 | 加权得分 |
|------|-------|------------|-----------|------|---------|
| 市盈率 | 18 | (18-0)/(100-0)×100=18 | 100-18=82 | 0.13 | 10.66 |
| 营收增速 | 25% | (25+50)/150×100=50 | 50 | 0.14 | 7.00 |
| 利润增速 | 40% | (40+100)/300×100=46.7 | 46.7 | 0.13 | 6.07 |
| ROE | 18% | (18+20)/70×100=54.3 | 54.3 | 0.10 | 5.43 |
| 股息率 | 3.2% | 3.2/8×100=40 | 40 | 0.05 | 2.00 |
| 研发投入占比 | 8% | 8/30×100=26.7 | 26.7 | 0.05 | 1.33 |
| **合计** | — | — | — | — | **（其余因子相加后）** |

要点：低估值因子必须先归一再用"100−归一值"翻转，否则会把高PE标的误判为最优。

**示例 2｜因子有效性检验（避免"看着好用"）**

| 检验项 | 方法 | 通过标准 | 不通过时处置 |
|-------|------|---------|------------|
| 单因子IC | 因子值与下期收益的秩相关 | 绝对值 ≥0.03 且方向稳定 | 降低权重或剔除 |
| 分组单调性 | 分5组看收益排序 | 收益随分组单调 | 检查极值处理方式 |
| 样本外表现 | 分年度滚动验证 | 样本外方向一致 | 缩短回看窗口 |
| 换手成本 | 统计换仓频率与手续费 | 年化换手成本 <3% | 引入换手惩罚 |
| 相关性 | 因子间相关系数 | 两两相关 <0.7 | 合并或删减冗余因子 |

### 2. Thematic Stock Screening / 主题投资筛选

```python
THEMATIC_SCREENING = {
    "AI人工智能": {
        "核心标的": ["科大讯飞", "海康威视", "中科曙光", "寒武纪", "商汤-W"],
        "概念股池": {
            "基础层": ["芯片", "算力", "服务器"],
            "技术层": ["大模型", "算法", "API"],
            "应用层": ["办公", "医疗", "金融", "教育"]
        },
        "筛选标准": {
            "市值": ">100亿",
            "研发投入": ">10%",
            "AI收入占比": ">30%"
        },
        "风险提示": "技术迭代快，竞争格局未定，估值波动大"
    },
    
    "新能源汽车": {
        "核心标的": ["比亚迪", "宁德时代", "理想汽车-W", "小鹏汽车-W"],
        "筛选维度": {
            "整车": ["销量增速", "毛利率", "智能化水平"],
            "电池": ["能量密度", "成本", "产能"],
            "配件": ["单车价值量", "客户集中度"]
        },
        "政策催化": "以旧换新补贴、购置税减免、新能源渗透率目标"
    },
    
    "创新药": {
        "核心标的": ["恒瑞医药", "百济神州", "信达生物", "药明康德"],
        "筛选标准": {
            "管线丰富度": ">10个临床管线",
            "first-in-class": "至少1个",
            "BD能力": "有海外授权记录"
        },
        "风险因素": "医保谈判降价、临床失败风险、同靶点竞争"
    },
    
    "红利低波": {
        "筛选标准": {
            "股息率": ">3%",
            "连续分红年数": ">=3年",
            "近1年波动率": "低于全市场中位数",
            "自由现金流": "为正且覆盖分红"
        },
        "适用环境": "利率下行、市场震荡、追求现金流回报",
        "风险提示": "股息率因股价下跌被动抬高需剔除；分红不可持续的高股息为陷阱"
    },
    
    "高端制造": {
        "筛选维度": {
            "机床/母机": ["订单增速", "国产化率", "毛利率"],
            "自动化": ["下游资本开支", "在手订单"],
            "精密零部件": ["单车/单机价值量", "客户集中度"]
        },
        "政策催化": "设备更新改造、国产替代、制造业投资周期",
        "风险因素": "下游资本开支不及预期、价格竞争、应收账款回收"
    }
}
```

**主题筛选执行清单（从主题到候选池）**

| 步骤 | 动作 | 产出 | 卡点 |
|------|------|------|------|
| 1 | 拆解产业链上下游环节 | 环节清单 | 环节定义须无重叠 |
| 2 | 为每个环节设定量化筛选标准 | 标准表 | 标准须可用财报数据验证 |
| 3 | 拉取候选池并剔除不达标标的 | 候选清单 | 剔除理由须留档 |
| 4 | 补充流动性与拥挤度过滤 | 可交易候选池 | 单笔建仓 ≤日均成交额5% |
| 5 | 计算综合评分排序 | 排序表 | 标注数据报告期 |
| 6 | 输出并附风险提示 | 主题选股报告 | 保留免责声明 |

**示例｜同一主题的两种筛选口径对比**

| 口径 | 条件 | 候选数量 | 入选标的特征 | 适用场景 |
|------|------|---------|------------|---------|
| 严格口径 | 研发占比>10% + 主题收入占比>30% + 市值>100亿 | 8只 | 纯度高、弹性中等 | 中长期配置 |
| 宽松口径 | 主题收入占比>10% 或 有明确订单 | 26只 | 纯度低、弹性大 | 主题轮动早期 |
| 事件口径 | 近3个月有订单/中标/产能公告 | 12只 | 催化明确、波动大 | 事件驱动交易 |

使用要点：三种口径不可混用；若报告使用宽松口径，必须在结论中注明"纯度较低、可能与主题关联度不足"。

### 3. Technical Signal Detection / 技术信号检测

```python
class TechnicalSignals:
    """技术信号检测"""
    
    @staticmethod
    def detect_moving_average_signals(prices: pd.Series, 
                                      short_ma: int = 20,
                                      long_ma: int = 60) -> dict:
        """均线信号检测"""
        ma_short = prices.rolling(short_ma).mean()
        ma_long = prices.rolling(long_ma).mean()
        
        # 金叉/死叉判断
        current_ma_diff = ma_short.iloc[-1] - ma_long.iloc[-1]
        prev_ma_diff = ma_short.iloc[-2] - ma_long.iloc[-2]
        
        if current_ma_diff > 0 and prev_ma_diff <= 0:
            signal = "GOLDEN_CROSS"  # 金叉
        elif current_ma_diff < 0 and prev_ma_diff >= 0:
            signal = "DEAD_CROSS"  # 死叉
        else:
            signal = "NEUTRAL"
        
        return {
            "signal": signal,
            "short_ma": round(ma_short.iloc[-1], 2),
            "long_ma": round(ma_long.iloc[-1], 2),
            "ma_diff_pct": round((current_ma_diff / ma_long.iloc[-1]) * 100, 2)
        }
    
    @staticmethod
    def detect_support_resistance(prices: pd.Series, 
                                 lookback: int = 60) -> dict:
        """支撑压力位检测"""
        recent = prices.tail(lookback)
        
        # 计算枢轴点
        pivot = (recent.max() + recent.min() + recent.iloc[-1]) / 3
        
        r1 = 2 * pivot - recent.min()
        s1 = 2 * pivot - recent.max()
        r2 = pivot + (recent.max() - recent.min())
        s2 = pivot - (recent.max() - recent.min())
        
        return {
            "resistance_1": round(r1, 2),
            "resistance_2": round(r2, 2),
            "pivot": round(pivot, 2),
            "support_1": round(s1, 2),
            "support_2": round(s2, 2),
            "current_price": round(prices.iloc[-1], 2)
        }
    
    @staticmethod
    def detect_volume_anomaly(prices: pd.Series, 
                             volumes: pd.Series,
                             threshold: float = 2.0) -> dict:
        """量价异常检测"""
        avg_volume = volumes.tail(20).mean()
        current_volume = volumes.iloc[-1]
        volume_ratio = current_volume / avg_volume
        
        # 价格与成交量背离
        price_change = (prices.iloc[-1] - prices.iloc[-2]) / prices.iloc[-2]
        
        return {
            "volume_ratio": round(volume_ratio, 2),
            "is_volume_surge": volume_ratio > threshold,
            "price_change": round(price_change * 100, 2),
            "divergence": "量价背离" if (price_change > 0 and volume_ratio < 0.5) or
                                      (price_change < 0 and volume_ratio > 2) else "正常"
        }
```

**信号组合矩阵（单一信号不决策，组合才决策）**

| 均线信号 | 量能状态 | 价格位置 | 综合判断 | 建议动作 |
|---------|---------|---------|---------|---------|
| 金叉 | 放量（>2倍） | 突破压力位 | 强势确认 | 可分批建仓 |
| 金叉 | 缩量（<0.8倍） | 未突破压力位 | 信号弱，可能反复 | 观察，暂不动 |
| 金叉 | 放量 | 已连续大涨后 | 追高风险 | 不追，等回调 |
| 死叉 | 放量 | 跌破支撑位 | 趋势转弱 | 按纪律减仓 |
| 死叉 | 缩量 | 支撑位附近 | 可能假跌破 | 观察一日再定 |
| 中性 | 量价背离 | 高位滞涨 | 分歧加大 | 降低仓位 |

**示例｜信号有效性统计（先验证再使用）**

| 信号 | 样本数 | 5日胜率 | 20日胜率 | 平均20日收益 | 结论 |
|------|-------|--------|---------|------------|------|
| 金叉+放量 | 320 | 58% | 61% | +3.2% | 保留，作为主要信号 |
| 金叉（缩量） | 410 | 49% | 47% | +0.4% | 弱化，需叠加其他条件 |
| 死叉+跌破支撑 | 260 | — | — | -2.8% | 保留，作为减仓信号 |
| 量价背离 | 180 | 44% | 41% | -1.1% | 作为预警信号使用 |

使用要点：胜率需按市场状态分层统计（上涨/震荡/下跌），单一整体胜率可能掩盖失效区间；若某信号在震荡市胜率低于45%，应暂停使用。

**示例｜信号与仓位对应（把信号变成纪律）**

| 综合评分 | 信号状态 | 建议仓位上限 | 单标的上限 | 止损参考 |
|---------|---------|------------|-----------|---------|
| ≥80 | 金叉+放量 | 80% | 15% | −8% |
| 70-79 | 金叉（等确认） | 60% | 12% | −8% |
| 60-69 | 中性 | 40% | 10% | −10% |
| <60 | 死叉或背离 | 20% | 8% | 立即评估 |

### 4. Financial Fraud Detection / 财报异常检测

```python
class FraudDetection:
    """财报异常信号检测"""
    
    @staticmethod
    def check_revenue_quality(stock_code: str, 
                             financial_data: dict) -> dict:
        """营收质量检测"""
        indicators = {
            # 应收账款异常
            "ar_growth_vs_revenue": financial_data.get("ar_growth", 0) - 
                                    financial_data.get("revenue_growth", 0),
            
            # 存货异常
            "inventory_growth_vs_cost": financial_data.get("inv_growth", 0) - 
                                        financial_data.get("cost_growth", 0),
            
            # 现金流匹配
            "cash_flow_ratio": financial_data.get("cfo", 0) / 
                              max(financial_data.get("net_profit", 1), 1),
            
            # 毛利率异常
            "gross_margin_volatility": financial_data.get("gm_std", 0),
            
            # 关联交易占比
            "related_party_ratio": financial_data.get("rpt_revenue", 0) / 
                                  max(financial_data.get("total_revenue", 1), 1)
        }
        
        # 预警信号
        warnings = []
        if indicators["ar_growth_vs_revenue"] > 30:
            warnings.append("应收账款增速显著高于营收增速，可能存在虚构收入")
        if indicators["cash_flow_ratio"] < 0.5:
            warnings.append("经营现金流显著低于净利润，盈利质量存疑")
        if indicators["related_party_ratio"] > 0.5:
            warnings.append("关联交易占比过高，存在利益输送风险")
        
        return {
            "indicators": indicators,
            "warnings": warnings,
            "overall_risk": "高" if len(warnings) >= 2 else 
                           "中" if warnings else "低"
        }
    
    @staticmethod
    def check_auditor_warnings(audit_reports: list) -> dict:
        """审计意见检测"""
        risk_keywords = ["保留意见", "无法表示意见", "非标准无保留", 
                        "持续经营重大不确定性", "强调事项段"]
        
        findings = []
        for report in audit_reports:
            for keyword in risk_keywords:
                if keyword in report:
                    findings.append({
                        "keyword": keyword,
                        "context": report
                    })
        
        return {
            "has_warnings": len(findings) > 0,
            "findings": findings,
            "risk_level": "高" if findings else "低"
        }
```

**财报异常指标阈值表（触发即预警）**

| 指标 | 计算口径 | 关注阈值 | 预警阈值 | 说明 |
|------|---------|---------|---------|------|
| 应收增速−营收增速 | 两个同比增速之差 | >15pct | >30pct | 可能虚构收入或放宽信用 |
| 存货增速−成本增速 | 同比增速之差 | >15pct | >30pct | 可能存货积压或虚增 |
| 经营现金流/净利润 | CFO ÷ 归母净利润 | <0.8 | <0.5 | 盈利质量存疑 |
| 毛利率波动率 | 近8期标准差 | >2.5pct | >4pct | 可能人为调节 |
| 关联交易收入占比 | 关联收入 ÷ 营收 | >30% | >50% | 利益输送风险 |
| 商誉/净资产 | 商誉 ÷ 净资产 | >20% | >40% | 减值风险 |
| 审计意见类型 | 意见段 | 带强调事项段 | 保留/无法表示意见 | 直接排除 |

**示例｜综合风险判定（三项指标联动）**

| 标的 | 应收−营收 | CFO/净利润 | 关联占比 | 命中预警数 | 风险判定 | 处置 |
|------|----------|-----------|---------|-----------|---------|------|
| 标的A | +8pct | 1.12 | 12% | 0 | 低 | 正常纳入评分 |
| 标的B | +34pct | 0.62 | 21% | 2 | 高 | 直接排除，不参与评分 |
| 标的C | +18pct | 0.75 | 33% | 2 | 高 | 核查后决定是否排除 |
| 标的D | +5pct | 0.95 | 8% | 0 | 低 | 正常纳入评分 |

使用要点：命中2项及以上预警阈值即判定为高风险，无论综合评分多高均不纳入候选池；单一指标命中需在报告中说明核查进展，不得直接作为结论。

### 5. Portfolio Construction / 组合构建

```python
class PortfolioBuilder:
    """智能组合构建"""
    
    def __init__(self, target_stocks: List[dict], 
                 total_capital: float = 1000000):
        self.stocks = target_stocks
        self.capital = total_capital
    
    def build_equal_weight(self, max_positions: int = 10) -> dict:
        """等权重配置"""
        selected = self.stocks[:max_positions]
        per_stock = self.capital / len(selected)
        
        positions = []
        for stock in selected:
            shares = int(per_stock / stock["price"] / 100) * 100  # 100股整数
            positions.append({
                "code": stock["code"],
                "name": stock["name"],
                "shares": shares,
                "amount": shares * stock["price"],
                "weight": 1 / len(selected)
            })
        
        return {
            "strategy": "等权重",
            "positions": positions,
            "total_invested": sum(p["amount"] for p in positions),
            "cash_remaining": self.capital - sum(p["amount"] for p in positions),
            "expected_return": sum(s.get("expected_return", 0) for s in selected) / len(selected),
            "estimated_risk": self._calculate_portfolio_risk(positions)
        }
    
    def build_risk_parity(self, max_positions: int = 10) -> dict:
        """风险平价配置"""
        selected = self.stocks[:max_positions]
        
        # 使用波动率倒数作为权重
        inv_vol = [1 / s.get("volatility", 0.3) for s in selected]
        total_inv_vol = sum(inv_vol)
        weights = [v / total_inv_vol for v in inv_vol]
        
        positions = []
        for stock, weight in zip(selected, weights):
            amount = self.capital * weight
            shares = int(amount / stock["price"] / 100) * 100
            positions.append({
                "code": stock["code"],
                "name": stock["name"],
                "shares": shares,
                "amount": shares * stock["price"],
                "weight": round(weight * 100, 2)
            })
        
        return {
            "strategy": "风险平价",
            "positions": positions,
            "total_invested": sum(p["amount"] for p in positions)
        }
    
    def _calculate_portfolio_risk(self, positions: list) -> float:
        """简化组合风险估算"""
        # 假设相关性0.3
        individual_risks = [0.25] * len(positions)  # 默认25%波动率
        correlation = 0.3
        
        portfolio_var = 0
        for i, risk_i in enumerate(individual_risks):
            for j, risk_j in enumerate(individual_risks):
                weight_i = 1 / len(positions)
                weight_j = 1 / len(positions)
                corr = correlation if i != j else 1
                portfolio_var += weight_i * weight_j * risk_i * risk_j * corr
        
        return round(np.sqrt(portfolio_var) * 100, 2)
```

**示例 1｜等权重 vs 风险平价（同一候选池两种结果）**

| 标的 | 预期收益 | 波动率 | 等权重 | 风险平价权重 | 差异说明 |
|------|---------|-------|-------|------------|---------|
| 标的A | 18% | 20% | 10.0% | 12.5% | 低波动，风险平价提升权重 |
| 标的B | 25% | 35% | 10.0% | 7.1% | 高波动，风险平价下调权重 |
| 标的C | 15% | 18% | 10.0% | 13.9% | 最低波动，权重最高 |
| 标的D | 30% | 45% | 10.0% | 5.6% | 最高波动，权重最低 |

结论：等权重简单透明、易执行；风险平价会在不牺牲过多收益的前提下降低组合波动，适合波动容忍度较低的账户。两种方式都应同时给出，便于对照选择。

**示例 2｜组合风控阈值表（建仓前先设红线）**

| 风控项 | 阈值 | 超限动作 | 检查频率 |
|-------|------|---------|---------|
| 单标的权重 | ≤15% | 触发即减仓至阈值内 | 每周 |
| 单一行业权重 | ≤35% | 新增买入暂停，优先调出 | 每周 |
| 前三大标的合计 | ≤40% | 降低集中度 | 每两周 |
| 组合预估波动率 | ≤25% | 降仓或增加低波动资产 | 每月 |
| 单标的浮亏 | −8%至−10% | 按纪律评估减仓 | 每日 |
| 组合最大回撤 | −15% | 启动整体降仓预案 | 每日 |

**示例 3｜建仓分批节奏（避免一次性买在高点）**

| 批次 | 触发条件 | 投入比例 | 备注 |
|------|---------|---------|------|
| 第1批 | 信号确认（金叉+放量） | 40% | 建立底仓 |
| 第2批 | 回踩支撑不破 | 30% | 摊薄成本 |
| 第3批 | 突破前高确认 | 30% | 趋势延续加仓 |
| 例外 | 跌破止损位 | 0%（不补） | 按纪律减仓 |

---

## Usage Examples / 使用示例

**启动选股：**
```
用以下条件筛选股票：
- 市盈率 < 30
- 营收增速 > 20%
- ROE > 15%
- 综合评分 > 70
```

**主题选股：**
```
筛选AI人工智能概念中估值最低的10只股票
```

**技术面选股：**
```
找出所有出现均线金叉且放量突破的股票
```

**因子有效性检验：**
```
对[因子名称]做有效性检验：输出IC值、分组单调性、
样本外方向一致性、换手成本与因子间相关性，并给出是否保留的结论。
```

**组合构建与风控：**
```
用以下候选池构建组合，同时输出等权重与风险平价两种方案，
并检查单标的上限（15%）、行业上限（35%）、组合波动率（≤25%）是否超限。
```

---

## Disclaimer

This skill provides stock screening tools and analysis for educational purposes. Stock selection results are based on quantitative models and historical data, which do not guarantee future performance. All investment decisions should be made based on independent research and professional advice. Past performance does not indicate future results.
