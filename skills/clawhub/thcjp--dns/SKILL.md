---
name: dns
slug: dns
displayName: "DNS"
version: "1.0.0"
summary: "正确配置DNS记录,TTL/邮件认证/迁移策略得当"
description: "正确配置DNS记录,TTL/邮件认证/迁移策略得当。Configure DNS records correctly with proper TTLs, email authentication,。触发关键词: correctly, dns, records, proper, configure。轻量级设计,低资源占用,适配云端与本地部署。"
license: "MIT"
tools:
  - read
---

# DNS

## Pre-Migration TTL

* Lower TTL to 300s at least 48h before changing records—current TTL must expire first
* Check current cached TTL before planning: `dig +nocmd +noall +answer example.com`
* After migration stable 24h, raise TTL back to 3600-86400s
* Test with multiple resolvers: Google (8.8.8.8), Cloudflare (1.1.1.1), local ISP—they cache independently

## Email Authentication (All Three Required)

* SPF alone insufficient—DKIM and DMARC both needed for deliverability
* DMARC record: `_dmarc.example.com TXT "v=DMARC1; p=quarantine; rua=mailto:dmarc@example.com"`
* SPF must be single TXT record—multiple SPF records invalid; use `include:` for multiple sources
* SPF ending: `-all` (reject) or `~all` (soft fail)—never `+all` or `?all`
* Verify complete setup with mail-tester.com after configuration

## CAA Records

* Limits which Certificate Authorities can issue certs for domain—prevents unauthorized issuance
* Basic: `example.com. CAA 0 issue "letsencrypt.org"`
* Wildcard requires separate entry: `CAA 0 issuewild "letsencrypt.org"`
* Incident reporting: `CAA 0 iodef "mailto:security@example.com"`
* Without CAA, any CA can issue—set explicitly for security-conscious domains

## www Handling

* Configure both apex and www—or redirect one to other; leaving www unconfigured breaks links
* Pick canonical form and stick to it: www → apex OR apex → www
* HTTPS redirect requires cert for both variants before redirect works
* Test both URLs explicitly after setup

## Debugging Commands

* `dig +trace example.com`—full resolution chain from root; reveals where problem occurs
* `dig @ns1.provider.com example.com`—query authoritative nameserver directly, bypasses cache
* Compare authoritative vs cached response—mismatch indicates propagation in progress
* Check all relevant record types—A working doesn't mean AAAA, MX, or TXT are correct

## Cloudflare Proxy Behavior

* Orange cloud (proxied) hides origin IP—breaks SSH, mail, game servers; use grey cloud for non-HTTP
* Proxied records ignore your TTL setting—Cloudflare controls caching
* CNAME flattening at apex works in Cloudflare but causes confusion when migrating away
* Universal SSL only on proxied records—DNS-only requires origin certificate

## Wildcard Records

* `*.example.com` does not match apex `example.com`—both need explicit records
* Explicit subdomain record takes precedence over wildcard
* Wildcard SSL certificates require separate issuance—use DNS challenge with Let's Encrypt

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent( Code / Cursor / Codex /  CLI等)
- **操作系统**: Windows / macOS / Linux

### 依赖说明
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
- 本Skill基于Markdown指令,无需额外API Key(除内容中明确标注的外部API)

### 可用性分类
- **分类**: MD+execute(纯Markdown指令,部分功能需要exec命令行执行能力)
- **说明**: 基于Markdown的AI Skill,通过自然语言指令驱动Agent执行任务

## 核心能力

- Configure DNS records correctly with proper TTLs, email authentication,
  and migration strategies
- 触发关键词: correctly, dns, records, proper, configure

## 适用场景

| 场景 | 输入 | 输出 |
|------|------|------|
| 基础使用 | 用户请求 | 处理结果 |

**不适用于**：需要人工判断的复杂决策场景

## 使用流程

1. 确认运行环境满足依赖说明中的要求
2. 根据适用场景选择合适的使用方式
3. 执行操作并检查输出结果
4. 如遇错误，参考错误处理章节

## 示例

### 示例1：基础用法

```
输入: 用户请求
处理: 根据使用流程执行
输出: 处理结果
```

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 检查网络连接后重试，参考国内替代方案 |

## 常见问题

### Q1: 如何开始使用DNS？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: DNS有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力

---
## 边界条件与限制

### 输入限制
- **输入格式**：技能仅接受符合DNS记录标准的输入，包括A、CNAME、MX、TXT等记录类型。
- **记录长度**：输入的DNS记录长度不应超过255个字符。
- **参数有效性**：输入的DNS参数必须符合相应的DNS记录规范，如SPF记录中的域名和IP地址格式。

### 性能边界
- **并发处理**：技能在同一时间点仅能处理一个DNS请求。
- **响应时间**：技能的响应时间受限于DNS查询的复杂性和网络延迟。

### 兼容性约束
- **操作系统**：技能在Windows、macOS和Linux操作系统上运行，但可能不兼容所有DNS服务器软件。
- **DNS服务器**：技能依赖于DNS服务器的响应，因此可能受到服务器性能和配置的限制。
- **网络环境**：技能在网络连接不稳定或延迟较高的环境下可能无法正常工作。

### 安全限制
- **敏感信息**：技能不支持处理包含敏感信息的DNS记录，如密码或个人数据。
- **外部API**：技能不直接调用外部API，但可能依赖于外部API进行某些操作，如验证SPF记录。

### 功能限制
- **记录类型**：技能不支持所有DNS记录类型，如AAAA、NAPTR等。
- **高级功能**：技能不支持某些高级DNS功能，如DNSSEC、动态DNS更新等。

---
