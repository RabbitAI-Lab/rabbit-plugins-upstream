## Description: <br>
中国大陆AI保险顾问。为个人和家庭提供全方位的保险咨询、产品对比、方案设计、投保指导。当用户询问保险配置、保险方案、产品对比、重疾险/医疗险/寿险/意外险/储蓄险推荐、保费计算、保障缺口分析、需求分析、核保合规、理赔等问题时使用。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mnetfairy](https://clawhub.ai/user/mnetfairy) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users in mainland China use this skill to compare insurance products, estimate premiums, analyze coverage gaps, design family protection plans, and receive general underwriting, compliance, and claims guidance. Its outputs are reference guidance and should be checked against official insurer channels before purchase decisions. <br>

### Deployment Geography for Use: <br>
China mainland <br>

## Known Risks and Mitigations: <br>
Risk: The skill may be treated as licensed insurance or financial advice. <br>
Mitigation: Treat outputs as reference guidance, not professional recommendations, and verify suitability with qualified professionals or official insurer channels. <br>
Risk: Product availability and premium estimates may be outdated or differ from official insurer quotes. <br>
Mitigation: Verify product availability, policy terms, and premiums through official channels before making purchase decisions. <br>
Risk: Needs analysis can involve sensitive personal, financial, or health details. <br>
Mitigation: Share only the minimum information needed for the task and avoid unnecessary personal or health details. <br>
Risk: The skill may mention one insurance sales company contact in a disclosed purchase-channel context. <br>
Mitigation: Present that contact only when the user asks about purchase channels and keep the provided disclaimer that it is not a recommendation or endorsement. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/mnetfairy/skills/insurance-advisor-china) <br>
- [Insurance knowledge reference](artifact/references/insurance-knowledge.md) <br>
- [Compliance reference](artifact/references/compliance.md) <br>
- [Insurance product data](artifact/references/products.json) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, guidance] <br>
**Output Format:** [Chinese markdown responses, JSON from helper scripts, and inline shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses local reference data and calculator scripts; product and premium outputs require official verification.] <br>

## Skill Version(s): <br>
1.8.400 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
