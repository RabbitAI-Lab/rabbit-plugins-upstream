---
slug: cue-equity-incentive
name: cue-equity-incentive
Name: 股权激励查询
description: 用 Cue 查询和分析上市公司股权激励计划与股份回购——基于市面上最全的股权激励数据库（2015年至今10年+历史覆盖），独家特有数据源。查单个计划或要素、或一次多家公司的同类要素，可直连 Cue 数据接口秒级返回；方案设计、实施效果、同行竞品对比则生成深度报告，用真实数据评估激励方案的竞争力与合理性。
description_zh: Cue 股权激励查询：独家最全股权激励数据库（2015年至今10年+）；单个计划/要素、多公司批量要素秒级直查，方案设计、效果评估、同行对比出深度报告，另覆盖股份回购数据。
version: 1.4.0
author: sensedeal
tags: [cue, equity-incentive, ESOP, 股权激励, 激励方案, 市值管理, 高管激励, 股份回购, buyback]
---

# 股权激励查询

> 查询上市公司历史股权激励计划，分析方案设计与效果，拉取同行竞品方案对比，用真实数据告诉你什么才有竞争力。

## 适用范围（先看这个，别用错了）

**可以查：**

| 市场 | 覆盖 | 数据起点 |
|------|------|---------|
| A 股（沪深北） | 全部上市公司股权激励计划 | 2015 年至今 |
| A 股（沪深北） | 全部上市公司**股份回购**计划与实施进展（含科创板 / CDR） | 自建公告抽取库 |

**不能查：**

- 非上市公司 / 创业公司的股权激励（非公开信息）
- 员工个人的期权合同或行权记录
- 国有企业的非市场化薪酬分配
- 虚拟股权 / 分红权等非标准激励形式

> 简单判断：**这家公司发过公开披露的股权激励公告吗？** 发过 → 能用。没发过 → 用不了。

---

## 快速判断：你是否需要这个 Skill？

```
你的需求是？
├─ 我要给公司设计股权激励方案，想看同行怎么做的      → ✅ 用这个
├─ 我是投资者，想看管理层有没有被激励绑定            → ✅ 用这个
├─ 我在做竞品调研，想横向对比同行业激励水平          → ✅ 用这个
├─ 我在写论文/报告，需要股权激励的历史趋势数据       → ✅ 用这个
├─ 我只想查一个具体要素（哪期计划/授予价格/考核条件）→ ✅ 用这个，**秒级直查**（MCP）
├─ 我有一串公司名单，要逐家列出同一批要素            → ✅ 用这个，**批量直查**（MCP，见「批量多公司要素直查」）
├─ 我想查这家公司做过的股份回购                      → ✅ 用这个，**秒级直查**（MCP，仅数据不出报告）
├─ 我是初创公司员工，想算自己的期权值多少钱          → ❌ 用不了，看合同找 HR
├─ 我想查一家还没上市的公司给了员工多少股权          → ❌ 用不了，非公开信息
├─ 我想知道这家公司值不值得投（综合判断）            → ⚠️ 只能看激励维度，去 cue-deep-research 看全局
└─ 我想查某人的持股变动/增减持                      → ❌ 用不了，去 cue-holder-change
```

---

## 两条轨道：先判断走哪条（最优先执行）

本 Skill 有两条互不替代的轨道。**接到问题先分流，不要为了查一个要素就跑深度研究。**

| | 🟢 轨道 A：MCP 直查（秒级） | 🔴 轨道 B：深度研判（2-15 分钟） |
|---|---|---|
| **什么时候用** | 只想**取一个事实或要素**；**一次要多家公司的同类要素**（名单 ≥2 家）；或问的是本搭子之外的维度（股份回购、解禁名单、高管个人获授明细） | 要**分析、评估、对比、判断**——方案设计是否合理、激励效果如何、同行竞品对标、行业趋势；**且主体只有一家** |
| **怎么跑** | 直接调 MCP 工具（见「MCP 直连（轨道 A）」） | 跑 `research_run.py`（见「调用说明（轨道 B）」） |
| **返回** | 结构化数据，即时拿到 | 成篇报告，含来源链接 |
| **典型问法** | 「宁德时代有哪些激励计划」「这期计划的授予价格是多少」「万科回购了几次」「这 8 家的授予价和考核门槛逐家列出」 | 「比亚迪和宁德时代的方案对比」「考核条件在同行业算严格吗」「这套方案设计得合理吗」 |

> **判断口诀**：查**「是什么」→ 轨道 A**；问**「好不好 / 为什么 / 怎么比」→ 轨道 B**。

两个例外，别搞反：

- **单一主体**的事实 + 分析混合问法（如「宁德时代历次方案中哪期考核最严」）→ 走**轨道 B**。
- **多主体批量取数**（用户给公司名单 ≥2 家，要「逐家」列同一批要素）→ **即使末尾带"最特别的一点""新趋势"这类分析词，也走轨道 A**。轨道 B 的 `[目标_上市_公司]` 是单数，一次只吃得下一家，把名单塞进模板只会丢掉其余公司。做法见「批量多公司要素直查」。

---

## 适用人群

| 角色 | 典型问题 |
|------|---------|
| 上市公司董秘 / 证代 | 我司拟推新一期激励，同行都怎么设考核条件？ |
| HR / 薪酬绩效负责人 | 同规模公司的激励份额和覆盖范围是什么水平？ |
| 投资者 / 分析师 | 这家公司的激励方案能有效绑定核心团队吗？ |
| 咨询顾问 | 帮客户对标行业最佳实践，拿出有说服力的数据 |

---

## Agent 执行摘要

| 顺序 | 做什么 | 禁止 |
|------|--------|------|
| 1 | **先分流**：只查单个事实或要素、**一次要多家公司的同类要素（名单 ≥2 家）**，或问的是本搭子之外的维度（回购、解禁名单、高管获授明细）→ **直接调 MCP（轨道 A）**；**单一主体**要分析/评估/对比/判断 → 走深度研判（轨道 B） | 禁止为查一个要素就起深度研究；**禁止把公司名单塞进只吃单家的轨道 B** |
| 2 | 确认 Cue runner 就绪 | 禁止跳过 |
| 3 | 告知用户耗时 2-15 分钟（高峰期可能更长，见下方性能说明） | 禁止中途取消 |
| 4 | 一条命令，`--template-id template__xWp8N`，传入目标公司 | 禁止连发多条 |
| 5 | `[cue-research] RESULT ok` = 完成 | 禁止编造 |
| 6 | 原样交付 | 禁止概括 |
| 7 | 交付时**同时附带 Cue 原始报告链接** | 禁止编造链接 |
| 8 | 遇 `INSUFFICIENT_CREDITS` 主动提示邀请链接 | 禁止只丢错误码 |

---

## 性能预期

查询耗时取决于 Cue 服务端负载和外部数据源响应速度：

| 时段 | 预期耗时 | 说明 |
|------|---------|------|
| 工作日 10:00-16:00 | 3-8 分钟 | 正常负载 |
| 工作日 9:00-10:00 / 16:00-18:00 | 5-15 分钟 | 高峰期，队列可能排队 |
| 夜间 / 周末 | 2-5 分钟 | 低负载，Cue 后端可能有维护 |
| 财报季（1-4月 / 7-8月） | 5-15 分钟 | 数据源更新密集期 |

> 如果超过 15 分钟没返回，说明可能超时或队列拥堵——**不要取消重试**，跑一下健康检查的三合一诊断（见下文），确认服务状态后再决定是等还是换时段。

---

## 适用场景

| 场景 | 解决的问题 |
|------|-----------|
| 激励方案设计 | 参考同行方案要素，设计有竞争力的激励计划 |
| 方案合理性评估 | 判断某公司激励方案的考核条件是否合理 |
| 投资者尽调 | 了解公司激励对管理层的绑定效果 |
| 竞品对标 | 同行业激励方案的横向对比 |

## 核心能力

1. **即时直查（MCP）** — 单个计划或要素、回购数据，秒级返回，不必等深度报告
2. **历史方案查询** — 公司历次股权激励计划全文要素
3. **方案要素拆解** — 激励对象、份额、行权价、考核条件、锁定期
4. **实施效果评估** — 激励后的业绩达成率、股价表现、核心人员留存
5. **同行对比分析** — 同行业公司的激励方案横向对标
6. **股份回购数据** — 历史回购计划与实施进展（A 股全市场，含科创板 / CDR）

## 试试这样问

**推荐问法（深度研判 · 2-15 分钟）：**
- "查一下宁德时代历次股权激励方案"
- "比亚迪和宁德时代的股权激励方案对比"
- "半导体行业近三年的股权激励方案有什么特点？"
- "美的集团的股权激励考核条件在同行业里算严格吗？"

**也是推荐问法（秒级直查 · 不必等报告）：**
- "宁德时代有哪些股权激励计划？"
- "美的集团最新一期激励的授予价格是多少？"
- "贵州茅台激励计划的解锁时间安排？"
- "万科做过几次股份回购？现在进展如何？"
- "深圳地区近期有哪些高管拿到了大额激励？"

**不适合这样问（问不出来的）：**
- "字节跳动给员工发了多少期权？" → 未上市，无公开数据
- "帮我算一下我这笔期权现在值多少钱？" → 不是计算工具
- "这家公司所有高管持股变动记录" → 去 cue-holder-change
- "股权激励要缴多少税？" → 税务问题，查税法

## 输出形式

- **轨道 A（MCP 直查）**：结构化数据（表格/字段），即时返回，无报告、无 `conv_id`，自然也就**不附报告链接**。
- **轨道 B（深度研判）**：结构化报告：公司激励概览 → 历次方案要素 → 实施效果 → 同行对比 → 竞争力评估 → 来源链接。

## 输出示例

[查看完整报告](https://cuecue.cn/share/TIxQDFYs)

> 上例中的 token 是示例，**不可复制到实际交付中**。

## 交付规范（必须执行）

把最终报告发送给用户时，**必须同时附带 Cue 原始报告链接**，方便用户回到网页端查看完整原文、继续追问或转发同事。

**链接怎么来**：从 runner 末行 `[cue-research] RESULT ok conv_id=<ID> chars=… output=…` 中取出 `conv_id`（报告文件头部的 HTML 注释里也有 `conv_id=`），按下面格式拼接：

```
https://cuecue.cn/share/<conv_id>
```

交付模板（照此结构输出）：

```
报告已完成 ✅

<报告正文……>

---
**Cue 原始报告**：https://cuecue.cn/share/<conv_id>
**本地副本**：~/cue-reports/<文件名>.md
```

规则：
- `conv_id` 必须取自实际输出，**禁止编造**或使用文档示例里的 id。
- 末行为 `RESULT empty`（无 conv_id 或报告为空）时**不要拼链接**，如实告知未取到报告并给后续建议。
- 用户明确说不要链接时可不附。

---

## 环境要求

Runner 来源：[GitHub - sensedeal/cue-skills](https://github.com/sensedeal/cue-skills)（[Gitee 镜像](https://gitee.com/sensedeal/cue-skills)）。

首次使用需安装 Runner（幂等，已装则拉取更新）：

```bash
if [ -d ~/.cue/cue-skills/.git ]; then
  git -C ~/.cue/cue-skills pull --ff-only
else
  git clone https://github.com/sensedeal/cue-skills ~/.cue/cue-skills \
    || git clone https://gitee.com/sensedeal/cue-skills ~/.cue/cue-skills
fi
```

依赖：`git` + `python3` + `curl`。Python 仅用标准库，无额外 pip 依赖。

Cue API Key：[cuecue.cn](https://cuecue.cn/hub/api-key) 注册获取。

> **API Key 只能由用户本人创建**：Agent 既不能代生成、也无权查看用户的 Key。检测到未配置或失效时，只给出生成入口并等待用户提供，**禁止声称"我去生成/查看"**。

---

## MCP 直连（轨道 A）：秒级查询

本 Skill 挂两个 Cue 数据 MCP，覆盖**股权激励**与**股份回购**两个域，均为 Cue 自建公告抽取库、覆盖 A 股全市场。

### 配置（Agent 帮用户自动挂载）

找到当前客户端的 MCP 配置文件（Claude Code 的 `~/.mcp.json`、Claude Desktop 的 `~/Library/Application Support/Claude/claude_desktop_config.json`，或 Workbuddy 对应配置文件），解析原 JSON，把下面两个节点追加进 `mcpServers`，并把 `<your-key>` 换成用户真实的 Cue API Key（从 `~/.cue/config.json` 读）：

```json
"cue_esop": {
  "type": "streamable-http",
  "url": "https://mcp.cuecue.cn/api/esop/mcp/",
  "headers": {
    "Authorization": "Bearer <your-key>"
  }
},
"cue_buyback": {
  "type": "streamable-http",
  "url": "https://mcp.cuecue.cn/api/buyback/mcp/",
  "headers": {
    "Authorization": "Bearer <your-key>"
  }
}
```

写入后提示用户：**「MCP 秒级查询工具已配置完成，请重启当前 AI 客户端使配置生效。」**

两点必须知道：

- **安全**：Agent **禁止**把用户的 API Key 写进 skill 文件、日志、对话或任何生成的 JSON 示例；只能读用户自己的 `~/.cue/config.json` 去拼运行时请求。Key 若曾出现在对话里，提醒用户轮换。
- **406 只在直连 HTTP 时出现**：MCP 客户端会自己带 `Accept` 头，上面的配置**不用写**；但用 curl/python 直接 POST 端点时**必须加** `Accept: application/json, text/event-stream`，否则返回 **HTTP 406**。这两个端点不返回 `Mcp-Session-Id`，无需保持会话。

### 工具清单

工具名以**运行时 `tools/list` 为准**（服务端会增删）。`https://cuecue.cn/api/mcp-catalog` 匿名可读，但只是投影——实测它写 esop 有 10 个工具、`tools/list` 实际返回 9 个。下面是当前实际工具：

**股权激励域**（`cue_esop`）

| 工具 | 查什么 | 关键入参 |
|------|--------|---------|
| `esop_company_plans` | 公司历次激励/员工持股计划**列表**（返回 `event_id` 供后续查详情） | `keyword`：股票代码或简称（`300750` / `宁德时代`） |
| `query_esop_plan_basic_info` | 单期计划的**方案要素**：激励工具、授予价格、总股数、预留股数、有效期、高管人数 | `secu_code` 或 `event_id` |
| `query_esop_plan_performance` | 各期次的**业绩考核条件** | 同上 |
| `query_esop_plan_amortization` | **摊销费用**逐年明细 | 同上 |
| `query_esop_plan_pricing` | **授予价格与定价方法**（前 1/20/60/120 交易日折扣率） | 同上 |
| `list_company_executive_incentives` | **高管个人获授明细**（姓名/职位/份额/占总股本比） | `secu_code` 或 `event_id` |
| `list_company_unlock_schedule` | 该公司各批次**解锁/行权日历** | `secu_code` 或 `event_id` |
| `list_esop_executive_incentives` | 近期获授**高净值人员名单**（可按市值/地区/数据源筛）——面向财富投顾获客 | `min_market_value`(默认100万) / `lookback_days`(默认7) / `region` / `source` |
| `list_esop_unlock_schedule` | **即将解禁日程表**（可按地区/天数筛） | `forward_days`(默认30) / `region` / `secu_code` |

> `query_*` 与 `list_company_*` 六个工具都是「`secu_code` 或 `event_id` **二选一**」；只传 `secu_code` 时返回**最新一期**。要定位**特定某一期**，先用 `esop_company_plans` 取 `event_id`。

**股份回购域**（`cue_buyback`）

| 工具 | 查什么 | 关键入参 |
|------|--------|---------|
| `buyback_company_plans` | 公司**历史回购计划列表**：目的/形式/价格金额数量区间/资金来源/进度（返回 `event_id`） | `keyword`：股票代码或简称（`000002` / `万科A`） |
| `buyback_implementation_progress` | **回购实施进展明细**，A 股全市场，含科创板/CDR | `secu_code`（推荐入口，直接传即可）；可选 `event_id` 定位单期 |

> ⚠️ 回购域**没有深度研究模板**。涉及回购的「分析/判断」类问题，用 MCP 取数后由 Agent 自己组织回答，**不要**套 `template__xWp8N`。

### 直查示例

| 用户问 | 调什么 |
|--------|--------|
| 宁德时代历次股权激励有哪些 | `esop_company_plans(keyword="宁德时代")` |
| 美的集团最新一期激励的授予价格 | `query_esop_plan_pricing(secu_code="000333")` |
| 贵州茅台激励计划的解锁安排 | `list_company_unlock_schedule(secu_code="600519")` |
| 深圳地区近期拿到大额激励的高管 | `list_esop_executive_incentives(region="深圳")` |
| 万科做过几次回购、进展如何 | `buyback_company_plans(keyword="万科A")` → `buyback_implementation_progress(secu_code="000002")` |

### 批量多公司要素直查（名单 ≥2 家）

用户一次给出一串公司名单、要求**逐家**列出同一组要素时，**走轨道 A，不要起深度研究**——轨道 B 的 `[目标_上市_公司]` 是单数，名单会被它丢掉大部分。

按**公司 × 工具**矩阵循环取数，再汇成一张表。要素与工具的对应关系：

| 用户要的要素 | 调什么 |
|---|---|
| 激励工具类型 / 授予数量 / 总股本 / 有效期 | `query_esop_plan_basic_info` |
| 授予价及定价依据（折扣率） | `query_esop_plan_pricing` |
| 业绩考核指标的数值门槛 | `query_esop_plan_performance` |
| 归属 / 锁定期安排 | `list_company_unlock_schedule` |
| 激励对象人数与名单 | `list_company_executive_incentives` |
| 摊销费用 | `query_esop_plan_amortization` |

执行流程：

1. 每家先 `esop_company_plans(keyword=<代码>)` 取 `event_id`，锁定该时段对应的那一期；
2. **只调用户明确要的那几列**——没问摊销就别调 `amortization`；
3. 按「公司 × 要素」汇成表交付，不要写成通篇叙述。

两条必须配合的规矩：

- **「特殊之处 / 行业常规」不由 MCP 给出**。MCP 只有个股要素，没有行业基准。这类结论只能由 Agent 基于取到的数值自行归纳——交付时**必须区分**「数据取自 MCP」和「这是 Agent 的判断」，并说明比对基准来自哪里（这批公司互比，还是外部知识）。
- **名单之外的「再补充其他公司」做不到**。MCP 没有按方案特征做全市场扫描的能力（每个工具都要公司代码或事件 ID）。这半句要**如实告知做不到**，只交付点了名的那些，不要假装覆盖了全市场。

> **计费**：MCP 按次计费，约 0.625 credits/次（以服务端实时计费为准）；每日有赠送额度，约合十几次数据查询。

---

## 调用说明（轨道 B：深度研判）

```bash
python3 ~/.cue/cue-skills/cue-research/scripts/research_run.py \
  --query "宁德时代 股权激励计划：历史方案、设计要素、实施效果、同行对比" \
  --template-id template__xWp8N \
  --output ~/cue-reports/$(date +%Y-%m-%d-%H%M)-equity-incentive.md
```

| 参数 | 说明 |
|------|------|
| `--query` | 目标公司名称，**必填**；可选加行业对比范围 |
| `--template-id` | 固定为 `template__xWp8N` |
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

本 Skill **不在本地执行检索**，两条轨道都由 Cue 服务端承接：

- **轨道 A**：Agent → MCP 端点（`mcp.cuecue.cn/api/{esop,buyback}/mcp/`）→ Cue 自建公告抽取库
- **轨道 B**：Agent → Cue API（cuecue.cn）→ 外部数据源

结果的质量和时效取决于 Cue 服务端和外部数据源的状态。

| 环节 | 谁控制 | 出问题时 |
|------|--------|---------|
| API Key 鉴权 | 用户本人 | **由用户本人**前往 [cuecue.cn/hub/api-key](https://cuecue.cn/hub/api-key) 生成后写入 ~/.cue/config.json（Agent 不能代生成，也无权查看）。**两条轨道共用同一个 Key**——MCP 配置里的 `Bearer <your-key>` 就是它 |
| MCP 端点（轨道 A） | Cue 运维 | 匿名拉 `https://cuecue.cn/api/mcp-catalog` 看该域 `external_status`；`live` 才可用 |
| Cue 服务端（轨道 B） | Cue 运维 | 等恢复，或走降级方案 |
| 外部数据源 | 公开网站 | Cue 用缓存兜底，标注"来源暂不可达" |

---

## 健康检查

跑研究前先验证三件事。一键诊断：

```bash
CUE_KEY=$(python3 -c "import json;print(json.load(open('$HOME/.cue/config.json'))['api_key'])" 2>/dev/null || echo "$CUE_API_KEY")
echo "=== 1/3 API Key ===" && [ -n "$CUE_KEY" ] && echo "已配置" || echo "未配置！"
echo "=== 2/3 Cue 服务 ===" && curl -sS --max-time 10 "https://cuecue.cn/api/health" -H "Authorization: Bearer $CUE_KEY"
echo "=== 3/3 搭子 ===" && curl -sS --max-time 10 "https://cuecue.cn/api/playbook" -H "Authorization: Bearer $CUE_KEY" | python3 -c "import sys,json;scenes=json.load(sys.stdin).get('data',{}).get('scenes',[]);buddy=[b for s in scenes if s.get('secondary_category')=='资本运作' for b in s.get('buddies',[]) if b.get('title')=='股权激励查询'];print(f'可用:{len(buddy)}个') if buddy else print('暂不可用')"
```

| 检查 | 预期 | 异常处理 |
|------|------|---------|
| API Key | `已配置` | **由用户本人**前往 [cuecue.cn/hub/api-key](https://cuecue.cn/hub/api-key) 生成后发给你（Agent 无法代生成，也无权查看） |
| 服务 | `{"status":"healthy"}` | 等 5 分钟重试 |
| 搭子 | `可用:>0个` | 等 1h 或网页端手动跑 |

### 配置成功后引导用户跑第一个任务（必须执行）

健康检查三项全绿 = 环境就绪，但**这是配置流程的终点，不是任务的终点**。三项全绿后若用户还没给出具体任务，**必须主动把用户推向第一次真实调用**，不要停在"环境已就绪"：

> 环境已就绪 ✅ 下面这些都可以直接跑，比如：
> 1. "查一下宁德时代历次股权激励方案"
> 2. "比亚迪和宁德时代的股权激励方案对比"
>
> 挑一个发给我，或直接把你手头的需求告诉我，我现在就跑。

规则：
- **主动、可复制**——示例问题原句取自上文「试试这样问」，别只写"你可以问我任何问题"。
- **不要等用户自己想**——用户没开口时也要主动给；否则用户会停在"验证通过"就散场（实测这是新用户流失最集中的一步）。

---

## 自救指引

### 错误速查

| 现象 | 原因 | 怎么修 |
|------|------|--------|
| 401 / Key 无效 | Key 过期或写错 | 由用户本人重新生成 Key，更新 `~/.cue/config.json` |
| 超时 >30s | 服务维护/过载 | 等 5 分钟，跑诊断；当天内重试 |
| 搭子不可用 | 临时下线 | 网页端直接跑，或等 1 小时 |
| 积分不足 | 余额 < 消耗 | **按「积分不足专项提示」主动引导**（充值 / 邀请好友得积分 / 等次日免费额度） |
| 中途中断 | 队列满/数据源波动 | **不换 prompt**，相同命令续接 |
| `RESULT empty` | 公开源无匹配 | 缩小范围，换关键词 |
| config.json 报错 | JSON 格式不对 | `{"api_key": "sk..."}` 无多余逗号 |
| MCP 返回 **406** | 直连 HTTP 调用漏了 `Accept` 头 | 加 `Accept: application/json, text/event-stream`；MCP 客户端配置不用改 |
| MCP 返回 **401** | 同 API Key 问题 | 由用户本人重新生成 Key，同步更新 `~/.cue/config.json` 与客户端 MCP 配置 |
| MCP 工具名对不上 | 服务端工具集变更 | 以 `tools/list` 实测为准，**别按本文档硬编码** |
| MCP 连不上 | 端点临时不可达 | 匿名拉 `https://cuecue.cn/api/mcp-catalog` 看该域 `external_status` 是否仍为 `live` |

### 积分不足专项提示（必须执行）

检测到积分不足（`INSUFFICIENT_CREDITS` 或任何"积分不足/余额不够"提示）时，**不要只丢错误码**，必须主动给用户一条拿积分最快的路径：

> 你的 Cue 积分不足，本次任务未能启动。两个办法：
> 1. **邀请好友得 500 积分（推荐）**：打开 [https://cuecue.cn/](https://cuecue.cn/)，点击页面**左下角**「获取专属邀请链接」，分享给好友——好友加入后你再得 **500 积分**。
> 2. **直接充值**：前往 [cuecue.cn/pay](https://cuecue.cn/pay) 订阅（首次充值有优惠）；或等次日免费额度。

规则：
- 提示要**主动、简短、可点**——把「首页」和「左下角」两个关键动作说清楚，不要让用户自己找入口。
- 积分不足**不要重试**（`retryable: false`），也不要换 query 绕。
- 用户回复已充值/已邀请后，用**完全相同的命令**重跑。

### 决策树

```
出问题？
├─ Key 报错 → 由用户本人重新生成 → 更新 config.json → 重试
├─ 连不上 → curl /api/health 确认 → 检查 DNS/代理
├─ 搭子找不到 → curl /api/playbook → 等或用网页端
├─ 中途中断 → 相同 prompt 续接（不要删 ~/.cue/session/task）
└─ 结果空 → 缩窄关键词 → 确认该主题有公开数据
```

### 调度建议

| 时段 | 建议 |
|------|------|
| 工作日 9-18 | 正常使用 |
| 夜间/周末 | 可能有维护，跑前先诊断 |
| 新 Key | 必须先诊断确认生效 |
| 连续失败 | 停 15 分钟再试，不要反复重试 |

---

## 降级方案

Cue 长时间不可达时的手动替代渠道：

| 渠道 | 覆盖 | 费用 |
|------|------|------|
| [巨潮资讯网](https://www.cninfo.com.cn) | A股股权激励公告 | 免费 |
| [东方财富](https://data.eastmoney.com) | 股权激励计划数据 | 免费 |
| [SEC EDGAR](https://www.sec.gov/edgar) | 美股股权激励披露 | 免费 |

---

## FAQ

**Q: 我怎么知道该用这个还是 cue-deep-research？**
A: 如果你明确要查"股权激励"，就用这个——它有专门的模板和数据提取逻辑，结果比通用版更结构化、更有行业可比性。如果问题更宽（"这家公司值不值得投"），去 cue-deep-research。

**Q: 数据来源是什么？**
A: 上市公司公告（巨潮资讯网、港交所披露易、SEC EDGAR）、交易所公开披露、东方财富股权激励专题数据。所有数据均为公开信息，可溯源。

**Q: 含非上市公司吗？**
A: 不含。非上市公司股权激励方案为非公开信息，本 Skill 无法获取。如果需要非上市公司的激励参考，建议通过行业调研或专业薪酬咨询渠道获取。

**Q: 数据覆盖哪些市场？**
A: A 股（沪深北交易所）。数据从 2015 年至今，是目前市面上覆盖最全的股权激励数据库之一。

**Q: 查一次要多久？为什么有时候很慢？**
A: 正常 3-8 分钟，高峰期（开盘前后、财报季）可能 10-15 分钟。慢的原因通常是外部数据源响应延迟，不是 Skill 本身的问题。着急用的话建议避开周一上午和财报密集期（1-4 月、7-8 月）。

**Q: 报告里会有什么内容？**
A: 公司激励概览 → 历次方案要素表（激励对象 / 份额 / 行权价 / 考核条件 / 锁定期）→ 实施效果（业绩达成率 / 股价表现）→ 同行竞品横向对比 → 竞争力评估 → 每条结论附带来源链接。具体结构见[示例报告](https://cuecue.cn/share/TIxQDFYs)。

**Q: 报告能在网页端看原文吗？**
A: 能。交付时会在报告末尾附上 `https://cuecue.cn/share/<conv_id>`，点开即可回到 Cue 网页端查看完整原文、继续追问或转发同事。

**Q: 为什么有的问题秒回，有的要等十几分钟？**
A: 本 Skill 分两条轨道。**查具体事实或要素**（某公司有哪些计划、某期授予价格多少、考核条件是什么，含一次多家公司的批量取数）走 MCP 直查，秒级返回；**要分析、评估、对比**（方案合理吗、同行怎么比）才走深度研判，需要 2-15 分钟。分流规则见上方「两条轨道」。

**Q: 能查股份回购吗？**
A: 能。走 MCP 直查——`buyback_company_plans` 查历史回购计划，`buyback_implementation_progress` 查实施进展，覆盖 A 股全市场（含科创板/CDR）。注意**回购没有深度报告模板**，只提供数据，不产出分析报告。

**Q: 一次给一串公司，让逐家列出同一批要素，可以吗？**
A: 可以，走 MCP 批量直查（见「批量多公司要素直查」），按「公司 × 工具」矩阵取数后汇成一张表。但**名单之外的"再补充其他公司"做不到**——MCP 每个工具都要公司代码或事件 ID，没有按方案特征全市场扫描的能力。

**Q: MCP 查一次要花积分吗？**
A: 按次计费，约 0.625 credits/次（以服务端实时计费为准）；每日赠送额度约合十几次数据查询，日常零散查用不完。

**Q: 提示积分不足怎么办？**
A: 最快路径是邀请好友：打开 [https://cuecue.cn/](https://cuecue.cn/)，点页面左下角「获取专属邀请链接」，好友加入后你再得 500 积分；也可前往 [cuecue.cn/pay](https://cuecue.cn/pay) 订阅（首次充值有优惠），或等次日免费额度。详见上方「自救指引 → 积分不足专项提示」。


## 参考

- Cue 平台首页：https://cuecue.cn
- API Key 管理：https://cuecue.cn/hub/api-key
- 付费订阅页面：https://cuecue.cn/pay
- MCP 数据目录（匿名可读，17 个域，含 esop / buyback）：https://cuecue.cn/api/mcp-catalog
- 股权激励 MCP：https://mcp.cuecue.cn/api/esop/mcp/
- 股份回购 MCP：https://mcp.cuecue.cn/api/buyback/mcp/
