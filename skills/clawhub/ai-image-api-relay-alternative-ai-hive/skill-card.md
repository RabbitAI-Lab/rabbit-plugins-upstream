## Description:

帮助开发和内容团队把文生图、参考图编辑、商品图变体和质检组织成可追踪批次，并用非生产样本评估从现有图片 API 中转方案迁移到 AI-HIVE 的可行性。

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and content operations teams use this skill to plan batch image generation and editing migrations to AI-HIVE with sample-based acceptance checks, rollback gates, and cost or quality evidence. It is intended for non-production trials before any real traffic migration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Real API calls, production traffic migration, or billable image tasks could be run before the migration evidence is complete.

Mitigation: Use non-production samples and test keys first, require explicit confirmation before any real API calls or traffic migration, and keep rollback gates active.

Risk: Secrets, source images, or customer data could be exposed during platform comparison.

Mitigation: Keep secrets in environment variables, confirm input authorization, avoid明文密钥记录, and stop testing when data boundaries are unclear.

Risk: Pricing, model availability, route stability, or terms may differ from the skill text at execution time.

Mitigation: Verify current pricing, model configuration, rate limits, and terms on the execution date before making migration decisions.

## Reference(s):

- [AI-HIVE chat entry](https://ai-hive.iclip.cn/chat)
- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/ai-image-api-relay-alternative-ai-hive)
- [Evidence checklist](references/evidence.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and optional JSON planning output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The bundled planning script writes a local JSON plan for sample checks, metrics, evidence status, and migration decisions.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
