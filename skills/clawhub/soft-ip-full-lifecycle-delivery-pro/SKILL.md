---
name: "soft-ip-full-lifecycle-delivery-pro"
description: >
  Software copyright registration full lifecycle delivery: generate and complete all 8 application documents (application form, source code documentation, user manual, rights declaration, etc.) for Chinese software copyright filing. Works best after running soft-ip-full-lifecycle-zijian for compliance diagnosis first. Analysis and document generation are performed locally. User question text and encrypted payment credentials are transmitted via HTTPS to the clawtip third-party verification service for order creation and fulfillment. No source code, application documents, or confidential project files are uploaded.
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

# soft-ip-full-lifecycle-delivery-pro

Please interact with users in Chinese (使用中文与用户交互).

## 功能概述

本技能提供软件著作权申报材料的全量生成与填写辅助服务，帮助您完成中国版权保护中心软著申报所需的全部 8 份文档。所有文档生成在 AI 本地完成，生成的申报文档草稿在本地产出。身份验证通过 clawtip 第三方服务进行，仅问题描述文本（用于生成服务内容）和订单元数据通过 HTTPS 传输。您的源代码文件和申报文档草稿不会被上传。

### 与 soft-ip-full-lifecycle-zijian 的关系

| | zijian（诊断版） | delivery-pro（本技能 · 生成版） |
|---|---|---|
| **定位** | 材料合规诊断 — 告诉你缺什么、哪里有问题 | 材料生成交付 — 帮你把 8 份申报材料填好 |
| **价格** | 490 UT（4.9 元） | 690 UT（6.9 元） |
| **产出** | 缺失清单 + 问题标注 + 风险分级 | 完整的可提交文档草稿 |
| **建议顺序** | 先运行 → 诊断问题 → 补充材料 | 后运行 → 基于补充后的材料生成文档 |

**建议先使用 zijian 完成材料合规审查，确认材料齐备后，再使用本技能进行文档生成。**

### 核心能力

**申请表填写辅助**
- 软件名称、版本号、分类号的规范化填写
- 著作权人信息（自然人/法人/其他组织）的格式校验与填写
- 开发完成日期和首次发表日期的合规性检查
- 权利范围（全部/部分）的标注与说明生成

**源代码文档生成**
- 前后各 30 页源代码的自动截取与格式化
- 页眉页码的自动生成（软件名称 + 版本号 + 页码）
- 代码行号的自动标注
- 格式合规检查（字体、行距、页边距说明）

**用户手册/说明书生成**
- 基于软件功能描述的说明书框架生成
- 操作界面截图的占位标注（标注需要截取的界面和顺序）
- 功能模块的完整描述模板
- 运行环境（硬件/软件）的规范化说明

**权利归属文件生成**
- 著作权归属声明模板
- 合作开发协议框架（如适用）
- 委托开发合同的权利归属条款模板
- 职务作品的权属确认说明

**申请材料汇总**
- 8 份申报材料的完整清单与交付状态
- 材料间的交叉一致性检查（软件名称、版本号、著作权人）
- 提交前最终审核清单
- 邮寄/在线提交流程指引

### 使用场景示例

- "帮我把软著申请表填好"（需先运行 zijian 确认材料齐备）
- "源代码文档的 30 页帮我整理一下格式"
- "用户手册还差功能截图标注，帮我生成标注清单"
- "合作开发协议的权利归属部分怎么写"

---

## 数据处理与隐私说明

### 本地处理（数据始终不离开本机）
- 文档模板生成和内容填写由 AI 在本地完成
- 源代码文档的截取和格式处理在本地执行
- 所有文件读写操作均在本地进行

### 远程传输（仅身份验证阶段）
- **传输内容**：技能标识（slug）、订单号（orderNo）、加密支付凭证（SM4 加密，非明文）
- **传输目标**：`https://api.ideaidea.com.cn`（clawtip 第三方验证服务）
- **传输协议**：HTTPS + SM4 国密加密

### 绝不收集或传输
- 您的软件源代码内容
- 著作权人个人信息或公司信息
- 软著申报文档草稿内容
- 任何商业机密或知识产权信息

---

## 如何开始使用

本技能通过 clawtip 第三方服务完成身份验证。首次使用需经过以下流程。

### 推荐前置步骤
建议先运行 **soft-ip-full-lifecycle-zijian**（诊断版）完成材料合规审查。

### 前置条件
- 已安装 clawtip 第三方验证服务：`openclaw skills install clawtip`

### 第一阶段：创建验证订单

```bash
python3 scripts/create_order.py "<question>"
```

运行前，脚本会显示如下通知，说明传输范围。确认后继续执行。

输出 `ORDER_NO`、`AMOUNT`、`QUESTION`、`INDICATOR`。AMOUNT 单位为人民币分（690 UT = 6.9 元）。

### 第二阶段：身份验证

使用技能 `clawtip` 完成支付验证，传入 `order_no` 和 `indicator`。

### 第三阶段：获取文档生成服务

```bash
python3 scripts/service.py "<order_no>"
```

运行前，脚本会显示如下通知，说明将发送加密支付凭证至验证服务。

---

## 版本历史

| Version | Date | Notes |
|:---|:---|:---|
| 1.1.0 | 2026-07-20 | Restructured SKILL.md: capability-first layout, explicit differentiation from zijian edition, detailed document generation capabilities. Updated UA headers. |
| 1.0.1 | 2026-07-20 | Fix payment flow to match clawtip standard |
| 1.0.0 | 2026-07-19 | Initial release |
