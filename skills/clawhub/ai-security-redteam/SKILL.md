---
name: ai-security-redteam
slug: ai-security-redteam
display_name: AI安全与红队测试
displayName: AI安全与红队测试
title: AI安全与红队测试
version: 1.0.0
category: 通用技能
platforms:
  - windows
  - macos
  - linux
  - web
author: 注册老炮
license: MIT
description: AI 安全与红队测试实操手册——覆盖 AI 系统六大攻击面（提示注入、越权与工具滥用、数据与隐私泄露、幻觉与质量缺陷、供应链与模型投毒、拒绝服务），OWASP LLM Top 10 风险映射，完整红队测试流程（目标定义/攻击面建模/用例设计/执行/报告/修复复测），直接与间接提示注入测试用例库、Agent 越权与沙箱逃逸测试、训练数据泄露与记忆攻击测试、幻觉检测基准，附漏洞分级与修复建议、零依赖本地工具一键生成风险清单、测试用例与报告模板。面向 AI 工程、安全测试、信息安全负责人，与 AI 治理/智能体治理形成"制度+技术"闭环。
description_en: A hands-on playbook for AI security and red team testing — covering six attack surfaces of AI systems (prompt injection, overreach and tool misuse, data and privacy leakage, hallucination and quality defects, supply chain and model poisoning, denial of service), OWASP LLM Top 10 risk mapping, a complete red team workflow (objective definition/attack-surface modeling/test-case design/execution/reporting/remediation re-testing), direct and indirect prompt-injection test case libraries, agent overreach and sandbox escape tests, training-data leakage and memorization attack tests, hallucination detection baselines, plus vulnerability grading and remediation guidance. Includes a zero-dependency local toolkit for risk checklists, test cases and report templates. Built for AI engineering, security testing and information security leaders — the technical-side counterpart to AI governance and agent governance.
tags:
  - AI安全
  - 红队测试
  - 提示注入
  - LLM安全
  - OWASP
  - 渗透测试
  - 安全测试
  - AI红队
  - Red Teaming
  - Prompt Injection
  - AI Security
---

# AI 安全与红队测试

AI 安全验证工作台：**看得见攻击面、造得出测试用例、跑得了红队流程、出得来分级报告、修得了关键漏洞**。面向 AI 工程、安全测试与信息安全负责人——治理管"制度与风险"，红队管"技术验证"，两者闭环才是完整防线。

## 什么时候用这个技能

- **安全评估**：「我们的 AI 应用有什么攻击面？要测什么？」
- **红队流程**：「AI 红队测试怎么做？从哪开始？」
- **注入测试**：「提示注入怎么测？直接/间接注入用例怎么写？」
- **Agent 安全**：「Agent 越权/逃逸怎么测？沙箱怎么验证？」
- **数据隐私**：「训练数据会泄露吗？记忆攻击怎么测？」
- **报告修复**：「漏洞怎么分级？怎么修？怎么复测？」

## 怎么用（两种模式）

### 模式一：直接问（推荐）

> 「我们的客服 AI 有哪些攻击面？优先测什么？」
> 「提示注入测试用例给我来一组」
> 「红队测试报告怎么出？漏洞怎么分级？」

### 模式二：本地工具（要结构化结果）

```bash
# ① 风险清单：输入 AI 系统描述，输出攻击面与风险点
python tools/ai_redteam_toolkit.py risk --system "客服AI，接知识库，可调用CRM和发邮件"

# ② 测试用例生成（按攻击面）
python tools/ai_redteam_toolkit.py cases --surface injection     # injection/overreach/privacy/hallucination/supplychain/dos

# ③ 漏洞分级（按危害描述）
python tools/ai_redteam_toolkit.py grade --desc "攻击者可注入指令让AI泄露全部客户数据"

# ④ 红队报告模板
python tools/ai_redteam_toolkit.py report

# ⑤ 修复建议（按漏洞类型）
python tools/ai_redteam_toolkit.py fix --vuln injection

# 查看全部命令
python tools/ai_redteam_toolkit.py --help
```

## 知识库导航（references/）

| 模块 | 文件 | 解决什么问题 |
|---|---|---|
| ① 风险全景 | `references/01-AI安全风险全景.md` | 六大攻击面、OWASP LLM Top 10 映射 |
| ② 红队流程 | `references/02-红队测试流程.md` | 五步流程、范围界定、合规边界 |
| ③ 提示注入测试 | `references/03-提示注入测试.md` | 直接/间接注入、用例库、防御绕过 |
| ④ 越权与逃逸测试 | `references/04-越权与逃逸测试.md` | Agent 越权、工具滥用、沙箱逃逸 |
| ⑤ 数据与隐私测试 | `references/05-数据与隐私测试.md` | 训练数据泄露、记忆攻击、PII 提取 |
| ⑥ 幻觉与质量测试 | `references/06-幻觉与质量测试.md` | 幻觉检测、基准、RAG 场景 |
| ⑦ 供应链与 DoS | `references/07-供应链与拒绝服务.md` | 模型投毒、组件供应链、DoS |
| ⑧ 报告与修复 | `references/08-报告与修复.md` | 漏洞分级、修复建议、复测流程 |
| ⑨ FAQ | `references/09-FAQ.md` | 高频疑问 |

## 快速上手（三步）

1. **摸攻击面**：用 `risk` 命令输入系统描述，对照 01 模块六大攻击面；
2. **跑测试**：`cases` 命令取用例，按 02 模块流程执行；
3. **出报告**：`grade` 分级 + `report` 模板，`fix` 拿修复建议。

## 能力边界（如实说明）

- **本技能是方法库与工具，不是安全结论**：测试需由具备资质的安全团队在授权范围内执行；真实系统测试须取得书面授权；
- **OWASP LLM Top 10 等清单随版本更新**，引用前复核最新版；
- **工具不联网**：本地规则匹配，不发起任何真实攻击、不采集数据。

## 常见问题（FAQ）

- **Q：红队测试合法吗？** 只对已获书面授权的自有/托管系统执行；未授权测试可能违法（见 02 模块合规边界）。
- **Q：没有安全团队能做吗？** 可先做"轻量自测"（用例库 + 人工评审），高危项再委托专业红队。
- **Q：和渗透测试有什么区别？** 渗透测传统 IT 系统，AI 红队额外覆盖提示注入/幻觉/Agent 越权等 AI 特有攻击面。
- **Q：工具会真的攻击吗？** 不会——只生成用例与流程，不发起攻击、不联网。

## 版权与许可

**版权与许可**：© 2026 注册老炮。本作品（含方法论、模板、法规整理与原创表达）依 MIT License 提供，详见 `LICENSE.md`。

**知识版权声明**：本作品汇集的 AI 安全方法论、测试用例、流程整理与原创表达，归 注册老炮 所有。未经许可，不得复制、转载、转售本作品全部或实质部分，不得用于任何模型训练或二次分发牟利。

**免责声明**：本作品按「现状」(AS IS) 提供，不作任何明示或暗示的担保，包括但不限于适销性、特定用途适用性与安全保证。使用者应自行核实并承担使用后果，作者不对因使用本作品产生的任何直接或间接损失负责。
