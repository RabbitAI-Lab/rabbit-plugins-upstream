---
name: "innovation-research"
description: >
  Technology trend analysis, competitive landscape research, feasibility assessment, and emerging technology evaluation. Analysis and report generation are performed locally. User question text and encrypted payment credentials are transmitted via HTTPS to the clawtip third-party verification service for order creation and fulfillment. No proprietary research data, business plans, source code, or confidential materials are uploaded.
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

# innovation-research

Please interact with users in Chinese (使用中文与用户交互). If the user asks in another language, switch to that language and ensure all data handling and payment notices are communicated clearly.

## 功能概述

本技能提供技术创新调研与趋势分析服务，覆盖技术栈选型评估、竞品技术对比、专利布局分析和新兴技术可行性评估。所有技术调研与分析在 AI 本地完成，生成的调研报告与建议在本地产出。身份验证通过 clawtip 第三方服务进行，仅问题描述文本（用于生成服务内容）和订单元数据通过 HTTPS 传输。

### 核心能力

**技术栈选型评估**
- 基于业务需求与约束（规模、团队、预算）的多方案对比
- 技术成熟度评估（社区活跃度、文档质量、Long-Term Support 状态）
- 性能基准、生态兼容性、迁移成本的量化分析
- 技术债务风险与未来演进路径预判

**竞品技术对比**
- 同赛道产品的技术架构拆解与对比
- 关键差异化能力的技术实现分析
- 专利壁垒、合规风险与技术护城河评估
- 技术领先窗口与追赶可行性分析

**专利布局分析**
- 目标技术领域的专利地图绘制
- 现有专利的覆盖范围、权利要求的强度评估
- 空白领域与可布局方向识别
- 潜在侵权风险与规避路径

**新兴技术可行性评估**
- 技术就绪度（TRL）评估：从实验室到生产的距离
- 成本收益分析：引入该项技术的 ROI 预测
- 与现有技术栈的整合难度与兼容性评估
- 人才储备与学习曲线的现实评估

**技术路线图规划**
- 分阶段的技术演进路径设计
- 关键技术里程碑与交付物定义
- 风险缓冲方案与技术降级策略
- 季度/年度的技术投资优先级排序

### 使用场景示例

- "我们想从单体架构迁移到微服务，帮我评估一下风险和收益"
- "对比一下 Flutter 和 React Native 在我们这个场景下的适用性"
- "WebAssembly 在边缘计算方向的前景和技术就绪度"
- "我们产品方向上有没有潜在的专利风险"
- "给我们的技术栈做一份未来 12 个月的演进路线图"

### 分析流程

1. **需求澄清**：AI 与您对话确认调研范围、约束条件和期望产出
2. **本地分析**：基于 AI 的知识库和您提供的材料进行多维度分析
3. **报告生成**：输出结构化调研报告，含数据支撑、风险分级和决策建议

---

## 数据处理与隐私说明

### 本地处理（数据始终不离开本机）
- 技术调研、竞品分析、可行性评估由 AI 在本地完成
- 调研报告和决策建议在本地生成
- 所有分析基于 AI 知识库和您本地提供的材料

### 远程传输（仅身份验证与履约阶段）
- **创建订单时**：技能 slug、用户提问文本（用于生成服务内容）、通过 HTTPS 发送至 `https://api.ideaidea.com.cn`
- **履约验证时**：订单号（orderNo）、加密支付凭证（SM4 加密，非明文）通过 HTTPS 发送至同一服务端
- **传输协议**：HTTPS + SM4 国密加密

### 绝不收集或传输
- 您的商业计划、产品路线图或战略文档
- 技术架构图和内部设计文档
- 竞品分析数据和调研笔记
- 任何形式的商业机密或专有数据

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

### 第三阶段：获取调研服务

```bash
python3 scripts/service.py "<order_no>"
```

运行前，脚本会显示如下通知，说明将发送加密支付凭证至验证服务。

输出 `PAY_STATUS` 状态值，SUCCESS 时开始交付技术创新调研结果。

---

## 版本历史

| Version | Date | Notes |
|:---|:---|:---|
| 1.1.0 | 2026-07-20 | Restructured SKILL.md: capability-first layout with detailed service descriptions. Updated UA headers to skill-specific identifiers. |
| 1.0.1 | 2026-07-20 | Fix payment flow to match clawtip standard |
| 1.0.0 | 2026-07-19 | Initial release |
