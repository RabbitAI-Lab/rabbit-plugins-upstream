## Description:

从 Amazon 评论和商品详情中识别可能导致退货的体验与期望落差线索，并给出改进方向；仅用于评论证据线索，不宣称真实退货率，也不用于库存、退款或客服执行。

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers and ecommerce operations teams use this skill to analyze Amazon review evidence, surface likely return-risk themes, and prioritize product or listing improvements. It is intended for review-based operating insight, not refund automation, inventory decisions, or prediction of true return rates.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can use an ARI API key and access ARI account data.

Mitigation: Install only when the user accepts ARI account access, keep API keys out of reports and examples, and use environment or local configuration mechanisms for credentials.

Risk: Paid reports, exports, monitoring, schedules, competitors, watch management, alert marking, and workbench status updates can affect the user's account or credits.

Mitigation: Use explicit user confirmation for account-affecting actions, and set autoconfirm to ask every time when the user wants approval before each charge.

Risk: Interrupted paid operations may already have charged credits or produced saved reports.

Mitigation: Check saved reports or operation status before retrying a paid command, and only rerun after confirming that no completed result exists.

Risk: Review-analysis outputs can be mistaken for true return-rate or refund predictions.

Mitigation: Present findings as review-evidence clues, state sample size and time window limits, and avoid using the skill for inventory, refund, or customer-service execution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/funewa/skills/return-risk)
- [Operation workflow reference](artifact/references/operation-workflow.md)
- [ARI API reference](artifact/references/reference.md)
- [README](artifact/README.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Concise text or Markdown, with shell commands and configuration guidance when setup or troubleshooting requires them.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should distinguish review evidence from inferred recommendations, include data range and usage/cost context when applicable, and avoid exposing API keys.]

## Skill Version(s):

1.4.7 (source: server release evidence, SKILL.md frontmatter, _meta.json, CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
