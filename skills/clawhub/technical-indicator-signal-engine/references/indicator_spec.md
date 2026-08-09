# 指标计算口径详解

本文件供引擎实现与复核参考，确保信号口径与主流行情软件（通达信）一致。

## 布林带（对齐通达信公式）

通达信源码编译逻辑：

```
N := 20;
MID := MA(C, N);
VART1 := POW((C - MID), 2);
VART2 := MA(VART1, N);
VART3 := SQRT(VART2);
UPPER := MID + 2 * VART3;
LOWER := MID - 2 * VART3;
```

要点：

- 中轨 `MID = MA(C, N)`（简单移动平均）。
- 标准差 `VART3` 采用 `N` 日窗口内的**总体标准差**，即偏差平方和的简单移动平均再开方（`ddof=0`），与源码 `MA((C-MID)^2, N)` 一致；**不要**使用 pandas 默认的 `rolling().std()`（样本标准差，`ddof=1`），否则带宽会被系统性低估。
- 源码另以 `BOLL/UB/LB := REF(MID/UPPER/LOWER, 1)` 仅用于画线显示，信号判定使用当根 K 线的带宽（标准均值回归口径），故信号计算不套用 REF 移位。

## ADX（Wilder EWM 全链路）

链路：`+DM / -DM → TR → Wilder 平滑 → +DI / -DI → DX → ADX`。

- `+DM = max(high - prev_high, 0)` 当 `up_move > down_move`，否则 0；`-DM` 同理。
- `TR = max(high-low, |high-prev_close|, |low-prev_close|)`。
- 平滑采用 Wilder EWM：`ewm(alpha = 1/period, min_periods = period)`（**不是**普通滚动均值）。
- `+DI = 100 * smoothed_+DM / smoothed_TR`；`-DI` 同理。
- `DX = 100 * |+DI - -DI| / (+DI + -DI)`；`ADX = DX.ewm(alpha = 1/period)` 平滑。
- 趋势强度阈值默认 `25`：ADX 大于 25 视为有效趋势，小于则视为震荡。

## OBV（能量潮）

```
sign = sign(close.diff())
OBV = (volume * sign).cumsum()
```

量价维度以 `OBV` 与其 `N` 日移动平均比较：OBV 在均线上方视为量能配合看多，下方视为看空。

## 量比

量比由行情数据直接提供（如 westock-data 的 `quote` 字段），用于确认当日成交相对近 5 日均量的放大 / 萎缩程度，与 OBV 共同构成量价维度。

## 参数表

| 参数 | 默认 | 说明 |
|------|------|------|
| ema_fast | 13 | 快线 EMA 周期 |
| ema_slow | 55 | 慢线 EMA 周期 |
| adx_period | 14 | ADX 计算周期 |
| adx_threshold | 25.0 | ADX 趋势强度阈值 |
| bb_window | 20 | 布林带窗口 |
| bb_std | 2.0 | 布林带标准差倍数 |
| vol_ma_period | 20 | 成交量均线周期 |
| obv_ma_period | 20 | OBV 均线周期 |
