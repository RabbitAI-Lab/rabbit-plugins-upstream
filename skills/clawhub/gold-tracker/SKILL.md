# 黄金追踪 — 智能体操作手册

## 安装后初始化

安装此技能后，**必须先运行初始化脚本**：

```bash
python3 scripts/setup.py
```

该脚本会完成以下工作：
1. 检查 Python 版本（>=3.8）
2. 创建所需目录（`logs/` `archive/` `alerts/` `.cache/`）
3. 验证所有脚本和配置文件完整
4. 初始化 `state.json`（首次为空状态，`fetch.py` 运行后填入真实数据）
5. 运行健康检查

**初始化完成前不要执行其他命令。** 如果 `setup.py` 报错，修复后重新运行。

---

## 运行流程

每次运行黄金追踪时，按以下顺序执行。这是一个完整的分析周期：

### 第1步：获取数据

```bash
python3 scripts/fetch.py
```

- 从 `goldpricez.com` 获取美元金价，从 `open.er-api.com` 获取 USD/CNY 汇率
- 自动验证价格范围（$1000-$10000, 汇率 6.0-8.0），异常值会被拒绝
- 更新 `state.json` 中的 `current_price`、`last_price`、`change_pct` 等字段
- 5分钟内重复运行会使用缓存，避免频繁请求

**输出**：JSON 格式的价格数据，同时更新 `state.json`。

### 第2步：市场分析（智能体核心工作）

这是**你的工作**，不是脚本能完成的。读取 `state.json` 获取当前价格后：

1. **搜索新闻**：用 `web_search` 搜索当前影响金价的因素（见下方「新闻搜索」章节）
2. **读取来源**：用 `web_fetch` 读取找到的文章，提取关键信息
3. **推理判断**：对每个因素判断方向（bullish/bearish/mixed/neutral）并给出因果链
4. **综合判断**：权衡各因素权重，形成一句话核心判断

### 第3步：写入分析日志

将分析结果写入 `logs/YYYY-MM-DD.yaml`（同一天多次运行则追加新的 YAML 文档）：

```yaml
---
run_id: "20260723-1430"
timestamp: "2026-07-23T14:30+08:00"
price_data:
  gold:
    price_usd: 4090.09
    price_cny: 893.45
  fx:
    usd_cny: 6.78
    source: open.er-api.com
summary:
  focus: "一句话描述当前主线"
key_factors:
  - factor: "FOMC 即将召开会议"
    impact: "bearish"
    reasoning: "这个因素如何影响金价"
sources:
  - "https://..."
```

**影响方向值**（必须使用这些）：
`bullish` · `bearish` · `mixed` · `neutral` · `slightly_bullish` · `slightly_bearish`

### 第4步：更新完整分析

将完整分析写入 `analysis.md`（**覆盖更新**，不是追加）。格式参考现有 `analysis.md` 文件。

### 第5步：检测提醒

```bash
python3 scripts/alert_manager.py detect
```

- 基于动态阈值检测价格异动
- 对比多个基准（last_price、开盘价、24小时均价）
- 触发后自动创建提醒记录到 `alerts/YYYY-MM-DD.json`
- 同类提醒30分钟冷却期，每日最多10条

如果有提醒触发，你可以将其标记为已发送：
```bash
python3 scripts/alert_manager.py status <alert_id> sent
```

### 第6步：生成摘要

```bash
python3 scripts/summary.py brief   # 简报（用于推送）
python3 scripts/summary.py full    # 完整摘要
```

简报从 `state.json` 和当日最新日志生成。**审核内容后**再发送给用户。

### 第7步：维护（定期执行）

```bash
python3 scripts/normalize.py              # 标准化日志中的时间戳和影响方向
python3 scripts/archive_manager.py archive # 归档非当日日志到 archive/YYYY-MM/
python3 scripts/alert_manager.py auto_resolve  # 自动解决超时提醒
python3 scripts/alert_manager.py cleanup  # 清理30天前的提醒记录
```

或一键执行：
```bash
python3 scripts/validate.py && python3 scripts/normalize.py && python3 scripts/archive_manager.py archive && python3 scripts/alert_manager.py auto_resolve && python3 scripts/alert_manager.py cleanup
```

---

## 运行频率

数据获取由 crontab 自动调度（纯脚本，不消耗 token）；分析由智能体在关键时段主动触发（消耗 token）。详见下方「定时调度」章节。

| 操作 | 频率 | 调度方式 | Token 消耗 |
|------|------|----------|------------|
| `fetch.py` | 每 30 分钟 | cron | 无（纯脚本） |
| `alert_manager.py detect` | 每次 fetch 后 | cron | 无（纯脚本） |
| 市场分析 + 写日志 | 每日 4 次（关键时段） | 智能体主动触发 | 有 |
| `summary.py brief` | 每次分析后 | 智能体主动触发 | 无（纯脚本） |
| `alert_manager.py auto_resolve` | 每日 1 次（02:00） | cron | 无 |
| `alert_manager.py cleanup` | 每日 1 次（02:30） | cron | 无 |
| `archive_manager.py archive` | 每日 1 次（23:30） | cron | 无 |
| `normalize.py` | 每周 1 次（周一 03:30） | cron | 无 |
| `validate.py` | 每次维护时 | 智能体主动触发 | 无 |
| `archive_manager.py cleanup` | 每月 1 次（03:00） | cron | 无 |

**关键时段（智能体应主动触发分析）**：
- `09:00` 亚洲盘开盘
- `15:00` 欧洲盘开盘
- `21:00` 美国盘开盘
- `01:00` 美盘尾盘

---

## 定时调度（crontab）

安装此技能的智能体（如 OpenClaw）**应自动配置 crontab** 来执行纯脚本任务。以下为推荐配置模板（路径需替换为实际安装路径）：

```cron
# ===== 黄金追踪 crontab 配置 =====
# 假设 SKILL_PATH=/path/to/gold-tracker

# 数据获取 - 每 30 分钟
*/30 * * * * cd /path/to/gold-tracker && python3 scripts/fetch.py >> logs/cron.log 2>&1

# 异动检测 - fetch 后延迟 30 秒执行，避免文件竞争
*/30 * * * * cd /path/to/gold-tracker && sleep 30 && python3 scripts/alert_manager.py detect >> logs/cron.log 2>&1

# 自动解决超时提醒 - 每日 02:00
0 2 * * * cd /path/to/gold-tracker && python3 scripts/alert_manager.py auto_resolve >> logs/cron.log 2>&1

# 清理过期提醒 - 每日 02:30
30 2 * * * cd /path/to/gold-tracker && python3 scripts/alert_manager.py cleanup >> logs/cron.log 2>&1

# 归档非当日日志 - 每日 23:30
30 23 * * * cd /path/to/gold-tracker && python3 scripts/archive_manager.py archive >> logs/cron.log 2>&1

# 标准化日志 - 每周一 03:30
30 3 * * 1 cd /path/to/gold-tracker && python3 scripts/normalize.py >> logs/cron.log 2>&1

# 清理过期归档（>365天）- 每月 1 日 03:00
0 3 1 * * cd /path/to/gold-tracker && python3 scripts/archive_manager.py cleanup >> logs/cron.log 2>&1
```

**安装时智能体应执行**：
1. 将上述模板中的 `/path/to/gold-tracker` 替换为实际安装路径
2. 写入用户 crontab（`crontab -e` 或 `crontab < file`）
3. 验证 `crontab -l` 中已包含相关条目
4. 检查 `logs/cron.log` 是否有写入权限

**注意事项**：
- 市场分析（步骤 2-4）**不放入 cron** —— 分析消耗 token 且需要智能体推理判断
- 异动检测仅推送提醒，**不立即触发分析**；异动累积到下一个定时分析节点统一处理
- 周末/节假日 cron 仍会运行 fetch，但金价几乎无波动，无副作用
- 若 `cron.log` 超过 1MB，智能体应主动清理或轮转

---

## 新闻搜索：保持灵活

**不要局限于固定的信息来源。** 黄金的驱动因素随时间变化 —— 搜索当前影响市场的任何因素。

搜索角度（仅示例，非清单）：
- 美联储政策 / 利率
- 地缘政治冲突
- 通胀数据（CPI、PCE）
- 央行购金
- 美元指数（DXY）
- 实际利率
- ETF 资金流向 / 持仓
- 季节性模式

找到最佳来源，用 `web_fetch` 读取，引用它们。如果某个维度找不到数据，**跳过它 —— 不要编造**。

---

## 三条铁律

1. **每个数据点都要有来源 URL** — 不输出裸结论
2. **每个判断都要有因果链** — 说明为什么看多/看空
3. **不编造** — 没有数据就留白，不补全

---

## 状态文件（state.json）

`fetch.py` 运行后自动更新。读取它来获取最新价格，避免重复请求：

```json
{
  "date": "2026-07-23",
  "current_price": 4090.09,
  "last_price": 4100.00,
  "change_pct": -0.24,
  "change_abs": -9.91,
  "price_cny_per_gram": 893.45,
  "usd_cny": 6.78,
  "last_update": "2026-07-23T14:30+08:00",
  "sources": {"gold": "goldpricez.com", "fx": "open.er-api.com"},
  "key_data": {"open": 4120.43, "high": 4141.26, "low": 4086.97, "change_today": "-0.74%"}
}
```

**不要手动编辑 `state.json`**，它由 `fetch.py` 自动维护。

---

## 提醒系统

基于**动态阈值**的智能提醒系统：

1. **动态阈值**：根据过去7天波动率自动调整（默认 ±1%，范围 0.5%-3%）
2. **多基准比较**：同时对比 last_price、当日开盘价、24小时均价
3. **防震荡机制**：同类提醒30分钟冷却期，每日最多10条提醒
4. **状态管理**：pending → sent → acknowledged → resolved/dismissed
5. **自动清理**：24小时未处理自动标记resolved，30天后删除

```bash
python3 scripts/alert_manager.py detect          # 检测并创建提醒
python3 scripts/alert_manager.py list            # 列出活跃提醒
python3 scripts/alert_manager.py status <id> <status>  # 更新状态
python3 scripts/alert_manager.py auto_resolve    # 自动解决超时提醒
python3 scripts/alert_manager.py cleanup         # 清理过期提醒
python3 scripts/alert_manager.py threshold       # 查看当前动态阈值
```

提醒类型：
- `price_breakout_high/low` — 突破阈值的涨跌提醒
- `price_reversal_up/down` — 反转方向提醒（变动达阈值70%）

---

## 归档系统

```bash
python3 scripts/archive_manager.py archive       # 归档所有非当日日志
python3 scripts/archive_manager.py find <date>   # 查询某日历史记录
python3 scripts/archive_manager.py history <days> # 获取价格历史
python3 scripts/archive_manager.py cleanup       # 清理过期归档（>365天）
python3 scripts/archive_manager.py rebuild       # 重建索引
python3 scripts/archive_manager.py summary       # 显示索引摘要
```

归档文件命名：`YYYY-MM-DD-HHMM.yaml`（统一格式，避免冲突）

---

## 目录职责

| 路径 | 内容 | 生命周期 |
|------|------|----------|
| `logs/` | 当日 YAML 日志 | 自动归档（非当日） |
| `archive/YYYY-MM/` | 历史日志 | 365天 |
| `archive/index.json` | 归档索引 | 自动更新 |
| `alerts/` | 价格提醒 JSON | 30天 |
| `analysis.md` | 当前完整分析 | 覆盖更新 |
| `state.json` | 最新价格快照 | 自动更新 |
| `.cache/` | HTTP 响应缓存 | 自动过期（5分钟） |

---

## 错误处理

### fetch.py 失败

| 错误 | 原因 | 处理 |
|------|------|------|
| 金价获取失败 | 网络问题或 goldpricez.com 不可用 | 等待5分钟后重试；仍失败则使用上次 `state.json` 中的价格 |
| 汇率获取失败 | open.er-api.com 不可用 | 同上；可手动查询汇率并告知用户 |
| 金价异常 | 价格超出 $1000-$10000 范围 | 数据源可能返回错误数据，不要使用该价格 |
| state.json 不存在 | 首次运行或被误删 | 运行 `python3 scripts/setup.py` 重新初始化 |

### 数据源不可用时的降级策略

1. 优先使用缓存数据（`.cache/` 目录，5分钟有效）
2. 缓存过期则使用 `state.json` 中的最后已知价格
3. 在分析中明确标注「数据可能过期」
4. **不要使用过期数据触发提醒**

### validate.py 报告错误

- **state.json 缺少字段**：运行 `python3 scripts/setup.py` 修复
- **日志缺少 run_id 或 price_usd**：手动补全或删除该日志
- **impact 未标准化**：运行 `python3 scripts/normalize.py`
- **提醒 JSON 格式错误**：删除该提醒文件，系统会重新生成

---

## 脚本参考

| 脚本 | 作用 | 何时运行 |
|------|------|----------|
| `setup.py` | 环境初始化 | 安装后首次运行 |
| `fetch.py` | 获取金价和汇率 | 每次分析开始时 |
| `validate.py` | 验证项目完整性 | 维护时 |
| `normalize.py` | 标准化日志格式 | 每周1次 |
| `alert_manager.py` | 提醒检测与管理 | 每次 fetch 后 |
| `archive_manager.py` | 归档与历史查询 | 每日1次 |
| `summary.py` | 生成简报/摘要 | 每次分析后 |
| `dedup.py` | 旧版提醒去重（legacy） | 仅处理 .md 格式提醒时 |

---

## 推送通知格式（<2000 字节）

```
🥇 **黄金追踪** · MM-DD

💰 **金价**: $X,XXX.XX (+X.XX, +X.XX%)

| 因素 | 方向 | 逻辑 | 来源 |
|------|------|------|------|
| 标题 | 🟢 | 原因 | site.com |

**点评**: 一句话综合判断

来源: site · site · site
```
