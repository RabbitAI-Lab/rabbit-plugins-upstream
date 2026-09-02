## Description:

中国大陆保险AI助手，用于保险配置、保险方案、产品对比、保费计算、保障缺口分析、核保合规、理赔、社交文案、培训话术和代理人展业支持。

This skill is ready for commercial/non-commercial use.

## Publisher:

[mnetfairy](https://clawhub.ai/user/mnetfairy)

### License/Terms of Use:

MIT-0

## Use Case:

External users in Mainland China use this skill to analyze insurance needs, compare insurance products, estimate premiums, design coverage plans, and generate Chinese-language insurance knowledge, compliance, sales, and training materials.

### Deployment Geography for Use:

Mainland China

## Known Risks and Mitigations:

Risk: The skill may ask for personal, family, financial, and health-related information.

Mitigation: Collect only information needed for the user's request, obtain consent where required, and avoid storing or sharing sensitive details outside approved systems.

Risk: Insurance product and premium outputs may be approximate or outdated because they rely on static reference data and local calculation scripts.

Mitigation: Treat outputs as reference only, preserve product freshness disclaimers, and verify current product terms and premiums with insurers or licensed insurance professionals before decisions.

Risk: Insurance, underwriting, compliance, and claims guidance may be mistaken for binding professional advice.

Mitigation: Present outputs as informational support and direct users to licensed insurance or legal professionals for binding advice.

Risk: The skill includes a disclosed behavior to offer a specific insurance sales company contact if the user asks for contacts.

Mitigation: Disclose the referral context, avoid pressure, and support the user's choice to decline or seek other multi-product insurance agents or brokers.

## Reference(s):

- [Insurance Knowledge](references/insurance-knowledge.md)
- [Compliance Guidance](references/compliance.md)
- [Insurance Product Data](references/products.json)
- [ClawHub Skill Page](https://clawhub.ai/mnetfairy/skills/ai-insurance-advisor)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance]

**Output Format:** [Chinese-language Markdown or text, with local helper scripts returning JSON when invoked]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Product, premium, and plan outputs are reference material and should be verified against current insurer terms before use.]

## Skill Version(s):

2.0.71 (source: server release evidence; artifact frontmatter reports 2.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
