---
slug: "alpha-feed-creator"
name: "alpha-feed-creator"
version: 1.0.1
displayName: "内容采集器专业版"
summary: "多源批量采集并智能排名 AI 内容,支持群组推送与企业级内容运营工作流。"
license: "Proprietary"
edition: "pro"
description: |-
  面向内容团队与企业级运营的多源 AI 内容采集与智能排名平台。核心能力:
  - 跨平台多源采集(X、知乎、即刻、微博等),支持批量白名单与多关键词组
  - 基于语义相似度与质量评估的多维智能排名算法
  - 群组自动推送、定时调度、批量日报生成
  - 企业级权限隔离与多租户配置管理

  适用场景:
  - 内容团队每日选题与选题会素材准备
  - 企业品牌账号矩阵的内容运营
  - 行业研究与竞品动态追踪

  差异化: Pro 版在免费版基础上扩展多源采集、智能排名、群组推送、定时调度与企业级管理能力;与免费版配置完全兼容,可平滑升级
tags:
  - 内容采集
  - 企业运营
  - Communication
  - 智能排名
  - 批量调度
tools:
  - read
  - exec
homepage: "https://skillhub.cn"
# 定价元数据
suggested_price: "19.9 CNY/per_use"
pricing_tier: "L2-标准级"
pricing_model: "per_use"

---
# 内容采集器专业版

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|---|---|---|
| 基础功能 | 支持 | 支持 |
| 内容采集器专业版多源批量采集 | 不支持 | 支持 |
| 复杂工作流可视化编排 | 不支持 | 支持 |
| 条件分支与异常重试 | 不支持 | 支持 |
| 定时触发与事件驱动 | 不支持 | 支持 |
| 执行日志与审计追踪 | 不支持 | 支持 |

## 核心能力

| 能力模块 | 说明 | 免费版 | Pro 版 |
|:-----|:-----|:-----|:-----|
| 采集来源 | 支持的平台数量 | 单源(X) | 多源(5+ 平台) |
| 智能排名 | 排名算法维度 | 基础(互动数据) | 多维(语义+质量+互动) |
| 分类输出 | 内容分类层级 | 3 类 | 可配置 N 类 |
| 群组推送 | 自动推送到群组 | 不支持 | 支持(多渠道) |
| 批量调度 | 定时批量任务 | 不支持 | 支持(cron 调度) |
| 多租户管理 | 权限隔离 | 不支持 | 支持 |
| 日报模板 | 自定义模板 | 固定结构 | 可配置模板引擎 |
| 降级策略 | 容错与回退 | 基础降级 | 智能降级+告警 |
### 能力模块

针对能力模块,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应.
**输入**: 用户提供能力模块相关的配置参数、输入数据和处理选项.
**输出**: 返回能力模块的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`能力模块`的配置文档进行参数调优
### 采集来源

针对采集来源,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应.
**输入**: 用户提供采集来源相关的配置参数、输入数据和处理选项.
**输出**: 返回采集来源的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`采集来源`的配置文档进行参数调优
### 智能排名

针对智能排名,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应.
**输入**: 用户提供智能排名相关的配置参数、输入数据和处理选项.
**输出**: 返回智能排名的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`智能排名`的配置文档进行参数调优
#
## 适用场景

### 场景一:内容团队每日选题会

内容团队需要在每日早会前准备好当日的选题素材包,涵盖多个平台的热门 AI 内容.
```bash
# 1. 触发多源批量采集(支持 cron 定时)
# 每日 07:30 自动执行
0 7 * * * agent run alpha-feed-creator-pro --mode=batch --sources=all
# ...
# 2. 采集结果自动推送到团队群组
agent run alpha-feed-creator-pro \
  --push-channel=feishu \
  --push-target="content-team-daily" \
  --report-mode=summary
```

采集完成后,精简版日报会自动推送到团队飞书群,完整版写入 Obsidian 共享库:

```
<team_vault>/Skill平台/项目/AI内容日报/01-日报/2026-07-18_0730.md
```

### 场景二:品牌矩阵内容运营

管理多个品牌账号的内容运营,需要为每个账号定制差异化的采集配置和推送策略.
```bash
# 为不同品牌账号配置独立采集策略
agent run alpha-feed-creator-pro \
  --config=brand-a.yaml \
  --sources="x,zhihu,jike" \
  --keywords="AI Agent,大模型,行业应用" \
  --push-channel=wechat-work \
  --push-target="brand-a-ops"
# ...
agent run alpha-feed-creator-pro \
  --config=brand-b.yaml \
  --sources="x,weibo" \
  --keywords="开源,创业,融资" \
  --push-channel=feishu \
  --push-target="brand-b-ops"
```

### 场景三:行业研究与竞品追踪

研究机构需要持续追踪竞品在多个平台的动态,并生成结构化研究报告.
```bash
# 竞品动态追踪(按周汇总)
agent run alpha-feed-creator-pro \
  --mode=weekly-summary \
  --track-accounts="@competitor1,@competitor2" \
  --report-format=research \
  --output="<vault>/research/竞品追踪/"
```

## 使用流程

### 优秀步:升级配置文件

将免费版配置升级为 Pro 版多源配置:

```yaml
# pro-config.yaml
edition: pro
sources:
  - platform: x
    enabled: true
    api_priority: true
  - platform: zhihu
    enabled: true
  - platform: jike
    enabled: true
  - platform: weibo
    enabled: false  # 按需启用
# ...
whitelist:
  - "@xiaohu"
  - "@dotey"
  - "@marclou"
# ...
keyword_groups:
  - name: "技术深度"
    keywords: ["AI Agent", "LLM 训练", "多模态"]
  - name: "行业应用"
    keywords: ["AI 落地", "企业 AI", "RAG"]
# ...
ranking:
  algorithm: semantic-quality
  dimensions: [semantic, quality, engagement]
  weights:
    semantic: 0.4
    quality: 0.35
    engagement: 0.25
# ...
push:
  enabled: true
  channels:
    - type: feishu
      target: "content-team-daily"
      mode: summary
    - type: wechat-work
      target: "brand-ops"
      mode: full
# ...
schedule:
  cron: "0 7 * * *"
  timezone: "Asia/Shanghai"
# ...
output:
  obsidian_path: "<team_vault>/Skill平台/项目/AI内容日报/"
  structure:
    daily: "01-日报/"
    records: "02-运行记录/"
    docs: "03-文档/"
```

### 第二步:启动批量采集

```bash
# 立即执行一次完整采集
agent run alpha-feed-creator-pro --config=pro-config.yaml
# ...
# 启用定时调度
agent schedule add \
  --skill=alpha-feed-creator-pro \
  --cron="0 7 * * *" \
  --config=pro-config.yaml
```

### 第三步:验证推送

```bash
# 检查推送渠道连通性
agent run alpha-feed-creator-pro --check-push
# ...
# 测试推送一条样例日报
agent run alpha-feed-creator-pro \
  --dry-run \
  --push-test
```

#
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---:|---:|---:|---:|
| content | string | 否 | alpha-feed-creator处理的内容输入 |, 默认: 全部维度 |
| strict_level | string | 否 | 审查严格度, 可选: strict/normal/loose, 默认: normal |

## 输出格式

```json
{
  "success": true,
  "data": {
    "overall_grade": "A",
    "total_score": 92,
    "max_score": 100,
    "summary": "处理完成",
    "details": [
      {
        "item": "代码风格",
        "status": "pass",
        "score": 95,
        "comment": "符合规范"
      },
      {
        "item": "安全合规",
        "status": "warn",
        "score": 80,
        "comment": "符合规范"
      }
    ],
    "improvements": [
      {
        "priority": "high",
        "suggestion": "建议优化",
        "expected_gain": "+5分"
      },
      {
        "priority": "medium",
        "suggestion": "建议优化",
        "expected_gain": "+3分"
      }
    ]
  },
  "error": null
}
```

## 异常处理

| 错误场景 | 原因 | 处理方式 |
|:---:|:---:|:---:|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 

## 依赖说明

### 运行环境

- **Agent 平台**: 支持解析 SKILL.md 的任意 AI Agent(Claude Code / Cursor / Codex / Gemini CLI 等)
- **操作系统**: Windows / macOS / Linux(推荐 Linux 用于生产环境)
- **浏览器**: 多源采集需要 Agent 具备浏览器操作能力(API 不可用时的回退通道)
- **笔记库**: 推荐 Obsidian 团队库,亦支持任意 Markdown 文件管理工具
- **调度服务**: 定时任务依赖 Agent 平台的 cron 调度能力或系统 crontab

### 依赖说明(补充)

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:------|------:|:------|:------|
| LLM 能力 | API | 必需 | 由 Agent 内置大模型提供 |
| Embedding 模型 | API | 必需 | Agent 内置或外部 Embedding 服务 |
| 浏览器环境 | 运行时 | 可选 | Agent 自带浏览器或系统浏览器 |
| Obsidian | 软件 | 可选 | 官网下载,非强制依赖 |
| 飞书/企微 SDK | 库 | 可选 | 对应平台开放平台获取 |
| 采集脚本 | 脚本 | 可选 | `（请参考skill目录中的脚本文件）` 等批量脚本 |
| 调度器 | 服务 | 可选 | Agent 平台调度器或系统 crontab |

### API Key 配置

- **平台 API Key**: 多源采集若使用平台官方 API,需在 Agent 环境预配置各平台访问凭证(建议使用环境变量或密钥管理服务,切勿硬编码).
- **Embedding API**: 语义排名依赖 Embedding 能力,使用 Agent 内置大模型时无需额外 Key;使用外部 Embedding 服务时需配置对应 API Key.
- **推送渠道 Token**: 群组推送需配置对应渠道的机器人 Webhook 或应用 Token(飞书/企微/钉钉等).
- **配置安全**: 所有 API Key 建议通过环境变量注入,配置文件中仅保留引用占位符,避免敏感信息入库.
### 可用性分类

- **分类**: MD+EXEC(纯 Markdown 指令 + 部分功能需 `exec` 命令行执行能力)
- **说明**: 以自然语言指令驱动 Agent 完成多源采集、智能排名、群组推送与定时调度,浏览器操作与脚本执行作为增强通道
- **适用规模**: 团队/企业级,日采集量 500 条以上,支持多租户并发
- **兼容性**: 与 `alpha-feed-creator-free` 配置完全兼容,可平滑升级
- **支持级别**: 优先支持(Pro 版享有问题优先响应与功能迭代建议通道)

## 案例展示

### 企业级多租户配置

```yaml
# enterprise-config.yaml
edition: pro
tenant_mode: enabled
tenants:
  - id: 租户-content-team
    name: "内容团队"
    config: configs/content-team.yaml
    push: feishu://content-team
  - id: 租户-brand-ops
    name: "品牌运营"
    config: configs/brand-ops.yaml
    push: wechat-work://brand-ops
# ...
ranking:
  algorithm: semantic-quality
  cache_enabled: true
  cache_ttl: 3600
# ...
audit:
  enabled: true
  log_path: "logs/audit/"
  retention_days: 90
```

### 自定义日报模板

```markdown
<!-- template: research-report.md -->
# "creator_result" AI 行业研究报告
# ...
## 常见问题
# ...
### Q1: Pro 版如何与免费版共存?
# ...
Pro 版与免费版可共存。两者配置文件格式兼容,Pro 版会优先读取 Pro 专属字段(如 `sources`、`ranking.algorithm`、`push` 等),缺失时回退到免费版行为。建议生产环境统一使用 Pro 版,免费版仅用于个人测试.
# ...
### Q2: 多源采集会不会触发平台风控?
# ...
Pro 版内置防风控策略:每个平台独立限流、随机间隔、API 优先、浏览器回退。建议单平台单次采集不超过 100 条,日采集频次不超过 6 次。多租户场景务必错峰执行,避免同一出口 IP 并发过高.
# ...
### Q3: 群组推送支持哪些渠道?
# ...
Pro 版支持飞书、企业微信、钉钉、Slack 等主流群组渠道,以及 Webhook 通用推送。每个渠道可独立配置推送模式(summary 精简版 / full 完整版)和推送目标。新增渠道可通过实现 `PushChannel` 接口扩展.
# ...
### Q4: 智能排名算法需要额外模型吗?
# ...
语义维度依赖 Embedding 模型计算内容相似度,可使用 Agent 内置大模型的 Embedding 能力,无需额外部署模型。质量维度基于规则与统计特征,不依赖外部模型。所有计算在采集流程内完成,不增加额外 API 调用成本(除 Embedding 外).
# ...
### Q5: 如何为不同团队配置差异化策略?
# ...
使用多租户配置,每个租户独立配置白名单、关键词、排名权重和推送渠道。租户间数据隔离,采集结果与日报互不干扰。管理员可通过 `--租户` 参数指定运行租户.
# ...
### Q6: 定时调度如何管理?
# ...
Pro 版内置 cron 调度器,支持 `agent schedule add/list/remove` 命令管理定时任务。每个任务绑定独立配置文件,支持时区设置。调度日志写入 `02-运行记录/` 目录,便于排查执行异常.
# ...
### Q7: 日报模板如何自定义?
# ...
Pro 版支持 Handlebars 语法的模板引擎。将模板文件放入配置指定的模板目录,在配置中通过 `output.template` 指定模板文件名。模板变量包括 `date`、`summary`、`categories`、`competitor_section`、`degradation_notes` 等.
# ...
### Q8: 采集覆盖率不足时如何处理?
# ...
当某平台采集失败导致覆盖率低于阈值(默认 70%)时,Pro 版会在日报顶部标注降级说明,并通过告警通道通知管理员。建议配置备用来源,当主来源故障时自动启用备用来源补采.
# ...
## 错误处理
# ...
# ...
| 错误场景(续)| 原因 | 处理方式 |
|----:|:----|----:|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |
# ...
# ...