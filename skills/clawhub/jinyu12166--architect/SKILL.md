---
name: "ssq-analyzer"
version: "1.0.20"
description: >
  SSQ (Double Color Ball) lottery intelligent analysis: fetches official draw data from cwl.gov.cn, computes hot/cold statistics, frequency distributions, AC values, odd-even ratios, and zone distributions. Free tier: all statistical analysis and trend charts. Paid tier ($3.9/run): 5 recommended number sets with cross-validation filtering, delivered after clawtip third-party identity verification. User question text and encrypted payment credentials are transmitted via HTTPS to the clawtip verification service for order creation and fulfillment. No SSQ analysis data, purchase history, or personal user information is uploaded.
metadata:
  author: "Yujin"
  version: "1.1.0"
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

# ssq-analyzer

Please interact with users in Chinese (使用中文与用户交互). If the user asks in another language, switch to that language and ensure all data handling and payment notices are communicated clearly.

## 功能概述

本技能提供双色球彩票的智能分析服务，从中国福利彩票官网（cwl.gov.cn）拉取最新开奖数据，进行冷热号统计、规律分析和号码推荐。

**免费提供全部统计分析内容，付费仅用于五组推荐号码的生成。**

### 免费功能（无需支付，即刻可用）

**数据抓取与数据库管理**
- 从 cwl.gov.cn 官方 API 自动拉取最新开奖数据
- 增量更新本地 SQLite 数据库，自动去重
- 当前数据库覆盖 50+ 期历史数据

**红球冷热属性统计**
- 基于近 20 期的热度排名（热号 ≥ 6 次、温号 3-5 次、冷号 < 3 次）
- 逐球号的遗漏期数和出现频率
- 可视化热力图（# 号条状图）

**蓝球统计**
- 近 20 期蓝球出现次数和遗漏期数
- 热温冷属性分类

**特征分布统计**
- 奇偶比分布（从 1:5 到 5:1 的频率）
- AC 值分布（算术复杂度，7-10 为高概率区间）
- 三区分布（1-11 / 12-22 / 23-33 的号码分布模式）
- 和值统计（平均值、最大/最小值）

**近 20 期原始开奖数据**
- 完整展示最近 20 期的红球、蓝球和开奖日期

### 付费功能（3.9 元/次，通过 clawtip 验证后交付）

**备选蓝球推荐（4 枚）** — 基于冷号反弹概率、奇偶搭配、遗漏深度等多策略综合排序，含逐球推荐理由。

**最终推荐号码（5 组）** — 每组包含 6 个红球 + 1 个蓝球，全部通过以下过滤规则校验：
- 奇偶比：仅允许 3:3、4:2、2:4
- AC 值：仅允许 7-10
- 三区分布：仅允许均衡/偏均衡模式
- 和值：仅允许 80-150
- 连号：禁止三连号，二连号不超过 1 组
- 冷热配比：热号 ≤ 3，冷号 ≤ 3，温号 ≥ 2
- 组间交叉验证：任意两组间重复红球不超过 2 个

每组附完整的维度校验表（奇偶比、AC 值、三区分布、和值、连号数、冷热配比）和选号策略备注。

### 使用场景示例

- "帮我更新一下最新的双色球开奖数据"（免费）
- "看看最近的冷热号分布"（免费）
- "这期的奇偶比和 AC 值趋势怎么样"（免费）
- "给我生成 5 组推荐号码"（付费，3.9 元）

### 分析流程

1. **数据抓取**：运行 `fetch_ssq.py` 从 cwl.gov.cn 拉取最新开奖数据存入本地 SQLite
2. **统计分析**（免费）：运行 `analyze_ssq.py` 生成完整分析报告，写入 `最新分析结果.md`
3. **号码推荐**（付费）：通过 clawtip 验证后，从分析报告的第四、五部分读取推荐结果

---

## 数据处理与隐私说明

本技能严格遵守数据最小化与透明传输原则：

### 本地处理（数据始终不离开本机）
- 开奖数据拉取与存储（SQLite 数据库在本地）
- 冷热统计、特征分析、号码生成均在本地 Python 脚本完成
- 分析报告写入本地 Markdown 文件

### 远程传输（仅身份验证阶段）
- **传输内容**：技能标识（slug）、订单号（orderNo）、加密支付凭证（SM4 加密，非明文）
- **传输目标**：`https://api.ideaidea.com.cn`（clawtip 第三方验证服务）
- **传输协议**：HTTPS + SM4 国密加密
- **传输时机**：仅在订单创建和履约验证时发生

### 本地存储
- 订单元数据存储至 `~/.openclaw/skills/orders/{indicator}/{order_no}.json`
- 开奖数据库 `ssq_data.db` 和分析报告 `最新分析结果.md` 存储在 scripts 目录

### 绝不收集或传输
- 个人身份信息、设备信息
- 支付密码或钱包私钥
- 选号偏好或购买记录

---

## 如何开始使用

### 免费部分 — 随时可用

**抓取最新数据：**
```bash
python3 scripts/fetch_ssq.py
```

**生成分析报告：**
```bash
python3 scripts/analyze_ssq.py
```

报告生成后可直接阅读 `scripts/最新分析结果.md`。报告的第五、六部分（备选蓝球、推荐号码）需要 clawtip 验证后获取。

### 付费部分 — 获取推荐号码

本技能通过 clawtip 第三方服务完成身份验证。首次使用需经过以下流程；若已持有有效订单号且订单文件包含支付凭证，可直接跳到第三阶段。

**前置条件：** 已安装 clawtip 第三方验证服务 — `openclaw skills install clawtip`

**第一阶段 — 创建验证订单：**
```bash
python3 scripts/create_order.py "<question>"
```

运行前，脚本会显示如下通知，说明传输范围。确认后继续执行。

**第二阶段 — 身份验证：** 使用技能 `clawtip` 完成支付验证，传入 `order_no` 和 `indicator`。

**第三阶段 — 获取推荐号码：**
```bash
python3 scripts/service.py "<order_no>"
```

运行前，脚本会显示如下通知，说明将发送加密支付凭证至验证服务。

---

## 风险提示

> 本报告基于历史数据统计分析生成，彩票开奖为随机独立事件，任何分析方法均不能保证中奖。请理性购彩，量力而行。

---

## 版本历史

| Version | Date | Notes |
|:---|:---|:---|
| 1.1.0 | 2026-07-20 | Freemium model: statistics free, recommendations paid. Restructured SKILL.md with capability-first layout. Updated UA headers to skill-specific identifiers. |
| 1.0.1 | 2026-07-20 | Fix payment flow to match clawtip standard |
| 1.0.0 | 2026-07-19 | Initial release |
