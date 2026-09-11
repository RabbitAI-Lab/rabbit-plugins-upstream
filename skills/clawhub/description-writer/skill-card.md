## Description:

基于 Amazon 商品字段和评论反馈，识别商品描述的信息缺口并给出改写建议。

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT

## Use Case:

Amazon sellers and operators use this skill to review product fields and customer review feedback, then generate evidence-based guidance for improving product descriptions. It is focused on description diagnostics and recommendations, not automated Amazon page publishing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses authenticated ARI account access and may expose account data such as review history, alerts, report history, balances, and billing-confirmation settings to the agent workflow.

Mitigation: Install only for accounts where this access is acceptable, keep the API key out of chat and reports, and use the browser authorization or local configuration flow described by the artifact.

Risk: Some ARI workflows can spend credits, and account auto-confirm settings may allow eligible paid actions to run without a separate prompt.

Mitigation: Set autoconfirm to always ask when every paid action should require approval, use quote-only requests for pricing checks, and require explicit user intent before running commands with --confirm.

Risk: Network interruptions during paid analysis can occur after the service has already charged credits and archived a report.

Mitigation: Check existing reports or operation status with the original request ID before retrying any paid command.

## Reference(s):

- [Amazon 商品描述优化 README](README.md)
- [Amazon 商品描述优化 专属运营工作流](references/operation-workflow.md)
- [ARI CLI 与 API 参考](references/reference.md)
- [Skill Page](https://clawhub.ai/funewa/skills/description-writer)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with optional shell commands and JSON command results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include product-description recommendations, evidence summaries from ARI data, report links, pricing or balance notes, and explicit confirmation prompts before paid operations when required.]

## Skill Version(s):

1.4.8 (source: frontmatter, _meta.json, changelog, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
