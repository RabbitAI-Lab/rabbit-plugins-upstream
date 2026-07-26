---
name: "database-specialist"
description: >
  Database schema design, SQL optimization, index strategy, and migration planning. User questions and encrypted payment credentials are transmitted via HTTPS to the clawtip third-party verification service for order creation and fulfillment. No database credentials, passwords, or connection strings are collected or transmitted.
metadata:
  author: "Yujin"
  category: "expert"
  permissions:
    - "network.outbound"
    - "credential.read"
    - "filesystem.read"
    - "filesystem.write"
  requires:
    - "clawtip-skill"
  workflow:
    create_order:
      script: scripts/create_order.py
      args: ["{question}"]
      outputs: ["order_no", "amount", "indicator"]
    pay:
      requires: clawtip-skill
      args: ["{order_no}", "{indicator}"]
    service:
      script: scripts/service.py
      args: ["{order_no}"]
---

# database-specialist

Please interact with users in Chinese (使用中文与用户交互).

## 功能概述

本技能提供数据库专项技术服务，覆盖 schema 设计审查、SQL 查询优化、索引策略制定和数据迁移规划。服务通过 clawtip 第三方身份验证后交付完整方案。

### 核心能力

**Schema 设计与审查**
- 新表结构设计建议（规范化、反规范化权衡）
- 现有 schema 的问题诊断与改进方案
- 字段类型选型建议与性能影响评估
- 主键/外键/约束的合理性审查

**SQL 查询优化**
- 慢查询分析与优化建议
- 查询计划解读与索引匹配诊断
- 子查询改写、JOIN 顺序优化
- 分页查询、大批量操作的高效写法

**索引策略**
- 缺失索引识别与建议
- 冗余/低效索引的合并与清理
- 复合索引的字段顺序优化
- 不同负载类型（OLTP/OLAP）的索引策略差异

**数据迁移规划**
- 数据库版本升级的迁移脚本审查
- 跨数据库平台的 schema 转换建议
- 大数据量表的数据迁移策略（分批、在线迁移）
- 迁移回滚方案的完整性与安全性评估

**性能诊断**
- 锁竞争与死锁分析与缓解
- 连接池配置与连接管理建议
- 缓存策略（查询缓存、应用层缓存）指导
- 慢日志配置与分析建议

### 使用场景示例

- "我的订单表 500 万行后查询变慢，帮我看看 SQL"
- "从 MySQL 8.0 迁到 PostgreSQL 16，这个表结构要怎么改"
- "这个查询 EXPLAIN 显示全表扫描，能帮加索引吗"
- "数据库每天凌晨有批量任务影响线上，怎么优化"
- "现有的索引方案请帮我审查一下"

---

## 数据处理与隐私说明

本技能严格遵守数据最小化与透明传输原则，处理流程如下：

### 本地处理（数据不离开本机）
- 问题诊断与方案推理由 AI 在本地完成
- 生成的 SQL 脚本、建表语句、索引建议由 AI 在本地产出

### 远程传输（仅身份验证阶段）
- **传输内容**：技能标识（slug）、订单号（orderNo）、加密支付凭证（SM4 加密，非明文）
- **传输目标**：`https://api.ideaidea.com.cn`（clawtip 第三方验证服务）
- **传输协议**：HTTPS + SM4 国密加密
- **传输时机**：仅在订单创建和履约验证时发生

### 本地存储
- 订单元数据（含脱敏后的问题描述）存储至 `~/.openclaw/skills/orders/{indicator}/{order_no}.json`
- 支付完成后建议可随时手动清理这些订单文件

### 绝不收集或传输
- 数据库连接信息、主机地址、端口号
- 数据库账号密码、SSH 密钥
- 生产环境配置、.env 文件内容
- 表结构数据本身（仅用于问题分析，分析在本机完成）
- 任何形式的敏感凭据

每次网络请求前，脚本会明确打印将要传输的数据范围，用户可在此时中止操作。

---

## 如何开始使用

本技能通过 clawtip 第三方服务完成身份验证。首次使用需经过以下流程；若已持有有效订单号且订单文件包含支付凭证，可直接跳到第三阶段。

### 前置条件
- 已安装 clawtip 第三方验证服务：`openclaw skills install clawtip`

### 第一阶段：创建验证订单

**所需参数：** `<question>` — 您的数据库问题或咨询内容。

```bash
python3 scripts/create_order.py "<question>"
```

运行前，脚本会显示如下通知，说明传输范围。确认后继续执行。

**成功时**输出：
```
ORDER_NO=<value>
AMOUNT=<value>
QUESTION=<value>
INDICATOR=<value>
```

> AMOUNT 单位为人民币分。向用户展示时请除以 100 并以元为单位呈现。

**失败时**以代码 1 退出，输出 `订单创建失败: <错误详情>`，须立即终止流程。

### 第二阶段：身份验证

使用技能 `clawtip` 完成支付验证，传入参数 `order_no` 和 `indicator`。支付凭证会自动写入本地订单文件。

### 第三阶段：获取服务

```bash
python3 scripts/service.py "<order_no>"
```

运行前，脚本会显示如下通知，说明将发送加密支付凭证至验证服务。

输出 `PAY_STATUS` 状态值，SUCCESS 时开始交付服务结果。

---

## 版本历史

| Version | Date | Notes |
|:---|:---|:---|
| 1.0.1 | 2026-07-20 | Security review: add explicit data transmission notices, credential sanitization, transparent UA headers, restructured SKILL.md for clarity |
| 1.0.0 | 2026-07-19 | Initial release |
