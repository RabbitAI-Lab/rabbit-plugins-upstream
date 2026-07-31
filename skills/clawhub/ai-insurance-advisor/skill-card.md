## Description: <br>
Provides mainland China insurance guidance for coverage planning, product comparison, premium calculation, coverage gap analysis, underwriting and compliance questions, claims topics, sales copy, training scripts, and agent support. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mnetfairy](https://clawhub.ai/user/mnetfairy) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users in mainland China can use this skill to understand insurance needs, compare bundled product data, estimate premiums, design basic protection plans, and draft insurance sales or training materials. It is informational guidance and should not be treated as professional legal, financial, underwriting, or carrier-issued advice. <br>

### Deployment Geography for Use: <br>
China (mainland) <br>

## Known Risks and Mitigations: <br>
Risk: Insurance recommendations or premium estimates may be inaccurate, stale, or incomplete because the skill relies on bundled static product data and local calculators. <br>
Mitigation: Verify product availability, policy terms, and premiums with the relevant insurer or licensed insurance professional before acting. <br>
Risk: Use may involve sensitive personal, health, family, income, mortgage, and policy details. <br>
Mitigation: Enter only information needed for the task and avoid sharing unnecessary identifiers or confidential records. <br>
Risk: The skill includes a disclosed referral to a specific insurance sales company when users ask for contact information. <br>
Mitigation: Present the referral as optional and disclose the sales-company relationship before the user relies on the contact information. <br>
Risk: Outputs could be mistaken for professional financial, legal, underwriting, or claims advice. <br>
Mitigation: Label outputs as informational guidance and route final decisions to licensed professionals, insurers, or official policy documents. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/mnetfairy/skills/ai-insurance-advisor) <br>
- [Insurance knowledge base](references/insurance-knowledge.md) <br>
- [Compliance guidance](references/compliance.md) <br>
- [Insurance product database](references/products.json) <br>
- [Product data validation report](references/validation_report_20260524_090219.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, json, shell commands, guidance] <br>
**Output Format:** [Chinese Markdown responses with optional JSON outputs from local helper scripts] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses bundled static reference data and local calculators; security evidence reports no hidden data access or exfiltration. Risk mitigations: treat recommendations as informational, avoid entering unnecessary sensitive personal or health details, verify product availability and premiums with official sources, and disclose the referral to Ansheng Tianping Insurance Sales Co., Ltd. before using contact information.] <br>

## Skill Version(s): <br>
1.8.416 (source: server release metadata; artifact frontmatter says 1.8.351) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
