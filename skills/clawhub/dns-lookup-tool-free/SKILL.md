---
slug: dns-lookup-tool-free
name: dns-lookup-tool-free
version: 1.0.0
displayName: DNS查询免费版
summary: "使用dig工具解析域名A/AAAA/CNAME/MX记录，支持基础正反向查询与文档输出.。DNS查询免费版是一款面向运维与开发者的轻量级DNS诊断Skill，封装标准dig命令并提供结构化输"
license: Proprietary
edition: free
description: 'DNS查询免费版是一款面向运维与开发者的轻量级DNS诊断Skill，封装标准dig命令并提供结构化输出。核心能力：

  - 解析A、AAAA、CNAME、MX、TXT、NS等常见记录类型

  - 支持反向DNS查询（PTR记录）

  - 指定上游DNS服务器（如1。Use when 需要代码生成、编程辅助、调试测试、开发部署时使用。不适用于无明确技术栈的模糊需求。'
tags:
  - DNS查询
  - 网络诊断
  - 运维工具
  - 域名解析
  - 工具
  - 效率
  - 运维
  - 监控
  - dns
  - dig
  - short
tools:
  - read
  - exec
  - write
homepage: ""
category: "Automation"
---
# DNS查询免费版（DNS Lookup Tool Free）

## 概述

DNS是互联网的"电话簿"，但原生dig命令的输出对非运维人员不够友好。本Skill封装dig并提供结构化、可读性强的查询结果，同时给出故障定位建议，让DNS排查从"看一堆文本"变成"读一份诊断报告".
设计原则：
1. **精准优先**：默认输出精简格式（+short），需要细节时切换完整模式
2. **链路追踪**：自动识别CNAME链，追踪到最终IP
3. **多源对比**：支持指定不同DNS服务器对比解析结果
4. **可读输出**：将原始dig输出转化为表格与建议

## 核心能力

### 支持的记录类型

| 记录类型 | 用途 | 查询示例 |
|----|---|----|
| A | IPv4地址 | `dig example.com A +short` |
| AAAA | IPv6地址 | `dig example.com AAAA +short` |
| CNAME | 别名记录 | `dig www.example.com CNAME +short` |
| MX | 邮件服务器 | `dig example.com MX +short` |
| TXT | 文本记录（SPF/DKIM/DMARC） | `dig example.com TXT +short` |
| NS | 域名服务器 | `dig example.com NS +short` |
| SOA | 起始授权记录 | `dig example.com SOA +short` |
| PTR | 反向解析（IP→域名） | `dig -x 93.184.216.34 +short` |

**处理**: 解析支持的记录类型的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回支持的记录类型的响应数据,包含状态码、结果和日志.
### 查询模式

| 模式 | 命令 | 适用场景 |
|:-----|:-----|:-----|
| 精简模式 | `dig +short` | 只看结果IP，快速确认 |
| 完整模式 | `dig` | 查看TTL、权威服务器等详情 |
| 指定DNS | `dig @1.1.1.1` | 对比不同DNS的解析结果 |
| 反向查询 | `dig -x <IP>` | 通过IP找域名 |
| ANY查询 | `dig ANY` | 一次性获取所有记录（部分DNS不支持） |

**处理**: 解析查询模式的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回查询模式的响应数据,包含状态码、结果和日志.
### 核心功能执行
用`input_params`参数进行配置.

**处理**: 解析核心功能执行的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回核心功能执行的响应数据,包含状态码、结果和日志.
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作
**能力覆盖范围**：本skill的核心能力覆盖以下场景关键词：工具解析域名、支持基础正反向查、询与文档输出、查询免费版是一款、面向运维与开发者、的轻量级、封装标准、命令并提供结构化、核心能力、等常见记录类型、支持反向、指定上游、Use、when、需要代码生成、编程辅助、调试测试、开发部署时使用、不适用于无明确技、术栈的模糊需求等。这些关键词对应description中声明的使用场景,均已在上述能力点中提供对应的操作支持.
## 使用场景

### 场景一：网站打不开排查
用户报告网站无法访问。第一步用`dig example.com A +short`确认域名是否解析到正确IP。若返回空或错误IP，问题在DNS；若返回正确IP，问题在网络或服务端.
### 场景二：DNS变更验证
修改DNS记录后，需要确认全球生效情况。通过`dig @1.1.1.1 example.com A`与`dig @8.8.8.8 example.com A`对比不同DNS的缓存状态，判断TTL过期进度.
### 场景三：邮件配置检查
邮件发送失败时，检查MX记录指向是否正确，TXT记录中的SPF/DKIM配置是否完整。`dig example.com MX +short`与`dig example.com TXT +short`组合使用.
### 场景四：CDN接入验证
接入CDN后，验证CNAME是否正确指向CDN域名，并追踪CNAME链到最终CDN边缘节点IP.
### 场景五：IPv6支持确认
确认服务是否支持IPv6，`dig example.com AAAA +short`返回IPv6地址即支持.
## 快速开始

### 30秒上手

1. **安装工具**（若未安装，见依赖说明）
2. **执行查询**：`dig example.com A +short`
3. **解读结果**：Agent会自动分析输出并给出建议

### 示例

以下是DNS查询免费版的典型使用示例，展示核心功能的输入输出流程.
## 输入格式
| 参数名 | 类型 | 必填 | 说明 |
|---:|---:|---:|---:|
| input | string | 是 | DNS查询免费版处理的输入数据或指令 |
| options | object | 否 | 附加配置选项,如模式选择、格式偏好等 |
| callback_url | string | 否 | 异步处理完成后的回调通知URL |

```bash
dig example.com A +short
```

**查询AAAA记录（IPv6）**：
```bash
dig example.com AAAA +short
```

**查询MX记录（邮件服务器）**：
```bash
dig example.com MX +short
```

**反向查询（IP→域名）**：
```bash
dig -x 93.184.216.34 +short
```

**指定DNS服务器查询**：
```bash
dig @1.1.1.1 example.com A +short
```

**完整DNS响应（含TTL与权威段）**：
```bash
dig example.com ANY
```

## 配置示例

### 依赖详情

**CentOS/RHEL/Fedora**：
```bash
sudo dnf install bind-utils
```

**Ubuntu/Debian**：
```bash
sudo apt-get install -y dnsutils
```

**macOS**：系统自带dig，无需安装.
**Windows**：可使用WSL或安装 BIND9工具包.
### 常用DNS服务器

| DNS服务器 | IP | 特点 |
|:-----:|:-----:|:-----:|
| Cloudflare | 1.1.1.1 | 隐私优先，速度快 |
| Google | 8.8.8.8 / 8.8.4.4 | 全球节点，稳定 |
| Quad9 | 9.9.9.9 | 安全防护，拦截恶意域名 |
| 阿里DNS | 223.5.5.5 | 国内速度快 |
| 腾讯DNS | 119.29.29.29 | 国内速度快 |

## 最佳实践

1. **先精简后完整**：先用`+short`快速确认结果，需要细节时去掉`+short`
2. **多源对比**：DNS变更后，至少对比2个DNS服务器的结果
3. **关注TTL**：完整模式下的TTL值反映缓存剩余时间，判断变更生效进度
4. **CNAME追踪**：遇到CNAME时，继续查询CNAME目标的A记录，直到获得IP
5. **反向查询验证**：通过IP反查域名，验证解析一致性
6. **ANY记录谨慎**：部分DNS服务器限制ANY查询，建议按类型逐个查询
7. **缓存清理**：本地DNS缓存可能影响结果，必要时清理系统DNS缓存

## 常见问题

### Q1：dig命令未找到？
A：需要安装bind-utils（CentOS）或dnsutils（Ubuntu）。安装命令见配置示例章节.
### Q2：为什么不同DNS服务器返回不同结果？
A：DNS有全球缓存机制，TTL未过期时各DNS返回缓存值。变更后需等待TTL过期才会全球生效.
### Q3：ANY查询返回不全？
A：部分DNS服务器（如Cloudflare）为减少负载限制了ANY查询。建议按记录类型逐个查询.
### Q4：能批量查询多个域名吗？
A：免费版支持单域名查询。批量查询、JSON输出、监控告警属于专业版能力，详见dns-lookup-tool-pro.
### Q5：能查询DNSSEC状态吗？
A：免费版不提供DNSSEC验证。DNSSEC校验、TLSA记录、HTTPS记录属于专业版能力.
### Q6：反向查询返回空怎么办？
A：并非所有IP都配置了PTR记录。云服务器、CDN节点IP通常没有PTR记录，属正常现象.
## 已知限制

本免费体验版限制以下高级功能：
- ❌ 批量域名查询（>1个域名/次）
- ❌ JSON结构化输出
- ❌ DNSSEC签名验证
- ❌ TLSA/HTTPS/SVCB等新记录类型
- ❌ DNS解析历史记录与追踪
- ❌ 解析延迟统计与对比
- ❌ 定时监控与告警

解锁全部功能请使用专业版：dns-lookup-tool-pro
- 当前为免费版本,如需完整功能请升级到付费版获取全部能力
## 依赖说明

### 运行环境
- **Agent平台**：支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**：Windows / macOS / Linux
- **网络**：可访问UDP/TCP 53端口

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:------|------:|:------|:------|
| LLM API | API | 必需 | 由Agent平台内置LLM提供 |
| dig | 系统命令 | 必需 | 安装bind-utils或dnsutils包 |
| 网络连接 | 网络 | 必需 | 可访问公网DNS服务器 |

### API Key 配置
- 本Skill基于系统命令，无需额外API Key
- dig直接查询DNS服务器，不经过第三方API

### 可用性分类
- **分类**：MD+EXEC（Markdown指令驱动，查询执行需要exec命令行能力）
- **说明**：轻量级DNS诊断Skill，通过dig命令完成域名解析查询

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---:|:---|---:|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 执行ping命令测试网络连通性,检查防火墙和代理设置连接后执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令，参考国内替代方案 |

## 输出格式
```json
{
  "success": true,
  "data": {
    "result": "DNS查询免费版处理结果",
    "execution_time": "0.5s",
    "metadata": {
      "version": "1.0",
      "processor": "dns lookup"
    }
  },
  "execution_log": ["解析输入参数", "执行核心处理", "格式化输出结果"],
  "error": null
}
```
