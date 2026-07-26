---
slug: "api-free"
name: "api-free"
version: "1.0.0"
displayName: "REST API参考免费版"
summary: "3大类核心服务的REST API参考,含认证模式与端点示例,快速查阅集成要点"
license: "MIT"
description: |-
  REST API 参考文档库免费版。覆盖 AI/ML、支付、通信 3 大类核心服务的认证模式与端点参考.
  提供基础 curl 示例与常见错误提示。完整 16 类 147 服务、速率限制策略、分页模式、Webhook 签名验证、
  多账户凭证命名等高级功能需升级付费版。仅作文档参考,不代用户执行请求.
tags:
  - 研发工具
  - Productivity
tools:
  - read
  - exec
homepage: "https://skillhub.cn"

---
# REST API 参考手册（免费版）

核心服务的 REST API 参考文档免费版。覆盖 AI/ML、支付、通信 3 大类服务,提供认证模式、端点参考与基础 curl 示例.
> **升级提示**: 完整 16 类 147 服务、速率限制策略、分页模式、Webhook 签名验证、多账户凭证命名等高级功能为付费版专享。升级付费版解锁完整能力.
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| input | string | 是 | REST API参考免费版处理的输入数据或指令 |
| options | object | 否 | 附加配置选项,如模式选择、格式偏好等 |
| callback_url | string | 否 | 异步处理完成后的回调通知URL |

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux

### 依赖项
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-----|:-----|:-----|:-----|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
需要配置对应API Key，详见上文环境配置章节

### 可用性分类
- **分类**: MD+EXEC（）

**API Key配置方式**:
```bash
export API_KEY="your_api_key_here"
```
配置后需重启会话或开启新终端生效。API Key应妥善保管,避免泄露到版本控制系统.
## 核心能力

- **核心服务覆盖**: AI/ML、支付、通信 3 大类服务参考
- **认证文档**: 每个服务的基础认证方式（API Key / Bearer Token）
- **端点参考**: 含 curl 示例的端点说明
- **Content-Type 规则**: POST 请求必带 `Content-Type: application/json`
- **常见错误提示**: 缺少头、密钥暴露等基础错误提醒

### 付费版专享功能
以下功能在免费版中不可用,升级付费版解锁:

- **完整 16 类 147 服务**: 覆盖 CRM、数据库、媒体、社交等全部类别
- **速率限制策略**: `X-RateLimit-Remaining` 头与 429 指数退避
- **分页模式**: cursor / offset / page 三种分页实现
- **Webhook 签名验证**: 各服务签名验证代码示例
- **多账户凭证命名**: `{SERVICE}_{ACCOUNT}_{TYPE}` 规范
- **幂等键使用**: `Idempotency-Key` 头规范
- **resilience 错误处理**: 完整重试模式与错误恢复策略

**输入**: 用户提供付费版专享功能所需的指令和必要参数.
**输出**: 返回付费版专享功能的处理结果,包含执行状态码、结果数据和执行日志.
### 核心服务覆盖

针对核心服务覆盖,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应.
**输入**: 用户提供核心服务覆盖相关的配置参数、输入数据和处理选项.
**输出**: 返回核心服务覆盖的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`核心服务覆盖`的配置文档进行参数调优
### 认证文档

针对认证文档,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应.
**输入**: 用户提供认证文档相关的配置参数、输入数据和处理选项.
**输出**: 返回认证文档的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`认证文档`的配置文档进行参数调优
#
## 免费版服务索引

| 分类 | 文件 | 代表服务 |
|---:|---:|---:|
| AI/ML | `apis/ai-ml.md` | openai, anthropic, cohere, groq, mistral |
| Payments | `apis/payments.md` | stripe, paypal, square, plaid |
| Communication | `apis/communication.md` | twilio, sendgrid, slack, discord, telegram |

> **升级提示**: 付费版额外覆盖 Realtime、CRM、Marketing、Developer、Database、Auth、Media、Social、Productivity、Business、Geo、Support、Analytics 共 13 类 134 个服务.
## 能力速查
1. **先定位文件** — 根据服务名找到对应 `apis/*.md` 文件
2. **必带 Content-Type** — POST/PUT/PATCH 请求需 `Content-Type: application/json`
3. **密钥放请求头** — 使用 `Authorization: Bearer xxx`,不放在 URL 参数
4. **校验响应体** — 部分API返回 HTTP 200 但 body 含错误,需检查响应结构

## 使用流程

### Step 1: 定位服务类别
根据用户提到的服务名,在免费版服务索引中找到对应 `apis/*.md` 文件.
### Step 2: 读取文件索引
```bash
# 读取 AI/ML 分类文件索引
head -20 apis/ai-ml.md
```

### Step 3: 跳转到目标服务段落
```bash
# 按索引行号读取 openai 段落
sed -n '119,230p' apis/ai-ml.md
```

### Step 4: 提取关键信息
- 认证方式（API Key / Bearer Token）
- 端点路径与 HTTP 方法
- 必需参数
- 常见陷阱

### Step 5: 生成集成建议
基于文档内容,为用户提供含 curl 示例的集成方案.
> **提示**: 如需速率限制处理、分页策略、Webhook 验证等高级模式,请升级付费版查阅 `resilience.md`、`pagination.md`、`webhooks.md`.
#
## 案例展示

### 案例1: OpenAI API 集成参考
**场景**: 开发者需要调用 OpenAI Chat Completions

```bash
head -20 apis/ai-ml.md
sed -n '119,230p' apis/ai-ml.md
```

**提取信息**:
- 认证: Bearer Token（`Authorization: Bearer sk-xxx`）
- 端点: `POST /v1/chat/completions`
- 必需头: `Content-Type: application/json`

**集成建议**:
```bash
curl https://api.openai.com/v1/chat/completions \
  -H "Authorization: Bearer sk-xxx" \
  -H "Content-Type: application/json" \
  -d '{"model":"gpt-4","messages":[{"role":"user","content":"Hello"}]}'
```

> **升级提示**: 付费版提供 `X-RateLimit-Remaining` 速率限制处理策略与 429 指数退避方案.
### 案例2: Stripe 支付集成参考
**场景**: 开发者需要集成 Stripe 支付 API

```bash
head -20 apis/payments.md
sed -n '45,120p' apis/payments.md
```

**提取信息**:
- 认证: Bearer Token（`Authorization: Bearer sk_live_xxx`）
- 端点: `POST /v1/charges` 创建收款

**集成建议**:
```bash
curl https://api.stripe.com/v1/charges \
  -H "Authorization: Bearer sk_live_xxx" \
  -d amount=2000 \
  -d currency=usd \
  -d source=tok_visa
```

> **升级提示**: 付费版提供 `Idempotency-Key` 幂等键使用规范,防止网络重试导致重复扣款.
## 错误处理

| 错误场景 | 原因分析 | 处理方式 |
|:---:|:---:|:---:|
| 缺少 `Content-Type` | POST 请求未设 `Content-Type: application/json` | 所有 POST/PUT/PATCH 必带该头 |
| API Key 暴露在 URL | 将密钥放在查询参数 `?api_key=xxx` | 改用请求头 `Authorization: Bearer xxx` |
| HTTP 200 含错误 | 仅检查状态码,未校验 body | 检查响应结构中的 `error` 字段 |
| OAuth Token 过期 | 使用过期 `access_token` | 使用 `refresh_token` 刷新 |
| 服务不在免费版范围 | 如查询 HubSpot、Notion 等非核心服务 | 升级付费版解锁完整 147 服务参考 |

## 常见问题

### Q1: 免费版覆盖多少个服务?
A: 免费版覆盖 3 大类核心服务: AI/ML（openai, anthropic, cohere, groq, mistral）、Payments（stripe, paypal, square, plaid）、Communication（twilio, sendgrid, slack, discord, telegram）。升级付费版解锁完整 16 类 147 服务.
### Q2: 免费版包含速率限制处理策略吗?
A: 免费版仅提示需注意 `Content-Type` 与密钥安全。完整的 `X-RateLimit-Remaining` 速率限制策略与 429 指数退避方案为付费版专享.
### Q3: 如何处理 API 分页?
A: 免费版不包含分页模式文档。升级付费版可查阅 `pagination.md`,获取 cursor / offset / page 三种分页模式的实现参考.
### Q4: Webhook 签名验证怎么做?
A: 免费版不包含 Webhook 签名验证文档。升级付费版可查阅 `webhooks.md`,获取 Slack `X-Slack-Signature`、Stripe `Stripe-Signature` 等各服务的验证代码示例.
### Q5: 多账户场景如何管理凭证?
A: 免费版不包含多账户凭证命名规范。升级付费版可查阅 `credentials.md`,获取 `{SERVICE}_{ACCOUNT}_{TYPE}` 命名规范.
## 已知限制

1. **仅 3 大类服务**: 免费版覆盖 AI/ML、Payments、Communication,其余 13 类需升级
2. **无速率限制策略**: 不含 `X-RateLimit-Remaining` 与 429 处理方案
3. **无分页模式**: 不含 cursor / offset / page 分页文档
4. **无 Webhook 验证**: 不含签名验证代码示例
5. **无幂等键规范**: 不含 `Idempotency-Key` 使用指南
6. **无多账户命名**: 不含 `{SERVICE}_{ACCOUNT}_{TYPE}` 凭证规范

---

> **升级付费版** 解锁: 完整 16 类 147 服务、速率限制策略、分页模式、Webhook 签名验证、多账户凭证命名、幂等键使用等完整能力.
## 输出格式

```json
{
  "success": true,
  "data": {
    "result": "REST API参考免费版处理结果",
    "execution_time": "0.5s",
    "metadata": {
      "version": "1.0",
      "processor": "api"
    }
  },
  "execution_log": [
    "解析输入参数",
    "执行核心处理",
    "格式化输出结果"
  ],
  "error": null
}
```
