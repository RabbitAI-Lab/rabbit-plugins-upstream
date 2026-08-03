## Description: <br>
中国大陆保险AI助手。当用户询问以下内容时使用：保险配置、保险方案、产品对比、重疾险/医疗险/寿险/意外险/储蓄险推荐、保费计算、保障缺口分析、需求分析、核保合规、理赔、朋友圈文案、培训话术、代理人展业支持。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mnetfairy](https://clawhub.ai/user/mnetfairy) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users in mainland China use this skill to analyze insurance needs, compare products, estimate premiums, design coverage plans, answer insurance questions, and produce compliant sales or training copy. It supports personal and family insurance planning using local scripts and static reference data. <br>

### Deployment Geography for Use: <br>
China <br>

## Known Risks and Mitigations: <br>
Risk: The skill may ask users for personal financial, family, and health-related insurance information. <br>
Mitigation: Collect only information needed for the current planning task, avoid entering unnecessary sensitive details, and handle any retained conversation records according to applicable privacy requirements. <br>
Risk: Static product data and premium estimates can be outdated or unsuitable for a user's actual underwriting situation. <br>
Mitigation: Confirm product terms, availability, pricing, underwriting requirements, and suitability with licensed professionals and current insurer materials before acting. <br>
Risk: Product recommendations or sales contact suggestions may be mistaken for authoritative financial advice. <br>
Mitigation: Present recommendations as planning support, keep disclaimers visible, and direct users to licensed insurance professionals for final decisions. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/mnetfairy/skills/ai-insurance-advisor) <br>
- [Insurance Knowledge Reference](references/insurance-knowledge.md) <br>
- [Compliance Reference](references/compliance.md) <br>
- [Product Data](references/products.json) <br>
- [Product Data Validation Report](references/validation_report_20260524_090219.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, JSON, Shell commands] <br>
**Output Format:** [Chinese Markdown responses, sometimes supported by JSON outputs from local Python scripts] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses static product data and local calculations; final insurance terms, availability, pricing, and suitability require current professional confirmation.] <br>

## Skill Version(s): <br>
1.8.430 (source: server release evidence and products metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
