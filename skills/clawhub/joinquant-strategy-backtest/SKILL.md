---
name: joinquant-strategy-backtest
version: 0.2.0
description: 聚宽(JoinQuant)策略回测代码生成框架。基于六段式骨架模板，支持截面多因子选股、时序技术指标择时、以及因子库智能推荐三种模式，自动生成可直接在聚宽平台运行的回测代码。
author: weiyang
tags:
  - joinquant
  - 聚宽
  - 策略回测
  - 多因子
  - 截面策略
  - 时序策略
  - 因子推荐
  - 量化
---

# 聚宽策略回测代码生成框架

> **状态：迭代构建中** — v0.2 增加六段式骨架、截面/时序双模板、因子推荐模块。

## 适用场景

当用户需要：
- 在聚宽平台开发和回测量化策略
- 生成截面多因子选股策略代码
- 生成时序技术指标择时策略代码
- 从聚宽因子库推荐因子并自动生成策略
- 查阅聚宽API使用方法

## ⚠️ API文档获取陷阱

**聚宽官方API文档和因子库页面均为JavaScript SPA，无法通过curl/HTTP直接抓取。** 已验证：curl返回HTML框架无内容、搜索引擎被反爬、Wayback Machine不可达、browser工具Chrome启动失败（sandbox限制）。

**可行方案：** 依赖模型训练知识（已验证准确度较高）+ 用户贴文档内容补充 + 聚宽平台内代码验证。

---

## 一、六段式骨架模板

所有聚宽策略都遵循统一的六段式结构。截面和时序两种策略类型的差异仅体现在第4段「信号模块」。

### 骨架总览

```
1. 文件头          — 标题/作者/import
2. initialize      — set_option + set_benchmark + g.* 参数定义
3. before_trading_start — 滑点/手续费（可选，注释包裹）
4. 信号模块         — 截面版：get_buy_list()；时序版：signal_stock_buy/sell()
5. handle_data     — 配资 + 信号调用 + 先卖后买执行
6. after_trading_end — 盘后日志（可选，注释包裹）
```

### 1.1 initialize 必备项

```python
def initialize(context):
    set_option('use_real_price', True)
    g.benchmark = '000300.XSHG'        # 基准
    set_benchmark(g.benchmark)
    g.N = 30                            # 持仓数量
    g.period = 20                       # 调仓周期(交易日)
    g.inv_days = 0                      # 投资天数计数器
    g.stock_index = ['000300.XSHG']     # 股票池指数
```

### 1.2 before_trading_start 模板（可选）

```python
def before_trading_start(context):
    set_slip_fee(context)

def set_slip_fee(context):
    set_slippage(FixedSlippage(0))
    dt = context.current_dt
    if dt > datetime.datetime(2013, 1, 1):
        set_commission(PerTrade(buy_cost=0.0003, sell_cost=0.0013, min_cost=5))
    elif dt > datetime.datetime(2011, 1, 1):
        set_commission(PerTrade(buy_cost=0.001, sell_cost=0.002, min_cost=5))
    elif dt > datetime.datetime(2009, 1, 1):
        set_commission(PerTrade(buy_cost=0.002, sell_cost=0.003, min_cost=5))
    else:
        set_commission(PerTrade(buy_cost=0.003, sell_cost=0.004, min_cost=5))
```

### 1.3 handle_data 通用模板（截面版）

```python
def handle_data(context, data):
    if g.inv_days % g.period == 0:          # 调仓周期门控
        capital_unit = context.portfolio.portfolio_value / g.N
        list_to_buy = get_buy_list(context)  # 调信号模块
        list_to_sell = stocks_to_sell(context, list_to_buy)
        # 先卖后买
        for stk in list_to_sell:
            order_target_value(stk, 0)
        for stk in list_to_buy:
            order_target_value(stk, capital_unit)
    g.inv_days += 1
```

---

## 二、截面多因子策略模板

### 2.1 信号模块

```python
from jqfactor import get_factor_values
import math

def get_buy_list(context):
    # 1. 从指数成分获取候选股票池
    g.stock_list = []
    for ix_ in g.stock_index:
        g.stock_list.extend(get_index_stocks(ix_, date=context.previous_date))

    # 2. 批量取因子值
    factor_list = ['PEG', 'VOL120', 'roe_ttm_8y']
    a = get_factor_values(securities=g.stock_list,
                          factors=factor_list,
                          count=1, end_date=context.previous_date)

    # 3. 构建因子DataFrame
    df_far = pd.DataFrame()
    for far_ in factor_list:
        df_far = df_far.append(a[far_], ignore_index=True)
    df_far = df_far.T
    df_far.columns = factor_list

    # 4. 去极值 + 标准化
    df_far = median_remove_extrame(factor_list, df_far, multiplier=5)
    df_far = standardize(factor_list, df_far)

    # 5. 因子合成（等权或加权）
    # IC>0 正向加权(+)，IC<0 负向加权(-)
    df_far['far_deal'] = -df_far['PEG'] + df_far['roe_ttm_8y'] - df_far['VOL120']

    # 6. 排序取Top N
    df_far = df_far.sort_values(by='far_deal', ascending=False)
    return list(df_far.dropna().head(g.N).index)

# 中位数去极值(MAD法)
def median_remove_extrame(factor_list, df_, multiplier=5):
    for x_ in factor_list:
        median_ = df_[x_].quantile(0.5)
        dis2media = np.abs(df_[x_] - df_[x_].quantile(0.5))
        dis_media = dis2media.quantile(0.5)
        up_limit = median_ + multiplier * dis_media
        down_limit = median_ - multiplier * dis_media
        df_[x_] = [up_limit if i >= up_limit else (down_limit if i <= down_limit else i) for i in df_[x_]]
    return df_

# 截面标准化(Z-score)
def standardize(factor_list, df_):
    for x_ in factor_list:
        df_[x_] = (df_[x_] - df_[x_].mean()) / df_[x_].std()
    return df_

# 卖出清单
def stocks_to_sell(context, list_to_buy):
    list_to_sell = []
    for stock_sell in context.portfolio.positions:
        if stock_sell not in list_to_buy:
            list_to_sell.append(stock_sell)
    return list_to_sell
```

### 2.2 因子合成规则

- IC > 0 的因子：正向加权（`+w * factor`）
- IC < 0 的因子：负向加权（`-w * factor`），即引入负号
- 等权组合：所有因子权重绝对值相同（`w=1`）

---

## 三、时序技术指标择时模板

### 3.1 信号模块

```python
import talib

def signal_stock_sell(context):
    sell = [0] * len(g.security)
    for i in range(len(g.security)):
        (ma_long_pre, ma_long_now) = get_EMA(context, g.security[i], g.N_sell_slow)
        (ma_short_pre, ma_short_now) = get_EMA(context, g.security[i], g.N_sell_fast)
        # 死叉：短下穿长 + 有持仓
        if ma_short_now < ma_long_now and ma_short_pre > ma_long_pre \
                and context.portfolio.positions[g.security[i]].sellable_amount > 0:
            sell[i] = 1
    return sell

def signal_stock_buy(context):
    buy = [0] * len(g.security)
    for i in range(len(g.security)):
        (ma_long_pre, ma_long_now) = get_EMA(context, g.security[i], g.N_buy_slow)
        (ma_short_pre, ma_short_now) = get_EMA(context, g.security[i], g.N_buy_fast)
        # 金叉：短上穿长 + 无持仓
        if ma_short_now > ma_long_now and ma_short_pre < ma_long_pre \
                and context.portfolio.positions[g.security[i]].sellable_amount == 0:
            buy[i] = 1
    return buy

def get_EMA(context, code, days):
    a = get_price(code, start_date='2005-01-04',
                  end_date=context.previous_date).close
    ema = talib.EMA(a, days)
    return ema[-2], ema[-1]
```

### 3.2 时序模板 handle_data

```python
def handle_data(context, data):
    capital_unit = context.portfolio.portfolio_value / g.N
    toSell = signal_stock_sell(context)
    toBuy = signal_stock_buy(context)
    # 先卖后买
    for i in range(len(g.security)):
        if toSell[i] == 1:
            order_target_value(g.security[i], 0)
    for i in range(len(g.security)):
        if toBuy[i] == 1:
            order_target_value(g.security[i], capital_unit)
```

### 3.3 时序模板 initialize

```python
def initialize(context):
    set_option('use_real_price', True)
    g.benchmark = '000300.XSHG'
    set_benchmark(g.benchmark)
    # 交易标的列表
    g.security = ['000300.XSHG', '000905.XSHG', '000852.XSHG']
    g.N = len(g.security)
    # EMA均线参数
    g.N_buy_fast = 5
    g.N_buy_slow = 20
    g.N_sell_fast = 5
    g.N_sell_slow = 20
```

---

## 四、因子推荐模块

### 4.1 推荐逻辑

当用户没有明确策略思路时，按以下流程推荐因子：

1. **查阅因子库**：访问聚宽因子库页面 `https://www.joinquant.com/view/factorlib/list`
2. **筛选规则**：
   - 获取每个因子的 **IC均值** 和 **分位数收益率**
   - 如果 IC > 0：看**最大分位数收益率**（Top quantile收益越高越好）
   - 如果 IC < 0：看**最小分位数收益率**（Bottom quantile收益越低越好，负向使用）
3. **排序选取**：按 IC绝对值 × 分位数收益幅度 综合排序，取 Top 2-3 个因子
4. **等权组合**：
   - IC > 0 的因子 → 正向加权（`+factor`）
   - IC < 0 的因子 → 负向加权（`-factor`）
5. **生成代码**：自动填入截面多因子模板（第二节），生成完整可回测代码

### 4.2 因子库访问限制

聚宽因子库页面为SPA，API（`/api/factorlib/list`）需要前端生成的鉴权参数（返回 `{"code":4,"msg":"缺失必要的通用参数"}`）。当前环境无法直接抓取。

**替代方案**：
- **方案A**：用户手动打开因子库页面，将因子名称和IC数据贴给Agent
- **方案B**：Agent基于已知聚宽因子库信息推荐（见下方常见因子表）
- **方案C**：用户在聚宽研究环境内运行IC查询代码（见下方）

### 4.3 常见聚宽因子参考表

| 因子名 | 类别 | 典型IC方向 | 含义 |
|--------|------|-----------|------|
| `PEG` | 估值 | 负 | 市盈率相对盈利增长比，越低越好 |
| `VOL120` | 量价 | 负 | 120日换手率，低换手率超额收益 |
| `VOL240` | 量价 | 负 | 240日换手率 |
| `VOL20` | 量价 | 负 | 20日换手率 |
| `roe_ttm_8y` | 盈利 | 正 | ROE_TTM的8年均值 |
| `market_cap` | 规模 | 负 | 总市值，小市值效应 |
| `circulating_market_cap` | 规模 | 负 | 流通市值 |
| `PB` | 估值 | 负 | 市净率，低PB效应 |
| `PS` | 估值 | 负 | 市销率 |
| `turnover_ratio` | 量价 | 负 | 换手率 |
| `pe_ratio` | 估值 | 负 | 市盈率 |
| `debit_to_asset` | 质量 | 负 | 资产负债率 |
| `net_profit_margin` | 盈利 | 正 | 净利率 |
| `gross_income_ratio` | 盈利 | 正 | 毛利率 |
| `inc_revenue_year_on_year` | 成长 | 正 | 营收同比增长率 |
| `inc_net_profit_year_on_year` | 成长 | 正 | 净利润同比增长率 |

### 4.4 因子IC查询代码（聚宽研究环境内运行）

```python
# 在聚宽研究环境内运行，查询因子IC
from jqfactor import get_factor_values
import pandas as pd
import numpy as np

# 指定要测试的因子列表
factors_to_test = ['PEG', 'VOL120', 'roe_ttm_8y', 'market_cap', 'PB']

# 获取沪深300成分股
stocks = get_index_stocks('000300.XSHG')

# 获取因子值和未来收益率，计算IC
for factor_name in factors_to_test:
    factor_data = get_factor_values(
        securities=stocks,
        factors=[factor_name],
        count=1,
        end_date='2024-01-01'
    )
    # 计算IC均值（简化版，实际需循环多日）
    # ... IC计算逻辑 ...
    print(f'{factor_name}: IC = ...')
```

---

## 五、代码生成工作流

### 5.1 用户输入 → 代码生成流程

```
用户需求
   │
   ├── 有明确因子/策略思路？
   │     ├── 是 → 选择模板（截面/时序）→ 填入因子/参数 → 生成代码
   │     └── 否 → 因子推荐模块
   │               ├── 查阅因子库（或用常见因子表）
   │               ├── 按IC+分位数收益筛选Top 2-3因子
   │               ├── 确定加权方向（IC正→+，IC负→-）
   │               └── 填入截面模板 → 生成代码
   │
   ├── 策略类型？
   │     ├── 截面多因子 → 使用第二节模板
   │     └── 时序择时   → 使用第三节模板
   │
   └── 生成完整代码（六段式骨架 + 信号模块 + 注释）
```

### 5.2 代码生成检查清单

- [ ] `initialize` 包含 `set_option`, `set_benchmark`, 所有 `g.*` 参数
- [ ] `handle_data` 包含调仓周期门控（截面策略）或每日信号检查（时序策略）
- [ ] 先卖后买顺序
- [ ] `order_target_value` 而非 `order`（自动计算差额）
- [ ] 因子去极值 + 标准化（截面策略）
- [ ] 因子合成方向正确（IC正→+，IC负→-）
- [ ] 可选模块（before_trading_start / after_trading_end）用注释包裹
- [ ] 文件头包含标题、作者、import
- [ ] 代码可直接复制到聚宽平台运行

---

## 六、聚宽API速查

### 6.1 策略框架函数

| 函数 | 用途 | 调用时机 |
|------|------|---------|
| `initialize(context)` | 全局初始化 | 回测开始前一次 |
| `before_trading_start(context)` | 盘前准备 | 每日开盘前 |
| `handle_data(context, data)` | 交易执行 | 每日交易时段 |
| `after_trading_end(context)` | 盘后处理 | 每日收盘后 |
| `process_initialize(context)` | 进程初始化 | 进程启动时 |

### 6.2 设置函数

| 函数 | 用途 |
|------|------|
| `set_option('use_real_price', True)` | 使用真实价格 |
| `set_benchmark(code)` | 设置基准 |
| `set_commission(PerTrade(...))` | 设置手续费 |
| `set_slippage(FixedSlippage(0))` | 设置滑点 |

### 6.3 下单函数

| 函数 | 用途 |
|------|------|
| `order(security, amount)` | 按股数下单 |
| `order_value(security, value)` | 按金额下单 |
| `order_target(security, target_amount)` | 调至目标股数 |
| `order_target_value(security, target_value)` | 调至目标金额 |
| `order_target_percent(security, percent)` | 调至目标百分比 |
| `cancel_order(order)` | 撤单 |

### 6.4 数据函数

| 函数 | 用途 |
|------|------|
| `get_price(code, start_date, end_date)` | 获取历史行情 |
| `get_bars(code, count, unit)` | 获取K线数据 |
| `attribute_history(code, count, unit, fields)` | 获取个股历史数据 |
| `get_fundamentals(query_object)` | 查询财务数据 |
| `get_factor_values(securities, factors, count, end_date)` | 批量获取因子值 |
| `get_index_stocks(index, date)` | 获取指数成分股 |
| `get_security_info(code)` | 获取证券信息 |
| `get_industry(security)` | 获取行业分类 |
| `get_current_data()` | 获取实时行情快照 |
| `get_all_securities(types=['stock'])` | 所有股票列表 |
| `get_trade_days(start_date, end_date)` | 交易日历 |

### 6.5 上下文对象

| 属性 | 用途 |
|------|------|
| `context.current_dt` | 当前回测时间 |
| `context.previous_date` | 上一交易日 |
| `context.portfolio.available_cash` | 可用资金 |
| `context.portfolio.portfolio_value` | 总资产 |
| `context.portfolio.positions` | 持仓字典 |
| `context.portfolio.positions[stk].sellable_amount` | 可卖数量 |
| `g.*` | 全局自定义变量 |

### 6.6 定时调度

| 函数 | 用途 |
|------|------|
| `run_daily(func, time)` | 每日定时执行 |
| `run_weekly(func, weekday, time)` | 每周定时执行 |
| `run_monthly(func, monthday, time)` | 每月定时执行 |

### 6.7 证券代码格式

| 市场 | 格式 | 示例 |
|------|------|------|
| 深圳股票 | `.XSHE` | `000001.XSHE`（平安银行） |
| 上海股票 | `.XSHG` | `600519.XSHG`（贵州茅台） |
| 指数 | `.XSHG`/`.XSHE` | `000300.XSHG`（沪深300） |
| 场内基金 | `.XSHG`/`.XSHE` | `510300.XSHG`（沪深300ETF） |

---

## 七、坑点提醒

1. **成交金额限制**：若下单金额超过当日实际成交额，只能成交部分（ETF常见）
2. **最低成交单位**：聚宽默认最低100股，建议个股回测金额≥100万、指数≥1000万
3. **`get_factor_values`** 需要 `from jqfactor import get_factor_values`，仅在聚宽平台内可用
4. **`talib`** 在聚宽平台预装，本地环境需自行安装
5. **`context.previous_date`** 是上一交易日（非前一天），用于取因子值避免未来数据
6. **`pd.DataFrame.append`** 在pandas 2.0+已废弃，聚宽平台内pandas版本可能较旧仍可用
7. **`order_target_value`** 会自动计算差额下单，比手动计算买卖数量更简洁
8. **持仓状态跟踪**：时序策略中需在买卖信号中同步更新持仓状态
9. **`set_option` vs `set_options`**：聚宽API中两个函数都存在，`set_option`（单数）设置单个选项，`set_options`（复数）可批量设置

## 更新日志

### v0.2.0
- 新增：六段式骨架模板（文件头/initialize/before_trading_start/信号模块/handle_data/after_trading_end）
- 新增：截面多因子策略模板（含去极值MAD法、Z-score标准化、因子合成）
- 新增：时序技术指标择时模板（EMA金叉死叉、talib集成）
- 新增：因子推荐模块（IC+分位数收益率筛选逻辑、常见因子参考表、IC查询代码）
- 新增：代码生成工作流（用户需求→模板选择→代码生成→检查清单）
- 保留：聚宽API速查（框架函数/设置/下单/数据/上下文/调度/代码格式）
- 保留：坑点提醒

### v0.1.0
- 初始创建，包含API骨架、生命周期、下单、数据获取、定时调度、基础模板
