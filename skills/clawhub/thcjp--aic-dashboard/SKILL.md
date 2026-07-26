---
slug: "aic-dashboard"
name: "aic-dashboard"
version: 1.8.1
displayName: "AIC仪表盘监控"
summary: "轻量级只读监控面板,展示入站邮件与浏览器会话状态,token保护,5秒自动刷新"
license: "Proprietary"
description: |-
  AI Commander 配套管理仪表盘。轻量级只读 Web UI,读取 inbox.jsonl 展示最近 50 封入站邮件,
  读取 session.json 展示浏览器会话状态。通过 token 保护的本地端口提供服务,每 5 秒自动刷新.
  不捕获凭证、不控制浏览器、不发送消息,仅读取本地数据文件并安全呈现.
  适用于独立开发者监控邮件收集器与浏览器认证会话的运行状态.
tags:
  - 研发工具
  - Monitoring
tools:
  - read
  - exec
homepage: "https://skillhub.cn"
# 定价元数据
suggested_price: "99.9 CNY/monthly"
pricing_tier: "L4-企业级"
pricing_model: "monthly"

---
# AIC 仪表盘监控

AI Commander 配套管理仪表盘。轻量级只读 Web UI,读取邮件收集器写入的 `inbox.jsonl` 和浏览器认证写入的 `session.json`,在 token 保护的本地端口统一展示。不捕获凭证、不控制浏览器、不发送消息.
**范围外**（本技能不做）: 邮件收发、浏览器自动化控制、凭证捕获与存储、远程会话管理.
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| input | string | 是 | AIC仪表盘监控处理的输入数据或指令 |
| options | object | 否 | 附加配置选项,如模式选择、格式偏好等 |
| callback_url | string | 否 | 异步处理完成后的回调通知URL |

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|:-----|:-----|:-----|
| 基础功能 | 支持 | 支持 |
| AIC仪表盘监控轻量级只读监控 | 不支持 | 支持 |
| 多标签页并行抓取 | 不支持 | 支持 |
| 反爬虫策略自动绕过 | 不支持 | 支持 |
| 页面结构变化自适应 | 不支持 | 支持 |
| 批量导出结构化数据 | 不支持 | 支持 |

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux

### 依赖项
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|---:|---:|---:|---:|
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

- **邮件展示**: 读取 `inbox.jsonl`,显示最近 50 封入站邮件的发件人、主题、时间、摘要
- **会话状态**: 读取 `session.json`,显示浏览器会话是否活跃、隧道地址、过期时间
- **Token 保护**: 所有请求需携带有效 token,支持 3 种传递方式
- **自动刷新**: 前端每 5 秒轮询后端,无需手动刷新页面
- **零配置启动**: 未设置 `DASHBOARD_TOKEN` 时自动生成随机 token
### 邮件展示

针对邮件展示,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应.
**输入**: 用户提供邮件展示相关的配置参数、输入数据和处理选项.
**输出**: 返回邮件展示的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`邮件展示`的配置文档进行参数调优
### 会话状态

针对会话状态,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应.
**输入**: 用户提供会话状态相关的配置参数、输入数据和处理选项.
**输出**: 返回会话状态的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`会话状态`的配置文档进行参数调优
### Token 保护

针对Token 保护,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应.
**输入**: 用户提供Token 保护相关的配置参数、输入数据和处理选项.
**输出**: 返回Token 保护的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`Token 保护`的配置文档进行参数调优
#
## 环境变量

| 变量 | 必需 | 默认值 | 说明 |
|:---:|:---:|:---:|:---:|
| `DASHBOARD_TOKEN` | 是 | *(随机生成)* | 访问仪表盘的密钥 token |
| `PORT` | 否 | `19195` | Web 服务监听端口 |
| `DASHBOARD_HOST` | 否 | `127.0.0.1` | 绑定地址,设为 `0.0.0.0` 允许局域网访问 |
| `INBOX_PATH` | 否 | `./data/inbox.jsonl` | 邮件数据文件路径 |
| `SESSION_PATH` | 否 | `./data/session.json` | 会话数据文件路径 |

## 安全机制

- 每次启动时,若 `DASHBOARD_TOKEN` 未设置则生成 32 字符随机 token
- 所有请求必须携带 token,支持 3 种方式:
  - URL 查询参数: `?token=xxx`
  - 请求头: `X-Dashboard-Token: xxx`
  - Bearer 认证: `Authorization: Bearer xxx`
- 前端将 token 存入 `localStorage`,页面加载后从 URL 中移除,避免泄露
- 默认绑定 `127.0.0.1`,仅本机可访问;需局域网访问时设 `DASHBOARD_HOST=0.0.0.0`

## 使用流程

### Step 1: 安装依赖
```bash
npm install express@4.21.2
```

### Step 2: 启动服务
```bash
# 零配置启动（自动生成 token）
node （请参考skill目录中的脚本文件）
# ...
# 自定义端口与 token
DASHBOARD_TOKEN=mysecret123 PORT=8080 node （请参考skill目录中的脚本文件）
```

### Step 3: 获取访问 URL
启动后终端输出:
```
AIC DASHBOARD READY
Access URL: http://127.0.0.1:19195/?token=a3f9c2e7b1d4...
```

### Step 4: 浏览器访问
复制完整 URL（含 token）到浏览器打开。页面加载后 token 自动存入 `localStorage`,URL 中的 token 被清除.
### Step 5: 验证数据源
- 邮件区为空: 检查 `INBOX_PATH` 指向的 `inbox.jsonl` 是否存在且有内容
- 会话显示离线: 检查 `SESSION_PATH` 指向的 `session.json` 是否存在且未过期

## 案例展示

### 案例1: 本机默认启动
**场景**: 开发者需要快速查看邮件收集器与浏览器会话状态

```bash
node （请参考skill目录中的脚本文件）
```

**输出**:
```
AIC DASHBOARD READY
Access URL: http://127.0.0.1:19195/?token=a3f9c2e7b1d4f8a6...
```

**说明**: 零配置启动,自动生成 token,绑定 `127.0.0.1:19195`,仅本机可访问。读取 `./data/inbox.jsonl` 与 `./data/session.json`.
### 案例2: 局域网共享监控面板
**场景**: 团队需要在同一局域网内共享监控面板

```bash
DASHBOARD_HOST=0.0.0.0 PORT=19195 DASHBOARD_TOKEN=team-shared-key node （请参考skill目录中的脚本文件）
```

**输出**:
```
AIC DASHBOARD READY
Access URL: http://0.0.0.0:19195/?token=team-shared-key
```

**说明**: 绑定 `0.0.0.0` 允许局域网设备通过 `http://<本机IP>:19195/?token=team-shared-key` 访问。使用固定 token 便于团队共享.
### 案例3: 自定义数据源路径
**场景**: 邮件与会话数据存储在非默认位置

```bash
INBOX_PATH=/var/data/mail/inbox.jsonl \
SESSION_PATH=/var/data/auth/session.json \
node （请参考skill目录中的脚本文件）
```

**说明**: 通过环境变量指向自定义路径,仪表盘读取指定文件渲染内容.
## 错误处理

| 错误场景 | 错误信息 | 原因分析 | 处理方式 |
|:------|------:|:------|:------|
| token 缺失 | `{"error":"token_required"}` | 请求未携带 token | 引导用户使用带 `?token=` 的完整 URL 访问 |
| token 无效 | `{"error":"invalid_token"}` | token 与服务端不匹配 | 检查 `DASHBOARD_TOKEN` 环境变量或重启服务获取新 token |
| 端口被占用 | `EADDRINUSE: address already in use :::19195` | 端口 19195 被其他进程占用 | 修改 `PORT` 环境变量换端口,或停止占用进程 |
| express 未安装 | `Cannot find module 'express'` | 未执行 `npm install express@4.21.2` | 执行依赖安装命令后重新启动 |
| inbox.jsonl 不存在 | 邮件区显示空,控制台 `ENOENT` | `INBOX_PATH` 路径错误或邮件收集器未运行 | 确认邮件收集器已启动并写入文件,检查路径 |
| session.json 格式错误 | 会话区显示异常 | 文件内容非合法 JSON | 检查浏览器认证写入逻辑,确保输出合法 JSON |
| Node.js 版本过低 | `SyntaxError: Unexpected token` | Node.js 版本低于 14 | 升级 Node.js 至 18+ |

## 常见问题

### Q1: 仪表盘是只读的吗? 会修改邮件或会话数据吗?
A: 是的,仪表盘是纯只读视图。仅读取 `inbox.jsonl` 与 `session.json` 文件内容进行展示,不写入、不修改、不删除任何数据,也不发送邮件或控制浏览器.
### Q2: token 每次启动都变吗?
A: 若未设置 `DASHBOARD_TOKEN` 环境变量,每次启动都会生成新的随机 token。如需固定 token,启动前设置 `DASHBOARD_TOKEN=your-fixed-token`.
### Q3: 如何让团队其他成员访问仪表盘?
A: 将 `DASHBOARD_HOST` 设为 `0.0.0.0`,团队成员通过 `http://<你的IP>:<PORT>/?token=<TOKEN>` 访问。注意: 局域网内任何拿到 token 的人都能访问,请妥善保管.
### Q4: 最多显示多少封邮件?
A: 仪表盘读取 `inbox.jsonl` 的最后 50 封邮件进行展示。如需查看更多,建议直接查看原始 JSONL 文件或调整收集器的轮转策略.
### Q5: 页面需要手动刷新吗?
A: 不需要。前端每 5 秒自动向后端轮询最新数据,邮件与会话状态会自动更新。也可手动刷新页面强制重新加载.
### Q6: 浏览器会话状态显示"离线"是什么意思?
A: 表示 `session.json` 文件不存在、内容为空或会话已过期。检查浏览器认证服务是否正常运行,以及 `SESSION_PATH` 路径是否正确.
## 已知限制

1. **仅展示最近 50 封邮件**: 不支持分页浏览历史邮件,需查看原始文件获取完整记录
2. **只读视图**: 不支持邮件回复、会话控制等写操作
3. **依赖外部数据源**: 邮件与会话数据由配套服务写入,仪表盘本身不采集数据
4. **Token 安全性**: token 以明文形式存在于 URL 与 `localStorage`,HTTPS 环境下更安全
5. **单用户设计**: 不支持多用户权限隔离,任何持有 token 的人拥有完整查看权限
6. **Node.js 依赖**: 需安装 `express@4.21.2`,非零依赖运行
