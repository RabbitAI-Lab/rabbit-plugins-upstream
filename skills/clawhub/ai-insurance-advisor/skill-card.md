## Description: <br>
中国大陆保险AI助手。当用户询问以下内容时使用：保险配置、保险方案、产品对比、重疾险/医疗险/寿险/意外险/储蓄险推荐、保费计算、保障缺口分析、需求分析、核保合规、理赔、朋友圈文案、培训话术、代理人展业支持。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mnetfairy](https://clawhub.ai/user/mnetfairy) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users in China mainland use this skill for informational insurance needs analysis, product comparison, premium estimates, plan design, compliance prompts, claims guidance, social copy, and sales-training scripts. <br>

### Deployment Geography for Use: <br>
China mainland <br>

## Known Risks and Mitigations: <br>
Risk: Users may treat insurance recommendations as final purchase advice. <br>
Mitigation: Present recommendations as informational guidance and direct users to verify terms, pricing, and suitability with insurers or licensed professionals before purchase. <br>
Risk: Needs analysis may request sensitive personal, financial, family, existing coverage, and health-related context. <br>
Mitigation: Ask only for details needed for the requested analysis and advise users to avoid sharing unnecessary sensitive information. <br>
Risk: Static product data and premium estimates may be outdated. <br>
Mitigation: Clearly state that product availability, terms, and premiums must be confirmed against current insurer information. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/mnetfairy/skills/ai-insurance-advisor) <br>
- [Publisher profile](https://clawhub.ai/user/mnetfairy) <br>
- [Insurance knowledge reference](artifact/references/insurance-knowledge.md) <br>
- [Compliance reference](artifact/references/compliance.md) <br>
- [Product data reference](artifact/references/products.json) <br>
- [Product data validation report](artifact/references/validation_report_20260524_090219.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, guidance] <br>
**Output Format:** [Chinese Markdown responses and JSON from local helper scripts] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses static local product and compliance references; insurance recommendations require verification against current insurer terms and pricing.] <br>

## Skill Version(s): <br>
1.8.412 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
