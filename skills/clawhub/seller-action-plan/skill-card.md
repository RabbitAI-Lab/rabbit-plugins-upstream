## Description:

Amazon 卖家行动计划 Skill 综合商品详情与评论，为单 ASIN 排列运营优先级和检查项，仅用于数据可支持的行动规划，不用于广告账户、库存或利润决策。

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers and operators use this skill to turn product detail and review evidence for a single ASIN into prioritized operational actions and checks. It is intended for review-backed planning, not advertising account management, inventory planning, profit analysis, tax, cash flow, or real-time store data decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can spend ARI account credits when workflows run under explicit confirmation or account-level auto-confirm rules.

Mitigation: Use "只报价，不要执行" for price checks, keep auto-confirm disabled when strict approval is required, and review credit amounts before confirming paid analysis.

Risk: The skill can change persistent account or monitoring settings, including auto-confirm behavior and recurring product monitoring.

Mitigation: Require clear user intent before changing account confirmation rules, starting monitoring, adding competitors, exporting data, or altering recurring schedules.

Risk: The skill requires an ARI API key and can manage review analysis workflows through that account.

Mitigation: Use a dedicated ARI API key, do not paste secrets into reports or examples, revoke keys from the publisher account page when no longer needed, and avoid installing unless ARI account access is acceptable.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/funewa/skills/seller-action-plan)
- [Amazon 卖家行动计划 专属运营工作流](references/operation-workflow.md)
- [ARI CLI 与 API 参考](references/reference.md)
- [ARI Amazon 评论智能助手使用指南](使用说明.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown guidance with concise operational recommendations and occasional inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should include data scope, evidence-backed issues, trend caveats when samples are limited, action priorities, usage or credit information when applicable, and report links when returned by ARI.]

## Skill Version(s):

1.4.8 (source: server release evidence, SKILL.md frontmatter, _meta.json, CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
