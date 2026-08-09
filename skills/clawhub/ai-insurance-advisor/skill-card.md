## Description:

中国大陆保险AI助手。当用户询问以下内容时使用：保险配置、保险方案、产品对比、重疾险/医疗险/寿险/意外险/储蓄险推荐、保费计算、保障缺口分析、需求分析、核保合规、理赔、朋友圈文案、培训话术、代理人展业支持。

This skill is ready for commercial/non-commercial use.

## Publisher:

[mnetfairy](https://clawhub.ai/user/mnetfairy)

### License/Terms of Use:

MIT-0

## Use Case:

External users in Mainland China use this skill to compare insurance products, estimate premiums, analyze protection gaps, design insurance plans, and receive Chinese-language compliance and sales-support guidance.

### Deployment Geography for Use:

Mainland China

## Known Risks and Mitigations:

Risk: Product recommendations and premium estimates may be outdated because the skill uses a static local product database.

Mitigation: Verify product availability, premiums, coverage terms, and underwriting details with licensed professionals before purchase.

Risk: Insurance planning may involve sensitive health, family, and financial information.

Mitigation: Share only the information needed for the task and avoid disclosing unnecessary personal data.

Risk: The skill may ask whether the user wants contact information for an insurance sales company.

Mitigation: Treat sales-contact suggestions as optional and independently evaluate any provider before sharing personal information or buying insurance.

## Reference(s):

- [Insurance Product Database](references/products.json)
- [Insurance Knowledge Base](references/insurance-knowledge.md)
- [Regulatory Compliance Notes](references/compliance.md)
- [Insurance Product Data Validation Report](references/validation_report_20260524_090219.md)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Markdown, JSON, Shell commands]

**Output Format:** [Chinese-language Markdown guidance with JSON outputs from helper scripts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include product comparison tables, premium estimates, protection-gap reports, plan designs, compliance reminders, and sales or training copy.]

## Skill Version(s):

1.8.440 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
