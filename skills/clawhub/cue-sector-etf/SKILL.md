---
slug: cue-sector-etf
displayName: 热门赛道与ETF深度投研
description: 用 Cue 一键深度拆解热门赛道与ETF——赛道全景分析、同类ETF横向对比、底层持仓穿透、估值水位研判，告诉你"这条赛道值不值得投、哪只ETF更匹配"。
description_zh: Cue 热门赛道与ETF深度投研：赛道全景+ETF横向对比+持仓穿透+估值研判，选赛道选ETF不再凭感觉。
version: 1.0.0
author: sensedeal
tags: [cue, sector-research, ETF, thematic-investing, 赛道分析, ETF对比, 行业研究, 主题投资, 估值]
---

# 热门赛道与ETF深度投研

> 新能源、AI、半导体、创新药……每个赛道都有十几只 ETF 在追。哪只跟踪得更准？哪只持仓更纯？现在的估值水位贵不贵？让 Cue 帮你把赛道和 ETF 拆开了看，下单之前心里有数。

## 适用范围与场景（先看这个，别用错了）

**可以查：**

| 维度 | 覆盖 |
|------|------|
| 市场 | 全市场 A 股 ETF（股票型、行业/主题型、跨境 ETF）及对应赛道 |
| 赛道类型 | 全行业——新能源/光伏/储能、AI/半导体/算力、医药/创新药、消费/白酒、军工、红利、黄金、跨境等 |
| 分析深度 | 赛道全景、ETF 横向对比、持仓穿透、估值水位、风险扫描 |

**适用场景：**

| 场景 | 解决的问题 |
|------|-----------|
| 赛道选择 | 大家都在说 AI 赛道，它到底包含哪些环节？现在进去贵不贵？ |
| ETF 对比筛选 | 跟踪新能源的 ETF 有十几只，哪只跟踪误差最小、持仓最纯？ |
| 持仓纯度检查 | 买了一只"芯片 ETF"，结果前十大里一半是消费电子——纯度不够 |
| 估值水位研判 | 这个赛道现在的 PE 在历史什么位置？是低估区间还是已经炒高了？ |

**不能查：**

- 具体买卖时点建议（不做择时推荐，只给估值水位参考）
- ETF 实时盘中净值（IOPV）或日内套利策略
- 非上市交易产品（私募基金、场外专户）
- 港/美股 ETF（当前仅覆盖 A 股上市 ETF）

> 简单判断：**这是一条有 A 股 ETF 跟踪的赛道吗？** 是 → 能用。是纯概念、没有 ETF 产品 → 用不了。

### 快速判断：你是否需要这个 Skill？

```
你的需求是？
├─ 我想投一个热门赛道但不知道从哪里下手                    → ✅ 用这个，先看赛道全景
├─ 我已经看好一个赛道，但不知道该选哪只 ETF                 → ✅ 用这个，横向对比
├─ 我持有一只行业 ETF，想看看它底层到底持有什么               → ✅ 用这个，持仓穿透
├─ 我想知道这个赛道现在的估值在历史上是什么水平               → ✅ 用这个，估值水位
├─ 新能源/芯片/医药/白酒/AI，哪个赛道现在性价比最高         → ✅ 用这个，跨赛道对比
├─ 我想知道明天买还是后天买                                 → ❌ 用不了，不做择时
├─ 我想看美股 ETF（如 QQQ/ARKK）的深度分析                  → ❌ 用不了，仅 A 股 ETF
└─ 我想找一只能涨 10 倍的个股                               → ❌ 用不了，去 cue-supply-chain-mining
```

## 试试这样问

**推荐问法（直接对 Agent 说即可触发本 Skill）：**

- "帮我用热门赛道ETF深度投研，分析一下新能源赛道现在值不值得投，哪只 ETF 最好"
- "用 Cue 赛道投研，帮我把市面上跟踪半导体的 ETF 做一个横向对比"
- "帮我研究一下 AI 算力赛道：产业链全景 + 相关 ETF 对比 + 现在的估值水位"
- "我手里有芯片 ETF（159995），帮我穿透持仓看看底层到底是什么，纯度够不够"
- "帮我比较一下创新药赛道，看看现在是不是低估区间，相关 ETF 有哪些选择"

**对应到命令行 query：**

```bash
# 赛道全景 + ETF 筛选
--query "新能源 赛道全景与ETF深度投研：产业链结构→相关ETF对比→估值水位→持仓纯度"

# ETF 横向对比
--query "半导体ETF 横向对比：芯片ETF(159995) vs 半导体ETF(512480) vs 科创芯片ETF(588200)，跟踪误差与持仓纯度"

# 单只 ETF 深挖
--query "芯片ETF(159995) 深度投研：指数编制方法→前十大持仓→行业分布→估值水位→跟踪误差"

# 赛道估值研判
--query "医药赛道 估值水位研判：PE/PB历史分位+盈利增速预期+政策环境+ETF产品对比"
```

> **模板**：`"<赛道名称/ETF名称> 赛道与ETF深度投研：<你想重点分析的方向>"`

---

## 适用人群

| 角色 | 典型问题 |
|------|---------|
| 个人 ETF 投资者 | 想投新能源，打开交易软件搜"新能源 ETF"出来 20 只——选哪只？ |
| 定投用户 | 每月定投半导体 ETF，但不确定现在估值是不是太高了该暂停 |
| 资产配置型投资者 | 看好 AI 赛道想配置 15% 仓位，但不知道该选宽基科技 ETF 还是纯 AI 主题 ETF |
| 理财经理 / 投顾 | 帮客户筛选赛道 ETF，需要一份有数据支撑的对比分析给客户看 |

---

## Agent 执行摘要

| 顺序 | 做什么 | 禁止 |
|------|--------|------|
| 1 | 确认 Cue runner 就绪 | 禁止跳过 |
| 2 | 告知用户耗时 2-15 分钟（对比多只 ETF 时更久，见下方性能说明） | 禁止中途取消 |
| 3 | 一条命令，`--template-id template__St9E2w`，传入赛道名称或 ETF 代码 | 禁止连发多条 |
| 4 | `[cue-research] RESULT ok` = 完成 | 禁止编造 |
| 5 | 原样交付 | 禁止概括 |

## 核心能力

1. **赛道全景分析** — 产业链结构、竞争格局、政策环境、增长驱动因素
2. **ETF 横向对比** — 跟踪指数、规模、费率、跟踪误差、流动性、持仓重合度
3. **持仓纯度检查** — 穿透 ETF 底层，判断持仓是否"纯正"——有没有挂着 AI 名头买了一堆消费电子
4. **估值水位研判** — PE/PB 历史分位、盈利增速预期、国内外同业估值对比
5. **风险扫描** — 政策风险、集中度风险、流动性风险、风格漂移风险

## 输出形式

结构化研报：赛道全景（产业链 + 竞争格局 + 政策）→ 相关 ETF 清单 → 横向对比表（规模/费率/跟踪误差/流动性/持仓纯度）→ 持仓穿透分析 → 估值水位图 → 风险提示 → 来源链接。

---

## 性能预期

查询耗时取决于分析维度和 Cue 服务端负载：

| 维度 | 预期耗时 | 说明 |
|------|---------|------|
| 单赛道全景 | 3-8 分钟 | 产业链 + 估值 + ETF 清单 |
| 单 ETF 深度穿透 | 2-5 分钟 | 持仓 + 跟踪误差 + 风格分析 |
| ETF 横向对比（3-5 只） | 5-10 分钟 | 多只 ETF 交叉对比 |
| 跨赛道对比（2-3 个赛道） | 8-15 分钟 | 数据量最大 |
| 财报季（1-4月 / 7-8月） | 5-15 分钟 | 基金季报与半年报集中披露 |

> 如果超过 15 分钟没返回，说明可能超时或队列拥堵——**不要取消重试**，跑一下健康检查的三合一诊断（见下文），确认服务状态后再决定是等还是换时段。中途中断时用**相同命令**续接，Cue 会从 session 断点继续，不重复计费。Session 状态存储在 `~/.cue/session/task`，**不要手动删除**。

---

## 环境要求

Runner 来源：[GitHub - sensedeal/cue-skills](https://github.com/sensedeal/cue-skills)（[Gitee 镜像](https://gitee.com/sensedeal/cue-skills)）。

依赖：`git` + `python3` + `curl`（macOS 自带，Linux `apt install git python3 curl`）。Python 仅用标准库，无额外 pip 依赖。

Cue API Key：[cuecue.cn](https://cuecue.cn/hub/api-key) 注册获取。新账号送免费积分，每天再免费送 10 分。

---

## 调用说明

```bash
python3 ~/.cue/cue-skills/cue-research/scripts/research_run.py \
  --query "新能源 赛道全景与ETF深度投研：产业链结构→相关ETF对比→估值水位→持仓纯度" \
  --template-id template__St9E2w \
  --output ~/cue-reports/$(date +%Y-%m-%d-%H%M)-sector-etf.md
```

| 参数 | 说明 |
|------|------|
| `--query` | 赛道名称或 ETF 代码，**必填**。可指定分析维度（如估值水位、ETF 对比） |
| `--template-id` | 固定为 `template__St9E2w` |
| `--output` | 落盘路径 |

---

## 格式转换

Cue 输出 Markdown。安装 pandoc 后可转换为 Word 或 PDF：

```bash
# .md → .docx（Word）
pandoc report.md -o report.docx

# .md → .pdf
pandoc report.md -o report.pdf --pdf-engine=xelatex
```

输出文件与输入同目录、同名、不同后缀。

### 依赖安装

| 目标格式 | 依赖 | macOS | Ubuntu |
|----------|------|-------|--------|
| Word (.docx) | pandoc | `brew install pandoc` | `sudo apt install pandoc` |
| PDF (.pdf) | pandoc + LaTeX | `brew install --cask basictex` | `sudo apt install texlive-xetex` |

---

## 架构说明

本 Skill **不在本地执行检索**。流程是 Agent → Cue API（cuecue.cn）→ 外部数据源（ETF 发行商公告、指数公司、基金季报/年报）。分析结果的质量和时效取决于 ETF 公开数据的完整性和 Cue 服务端状态。

| 环节 | 谁控制 | 出问题时 |
|------|--------|---------|
| API Key 鉴权 | 你 | 重新生成 Key，更新 ~/.cue/config.json |
| Cue 服务端 | Cue 运维 | 等恢复，或走降级方案 |
| ETF 与指数数据源 | 基金公司/指数公司公开披露 | Cue 用缓存兜底，标注"来源暂不可达" |

---

## 健康检查

跑研究前先验证三件事。一键诊断：

```bash
CUE_KEY=$(python3 -c "import json;print(json.load(open('$HOME/.cue/config.json'))['api_key'])" 2>/dev/null || echo "$CUE_API_KEY")
echo "=== 1/3 API Key ===" && [ -n "$CUE_KEY" ] && echo "已配置" || echo "未配置！"
echo "=== 2/3 Cue 服务 ===" && curl -sS --max-time 10 "https://cuecue.cn/api/health" -H "Authorization: Bearer $CUE_KEY"
echo "=== 3/3 搭子 ===" && curl -sS --max-time 10 "https://cuecue.cn/api/playbook" -H "Authorization: Bearer $CUE_KEY" | python3 -c "import sys,json;scenes=json.load(sys.stdin).get('data',{}).get('scenes',[]);buddy=[b for s in scenes for b in s.get('buddies',[]) if b.get('title')=='热门赛道与ETF深度投研'];print(f'可用:{len(buddy)}个') if buddy else print('暂不可用')"
```

| 检查 | 预期 | 异常处理 |
|------|------|---------|
| API Key | `已配置` | [cuecue.cn/api-key](https://cuecue.cn/api-key) 重新生成 |
| 服务 | `{"status":"healthy"}` | 等 5 分钟重试 |
| 搭子 | `可用:>0个` | 等 1h 或网页端手动跑 |

---

## 自救指引

### 错误速查

Cue 返回结构化错误，包含 `code`（错误码）、`retryable`（是否可重试）、`user_action`（操作建议）。

| 错误码 | 现象 | 可重试？ | 处理 |
|--------|------|---------|------|
| `AUTH_FAILED` | 401 / Key 无效 | ❌ | 重新生成 Key，更新 `~/.cue/config.json` |
| `TIMEOUT` | 超时 >30s 无响应 | ✅ | 等 5 分钟，跑诊断确认服务在线后重试，最多 3 次 |
| `BUDDY_UNAVAILABLE` | 搭子临时下线 | ✅（延迟） | 等 1h 或网页端直接跑 |
| `INSUFFICIENT_CREDITS` | 积分不足 | ❌ | [cuecue.cn](https://cuecue.cn) 充值或等次日免费额度 |
| `SESSION_INTERRUPTED` | 中途中断 | ✅ | **不换 prompt**，相同命令续接——Cue 从 session 断点继续，不重复计费 |
| `ETF_NOT_FOUND` | ETF 代码/名称无法识别 | ❌（需改输入） | 检查 ETF 代码是否正确（6 位数字），尝试用全称替代简称 |
| `SECTOR_NOT_RECOGNIZED` | 赛道名称模糊 | ❌（需改输入） | 更具体描述赛道，如"半导体设备"而非"芯片" |
| `RESULT_EMPTY` | 无匹配结果 | ❌（需改条件） | 确认该赛道有 A 股 ETF 产品覆盖，换关键词 |
| `CONFIG_PARSE_ERROR` | config.json 报错 | ❌ | 修复 JSON 格式：`{"api_key": "sk..."}` 无多余逗号 |

### 中断恢复机制

Cue 的调研任务是**有状态**的。如果中途超时或网络波动导致中断：

```
中断 ≠ 失败，cancel 才 = 失败
├─ 超时 → 等一会，相同命令续接（session 存在 ~/.cue/session/task）
├─ 网络波动 → 同上，相同命令续接
├─ 手动 cancel → 无法恢复，需要重新发起
└─ 恢复后 → Cue 从断点继续，已查过的阶段不会重复计费
```

> **关键规则**：中断后**不要换 prompt、不要删 session 文件、不要 cancel**。三个"不要"记住了就不会白跑。

### 重试决策

```
收到错误
├─ retryable = true → 按 user_action 建议操作后重试
│   ├─ 超时/网络类 → 等 5min，跑诊断，最多 3 次
│   └─ 搭子下线 → 等 1h 或换网页端
├─ retryable = false → 不要重试，改了条件再说
│   ├─ Key/ETF代码问题 → 修正输入后重试
│   ├─ 积分不足 → 充值或等次日
│   ├─ 赛道未覆盖 → 换关键词 / 确认赛道有 ETF 产品
│   └─ 结果空 → 换 ETF 代码 / 缩小赛道范围
└─ 重试 3 次仍失败 → 记下 request_id，走降级方案
```

### 调度建议

| 时段 | 建议 |
|------|------|
| 工作日 10:00-16:00 | 最佳时段，3-8 分钟完成 |
| 工作日 9:00-10:00 / 16:00-18:00 | 高峰期，跨赛道对比等大查询避开 |
| 基金季报披露后（1/4/7/10 月下旬） | ETF 持仓数据最新鲜，适合做持仓纯度检查 |
| 夜间/周末 | 可能有维护，跑前先诊断 |
| 连续失败 ≥2 次 | 停 15 分钟，记下 request_id 后重试 |

---

## 降级方案

Cue 长时间不可达时的手动替代渠道：

| 渠道 | 覆盖 | 费用 |
|------|------|------|
| [天天基金](https://fund.eastmoney.com) | ETF 持仓 + 跟踪误差 + 规模 | 免费 |
| [东方财富](https://www.eastmoney.com) | 行业板块估值 + ETF 列表 | 免费 |
| [中证指数公司](https://www.csindex.com.cn) | 指数编制方法 + 成分股 | 免费 |
| [理杏仁](https://www.lixinger.com) | 行业/指数历史 PE/PB 分位 | 部分免费 |

---

## 输出示例

> 示例报告待补充，请通过 [cuecue.cn](https://cuecue.cn) 实际运行后获取。

## FAQ

**Q: ETF 分析和赛道分析的区别是什么？**
A: 赛道分析是"面"——这个行业的结构、景气度、估值水位、政策环境。ETF 分析是"点"——跟踪这条赛道的具体产品，谁的跟踪误差最小、谁的持仓最纯、谁的流动性最好。本搭子两个都做：先看赛道值不值得投，再看哪只 ETF 最合适。

**Q: 怎么知道该用这个还是 cue-supply-chain-mining？**
A: 本搭子焦点是 ETF 产品对比和赛道估值，解决"选哪只 ETF、现在贵不贵"。cue-supply-chain-mining 焦点是产业链里找个股，解决"这条链上哪家公司最有弹性"。如果你最终想买个股，先跑本搭子看赛道方向 → 再跑 supply-chain-mining 找标的。

**Q: 能分析港美股 ETF 吗？**
A: 当前仅覆盖 A 股上市 ETF（含跨境 ETF，如纳指 ETF、恒生 ETF 等在 A 股上市的品种）。港/美股本地 ETF（如 QQQ、ARKK）不在覆盖范围。

**Q: 持仓纯度是什么意思？**
A: 比如一只叫"AI 人工智能 ETF"的产品，前十大重仓里却有海康威视（安防）、立讯精密（消费电子代工）这些跟 AI 核心环节关联没那么直接的公司——这就是纯度不够。Cue 会穿透持仓，告诉你在"AI"这个主题上的实际暴露程度。

**Q: 估值水位怎么看？**
A: PE/PB 在当前时间点在历史（过去 3-5 年）中所处的百分位。比如 PE 处于历史 85% 分位，说明比过去 85% 的时间都贵，属于偏高区间；处于 15% 分位则相反。不是买卖信号，是风险提示——"现在入场，安全边际是多少"。

**Q: ETF 对比只比跟踪误差吗？**
A: 不止。Cue 会从跟踪指数、规模、管理费率、日均成交额、跟踪误差、持仓重合度、前十大集中度、成立时间等多个维度做对比，给出综合评价。

**Q: 分析完了我该怎么做？**
A: 本搭子帮你做赛道和 ETF 的选择决策。定了之后，可以用 cue-asset-allocation 确认这条赛道在你的整体配置里占多少比例合适，用 cue-deep-research 对 ETF 里的核心持仓股做深度尽调。
