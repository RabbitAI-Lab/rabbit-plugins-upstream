## Description: <br>
中国大陆AI保险顾问。为个人和家庭提供全方位的保险咨询、产品对比、方案设计、投保指导。当用户询问保险配置、保险方案、产品对比、重疾险/医疗险/寿险/意外险/储蓄险推荐、保费计算、保障缺口分析、需求分析、核保合规、理赔等问题时使用。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mnetfairy](https://clawhub.ai/user/mnetfairy) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users in mainland China use this skill for Chinese-language insurance needs analysis, product comparison, premium estimates, plan design, underwriting and compliance guidance, and general claims support. It is intended as reference support and not as a final insurance purchasing decision. <br>

### Deployment Geography for Use: <br>
China <br>

## Known Risks and Mitigations: <br>
Risk: Insurance products, premiums, and availability may change after the bundled reference data is published. <br>
Mitigation: Verify recommendations against current official product documents or a licensed professional before making purchasing decisions. <br>
Risk: The skill may request sensitive family, financial, and health-related details to analyze insurance needs. <br>
Mitigation: Provide only the information needed for the requested analysis and avoid unnecessary personal identifiers. <br>
Risk: A disclosed sales-company contact could be mistaken for an endorsement. <br>
Mitigation: Show the contact only when the user asks for a buying channel and keep the accompanying disclaimer that it is not a recommendation or endorsement. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/mnetfairy/skills/insurance-advisor-china) <br>
- [Insurance product data](references/products.json) <br>
- [Insurance knowledge base](references/insurance-knowledge.md) <br>
- [Compliance guidance](references/compliance.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, text, json, shell commands] <br>
**Output Format:** [Chinese-language Markdown and text, with JSON outputs from local helper scripts] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses local reference data and calculators; recommendations should be checked against official product documents and licensed professional advice.] <br>

## Skill Version(s): <br>
1.8.410 (source: server release metadata; artifact frontmatter is 1.8.347) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
