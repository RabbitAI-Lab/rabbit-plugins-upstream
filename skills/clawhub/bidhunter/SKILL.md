---
name: bidhunter
slug: bidhunter
displayName: 标讯猎手 BidHunter
version: "2.5.3"
summary: 国央企招投标信息监控与研判：自动采集多平台公告，按资质规则判断可投性，生成研判简报并推送；支持 AI 速读标书、投标策略建议与合规红线扫描。本地运行，零云成本。
license: MIT-0
description: "国央企招投标信息监控与研判技能。自动采集多平台公告，按资质规则比对可投性（可投/不可投/需确认），生成带研判简报并多通道推送。v1.5 起新增：资质匹配度评分(0-100)、投标日历与开标倒计时、金额/地区/行业多维筛选、零代码规则编辑器、诊断中心、示例模式、集中FAQ、统一命令入口；v2.0 本地AI增强（招标文件AI速读+风险条款识别，零云成本）；v2.5 投标策略建议生成；v3.0 本地开放API+签名webhook；v3.5 合规红线引擎（31条法定废标红线本地扫描、交标前自查清单、多主体串标隔离，零API成本）。边界感知智能匹配防子串误匹配，规则库健康检查，钉钉/企业微信/邮件推送。触发词：抓招投标、今日哪些能投、标讯监控、标书研判、招投标公告、央企招标、投标资质匹配、AI读标书、投标建议、这份标会不会被废、废标风险、交标前检查、合规红线扫描、多主体投标、会不会被认定串标。"
agent_created: true
---

# 标讯猎手 BidHunter

> 采集国央企/公共资源招投标公告 → 资质规则比对可投性 → 生成带研判简报 → 多通道推送 → （v1.5+）评分排序/日历提醒/多维筛选/零代码配规则 → （v2.0+）AI 速读标书与风险识别 → （v2.5+）投标策略建议 → （v3.5+）**交标前法定红线扫描与废标预警**。
> 自包含、已脱敏：不含任何私有主体、个人联系方式、公司档案。使用者按自己的营业执照与业务规则填充配置即可。

## 60 秒跑通

一条命令看完整效果，无需任何配置：

```bash
python3 bidhunter.py demo
```

跑完按提示把 `demo_rules.json` 换成你的营业执照规则，即可跑真实采集：`bash pipeline.sh`。

## 卡住了？先跑诊断

任何异常先跑这一条，30 秒定位问题（E001~E005 + W001~W004，每条都带修复建议）：

```bash
python3 bidhunter.py doctor
```

> 最常见的失败原因是 **E002：规则库仍是示例占位符**。装上不等于能用——把自己的资质规则填进 `qual_rules.json` 才算真正跑起来。

## 版本能力一览

| 版本 | 主题 | 关键能力 |
|---|---|---|
| v1.1 | 准 | 边界感知智能匹配、规则健康检查、精华版报告 |
| v1.2 | 达 | 钉钉/企微/邮件多通道推送、配置向导、推送历史与告警 |
| **v1.5** | 易+功能 | 匹配度评分、投标日历、多维筛选、规则编辑器、诊断/示例/FAQ/统一入口 |
| **v2.0** | 智(本地AI) | 招标文件 AI 速读、排他/内定风险识别、业主品类画像（零云成本） |
| **v2.5** | 策 | 投标策略建议生成（仅供参考，不代填报价/资质） |
| **v3.0** | 开(本地) | 本地查询 API + 签名 webhook（云/SaaS 部分因成本约束未启用） |
| **v3.5** | 规 | 合规红线引擎：31 条法定废标红线本地扫描 + 交标前自查清单 + 多主体串标隔离（零 API 成本） |

## 何时使用

- "抓一下招投标" / "今日哪些能投" / "重新分析一遍标讯"
- "AI 读一下这份标书" / "这份招标文件有什么风险" / "帮我出投标建议"
- "这份标会不会被废" / "交标前帮我过一遍" / "有没有废标风险" / "合规红线扫一下"
- "我们几家一起投 / 多主体投标会不会被认定串标"（v3.5 先查实施条例第34条）
- 需要判断公告可投性、归属投标主体、监控重点平台
- 搭建/优化招投标监控工作流

## 安装与初始化

1. 脚本已随 skill 就位（`~/.workbuddy/skills/bidhunter/scripts/`）。
2. 编辑 `qual_rules.json` 填入你的投标主体与资质能力词：
   - 零代码：运行 `python3 bidhunter.py rules edit` → 浏览器图形化编辑，内置「能源/建筑/IT/市政」行业模板可一键预填
   - 或复制 `scripts/samples/demo_rules.json` 改
   - 校验：`python3 qual_check.py --validate-rules qual_rules.json`
3. （可选）配置推送：`python3 config_wizard.py`（钉钉/企微/邮件）
4. （可选）配置 AI：`~/.config/bidhunter/ai.json` 写入 `{"api_key":"你的MiniMaxKey"}`（v2.0+ 用，仅消耗你的 API 余额，零云成本）。AI 速读 PDF/Word 建议先 `pip install -r requirements.txt`（PyPDF2/python-docx）；未装则自动降级为正则抽取。

> 先看效果再配：直接 `python3 bidhunter.py demo` 跑内置示例。

## 统一命令入口（v1.5 · A9，零命令行门槛）

```bash
python3 bidhunter.py run [--fresh] [--summary] [--calendar]   # 采集+比对+报告(+推送)
python3 bidhunter.py status                                    # 今日状态
python3 bidhunter.py doctor                                    # 一键诊断
python3 bidhunter.py demo                                      # 示例效果
python3 bidhunter.py calendar [--days 7]                        # 投标日历
python3 bidhunter.py faq [关键词]                               # 查常见问题
python3 bidhunter.py rules edit [--port 8080]                  # 图形化配规则
python3 bidhunter.py ai read <标书.pdf>                        # v2.0 AI 速读
python3 bidhunter.py ai advise <标书.pdf>                      # v2.5 投标建议
python3 bidhunter.py api serve [--port 8765]                   # v3.0 本地API
python3 bidhunter.py compliance scan <标书> [--mode tender|bid] # v3.5 合规红线扫描
python3 bidhunter.py compliance checklist                      # v3.5 交标前自查清单
```

## 标准流程

### 1. 采集 + 比对 + 报告
```bash
bash pipeline.sh                  # 全流程（缓存优先）
bash pipeline.sh --fresh         # 强制重采当天
bash pipeline.sh --calendar      # 生成后额外打印投标日历
# A4 多维筛选（后过滤）
bash pipeline.sh --budget-min 500000 --budget-max 20000000 --region 天津 --industry 智能设备
```
报告：`bid_reports/report_YYYY-MM-DD.txt`（文字，适配 IM）、`report_YYYY-MM-DD.html`（浏览器）。

### 2. 多通道推送（v1.2）
首次 `python3 config_wizard.py` 配置；`pipeline.sh` 生成报告后自动推送。`push_manager.py` 支持 `test/history/stats/health-check/retry-failed`。关闭用 `pipeline.sh --no-push`。

### 3. v1.5 新能力
- **匹配度评分（A1）**：可投标按 0-100 分排序，等级 强烈推荐/建议跟/可投一般。报告直接显示分数。
- **投标日历（A2）**：`python3 calendar.py <qual文件> --days 30` 看开标/截止日；`--remind` 对临近截止（默认48h）自动推送提醒。
- **多维筛选（A4）**：规则库设 `region_priority.high` / `industry_categories`+`industry_priority` / `budget_priority`，运行时用 `--region/--industry/--budget-min/--budget-max` 过滤。
- **规则编辑器（可视化）**：`python3 bidhunter.py rules edit` → http://localhost:8080，选行业模板、填能力词、实时试标、保存。
- **诊断中心（A6）**：`python3 doctor.py` 输出带错误码（E001~E005 / W001~W004）的诊断与下一步。
- **示例模式（A7）**：`python3 demo.py [--summary] [--calendar]` 用内置示例看完整效果。
- **集中 FAQ（A8）**：`python3 faq.py <关键词>` 检索常见问题。
- **平台扩展（A5）**：内置 3 适配器（cnooc/cebpubservice/ccgp）+ 自定义数据源 `sources.json`（json/rss/html 三种模式，零代码接入任意公开平台）。

### 4. v2.0 本地 AI 增强（零云成本）
```bash
python3 bidhunter.py ai read 招标文件.pdf     # 解析+结构化抽取+风险扫描
python3 bidhunter.py ai read 招标文件.pdf --llm   # 加 LLM 风险扫描
python3 ai/analytics.py --days 30              # 本地业主/品类画像
```
调用你自己的 MiniMax API（仅耗余额），不外传数据到任何 BidHunter 云端（我们无云端）。

### 5. v2.5 投标策略建议
```bash
python3 bidhunter.py ai advise 招标文件.pdf    # 资质自检+评分得分点+报价策略+时间节点
```
**合规边界**：只建议不代劳——不自动填报价、不伪造资质、不写技术方案。所有建议标注"仅供参考，人工确认"。

### 6. v3.0 本地开放能力（零云成本子集）
```bash
python3 api_server.py --port 8765             # 本地查询 API（127.0.0.1，无云端）
python3 webhook_publish.py qual_xxx.jsonl     # 把标讯签名推送到你自己的系统
```
> v3.0 原规划的云/SaaS 部分（多租户、第三方插件市场、数据市场、Salesforce/金蝶连接器）因涉及付费云基础设施，按成本约束未启用。本机 API + 签名 webhook 是其零成本替代。

### 7. v3.5 合规红线引擎（零 API 成本）★

找到标只是第一步，**交了标不被废**才是最后一公里。v3.5 把《招标投标法》《实施条例》《评标委员会和评标方法暂行规定》（12号令）蒸馏成机器可读的 **31 条法定红线**，本地扫描，**不调用任何 LLM，零 API 成本**。

```bash
# 扫招标文件：找出文件里埋了哪些"雷"（实质性要求、违规条款、致命形式要件）
python3 bidhunter.py compliance scan 招标文件.pdf --mode tender

# 扫投标文件：交标前最后一检，找自己文件里的致命项
python3 bidhunter.py compliance scan 投标文件.pdf --mode bid

# 交标前自查清单（31 条，逐条打勾）
python3 bidhunter.py compliance checklist

# 输出 JSON（供其他系统消费）/ 追加 LLM 深度扫描（耗 MiniMax 余额）
python3 bidhunter.py compliance scan 招标文件.pdf --json
python3 bidhunter.py compliance scan 招标文件.pdf --llm
```

**红线分类（31 条）**

| 类 | 名称 | 条数 | 发生阶段 | 决定方 | 后果 |
|---|---|---|---|---|---|
| A | 拒收/不予受理 | 4 | 交标现场 | 招标人/代理机构 | 当场拒收，进不了评标 |
| B | 否决投标 | 14 | 评标阶段 | 评标委员会 | 该份投标出局 |
| C | 投标无效 | 4 | 全程 | 无需认定 | 相关投标**均**无效 |
| D | 反向保护条款（盾牌） | 3 | 维权 | 投标人主张 | 可据此质疑/投诉 |
| E | 多主体串标隔离 | 6 | 评审/调查 | 评标委员会/行政监督 | 视为串通，中标无效 |

**三条最值钱的认知**（其余详见 `compliance/redlines.json`）：

1. **多主体投同一标段，先查《实施条例》第34条**（C02）：单位负责人为同一人、或存在控股/管理关系的不同单位**不得**参加同一标段投标，违反则相关投标均无效。这是**资格硬禁止**，无需任何串通证据，且优先于一切串标推定。
2. **细微偏差不影响投标有效性**（D02，12号令第26条）：个别漏项只会被要求补正，招标文件没规定量化标准的**不得扣分**。与"重大偏差=否决"严格区分——这条能救命。
3. **标底不能作为否决依据**（D01，实施条例第50条）：招标文件若写"报价超出标底±X%作废标处理"，该条款**本身违法**，可据此质疑投诉。扫描器会自动识别此类违规条款并标为"盾牌"。

**合规边界（与 v2.5 一致）**：
- ✅ 做：法条索引、风险提示、自查清单、违规条款识别
- ❌ 不做：法律意见、胜诉承诺、代填报价、伪造资质
- ⚠️ 扫描结果**不构成法律意见**，最终判定以招标文件、评标委员会认定及有权机关解释为准。法规未给出量化标准的（如"低于成本"），本引擎**不设阈值**

**深度审查联动**：本地扫描是"浅层快速筛"，需要逐条法理分析和举证策略时，联动蒸馏姊妹 skill（需另行安装）：`bid-rejection-guard`（25条红线深度审查）、`bid-price-redline`（低于成本举证自救）、`multi-entity-bid-isolation`（多主体串标隔离 10 条清单）。

## 系统组件（位于 `scripts/`）

| 文件 | 作用 | 版本 |
|---|---|---|
| `bid_monitor.sh` | 采集（含自定义数据源加载） | base+A5 |
| `qual_rules.json` | 资质规则库（**必须自定义**） | base+A4字段 |
| `qual_check.py` | 比对引擎 + A1 评分/预算/行业提取 | v1.5 |
| `report_text.py` / `report_html.py` | 文字/HTML 简报（含评分展示） | v1.5 |
| `push_manager.py` / `config_wizard.py` | 推送+配置向导 | v1.2 |
| `calendar.py` | A2 投标日历/倒计时提醒 | v1.5 |
| `filter_multi.py` | A4 多维筛选 | v1.5 |
| `rule_editor.py` | 零代码规则编辑器（HTTP） | v1.5 |
| `doctor.py` | A6 诊断中心 | v1.5 |
| `demo.py` + `samples/` | A7 示例模式 | v1.5 |
| `faq.py` + `docs/FAQ.md` | A8 集中 FAQ | v1.5 |
| `bidhunter.py` | A9 统一命令入口 | v1.5 |
| `custom_source.py` + `sources.example.json` | A5 自定义数据源 | v1.5 |
| `ai/minimax_client.py` | MiniMax 客户端（urllib，零依赖） | v2.0 |
| `ai/doc_parser.py` | B1 标书解析（PDF/Word，优雅降级） | v2.0 |
| `ai/clause_extractor.py` | B1 条款结构化抽取 | v2.0 |
| `ai/risk_scanner.py` | B2 风险条款识别 | v2.0 |
| `ai/doc_reader.py` | B1 总装：AI 速读 | v2.0 |
| `ai/analytics.py` | A3 业主/品类画像 | v2.0 |
| `ai/bid_advisor.py` | v2.5 投标策略建议 | v2.5 |
| `api_server.py` / `webhook_publish.py` | v3.0 本地开放能力 | v3.0 |
| `compliance/redlines.json` | C1 法定红线规则库（31条：A4/B14/C4/D3/E6） | v3.5 |
| `compliance/compliance_scanner.py` | C1 合规红线本地扫描引擎（零 API，含反向排除） | v3.5 |

## 已知坑点

- **IM 发文件失败**：个人 IM 不支持发文件，只能文字。可视化网页供电脑浏览器看。
- **list API 无截止日**：部分平台返回仅 id/title，截止日需 detail 接口（常 401），故只采集当天近似；日历日期从标题解析，未含明确日期的标归入"待核实截止日"。
- **IP 限流**：连发约 20 次后可能 401/403，翻页 sleep 2s + 失败重试冷却 10s。
- **匹配边界**：边界感知规则会挡掉词中误匹配（如"电气设备"里的"电气"因前有 CJK 被挡属正常防误匹配）。能力词尽量让其出现在词首边界可稳定命中。
- **AI 依赖**：v2.0/v2.5 需配置 MiniMax API Key；未配置时 AI 功能自动跳过，不影响基础采集研判。
- **标书解析**：最佳效果需 `pip install PyPDF2 python-docx`（可选）；未装时 PDF 走正则降级、DOCX 可能解析不全。

## 反馈（零成本，30 秒）

| 方式 | 怎么用 | 说明 |
|---|---|---|
| **快速反馈** | `python3 bidhunter.py feedback` | 交互式问三句 → 自动格式化 → 写进剪贴板 → 打开平台评论页，粘贴即可 |
| SkillHub 评论区 | <https://skillhub.cn/skills/user_7a89592b/bidhunter> | 公开讨论，作者可见 |
| ClawHub 评论区 | <https://clawhub.ai/419597334-sudo/bidhunter> | 公开讨论，作者可见 |

> 反馈模块**不上传任何数据**：全程只在本机生成文本、写剪贴板、唤起你的浏览器，无任何后端与网络请求。

## 参考文档

- `references/platforms.md`：支持平台清单、自定义数据源指南
- `references/filter_rules.md`：筛选规则结构
- `references/field_standard.md`：标讯字段标准
- `docs/FAQ.md`：常见问题（`faq.py` 检索）
- `samples/`：示例规则与模板（demo / 行业模板）
