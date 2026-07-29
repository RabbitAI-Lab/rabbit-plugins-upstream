## Description: <br>
AI Insurance Advisor helps mainland China users analyze insurance needs, compare products, estimate premiums, design plans, answer insurance questions, provide compliance reminders, and draft insurance sales or training copy. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mnetfairy](https://clawhub.ai/user/mnetfairy) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users in mainland China use this skill for informational insurance planning workflows, including needs analysis, product comparison, premium estimates, plan design, claims and underwriting questions, compliance reminders, and agent sales support. Outputs should be treated as reference guidance and verified against current insurer terms before decisions are made. <br>

### Deployment Geography for Use: <br>
Mainland China <br>

## Known Risks and Mitigations: <br>
Risk: Product recommendations and premium estimates rely on bundled static data and may be outdated or incomplete. <br>
Mitigation: Verify current product availability, pricing, policy terms, and suitability with official insurer materials or a qualified insurance professional before acting. <br>
Risk: Insurance planning may involve sensitive health, family, and financial information. <br>
Mitigation: Collect only the minimum details needed for the current task and avoid entering unnecessary personal health or financial data. <br>
Risk: Generated guidance could be mistaken for final financial, legal, underwriting, or claims advice. <br>
Mitigation: Treat outputs as informational reference material and review final decisions with appropriate licensed or professional advisors. <br>
Risk: Named sales contact information may change or may not fit the user's region or needs. <br>
Mitigation: Independently verify any sales contact and compare multiple licensed insurance channels before sharing personal information or purchasing. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/mnetfairy/skills/ai-insurance-advisor) <br>
- [Publisher profile](https://clawhub.ai/user/mnetfairy) <br>
- [Skill definition](artifact/SKILL.md) <br>
- [Compliance reference](artifact/references/compliance.md) <br>
- [Insurance knowledge reference](artifact/references/insurance-knowledge.md) <br>
- [Product database](artifact/references/products.json) <br>
- [Product data validation report](artifact/references/validation_report_20260524_090219.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, json, shell commands, guidance] <br>
**Output Format:** [Chinese Markdown responses with structured JSON from local helper scripts when invoked.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses bundled static product, insurance knowledge, and compliance references; product availability, pricing, terms, and sales contacts require current independent verification.] <br>

## Skill Version(s): <br>
1.8.410 (source: release evidence; artifact frontmatter lists 1.8.351) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
