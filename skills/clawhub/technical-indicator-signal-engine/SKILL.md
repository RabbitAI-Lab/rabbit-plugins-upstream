---
name: technical-indicator-signal-engine
description: 三维技术面信号引擎，融合趋势类 EMA(13/55)+ADX(14)、均值回归类布林带(20,±2)、量价类 OBV+量比，通过三维投票生成买入/卖出/观望信号。触发口令「分析 XXXX」（个股名称或代码）。纯 pandas 实现，适用于任意 OHLCV 行情。
license: MIT
agent_created: true
version: 1.0.0
author: yanming
category: strategy
---

# 基础技术指标信号引擎（三维技术面分析）

## Overview

本技能提供一套纯 pandas 实现的三维技术面信号引擎，将三类经典西方技术分析指标合并为综合交易信号。适用于对个股、ETF、加密货币等任意 OHLCV 行情做量化择时判断。

触发口令：在对话中输入 **「分析 XXXX」**（XXXX 为个股名称或代码），即按本技能口径执行三维分析并输出买入 / 卖出 / 观望结论。

## When to Use

- 用户要求对某只标的做技术面买入 / 卖出信号判断时。
- 用户给出「分析 600519」「分析 贵州茅台」等带「分析」前缀的指令时。
- 需要在趋势、均值回归、量价三个维度交叉验证，而非依赖单一指标下结论时。

## 三维信号框架

| 维度 | 指标 | 作用 |
|------|------|------|
| 趋势 | EMA(13/55) + ADX(14) | 判定方向及趋势强度（ADX 阈值 25） |
| 均值回归 | 布林带(20, ±2) | 识别超买 / 超卖 |
| 量价 | OBV + 量比 | 确认量能配合 |

### 投票逻辑

- **买入（做多，信号 = 1）**：趋势看多（EMA 快线在慢线上方且 ADX 大于 25）或价格跌破布林下轨（超卖），且 OBV 上行，且未突破布林上轨。
- **卖出（做空，信号 = -1）**：趋势看空（EMA 快线在慢线下方且 ADX 大于 25）或价格突破布林上轨（超买），且 OBV 下行，且未跌破布林下轨。
- **观望（信号 = 0）**：三维度信号分裂、无法形成合力。

信号约定：`1` = 做多，`-1` = 做空，`0` = 观望。

## 引擎用法

核心实现见 `scripts/signal_engine.py`，提供 `SignalEngine` 类：

```python
import pandas as pd
from scripts.signal_engine import SignalEngine

# df 需含 open/high/low/close/volume 列，index 为 datetime
engine = SignalEngine()  # 默认参数：ema_fast=13, ema_slow=55, adx_period=14, adx_threshold=25, bb_window=20, bb_std=2
signal = engine.generate({"SH600519": df})["SH600519"]
```

指标计算口径（含布林带总体标准差 ddof=0、ADX Wilder 平滑链路的完整实现）见 `references/indicator_spec.md`。

## Dependencies

```bash
pip install pandas numpy requests
```

## 数据接入建议

- A 股 / 港股 / 美股行情：优先使用 `westock-data` 取结构化 K 线与财报（如 `westock-data kline <code> --period day --limit 250`）。
- 加密货币：引擎内置 OKX 示例（`SignalEngine` 演示用 `_fetch_okx`）。
- 关键陷阱：K 线列序需确认「收盘价为哪一列」，勿把最低价误当收盘价，否则信号建立在错误价格上。
