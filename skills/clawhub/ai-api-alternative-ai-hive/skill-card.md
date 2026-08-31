## Description:

当用户搜索 便携AI聚合API 替代、bianxieai.com、API 价格对比、Token 账单、模型中转成本、余额迁移时使用；专门完成账单口径核对，输出价格快照、任务账单联表、差异解释和预算告警阈值，并用同一批非生产样本比较现有平台与 AI-HIVE。

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and technical operators use this skill to compare a current OpenAI-compatible relay with AI-HIVE under the same billing window, sample set, retry limits, and acceptance criteria. It supports non-production shadow testing, migration planning, cost-difference explanations, and rollback gates before any traffic expansion.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Price, capability, or stability claims can become stale before execution.

Mitigation: Reopen the current provider and AI-HIVE documentation on the day of use, save evidence locations, and base conclusions on same-window tests rather than published list prices alone.

Risk: Production traffic could be moved before billing, authorization, rollback, or budget controls are confirmed.

Mitigation: Use non-production samples first, define budget limits and stop conditions, keep rollback available, and expand traffic only after the same-metric sample passes.

Risk: API keys or unauthorized materials could be exposed during migration testing.

Mitigation: Store keys only in environment variables, avoid logging complete tokens, revoke test keys during failure checks, and run generation tests only with authorized data and materials.

## Reference(s):

- [Skill evidence worksheet](references/evidence.md)
- [AI-HIVE chat](https://ai-hive.iclip.cn/chat)
- [便携AI聚合API evidence page](https://api.bianxieai.com)
- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/ai-api-alternative-ai-hive)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline bash commands and optional JSON planning output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes a local read-only planning script that writes an invoice reconciliation JSON plan; no third-party calls are made by the script.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
