## Description: <br>
中国大陆AI保险顾问，为个人和家庭提供保险咨询、产品对比、方案设计、投保指导、保费计算、保障缺口分析、核保合规和理赔支持。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mnetfairy](https://clawhub.ai/user/mnetfairy) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users in mainland China can use this skill to assess household insurance needs, compare Chinese insurance products, estimate premiums, design coverage plans, and receive general compliance or claims guidance. <br>

### Deployment Geography for Use: <br>
China (Mainland) <br>

## Known Risks and Mitigations: <br>
Risk: The skill may ask for personal, family, health, income, mortgage, and existing-policy details. <br>
Mitigation: Provide only information needed for the advisory task and avoid entering unnecessary sensitive details. <br>
Risk: Static product data may be outdated or may not reflect current premiums, coverage, availability, or sales contacts. <br>
Mitigation: Verify premiums, coverage terms, product availability, and any sales contact directly with licensed insurance professionals before buying. <br>
Risk: Insurance guidance can affect financial, health, and legal decisions. <br>
Mitigation: Treat outputs as general advice and have final purchase, underwriting, compliance, and claims decisions reviewed by qualified professionals. <br>


## Reference(s): <br>
- [Insurance Knowledge](references/insurance-knowledge.md) <br>
- [Compliance Guidance](references/compliance.md) <br>
- [Insurance Product Data](references/products.json) <br>
- [ClawHub Skill Page](https://clawhub.ai/mnetfairy/skills/insurance-advisor-china) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, json, shell commands, guidance] <br>
**Output Format:** [Chinese Markdown advice with JSON outputs from local helper scripts] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May use local script calls for needs analysis, premium calculation, and plan design; product data is static and should be verified before purchase decisions.] <br>

## Skill Version(s): <br>
1.8.429 (source: server release evidence and product metadata; artifact SKILL.md frontmatter says 1.8.347) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
