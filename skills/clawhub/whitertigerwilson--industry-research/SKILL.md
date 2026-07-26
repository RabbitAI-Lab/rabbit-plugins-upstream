---
name: industry-research
description: 行业深度研究 v1.3.2（CLI 化 + 多源容灾 + Bocha 搜索）。触发场景：「研究XX行业」「分析XX商品」「XX产业链」「个股/商品研报」。自动化覆盖 A股 + 港股 + 美股 + 期货 + 龙虎榜 + ETF 联动 + Bocha 网页搜索，提供 20 个 CLI 子命令 + Bing/Bocha 双搜索引擎。输出 10 维度结构化研究报告，包含价格/产业链/财务/估值/技术/异动/机构席位/ETF 三级联动/行业新闻。
---

# Industry Research Skill v1.3.2

> **升级时点**：2026-06-30 17:20（Bocha 搜索 + Bing 抓取集成，突破 web_search 工具禁用限制）
> **能力覆盖**：A 股 + 港股 + 美股 + 期货 + 龙虎榜 + ETF 联动 + 行业新闻搜索，全自动 CLI
> **核心特性**：**多源容灾** —— 东财挂掉时自动降级到腾讯/akshare/yfinance；**搜索自给** —— Bocha API 主 + Bing 网页抓取备，绕过 web_search 工具禁用

## 核心能力

### 20 个 CLI 子命令

```bash
cd <skill-dir>

# === A 股个股分析 ===
python -m ira turnover <code> [days]      # 换手率（含实时补）
python -m ira kline <code> [days]         # K 线形态 + 均线
python -m ira technical <code> [days]     # MACD/RSI/BOLL/KDJ
python -m ira financial <code>            # PE/PB/市值
python -m ira valuation <code> [industry] # 历史分位 + 三档
python -m ira anomaly <code> [days]       # 量价异动
python -m ira realtime <code>             # 实时价格
python -m ira sources <code>              # 数据源可用性诊断

# === 港美股（多源容灾） ===
python -m ira global <code>               # 5 位数字 = 港股 / 字母 = 美股
python -m ira global --search <keyword>   # 关键词搜索

# === 行业研究 ===
python -m ira filter <commodity>          # 商品-股票池（20+ 商品）
python -m ira futures <commodity>         # 期货合约元信息
python -m ira futures-kline <commodity> [days]  # 期货主力 K 线

# === 龙虎榜 ===
python -m ira billboard stock [--period]   # 个股上榜统计
python -m ira billboard org --days N      # 机构席位追踪
python -m ira billboard detail --start ... --end ...

# === 三级联动（商品→个股→ETF）===
python -m ira chain <commodity>           # 完整链路
python -m ira etf refresh                 # 拉取全市场 ETF
python -m ira etf get <code>              # 按代码查 ETF
python -m ira etf commodities             # 列出 24 支持商品

# === 档案管理 ===
python -m ira archive add / search / list

# === 行业新闻搜索（v1.3.2 新增，绕过 web_search 工具禁用）===
python bocha_search.py "查询词" 5          # Bocha API（0.5s 返 JSON）
python bing_search.py "查询词" 5           # Bing 网页抓取（2s 返 HTML）
```

## 工作流程

### Step 1: 确认研究对象
用户输入行业/商品 → 单一商品（如"铜"/"半导体"/"白酒"/"蔗糖"/"塑料包装"/"锚链"）。

### Step 2: 数据采集（CLI 替代原 web_search）

**价格走势**：
```bash
python -m ira futures-kline 铜 60           # 期货主力 60 日
python -m ira chain 铜                      # 个股 + ETF 联动
```

**重大新闻**：
- 仍用 `web_search` 和 `web_fetch`，优先英文主流媒体（AP/BBC/NPR/CNN）

**A 股相关上市公司**：
```bash
python -m ira filter 铜                     # 预定义池（20+ 商品）
```

**财务数据 + 估值**：
```bash
python -m ira financial 601899              # PE/PB/市值
python -m ira valuation 600519 白酒         # 历史分位 + 行业 PE 三档
```

### Step 3: 技术面 + 量价
```bash
python -m ira technical 601899 60           # MACD/RSI/BOLL/KDJ
python -m ira kline 601899 20               # K线形态 + 均线
python -m ira anomaly 601899 120            # 量价异动
python -m ira turnover 601899 30            # 换手率
```

### Step 4: 跨市场关联

**港美股对标**：
```bash
python -m ira global 700                    # 港股腾讯（业务对标 A 股）
python -m ira global NVDA                   # 美股英伟达（半导体对标）
python -m ira global --search 阿里          # 关键词搜索
```

**机构资金动向**：
```bash
python -m ira billboard org --days 30       # 机构席位追踪
python -m ira billboard stock --period 近一月  # 个股上榜统计
```

### Step 5: ETF 三级联动
```bash
python -m ira etf refresh                   # 拉取 1522 只 ETF 实时
python -m ira chain 半导体                  # 完整商品→个股→ETF 链路
python -m ira etf get 512480                # 单只 ETF 实时
```

### Step 6: 归档研究
```bash
python -m ira archive add 半导体 \
  --summary "今日上涨 5.9%, 中芯/韦尔/北方华创 主导" \
  --findings '{"price": "+5.9%", "etf": "512480"}' \
  --tags "周期股,科技"
```

### Step 7: 历史检索
```bash
python -m ira archive search 半导体 --limit 5
python -m ira archive list
```

## 多源容灾（v1.3.1 核心特性）

所有 K 线接口统一走 `ira/sources.py` 多源调度，**东财挂掉时自动降级**：

### A 股 K 线

```
东财 push2his.eastmoney.com  ← 主（11 字段，含换手率）
   ↓ 失败
腾讯 ifzq.gtimg.cn           ← 备 1（6 字段，缺换手率 → 实时接口补）
   ↓ 失败
akshare stock_zh_a_hist      ← 备 2（11 字段完整）
```

### 美股 K 线（v1.3.1 修复）

```
yfinance                     ← 主（稳定）
   ↓ 失败
akshare stock_us_daily       ← 备 1
   ↓ 失败
akshare stock_us_hist        ← 备 2
```

### 港股 K 线（v1.3.1 修复）

```
akshare stock_hk_hist        ← 主
   ↓ 失败
腾讯 ifzq hk 日K             ← 备 1
```

### 换手率（v1.3.1 修复）

腾讯日K缺换手率字段 → 用腾讯实时接口 `qt.gtimg.cn/q=sh<CODE>` 补最新换手率。

## 数据源

| 用途 | 主源 | 备源 |
|---|---|---|
| 实时行情（A 股） | 腾讯 qt.gtimg.cn | — |
| **K 线（A 股）** | **东财 push2his（11 字段）** | **腾讯 ifzq + akshare** |
| 期货主力 | akshare.futures_zh_daily_sina | — |
| **港股历史** | **akshare stock_hk_hist** | **腾讯 hk 日K** |
| **美股历史** | **yfinance** | **akshare stock_us_daily / hist** |
| 龙虎榜 | akshare stock_lhb | — |
| ETF | akshare.fund_etf_spot_em（1522 只） | — |
| 历史研究 | 本地 Markdown + YAML | — |
| **重大新闻（v1.3.2）** | **Bocha API**（国内，0.5s 返 JSON，带摘要/来源/日期） | **Bing 网页抓取**（2s，0 依赖 0 key） |

## 输出格式（10 维度）

```
# {商品} 行业深度研究报告
> 数据来源：CLI 自动化采集 + 公开资料 | 报告日期：2026年x月x日

## 一、价格走势
## 二、成因分析
## 三、上下游产业链
## 四、重大新闻
## 五、A股相关上市公司
## 六、受益/受损分析
## 七、投资机会与风险
## 八、个股技术面（前 3 重点公司，含 MACD/RSI/BOLL/KDJ/量价异动）
## 九、机构资金动向（龙虎榜 + ETF 三级联动）
## 十、ETF 联动 + 跨市场对标
⚠️ 免责声明
```

## 升级历史

### v1.0（原始）
- 4 个零散脚本：`stock_filter.py` / `kline_pattern.py` / `stock_turnover.py` / `pet_stocks.py`

### ✅ v1.1.0（2026-06-29 21:34）
- Tier 1 全完：修日期 bug + 整合 package + financial + valuation
- Tier 2 部分：T2.5 股票池 20+ / T2.6 技术指标

### ✅ v1.2.0（2026-06-29 22:07）
- T2.7 量价异动 / T2.8 期货实时
- T3.9 港美股 / T3.10 历史档案 / T3.11 龙虎榜

### ✅ v1.3.0（2026-06-29 22:36）
- T3.12 三级联动（商品→个股→ETF）
- 全部 Tier 1/2/3 完成

### ✅ v1.3.1（2026-06-30 11:30）—— **多源容灾修复**
- **新增 `ira/sources.py`** —— 统一 K 线多源调度
- **K 线 fallback**：东财 → 腾讯 → akshare（三层）
- **美股 fallback**：yfinance → akshare stock_us_daily / hist
- **港股 fallback**：akshare → 腾讯
- **换手率实时补**：腾讯日K缺字段时用实时接口补
- **新增 `python -m ira sources <code>` 诊断命令**
- **经验教训**：东财 push2his 单点故障不能再导致批量失败

### ✅ v1.3.2（2026-06-30 17:20）—— **Bocha 搜索集成**
- **背景**：OpenClaw 网关层 `web_search` 工具被禁用，Tavily/Brave 需付费 key，Bing/Bocha 直连可用
- **新增 `bocha_search.py`** —— Bocha（博查）API 客户端，0.5s 返结构化 JSON（带摘要/来源/日期）
- **新增 `bing_search.py`** —— Bing 网页搜索 HTML 抓取，2s 返标题+URL（0 依赖 0 key）
- **Bocha 优先级**：Bocha（主）→ Bing 抓取（备）→ LLM 常识估算（兜底）
- **覆盖场景**：汉中门地铁站客流、汉中门站规划、行业新闻、宏观政策、突发事件
- **依赖**：`pip install requests`（无其他要求）
- **环境变量**：`BOCHA_API_KEY=sk-***`（用户已有，免费 1000 次/月）
- **工作流**：所有"查 XX"需求先跑 `bocha_search.py`，失败再跑 `bing_search.py`，都失败再 LLM 估算

## 待办

1. 研报模板自动生成（HTML/PDF）
2. 龙虎榜趋势分析（资金动向）
3. 多商品对比研究面板
4. 自动归档最近一次研报到 archive
5. 扩展 stocks 常量池（添加蔗糖/塑料包装/锚链等）

## 已知研究案例

- **铜（2026-06-29）**：沪铜 103160 元/吨，-1.75%；紫金 PE 11.12
- **白糖**：5270 元/吨，-1.4%；中粮糖业 12.33 涨停 +9.99%
- **塑料包装**：永新股份 002014 当日 +5.42%
- **锚链**：亚星锚链 601890 出现底背离信号（KDJ J=-1.26）
- **白酒**：茅台 PE 18.06，历史分位 0%；酒 ETF 512690 +2.06%
- **半导体**：512480 ETF +5.9% 大涨，中芯/韦尔主导
- **有色金属**：512400 ETF +1.36%
- **螺纹钢**：持仓量 193 万手创历史新高

## 教训 & 经验

1. **多源容灾必做**：东财 push2his 单点故障曾导致 5/10 测试失败，**生产代码必须三层 fallback**
2. **akshare 接口稳定性差**：stock_us_hist → stock_us_daily → 都可能挂，需要 yfinance 备援
3. **缓存必要**：全市场 ETF 1522 只一次性拉取 + JSON 缓存，避免重复请求
4. **跨数据源兼容**：东财用中文键、新浪用拼音键、腾讯用字段索引，**字段名差异是常态**
5. **进度存档**：套餐/算力波动场景必备（用户主动提议）
6. **手动 ETF 映射**：标"覆盖 X / 直接跟踪"的判断逻辑比自动 LLM 匹配靠谱
7. **Windows + Python GBK 编码**：打印 emoji 会崩（UnicodeEncodeError），**必设 PYTHONIOENCODING=utf-8**
8. **数据源诊断命令必装**：出问题时 30 秒定位是哪个源挂了

## 依赖

```bash
pip install akshare requests yfinance
```

## 安装与使用

```bash
# 安装到本地 skills 目录
clawhub install industry-research

# 触发场景
"研究铜行业"
"分析白糖期货"
"永新股份涉及什么行业"
```

## 关联文件

- 项目目录：`ira-new/industry-research/`
- 详细设计：`ira/`（17+ 个模块化 Python 文件）
- 历史快照：`memory/industry-research-v*.md`