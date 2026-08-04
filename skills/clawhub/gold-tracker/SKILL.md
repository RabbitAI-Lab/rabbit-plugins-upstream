# 黄金追踪 — 智能体操作手册

> 本文档使用 RFC 2119 关键词：**MUST**（必须）/ **MUST NOT**（不得）/ **SHOULD**（应当）。
> 任何违反 MUST/MUST NOT 的输出都会被 `check_analysis.py` 拒绝，本次分析视为失败。

---

## 0. 三条铁律（先读这一段）

1. **每个数据点 MUST 有来源 URL** —— 不输出裸结论。
2. **每个判断 MUST 有因果链** —— 说明为什么看多/看空，并显式引用至少 1 条 source URL。
3. **不得编造** —— 没有数据时 MUST 使用占位值 `no_data`，绝不补全、绝不臆测。

违反任意一条，`check_analysis.py` 都会以非零退出码拒绝本次分析。这意味着你不能宣布"分析完成"。

---

## 1. 安装后初始化

安装此技能后，**MUST 先运行**：

```bash
python3 scripts/setup.py
```

该脚本会检查 Python 版本（>=3.8）、创建目录、验证脚本完整、初始化 `state.json`、运行健康检查。

**初始化完成前 MUST NOT 执行其他命令。** 如果 `setup.py` 报错，修复后重新运行。

---

## 2. 运行流程（每次分析周期）

按以下顺序执行。每一步都标注了**输入 → 动作 → 输出 → 自检**四件套。

### 第 1 步：获取数据

| 项 | 内容 |
|---|---|
| 输入 | 无（自动从远程拉取） |
| 动作 | `python3 scripts/fetch.py` |
| 输出 | JSON 打印到 stdout，同时更新 `state.json` |
| 自检 | stdout 中 `price_usd > 0` 且 `errors` 为空 |

- 从 `goldpricez.com` 获取美元金价，从 `open.er-api.com` 获取 USD/CNY 汇率
- 自动验证价格范围（$1000-$10000, 汇率 6.0-8.0），异常值会被拒绝
- 5 分钟内重复运行会使用缓存

### 第 2 步：市场分析（智能体核心工作）

这是**你的工作**，不是脚本能完成的。读 `state.json` 取当前价格后，按以下子步骤执行：

#### 2.1 搜索新闻（web_search）

| 项 | 内容 |
|---|---|
| 输入 | `state.json` 中的当前价格 |
| 动作 | 用 `web_search` 检索当前影响金价的因素 |
| 输出 | 一组候选 URL |
| 自检 | 候选 URL 覆盖 ≥ 2 个独立域名（防止单源依赖） |

**MUST**：搜索角度随当前市场动态选择，**MUST NOT** 局限于固定来源。参考方向（仅示例，非清单）：
- 美联储政策 / 利率 / 降息预期
- 地缘政治冲突
- 通胀数据（CPI、PCE）
- 央行购金
- 美元指数（DXY）
- 实际利率
- ETF 资金流向 / 持仓
- 季节性模式

**来源多样性约束**：整篇分析最终 MUST 覆盖 ≥ 2 个独立域名（见 [config.yaml](file:///Users/jeromexqian/Projects/gold-tracker/config.yaml) `output.constraints.min_unique_domains`）。

#### 2.2 抓取并记录每个 URL（关键：反幻觉关卡）

| 项 | 内容 |
|---|---|
| 输入 | 2.1 选出的候选 URL |
| 动作 | 对每个 URL 执行：(a) `web_fetch <url>` 读取内容；(b) **立即** `python3 scripts/log_fetch.py <url> "<标题>"` 记录 |
| 输出 | `.cache/fetch_log.json` 中累积已抓取的 URL |
| 自检 | `python3 scripts/log_fetch.py list` 显示的 URL 数 ≥ 2，且覆盖 ≥ 2 个独立域名 |

**MUST**：每次 `web_fetch` 之后**立即**调用 `log_fetch.py` 记录该 URL。未记录的 URL 不会通过第 4 步的 sources 校验。

**MUST NOT**：在 `sources` 字段中写入未出现在 `fetch_log.json` 中的 URL —— 这会被识别为"凭空编造来源"并拒绝本次分析。

#### 2.3 推理判断

对每个因素判断方向并给出因果链。**MUST** 满足：

- `impact` MUST 取以下值之一（大小写敏感）：
  `bullish` · `bearish` · `mixed` · `neutral` · `slightly_bullish` · `slightly_bearish`
- `reasoning` MUST 是一条完整因果链（"因为 X → 所以 Y → 对金价影响 Z"），**MUST NOT** 是断言
- `reasoning` 中 MUST NOT 出现以下措辞（违反即拒绝）：
  `根据经验` / `众所周知` / `一般来说` / `通常情况下` / `据了解` / `据业内人士` / `显而易见`
- `reasoning` 中提到的任何数字/数据 MUST 在 sources 中能找到出处；找不到则 MUST 改写为定性描述或使用 `no_data`

#### 2.4 综合判断

权衡各因素权重，形成一句话核心判断（写入 `summary.focus`）。

**MUST NOT** 在 `summary.focus` 中使用上述禁用措辞。

### 第 3 步：写入分析日志

将本次分析追加到 `logs/YYYY-MM-DD.yaml`（同一天多次运行则追加新的 YAML 文档，用 `---` 分隔）。

#### 字段约束表（硬性）

| 字段 | 类型 | 必填 | 取值/格式 | 说明 |
|---|---|---|---|---|
| `run_id` | string | ✅ | `"YYYYMMDD-HHMM"` | 本次运行唯一 ID |
| `timestamp` | string | ✅ | ISO8601 带时区 `+08:00` | 例 `"2026-07-23T14:30+08:00"` |
| `price_data.gold.price_usd` | number | ✅ | 1000-10000 | 美元/盎司 |
| `price_data.gold.price_cny` | number | ✅ | > 0 | 元/克 |
| `price_data.fx.usd_cny` | number | ✅ | 6.0-8.0 | 美元兑人民币 |
| `price_data.fx.source` | string | ✅ | 任意 | 数据源标识 |
| `summary.focus` | string | ✅ | 非空，无禁用措辞 | 一句话核心判断 |
| `key_factors` | list | ✅ | 长度 2-6 | 至少 2 条，至多 6 条 |
| `key_factors[].factor` | string | ✅ | 非空 | 因素标题 |
| `key_factors[].impact` | string | ✅ | 枚举（见 2.3） | 方向 |
| `key_factors[].reasoning` | string | ✅ | 非空，无禁用措辞 | 因果链 |
| `key_factors[].sources` | list | ✅ | 长度 ≥ 1 | 该因素的支撑 URL |
| `sources` | list | ✅ | 长度 ≥ 2，覆盖 ≥ 2 域名 | 整篇分析的全部 URL |
| `sources[]` | string | ✅ | 合法 http(s) URL，且 MUST 在 fetch_log 中 | 顶层 sources 汇总 |

#### 模板（严格遵守）

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
  focus: "一句话描述当前主线（禁止使用'根据经验/众所周知'等措辞）"
key_factors:
  - factor: "FOMC 即将召开会议"
    impact: "bearish"
    reasoning: "因为 X → 所以 Y → 对金价影响 Z（因果链，引用来源中的具体数据）"
    sources:
      - "https://www.reuters.com/..."
  - factor: "央行持续购金"
    impact: "bullish"
    reasoning: "世界黄金协会数据显示 X 吨购入 → 需求端支撑 → 价格上行"
    sources:
      - "https://www.gold.org/..."
sources:
  - "https://www.reuters.com/..."
  - "https://www.gold.org/..."
```

**无数据时**：相应字段 MUST 填 `no_data`，**MUST NOT** 留空字符串，**MUST NOT** 编造。

### 第 4 步：通过硬校验门槛（关键）

**MUST** 依次运行以下两个命令，且都必须以 exit 0 通过：

```bash
python3 scripts/validate.py           # 项目级结构校验
python3 scripts/check_analysis.py     # 本次分析的反幻觉校验
```

`check_analysis.py` 会校验：
1. 顶层字段齐全（`run_id` / `timestamp` / `price_data` / `summary` / `key_factors` / `sources`）
2. `key_factors` 数量在 `[2, 6]` 之间
3. 每个 factor 含 `factor` / `impact` / `reasoning` / `sources` 四字段
4. `impact` 在允许枚举内
5. `sources` 是合法 http(s) URL
6. **每个 source URL MUST 出现在 `.cache/fetch_log.json` 中**（即真的 web_fetch 过）
7. 整篇 sources 覆盖 ≥ 2 个独立域名
8. 每个 factor 至少引用 1 条 source
9. `reasoning` 和 `summary.focus` 不含禁用措辞

**任意一条 ERROR 都意味着你不能宣布分析完成。** 必须修复日志后重新运行，直到通过为止。

### 第 5 步：更新完整分析

将通过校验的完整分析写入 `analysis.md`（**覆盖更新**，不是追加）。格式参考现有 `analysis.md` 文件。

### 第 6 步：检测提醒

```bash
python3 scripts/alert_manager.py detect
```

- 基于动态阈值检测价格异动
- 对比多个基准（last_price、开盘价、24 小时均价）
- 触发后自动创建提醒记录到 `alerts/YYYY-MM-DD.json`
- 同类提醒 30 分钟冷却期，每日最多 10 条

如果有提醒触发，可标记为已发送：
```bash
python3 scripts/alert_manager.py status <alert_id> sent
```

### 第 7 步：生成摘要

```bash
python3 scripts/summary.py brief   # 简报（用于推送）
python3 scripts/summary.py full    # 完整摘要
```

简报从 `state.json` 和当日最新日志生成。**审核内容后**再发送给用户。

### 第 8 步：维护（定期执行）

```bash
python3 scripts/normalize.py              # 标准化日志中的时间戳和影响方向
python3 scripts/archive_manager.py archive # 归档非当日日志到 archive/YYYY-MM/
python3 scripts/alert_manager.py auto_resolve  # 自动解决超时提醒
python3 scripts/alert_manager.py cleanup  # 清理 30 天前的提醒记录
```

或一键执行：
```bash
python3 scripts/validate.py && python3 scripts/normalize.py && python3 scripts/archive_manager.py archive && python3 scripts/alert_manager.py auto_resolve && python3 scripts/alert_manager.py cleanup
```

---

## 3. 输出前自检 Checklist

宣布"分析完成"前，**MUST** 逐条确认（任何一条 No 都不能宣布完成）：

- [ ] `python3 scripts/validate.py` 退出码 0
- [ ] `python3 scripts/check_analysis.py` 退出码 0
- [ ] `key_factors` 至少 2 条、至多 6 条
- [ ] 每个 factor 都有 `factor` / `impact` / `reasoning` / `sources`
- [ ] 所有 `impact` 都在 6 个标准值内
- [ ] 每个 factor 的 `sources` 至少 1 条 URL
- [ ] 整篇 `sources` 至少覆盖 2 个独立域名
- [ ] 每个 source URL 都在 `python3 scripts/log_fetch.py list` 的输出里
- [ ] `reasoning` 和 `summary.focus` 不含禁用措辞
- [ ] 没有数据的地方使用了 `no_data`，没有编造

---

## 4. 运行频率

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

## 5. 定时调度（crontab）

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

## 6. 新闻搜索：保持灵活 + 来源多样

**MUST NOT** 局限于固定信息来源。黄金的驱动因素随时间变化 —— 搜索当前影响市场的任何因素。

**MUST** 保证整篇分析的 `sources` 覆盖 ≥ 2 个独立域名，避免单源依赖。

**MUST NOT** 在 `sources` 中写入未实际 `web_fetch` 过的 URL。每次 `web_fetch` 后 MUST 调用 `log_fetch.py` 记录。

搜索角度（仅示例，非清单）：
- 美联储政策 / 利率
- 地缘政治冲突
- 通胀数据（CPI、PCE）
- 央行购金
- 美元指数（DXY）
- 实际利率
- ETF 资金流向 / 持仓
- 季节性模式

找到最佳来源，用 `web_fetch` 读取，再用 `log_fetch.py` 记录，最后在 YAML 中引用它们。如果某个维度找不到数据，**MUST 跳过它 —— MUST NOT 编造**。

---

## 7. 状态文件（state.json）

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

**MUST NOT** 手动编辑 `state.json`，它由 `fetch.py` 自动维护。

---

## 8. 提醒系统

基于**动态阈值**的智能提醒系统：

1. **动态阈值**：根据过去 7 天波动率自动调整（默认 ±1%，范围 0.5%-3%）
2. **多基准比较**：同时对比 last_price、当日开盘价、24 小时均价
3. **防震荡机制**：同类提醒 30 分钟冷却期，每日最多 10 条提醒
4. **状态管理**：pending → sent → acknowledged → resolved/dismissed
5. **自动清理**：24 小时未处理自动标记 resolved，30 天后删除

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
- `price_reversal_up/down` — 反转方向提醒（变动达阈值 70%）

---

## 9. 归档系统

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

## 10. 目录职责

| 路径 | 内容 | 生命周期 |
|------|------|----------|
| `logs/` | 当日 YAML 日志 | 自动归档（非当日） |
| `archive/YYYY-MM/` | 历史日志 | 365 天 |
| `archive/index.json` | 归档索引 | 自动更新 |
| `alerts/` | 价格提醒 JSON | 30 天 |
| `analysis.md` | 当前完整分析 | 覆盖更新 |
| `state.json` | 最新价格快照 | 自动更新 |
| `.cache/` | HTTP 响应缓存 + `fetch_log.json` | 自动过期（5 分钟）/ 分析结束前有效 |

---

## 11. 错误处理

### fetch.py 失败

| 错误 | 原因 | 处理 |
|------|------|------|
| 金价获取失败 | 网络问题或 goldpricez.com 不可用 | 等待 5 分钟后重试；仍失败则使用上次 `state.json` 中的价格 |
| 汇率获取失败 | open.er-api.com 不可用 | 同上；可手动查询汇率并告知用户 |
| 金价异常 | 价格超出 $1000-$10000 范围 | 数据源可能返回错误数据，不要使用该价格 |
| state.json 不存在 | 首次运行或被误删 | 运行 `python3 scripts/setup.py` 重新初始化 |

### 数据源不可用时的降级策略

1. 优先使用缓存数据（`.cache/` 目录，5 分钟有效）
2. 缓存过期则使用 `state.json` 中的最后已知价格
3. 在分析中明确标注「数据可能过期」
4. **MUST NOT** 使用过期数据触发提醒

### check_analysis.py 报告错误

- **缺顶层字段**：补全 YAML 模板对应字段
- **impact 不在枚举**：改为 6 个标准值之一（`bullish/bearish/mixed/neutral/slightly_bullish/slightly_bearish`）
- **source URL 未在 fetch_log**：要么真的 `web_fetch` 并 `log_fetch.py` 记录，要么从 sources 中删除该 URL
- **来源覆盖域名不足**：补抓一个不同域名的来源
- **含禁用措辞**：改写为有据可查的因果链
- **factor 数量不足/超限**：补足至 ≥ 2 或裁剪至 ≤ 6

### validate.py 报告错误

- **state.json 缺少字段**：运行 `python3 scripts/setup.py` 修复
- **日志缺少 run_id 或 price_usd**：手动补全或删除该日志
- **impact 未标准化**：运行 `python3 scripts/normalize.py`
- **提醒 JSON 格式错误**：删除该提醒文件，系统会重新生成

---

## 12. 脚本参考

| 脚本 | 作用 | 何时运行 |
|------|------|----------|
| `setup.py` | 环境初始化 | 安装后首次运行 |
| `fetch.py` | 获取金价和汇率 | 每次分析开始时 |
| `validate.py` | 验证项目完整性 | 维护时 + 分析完成后 |
| `check_analysis.py` | 本次分析的反幻觉硬校验 | **每次写日志后、宣布完成前** |
| `log_fetch.py` | 记录 web_fetch 行为到 fetch_log | **每次 web_fetch 后立即** |
| `normalize.py` | 标准化日志格式 | 每周 1 次 |
| `alert_manager.py` | 提醒检测与管理 | 每次 fetch 后 |
| `archive_manager.py` | 归档与历史查询 | 每日 1 次 |
| `summary.py` | 生成简报/摘要 | 每次分析后 |

---

## 13. 推送通知格式（< 2000 字节）

```
🥇 **黄金追踪** · MM-DD

💰 **金价**: $X,XXX.XX (+X.XX, +X.XX%)

| 因素 | 方向 | 逻辑 | 来源 |
|------|------|------|------|
| 标题 | 🟢 | 原因 | site.com |

**点评**: 一句话综合判断

来源: site · site · site
```

**MUST**：推送中的每个 `site.com` MUST 是本次分析 `sources` 中真实存在的域名，**MUST NOT** 编造。
