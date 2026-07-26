## Description: <br>
AI Insurance Advisor provides mainland China insurance guidance for coverage planning, product comparison, premium estimates, protection-gap analysis, underwriting compliance, claims questions, and agent sales support. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mnetfairy](https://clawhub.ai/user/mnetfairy) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users in mainland China use this skill to compare insurance products, estimate premiums, design household coverage plans, and receive insurance knowledge or compliance-oriented guidance. Agents can also use it to draft Chinese-language sales, training, and objection-handling materials. <br>

### Deployment Geography for Use: <br>
Mainland China <br>

## Known Risks and Mitigations: <br>
Risk: Product recommendations or premium estimates may be outdated because the skill relies on static local product data. <br>
Mitigation: Verify current product terms, availability, and pricing with licensed insurance providers before making purchase decisions. <br>
Risk: Insurance guidance may be mistaken for professional financial, legal, or compliance advice. <br>
Mitigation: Present outputs as informational guidance and route final plan, underwriting, claims, and compliance decisions to qualified professionals. <br>
Risk: The skill can name a specific insurance sales company when asking whether the user wants contact information. <br>
Mitigation: Disclose that any contact suggestion is informational and encourage users to compare multiple licensed providers. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/mnetfairy/skills/ai-insurance-advisor) <br>
- [Insurance knowledge reference](references/insurance-knowledge.md) <br>
- [Compliance reference](references/compliance.md) <br>
- [Product database](references/products.json) <br>
- [Product validation report](references/validation_report_20260524_090219.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, JSON, Shell commands] <br>
**Output Format:** [Chinese-language Markdown responses with structured JSON from local helper scripts when analysis, plan design, or premium calculation is requested] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses static local product data and local Python scripts; recommendations and premiums should be verified with licensed providers before purchase decisions.] <br>

## Skill Version(s): <br>
1.8.402 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
