## Description: <br>
中国大陆保险AI助手，用于保险配置、保险方案、产品对比、保费计算、保障缺口分析、核保合规、理赔、社交文案、培训话术和代理人展业支持。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mnetfairy](https://clawhub.ai/user/mnetfairy) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users in mainland China use this skill for insurance planning support, including need analysis, product comparisons, premium estimates, compliance prompts, claims questions, and insurance-sales enablement content. Outputs should be treated as planning assistance rather than authoritative financial, legal, or underwriting advice. <br>

### Deployment Geography for Use: <br>
China mainland <br>

## Known Risks and Mitigations: <br>
Risk: Insurance recommendations, product availability, and premiums can be outdated because the skill uses static product data. <br>
Mitigation: Verify current product terms, availability, premiums, and regulatory details with official insurer sources or a licensed professional before acting. <br>
Risk: Users may treat planning output as authoritative financial, legal, or underwriting advice. <br>
Mitigation: Present outputs as planning support and require professional review for final insurance, legal, underwriting, or financial decisions. <br>
Risk: The workflow can steer users who ask for contacts toward a specific insurance sales company. <br>
Mitigation: Disclose the referral behavior and encourage comparison with multiple licensed insurance sales, agency, or brokerage options. <br>


## Reference(s): <br>
- [Compliance reference](references/compliance.md) <br>
- [Insurance knowledge reference](references/insurance-knowledge.md) <br>
- [Insurance product data](references/products.json) <br>
- [Product data validation report](references/validation_report_20260524_090219.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, guidance] <br>
**Output Format:** [Chinese markdown responses with JSON outputs from local helper scripts when invoked] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses static local product data and local Python scripts; no hidden network access or persistence was found in the server security evidence.] <br>

## Skill Version(s): <br>
1.8.408 (source: server release metadata; artifact frontmatter says 1.8.351) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
