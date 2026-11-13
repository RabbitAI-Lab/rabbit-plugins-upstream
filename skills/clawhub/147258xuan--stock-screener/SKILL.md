---
name: stock-screener
description: "筛选A股：按估值（PE/PB）、成交量、涨跌幅、量比、市值、技术面（均线/MACD/RSI/布林带/涨跌停）等条件过滤，返回结果列表。支持 text/json/markdown/csv 输出。支持自选股 watchlist 保存与加载。支持快速预设（value/growth/dividend/momentum）。默认扫描全市场5200+只A股。"
---

# Stock Screener

用公开接口拉 A 股实时行情，按条件筛选。默认扫描全市场所有 A 股（约 5200 只），收盘后自动分析推荐股票。

## 用法

```bash
# 全市场筛选（默认，使用 all_a_shares.json）
node skills/stock-screener/index.js --pe 0-30 --limit 20
node skills/stock-screener/index.js --preset value --limit 10 --output markdown

# 快速测试（只用内置 25 只）
node skills/stock-screener/index.js --builtin --pe 0-30 --limit 10

# 自定义股票代码
node skills/stock-screener/index.js --codes sh600519,sz000858,sh601318 --pe 0-10 --output json

# 从文件加载股票代码
node skills/stock-screener/index.js --codes-file my_stocks.txt --pe 0-20 --output markdown

# 自选股管理
node skills/stock-screener/index.js --save-watchlist my-stocks --codes sh600519,sz000001,sh601398
node skills/stock-screener/index.js --watchlist my-stocks --pe 0-20 --output markdown
node skills/stock-screener/index.js --list-watchlists
node skills/stock-screener/index.js --delete-watchlist my-stocks
```

## 全市场扫描

- 默认使用 `all_a_shares.json`（约 5200 只沪深 A 股）
- 如需更新股票列表：`python3 scripts/update_stock_list.py`
- 快速测试用 `--builtin`（25 只内置股票）

## 自选股（Watchlist）

- `--save-watchlist <name>` 保存当前股票列表为自选股
- `--watchlist <name>` 加载自选股进行筛选
- `--list-watchlists` 列出所有已保存的自选股
- `--delete-watchlist <name>` 删除指定自选股

自选股保存在 `skills/stock-screener/watchlist.json`。

## 技术面筛选

技术指标采用两阶段分析：先用基础条件缩池，再对候选股计算技术指标。建议先用基础条件缩小范围，再叠加技术面过滤。

- `--ma-bullish` 均线多头排列（MA5>MA10>MA20）
- `--ma-bearish` 均线空头排列（MA5<MA10<MA20）
- `--macd-golden` MACD金叉（快线上穿慢线）
- `--macd-death` MACD死叉（快线下穿慢线）
- `--rsi-overbought` RSI超买（RSI>70）
- `--rsi-oversold` RSI超卖（RSI<30）
- `--boll-breakout` 布林带上轨突破
- `--boll-breakdown` 布林带下轨跌破
- `--limit-up` 涨停/接近涨停
- `--limit-down` 跌停/接近跌停

示例：
```bash
# 价值股 + 均线多头 + MACD金叉
node skills/stock-screener/index.js --preset value --ma-bullish --macd-golden --limit 5

# 超跌反弹：RSI超卖 + 低估值
node skills/stock-screener/index.js --preset value --rsi-oversold --limit 5

# 强势突破：量比>3 + 布林带上轨突破
node skills/stock-screener/index.js --volume-ratio '>3' --boll-breakout --limit 5
```

## 常用条件

- `--pe 0-30` 市盈率 0~30 倍
- `--pb 0-3` 市净率 0~3 倍
- `--turnover-rate 1-10` 换手率 1%~10%
- `--change-pct -5-5` 涨跌幅 -5%~5%
- `--volume-ratio ">2"` 量比大于 2
- `--market-cap 50-500` 总市值 50~500 亿
- `--min-price 10` 最低价 >= 10 元
- `--max-price 100` 最高价 <= 100 元
- `--sort-by pe` 按 PE 排序（默认降序）
- `--sort-asc` 升序排序（默认降序）
- `--file <path>` 将结果保存到文件（支持 csv/markdown 输出）

## 输出格式

- `text`（默认）
- `json`
- `markdown`
- `csv`

## 快速预设

- `--preset value` 价值型：PE<20, PB<3, 量比>1
- `--preset growth` 成长型：PE 20-50, 量比>2, 涨幅>0
- `--preset dividend` 高股息：PE<15, PB<2, 换手率 0.5-5
- `--preset momentum` 动量型：量比>2, 涨幅>1%, 换手率 1-10

预设可与其它筛选条件叠加。

## 数据源

- 股票列表：AKShare（Sina 财经接口），每日更新
- 实时行情：腾讯财经 API（qt.gtimg.cn），GBK 编码
- 自动解码中文，支持批量查询（每批最多 50 只）
- 非交易时间显示最近一个交易日数据

## 每日自动分析

建议设置定时任务，每个交易日收盘后自动运行：

```bash
# 示例：每个交易日 15:35 运行价值型筛选
node skills/stock-screener/index.js --preset value --limit 10 --output markdown --file daily_recommend.md
```
