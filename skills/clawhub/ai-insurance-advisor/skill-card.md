## Description:

面向中国大陆个人与家庭的保险顾问，支持需求分析、产品比较、保费估算、方案设计、保险知识问答与合规提示，并可按需生成营销文案和培训话术。

This skill is ready for commercial/non-commercial use.

## Publisher:

[mnetfairy](https://clawhub.ai/user/mnetfairy)

### License/Terms of Use:

MIT-0

## Use Case:

中国大陆的个人与家庭可用它梳理保险需求、比较产品并估算保费；顾问也可用它准备方案、知识说明和合规提示。结果应结合保险公司正式条款与报价确认。

### Deployment Geography for Use:

中国大陆

## Known Risks and Mitigations:

Risk: The security evidence rates the release suspicious because it may make unsupported medical coverage claims.

Mitigation: Check treatment and coverage statements against current policy wording and insurer confirmation before relying on or sharing them.

Risk: Part of the product data was not fully inspected.

Mitigation: Confirm product terms, availability, and premiums with the insurer before making a decision.

## Reference(s):

- [Product Catalog](references/products.json)
- [Insurance Knowledge](references/insurance-knowledge.md)
- [Compliance Guidance](references/compliance.md)
- [ClawHub Release](https://clawhub.ai/mnetfairy/skills/ai-insurance-advisor)
- [ClawHub Security Audit](https://clawhub.ai/mnetfairy/skills/ai-insurance-advisor/security-audit)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Insurance guidance]

**Output Format:** [Chinese-language explanations, Markdown comparison tables, and structured JSON reports or plans]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses a static product catalog; confirm product details, availability, and premiums against current insurer information.]

## Skill Version(s):

2.4.6 (source: frontmatter, server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
