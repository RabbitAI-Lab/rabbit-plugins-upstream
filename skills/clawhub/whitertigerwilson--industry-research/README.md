# industry-research skill（升级版 v1.3.0）🎉

> **状态：Tier 1 / 2 / 3 全部 12 项升级完成**（2026-06-29 23:29）
> 总耗时：~80 分钟（5 次会话）
> Skill proposal：`industry-research-20260629-eb9634ca14`（pending，待你点头 apply）

## 包结构（18 个模块）

```
ira/
├── __init__.py
├── __main__.py        # python -m ira <cmd>
├── cli.py             # 命令行路由（20 个子命令）
├── api_client.py      # 统一 HTTP 客户端（带 retry + 限流保护）
├── constants.py       # 20+ 商品股票池（KNOWN_MAP）
├── stock_data.py      # 商品筛选 / 实时价格
├── turnover.py        # 换手率分析
├── kline.py           # K线形态 + 均线排列
├── financial.py       # 财务摘要（PE/PB/市值/换手率）
├── valuation.py       # 历史价格分位 + PE 三档评估
├── technical.py       # MACD/RSI/BOLL/KDJ
├── anomaly.py         # 量价异动检测
├── futures.py         # 期货主力连续（akshare 实时）
├── global_stocks.py   # 港股 + 美股（33 个热门）
├── billboard.py       # 龙虎榜 + 机构席位追踪
├── etf_chain.py       # 三级联动（商品→个股→ETF，24 商品映射）
├── report.py          # **HTML 研报生成**（深色主题，单文件）
└── archive.py         # 历史研究案例库

data/etf_spot.json     # 1522 只 ETF 实时缓存
reports/               # 自动生成的 HTML 研报
tests/test_smoke.py    # 端到端冒烟测试（11/11 通过）
```

## CLI 全命令（20 个）

```bash
cd C:\Users\86182\.openclaw\workspace\ira-new\industry-research

# === A 股 ===
python -m ira turnover <code> [days]          # 换手率
python -m ira kline <code> [days]             # K线形态 + 均线
python -m ira technical <code> [days]         # MACD/RSI/BOLL/KDJ
python -m ira financial <code>                # PE/PB/市值
python -m ira valuation <code> [industry]     # 历史分位 + 三档
python -m ira anomaly <code> [days]           # 量价异动
python -m ira realtime <code>                 # 实时行情

# === 港美股 ===
python -m ira global <code>                   # 港股 5 位 / 美股字母
python -m ira global --search <keyword>       # 关键词搜索

# === 行业研究 ===
python -m ira filter <commodity>              # 商品-股票池（20+ 商品）
python -m ira futures <commodity>             # 期货合约元信息
python -m ira futures-kline <commodity> [days]  # 期货主力 K 线

# === 龙虎榜 ===
python -m ira billboard stock [--period 近一月]  # 个股上榜统计
python -m ira billboard org --days 30          # 机构席位追踪
python -m ira billboard detail --start ... --end ...  # 龙虎榜详情

# === 三级联动（商品→个股→ETF）===
python -m ira chain <commodity>               # 完整链路
python -m ira etf refresh                     # 拉取全市场 ETF
python -m ira etf get <code>                  # 按代码查 ETF
python -m ira etf commodities                 # 列出 24 支持商品

# === HTML 研报 ===
python -m ira report [commodity]              # 单商品或全部今日归档
# (输出深色主题 HTML 到 reports/ 目录)

# === 档案 ===
python -m ira archive add / search / list
```

## 数据源

| 用途 | 主源 |
|---|---|
| 实时行情（A 股） | 腾讯 qt.gtimg.cn |
| K 线（A 股） | 东方财富 push2his.eastmoney.com |
| 期货主力连续 | akshare.futures_zh_daily_sina |
| 港股 | akshare.stock_hk_hist |
| 美股 | akshare.stock_us_daily（新浪） |
| 龙虎榜 | 东方财富 + 新浪（akshare） |
| ETF 实时 | akshare.fund_etf_spot_em（1522 只） |
| 历史研究 | 本地 Markdown + YAML |
| 重大新闻 | AP/BBC/NPR/CNN（用户偏好海外媒体） |

## 升级历史

### ✅ Tier 1（必做）4/4
- T1.1 修硬编码日期 bug（end=20500101）
- T1.2 整合为 ira package
- T1.3 financial.py
- T1.4 valuation.py

### ✅ Tier 2（值得做）4/4
- T2.5 股票池 20+ 商品
- T2.6 技术指标 MACD/RSI/BOLL/KDJ
- T2.7 量价异动
- T2.8 期货实时

### ✅ Tier 3（进阶）4/4
- T3.9 港股 + 美股
- T3.10 历史研究案例库
- T3.11 龙虎榜 + 机构席位
- T3.12 三级联动（商品→个股→ETF）

## 实证发现（2026-06-29 close）

### A 股 + 商品
- 沪铜 06/29 收 **103160 元/吨**，5 日累跌 **-1.75%**
- 紫金矿业 PE 11.12（合理），KDJ 严重超卖（J=-3.88）
- 螺纹钢持仓量 **193 万手**（历史新高）
- 黄金 5 日 -3.08%

### 港美股
- 腾讯 420.2 港元 / 阿里 93 港元
- AAPL $283.78 / NVDA $192.53 / TSLA $379.71

### 龙虎榜（近 30 天净买入 TOP）
- 东山精密 **38.5 亿**
- 光库科技 **35.5 亿**
- 厦门钨业 **20.7 亿**
- TCL 科技 **20.4 亿**

### 三级联动亮点（半导体大涨）
- 512480 国联安半导体 ETF：2.909，**+5.9%** 🚀
- 159995 华夏国证半导体芯片 ETF：3.298，+5.47%
- 酒 ETF 512690：+2.06%
- 有色金属 ETF 512400：+1.36%

## 验证

```
$ python tests/test_smoke.py
11/11 通过 🎉
```

## 待办

1. **`skill_workshop` proposal 待你点头 apply**（proposal_id: `industry-research-20260629-eb9634ca14`）
2. 修 memory search（配 OpenAI key 或换 local embedding）
3. HTML 研报样式优化（PDF 输出 / 中文图表）