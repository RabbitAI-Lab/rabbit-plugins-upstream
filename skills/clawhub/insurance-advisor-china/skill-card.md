## Description: <br>
A China Mainland insurance advisor skill that helps individuals and families compare products, estimate premiums, analyze coverage gaps, design insurance plans, and understand underwriting, compliance, and claims topics. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mnetfairy](https://clawhub.ai/user/mnetfairy) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users in Mainland China use this skill to get Chinese-language insurance education, product comparisons, premium estimates, coverage-gap analysis, plan-design suggestions, and general claims or underwriting guidance. The outputs are informational and should be verified with insurers or licensed advisors before purchase decisions. <br>

### Deployment Geography for Use: <br>
China (Mainland) <br>

## Known Risks and Mitigations: <br>
Risk: Users may treat generated insurance guidance as a licensed professional recommendation. <br>
Mitigation: Present the skill output as informational guidance and direct users to verify suitability with insurers or licensed advisors before buying. <br>
Risk: The skill may process sensitive personal, health, and financial details during insurance needs analysis. <br>
Mitigation: Collect only details needed for the insurance question and avoid retaining or sharing sensitive user information outside the conversation. <br>
Risk: The local product database may not reflect current product availability, pricing, or underwriting terms. <br>
Mitigation: Ask users to confirm current product information directly with insurers or licensed advisors before making purchase decisions. <br>


## Reference(s): <br>
- [ClawHub skill release](https://clawhub.ai/mnetfairy/skills/insurance-advisor-china) <br>
- [Insurance product database](artifact/references/products.json) <br>
- [Insurance knowledge reference](artifact/references/insurance-knowledge.md) <br>
- [Compliance reference](artifact/references/compliance.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Chinese Markdown guidance with comparison tables and JSON calculator outputs] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses local reference data for insurance products and calculators; product availability, pricing, and suitability should be verified before purchase.] <br>

## Skill Version(s): <br>
1.8.416 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
