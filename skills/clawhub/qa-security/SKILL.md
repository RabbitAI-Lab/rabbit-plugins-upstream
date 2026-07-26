---
name: "qa-security"
description: >
  Code quality audit, vulnerability scanning, dependency security analysis, and test strategy design. Analysis is performed locally. User question text and encrypted payment credentials are transmitted via HTTPS to api.ideaidea.com.cn (clawtip verification service) for order creation and fulfillment. No source code, credentials, or project files are uploaded.
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

# qa-security

Please interact with users in Chinese (使用中文与用户交互).

## 功能概述

本技能提供代码质量审计与安全审查服务，覆盖代码漏洞扫描、依赖安全分析、测试策略设计和安全最佳实践审查。所有代码审计与安全分析在 AI 本地完成。身份验证通过 clawtip 第三方服务进行，仅问题描述文本（用于生成服务内容）和订单元数据通过 HTTPS 传输。

### 核心能力

**代码漏洞扫描**
- 常见 Web 漏洞检测（SQL 注入、XSS、CSRF、SSRF、命令注入）
- 输入验证与输出编码的完整性审查
- 认证与授权逻辑的缺陷检测
- 会话管理、JWT、OAuth 配置的安全审查
- 敏感数据（密钥、凭据、PII）的明文存储检测

**依赖安全分析**
- 第三方依赖版本审查与已知 CVE 对照
- 过时/弃用包的识别与升级路径建议
- 供应链风险评估（依赖深度、维护活跃度、许可证兼容性）
- 最小依赖原则审查（是否存在可移除的冗余依赖）

**安全最佳实践审查**
- OWASP Top 10 对齐度评估
- 安全编码规范（参数化查询、输出编码、CSP 头等）
- 加密实现审查（算法选择、密钥管理、盐值使用）
- 安全配置检查（CORS、Cookie 属性、TLS 配置）

**测试策略设计**
- 基于代码特征和风险面生成测试计划
- 单元测试覆盖率提升路径
- 集成测试与端到端测试的边界划分
- 安全测试用例设计（模糊测试、渗透测试场景）
- CI/CD 流水线中的质量门禁配置建议

**风险分级与修复优先级**
- 按 CVSS 思路对发现的问题进行严重性分级
- 输出风险矩阵（可能性 × 影响程度）
- 生成按优先级排序的修复路线图
- 每个问题附带可执行的修复代码示例

### 使用场景示例

- "帮我审查这个用户登录模块的安全性"
- "检查项目里的依赖有没有已知漏洞"
- "我们的 API 接口有认证漏洞吗"
- "给这个支付模块设计一套安全测试用例"
- "上线前的安全审查清单帮我看一下"

### 分析流程

1. **问题诊断**：AI 根据您的描述和代码片段进行风险面分析
2. **本地审计**：所有代码审查、依赖分析、策略设计在本地完成
3. **分级输出**：问题按严重性排序，附带修复方案和优先级

---

## 数据处理与隐私说明

### 本地处理（数据始终不离开本机）
- 代码审查、漏洞分析、依赖检查由 AI 在本地完成
- 测试策略和安全建议在本地生成
- 所有文件读取和分析均在本地执行

### 远程传输（仅身份验证阶段）
- **传输内容**：技能标识（slug）、订单号（orderNo）、加密支付凭证（SM4 加密，非明文）
- **传输目标**：`https://api.ideaidea.com.cn`（clawtip 第三方验证服务）
- **传输协议**：HTTPS + SM4 国密加密
- **传输时机**：仅在订单创建和履约验证时发生

### 绝不收集或传输
- 源代码文件内容和项目结构
- 数据库连接信息、API 密钥、环境变量
- 依赖包清单的具体内容（分析在本地完成）
- 任何形式的安全凭据（支付流程必需的加密支付凭证除外，仅通过 HTTPS 传输至 api.ideaidea.com.cn）

---

## 如何开始使用

本技能通过 clawtip 第三方服务完成身份验证。首次使用需经过以下流程。

### 前置条件
- 已安装 clawtip 第三方验证服务：`openclaw skills install clawtip`

### 第一阶段：创建验证订单

```bash
python3 scripts/create_order.py "<question>"
```

运行前，脚本会显示如下通知，说明传输范围。确认后继续执行。

输出 `ORDER_NO`、`AMOUNT`、`QUESTION`、`INDICATOR`。AMOUNT 单位为人民币分。

### 第二阶段：身份验证

使用技能 `clawtip` 完成支付验证，传入 `order_no` 和 `indicator`。

### 第三阶段：获取审计服务

```bash
python3 scripts/service.py "<order_no>"
```

运行前，脚本会显示如下通知，说明将发送加密支付凭证至验证服务。

输出 `PAY_STATUS` 状态值，SUCCESS 时开始交付安全审计与测试策略结果。

---

## 版本历史

| Version | Date | Notes |
|:---|:---|:---|
| 1.1.0 | 2026-07-20 | Restructured SKILL.md: capability-first layout with detailed service descriptions. Updated UA headers to skill-specific identifiers. |
| 1.0.1 | 2026-07-20 | Fix payment flow to match clawtip standard |
| 1.0.0 | 2026-07-19 | Initial release |
