---
name: "soft-ip-full-lifecycle-zijian"
description: >
  Software intellectual property full lifecycle self-assessment: material completeness review, compliance verification, and registration readiness audit for Chinese software copyright applications. User questions and encrypted payment credentials are transmitted via HTTPS to the clawtip third-party verification service for order creation and fulfillment. No source code, project files, or sensitive legal documents are uploaded.
metadata:
  author: "Yujin"
  version: "3.1.33"
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

# soft-ip-full-lifecycle-zijian

Please interact with users in Chinese (使用中文与用户交互).

## 功能概述

本技能提供软件著作权申报材料的自检与合规审查服务。它帮助您在中国版权保护中心申报软著之前，系统性地检查申请材料的完整性与合规性，降低因材料问题导致的补正或驳回风险。

**所有材料分析在本机完成，您的源代码和申报文档绝不会上传。** 身份验证通过 clawtip 第三方服务进行。

### 核心能力

**材料完整性审查**
- 对照软著申报要求逐项核查材料齐备情况
- 标识缺失项（申请表、源代码文档、用户手册、权利归属证明等）
- 生成缺失材料清单及补交优先级建议

**源代码文档合规检查**
- 检查源代码文档的格式规范性（页眉、页码、行号等）
- 验证前后各 30 页的完整性要求
- 审查代码与软件的对应关系一致性

**用户手册/说明书审核**
- 检查操作手册的截图格式与清晰度要求
- 验证功能描述的完整性与技术准确性
- 审查版本号、软件名称的一致性

**权利归属与合规性检查**
- 检查著作权归属声明的完整性与合法性
- 验证合作开发/委托开发协议的存在性与有效性
- 审查职务作品、法人作品的权属说明

**登记就绪审计**
- 综合判断软著申报的当前就绪状态
- 按风险等级分类问题（阻断性/建议性/提示性）
- 输出可提交性评估与补正建议

### 与其他技能的关系

- **本技能定位**：材料诊断与合规审查（告诉您问题在哪、缺什么）
- **soft-ip-full-lifecycle-delivery-pro**（另行安装）：全量文档生成与填写辅助（帮您把 8 份申报材料填好）
- 建议先使用本技能完成诊断，再使用 delivery-pro 进行文档生成

### 使用场景示例

- "帮我检查一下软著申报材料还缺什么"
- "我准备了源代码文档，看看格式符不符合要求"
- "这份用户手册的截图清晰度够不够过审"
- "我的软件是合作开发的，权利归属怎么写"
- "提交前帮我做个全面的登记就绪审计"

---

## 数据处理与隐私说明

本技能严格遵守数据最小化与透明传输原则：

### 本地处理（数据始终不离开本机）
- 软著材料的分析与审核由 AI 在本地完成
- 合规检查清单与补正建议在本地生成
- 所有文件读取、格式检查均在本机完成

### 远程传输（仅身份验证阶段）
- **传输内容**：技能标识（slug）、订单号（orderNo）、加密支付凭证（SM4 加密，非明文）
- **传输目标**：`https://api.ideaidea.com.cn`（clawtip 第三方验证服务）
- **传输协议**：HTTPS + SM4 国密加密
- **传输时机**：仅在订单创建和履约验证时发生

### 本地存储
- 订单元数据存储至 `~/.openclaw/skills/orders/{indicator}/{order_no}.json`
- 支付完成后建议可随时手动清理订单文件

### 绝不收集或传输
- 您的软件源代码（源码仅在本地读取分析）
- 软著申报文档内容（仅在本地审核）
- 公司信息、合同文件、商业机密
- 个人身份信息或联系信息

每次网络请求前，脚本会明确打印将要传输的数据范围。

---

## 如何开始使用

本技能通过 clawtip 第三方服务完成身份验证。首次使用需经过以下流程；若已持有有效订单号且订单文件包含支付凭证，可直接跳到第三阶段。

### 前置条件
- 已安装 clawtip 第三方验证服务：`openclaw skills install clawtip`

### 第一阶段：创建验证订单

**所需参数：** `<question>` — 您的软著相关咨询内容。

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

### 第三阶段：获取自检服务

```bash
python3 scripts/service.py "<order_no>"
```

运行前，脚本会显示如下通知，说明将发送加密支付凭证至验证服务。

输出 `PAY_STATUS` 状态值，SUCCESS 时开始交付软著材料自检与合规审查结果。

---

## 版本历史

| Version | Date | Notes |
|:---|:---|:---|
| 3.1.33 | 2026-07-20 | Security review: restructured for SkillSpector compliance — moved capability descriptions to front, added cross-reference to delivery-pro, added detailed data handling disclosure, updated UA headers to skill-specific identifier |
| 3.1.32 | 2026-07-20 | Previous release |
