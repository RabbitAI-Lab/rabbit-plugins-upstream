---
slug: "aic-dashboard-free"
name: "aic-dashboard-free"
version: "1.0.0"
displayName: "AIC仪表盘监控免费版"
summary: "轻量级只读监控面板,展示入站邮件与浏览器会话状态,本机访问,5秒自动刷新"
license: "MIT"
description: |-
  AI Commander 配套管理仪表盘免费版。轻量级只读 Web UI,读取 inbox.jsonl 展示最近 50 封入站邮件,
  读取 session.json 展示浏览器会话状态。通过 token 保护的本地端口提供服务,每 5 秒自动刷新.
  免费版支持本机访问与基础监控功能。局域网共享、自定义数据源路径等高级功能需升级付费版.
tags:
  - 研发工具
  - Monitoring
tools:
  - read
  - exec
homepage: "https://skillhub.cn"

---
# AIC 仪表盘监控（免费版）

AI Commander 配套管理仪表盘免费版。轻量级只读 Web UI,读取邮件收集器写入的 `inbox.jsonl` 和浏览器认证写入的 `session.json`,在 token 保护的本地端口统一展示。不捕获凭证、不控制浏览器、不发送消息.
> **升级提示**: 局域网共享访问、自定义数据源路径、固定 token 配置等高级功能为付费版专享。升级付费版解锁完整能力.
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| input | string | 是 | AIC仪表盘监控免费版处理的输入数据或指令 |
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
本Skill无需额外API Key（LLM能力由Agent平台内置提供）

### 可用性分类
- **分类**: MD+EXEC（）

## 核心能力

- **邮件展示**: 读取 `inbox.jsonl`,显示最近 50 封入站邮件的发件人、主题、时间、摘要
- **会话状态**: 读取 `session.json`,显示浏览器会话是否活跃
- **Token 保护**: 所有请求需携带有效 token,支持 `?token=` 与 `X-Dashboard-Token` 两种方式
- **自动刷新**: 前端每 5 秒轮询后端,无需手动刷新页面
- **零配置启动**: 未设置 `DASHBOARD_TOKEN` 时自动生成随机 token

### 付费版专享功能
以下功能在免费版中不可用,升级付费版解锁:

- **局域网共享访问**: `DASHBOARD_HOST=0.0.0.0` 允许团队设备远程查看
- **自定义数据源路径**: 通过 `INBOX_PATH` 与 `SESSION_PATH` 指向非默认位置
- **固定 Token 配置**: 设置 `DASHBOARD_TOKEN` 环境变量使用固定 token
- **Bearer 认证方式**: `Authorization: Bearer` 请求头传递 token
- **多环境部署**: 自定义 `PORT` 端口与绑定地址

**处理**: 解析付费版专享功能的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回付费版专享功能的处理结果,包含执行状态码、结果数据和执行日志.
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
#
## 环境变量（免费版支持）

| 变量 | 免费版 | 默认值 | 说明 |
|---:|---:|---:|---:|
| `DASHBOARD_TOKEN` | 自动生成 | *(随机)* | 免费版每次启动自动生成,不可自定义 |
| `PORT` | 固定 | `19195` | 免费版使用固定端口 19195 |
| `DASHBOARD_HOST` | 固定 | `127.0.0.1` | 免费版仅本机访问 |
| `INBOX_PATH` | 固定 | `./data/inbox.jsonl` | 免费版使用默认路径 |
| `SESSION_PATH` | 固定 | `./data/session.json` | 免费版使用默认路径 |

## 使用流程

### Step 1: 安装依赖
```bash
npm install express@4.21.2
```

### Step 2: 启动服务
```bash
node （请参考skill目录中的脚本文件）
```

### Step 3: 获取访问 URL
启动后终端输出:
```
AIC DASHBOARD READY
Access URL: http://127.0.0.1:19195/?token=a3f9c2e7b1d4...
```

### Step 4: 浏览器访问
复制完整 URL（含 token）到本机浏览器打开。页面加载后 token 自动存入 `localStorage`.
### Step 5: 验证数据源
- 邮件区为空: 确认 `./data/inbox.jsonl` 存在且有内容
- 会话显示离线: 确认 `./data/session.json` 存在且未过期

> **提示**: 如需指向自定义路径的数据文件,请升级付费版使用 `INBOX_PATH` 与 `SESSION_PATH` 环境变量.
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

**说明**: 零配置启动,自动生成 token,绑定 `127.0.0.1:19195`,仅本机可访问。读取默认路径的 `inbox.jsonl` 与 `session.json`.
> **升级提示**: 如需让团队其他成员通过局域网访问仪表盘,请升级付费版启用 `DASHBOARD_HOST=0.0.0.0`.
## 错误处理

| 错误场景 | 错误信息 | 原因分析 | 处理方式 |
|:---:|:---:|:---:|:---:|
| token 缺失 | `{"error":"token_required"}` | 请求未携带 token | 使用带 `?token=` 的完整 URL 访问 |
| token 无效 | `{"error":"invalid_token"}` | token 与服务端不匹配 | 重启服务获取新 token |
| 端口被占用 | `EADDRINUSE: address already in use :::19195` | 端口 19195 被占用 | 停止占用进程;付费版可自定义端口 |
| express 未安装 | `Cannot find module 'express'` | 未安装依赖 | 执行 `npm install express@4.21.2` |
| inbox.jsonl 不存在 | 邮件区显示空 | 默认路径无文件 | 确认邮件收集器已启动并写入 `./data/inbox.jsonl` |
| session.json 格式错误 | 会话区显示异常 | 文件非合法 JSON | 检查浏览器认证写入逻辑 |

## 常见问题

### Q1: 免费版可以局域网共享吗?
A: 免费版仅支持本机访问（`127.0.0.1`）。如需局域网共享,请升级付费版启用 `DASHBOARD_HOST=0.0.0.0`.
### Q2: token 每次启动都变,能固定吗?
A: 免费版每次启动自动生成随机 token,不支持固定。升级付费版可通过 `DASHBOARD_TOKEN` 环境变量设置固定 token.
### Q3: 最多显示多少封邮件?
A: 仪表盘读取 `inbox.jsonl` 的最后 50 封邮件进行展示。如需查看更多,建议直接查看原始 JSONL 文件.
### Q4: 页面需要手动刷新吗?
A: 不需要。前端每 5 秒自动轮询后端,邮件与会话状态自动更新.
### Q5: 如何使用自定义路径的数据文件?
A: 免费版使用固定默认路径 `./data/inbox.jsonl` 与 `./data/session.json`。升级付费版可通过 `INBOX_PATH` 与 `SESSION_PATH` 环境变量指向任意路径.
## 已知限制

1. **仅本机访问**: 免费版绑定 `127.0.0.1`,不支持局域网共享
2. **固定端口**: 免费版使用端口 `19195`,不可自定义
3. **默认数据路径**: 免费版使用 `./data/` 默认路径,不可自定义
4. **随机 token**: 免费版每次启动生成新 token,不支持固定
5. **仅展示最近 50 封邮件**: 不支持分页浏览历史邮件
6. **只读视图**: 不支持邮件回复、会话控制等写操作

---

> **升级付费版** 解锁: 局域网共享、自定义端口与路径、固定 token、Bearer 认证、多环境部署等完整能力.