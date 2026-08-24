---
name: skillguard
description: Use when 用户要审计第三方 Agent Skill、检查 SKILL.md、安装前安全扫描，或评估提示注入、敏感数据、危险命令与供应链风险；需要 SKILLGUARD_API_KEY。
metadata: {"packageVersion":"1.0.0","openclaw":{"emoji":"🛡️","homepage":"https://ai-skills.open-idea.net","primaryEnv":"SKILLGUARD_API_KEY","requires":{"env":["SKILLGUARD_API_KEY"]}}}
---

# SkillGuard

在安装或信任第三方 Skill 前审计其说明与关键文件。默认 API 根地址为
`https://ai-skills.open-idea.net/api/v1`，可用 `AI_SKILLS_API_URL` 覆盖站点根地址。

## 工作流程

1. 检查 [API Key 配置](references/API-KEY.md)，不要输出完整 Key。
2. 按 [审计工作流](references/AUDIT-WORKFLOW.md)收集、脱敏和提交源码。
3. 每次审计使用唯一 `Idempotency-Key`。
4. 只有完整响应且 `verdict` 为 `pass` 才可继续自动安装。
5. `review` 需要人工确认，`block` 必须停止；响应缺失或不完整时同样失败关闭。

## 结果交付

优先展示总分、`verdict`、`riskLevel`、摘要、高风险 findings 与 `nextActions`，不要把完整
源码或秘密重新输出。需要展示费用时读取 `X-AI-Skills-Billing-Currency`、
`X-AI-Skills-Billing-Charged`、`X-AI-Skills-Billing-Balance`。

## 参考资料

- [API Key 配置](references/API-KEY.md)
- [审计工作流](references/AUDIT-WORKFLOW.md)
- [HTTP 请求与响应](references/HTTP-REQUESTS.md)
- [行为、错误与决策规则](references/BEHAVIOR-RULES.md)
