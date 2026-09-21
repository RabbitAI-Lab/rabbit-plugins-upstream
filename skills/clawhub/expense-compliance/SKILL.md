---
name: expense-compliance
description: "使用场景: 用户要求识别报销票据、按其提供的报销制度检查金额与附件、检测同账户历史重复票据，或导出带规则和票据证据的报销合规审核建议时。"
license: MIT-0
metadata:
    {
        "packageVersion": "1.0.1",
        "openclaw":
            {
                "emoji": "🧾",
                "homepage": "https://ai-skills.open-idea.net",
                "primaryEnv": "EXPENSE_COMPLIANCE_API_KEY",
                "requires": { "env": ["EXPENSE_COMPLIANCE_API_KEY"], "bins": ["curl"] },
            },
    }
---

# 报销合规审核

## Skill 简介

报销合规审核 Skill 先识别发票、收据、行程单或客票，再依据用户创建的版本化制度执行金额、附件、币种、票据日期、禁用商户和历史重复检查。结果保留制度版本、票据来源任务、规则 ID 与证据，只提供审核建议，不代表付款批准、官方发票验真或舞弊认定。

## 平台入口与注册

1. 打开 [AI Skills 平台](https://ai-skills.open-idea.net/)，新用户可进入 [注册页面](https://ai-skills.open-idea.net/register)，已有账号进入 [登录页面](https://ai-skills.open-idea.net/login)。
2. 登录后进入 [产品管理](https://ai-skills.open-idea.net/dashboard/products) 开通本 Skill，再到 [API 密钥管理](https://ai-skills.open-idea.net/dashboard/keys) 创建密钥。

## Skill 安装与配置

1. 在 [API 密钥管理](https://ai-skills.open-idea.net/dashboard/keys)中选择已开通的产品，创建并复制 API 密钥。
2. 在 OpenClaw 中安装本 Skill。
3. 将复制的密钥配置到本 Skill 的 API 密钥环境变量，然后重启 Gateway：

```sh
openclaw config set env.EXPENSE_COMPLIANCE_API_KEY "你的平台APIKey"
openclaw gateway restart
```

## Agent 执行规则

1. 首次使用先通过 `policy.create`（创建报销制度）建立结构化制度；制度更新必须提供当前 `expected_version`（预期版本），历史审核继续保留原规则快照。
2. 每张票据先调用 `receipt.extract`（识别票据），持续轮询到成功终态；向用户展示低置信度字段并要求核对，不得自行补造票号、日期、销售方或金额。只有用户明确表示已对照原图核验后，才能把对应任务 ID 放入 `confirmed_receipt_task_ids`（已人工核对确认的票据任务 ID）。
3. 收集成功 OCR（文字识别）任务 ID 后调用 `claim.audit`（审核报销申请）。`confirmed_receipt_task_ids`（已人工核对确认的票据任务 ID）必须是本次 `receipt_task_ids`（本次审核引用的票据任务 ID 列表）的子集；金额、规则命中与重复检测结果以平台返回为准，不得使用模型重新计算、覆盖置信度或冒充用户确认。
4. `non_compliant`（不合规）表示命中拒绝级规则，`manual_review`（需人工复核）表示仍需人工核对，`compliant`（符合已配置规则）仅表示未命中已配置规则；三者都不是付款批准。
5. 不宣称完成税务机关验真，不把“疑似重复”表述为舞弊，不执行付款、退款、报销审批或财务系统写入。

## 完成标准

- 异步票据识别提交后持续轮询任务状态，直到成功或失败的终态再汇报；不要在 `queued`（排队中）/`processing`（处理中）中途停止。
- 遇 429（请求过于频繁）/503（服务暂时不可用）时遵循 `Retry-After`（建议重试等待时间）或有限指数退避；同一逻辑请求必须复用原 `Idempotency-Key`（幂等键）。
- 一次审核涉及多张票据时，全部识别完成并核对低置信度字段后再提交审核；部分失败要逐项说明。
- 最终说明制度版本、审核结果、各项发现、证据和限制，不把审核建议描述为已批准付款。

## 参考资料

- [API 密钥配置](https://ai-skills.open-idea.net/skill-docs/expense-compliance/API-KEY.md)
- [HTTP 请求、幂等与轮询](https://ai-skills.open-idea.net/skill-docs/expense-compliance/HTTP-REQUESTS.md)
- [操作、规则与结果结构](https://ai-skills.open-idea.net/skill-docs/expense-compliance/OPERATIONS.md)
- [证据、安全与人工复核规则](https://ai-skills.open-idea.net/skill-docs/expense-compliance/BEHAVIOR-RULES.md)
