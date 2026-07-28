## Description: <br>
A Mainland China insurance advisory skill for personal and family insurance consultation, product comparison, plan design, enrollment guidance, premium estimates, needs analysis, compliance guidance, and claims support. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mnetfairy](https://clawhub.ai/user/mnetfairy) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users in Mainland China use this skill to explore insurance needs, compare insurance products, estimate premiums, design coverage plans, and receive general compliance or claims guidance. Agents may use its bundled Python tools and reference files to produce structured Chinese-language insurance guidance. <br>

### Deployment Geography for Use: <br>
Mainland China <br>

## Known Risks and Mitigations: <br>
Risk: Insurance product data is static and may not reflect current availability, pricing, policy terms, or underwriting rules. <br>
Mitigation: Verify recommendations, premiums, and product details against current insurer materials before making or advising a purchase. <br>
Risk: One calculator script may error on some product records, which can make premium estimates incomplete or unreliable. <br>
Mitigation: Treat calculated premiums as estimates, check for script errors, and confirm final premiums through official insurer channels or a qualified advisor. <br>
Risk: Insurance recommendations may be mistaken for professional financial, legal, or sales advice. <br>
Mitigation: Present outputs as informational guidance and have any purchase decision reviewed with current insurer documents and a qualified insurance advisor. <br>
Risk: The workflow can collect personal, family, financial, and health-related details during needs analysis. <br>
Mitigation: Limit inputs to information needed for the task and avoid storing or sharing sensitive personal data outside the local agent session. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/mnetfairy/skills/insurance-advisor-china) <br>
- [Insurance knowledge reference](references/insurance-knowledge.md) <br>
- [Compliance reference](references/compliance.md) <br>
- [Product database](references/products.json) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, guidance] <br>
**Output Format:** [Chinese Markdown guidance with JSON outputs from bundled Python scripts] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses local reference files and a static product database; script results should be treated as estimates and verified against current insurer materials.] <br>

## Skill Version(s): <br>
1.8.406 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
