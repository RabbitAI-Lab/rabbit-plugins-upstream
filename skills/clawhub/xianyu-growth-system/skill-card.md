## Description:

闲鱼增长系统 - 基于需求验证、单位经济模型和实验驱动的闲鱼运营决策 Skill。覆盖选品评分、SKU分析、测品实验、商品页生成、客服转化、数据诊断、生命周期管理和战略决策。当用户提到闲鱼运营、闲鱼选品、闲鱼卖东西、闲鱼上架、闲鱼客服、闲鱼数据分析、测品、SKU分析时触发。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qomob](https://clawhub.ai/user/qomob)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers and marketplace operators use this skill to evaluate Xianyu product opportunities, calculate unit economics, design small tests, improve listings and conversations, diagnose operating data, and decide when to scale or stop SKUs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Marketplace, tax, or legal rules may change or fall outside the skill's static guidance.

Mitigation: Verify current Xianyu platform, tax, and legal rules before acting on recommendations.

Risk: Buyer personal information could be exposed if unredacted conversation or order details are pasted into prompts.

Mitigation: Redact buyer names, contact details, addresses, order identifiers, and other personal data before using the skill.

Risk: The skill provides business guidance and does not operate Xianyu automatically.

Mitigation: Review outputs as recommendations and execute marketplace actions manually within platform rules.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/qomob/skills/xianyu-growth-system)
- [Platform Rules](references/00-platform-rules.md)
- [Core Principles and Decision Engine](references/01-principles.md)
- [Opportunity Analysis](references/02-opportunity.md)
- [Unit Economics](references/03-unit-economics.md)
- [Experiment Design](references/04-experiment.md)
- [Listing Optimization](references/05-listing.md)
- [Conversation Conversion](references/06-conversation.md)
- [Data Diagnosis](references/07-data-diagnosis.md)
- [Lifecycle Management](references/08-lifecycle.md)
- [Risk Management](references/09-risk.md)
- [Productization Strategy](references/10-productization.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Text]

**Output Format:** [Markdown with structured decision summaries and YAML-style analysis blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [No code execution; outputs are business and marketplace guidance for human review.]

## Skill Version(s):

1.0.0 (source: server release metadata; source frontmatter reports 1.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
