## Description: <br>
Provides China mainland insurance consultation, product comparison, plan design, premium calculation, coverage gap analysis, underwriting compliance guidance, and claims support for individuals and families. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mnetfairy](https://clawhub.ai/user/mnetfairy) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this skill to compare China mainland insurance products, analyze personal or family coverage needs, design insurance plans, estimate premiums, and explain underwriting, compliance, and claims considerations. <br>

### Deployment Geography for Use: <br>
China mainland <br>

## Known Risks and Mitigations: <br>
Risk: The skill supports sensitive insurance and financial decisions and should not be treated as licensed advice. <br>
Mitigation: Treat outputs as advisory, verify product terms, availability, and premiums with official insurers or licensed professionals, and make final decisions using authoritative policy documents. <br>
Risk: Users may share personal, financial, or medical details while requesting coverage analysis or underwriting guidance. <br>
Mitigation: Collect only the minimum details needed for the task and avoid sharing unnecessary medical, identity, or account information. <br>
Risk: Bundled helper scripts appear functionally unreliable: example stdin calls may be ignored and premium calculation can crash on product records with missing fields. <br>
Mitigation: Test helper scripts with the intended invocation pattern, validate product records before calculation, and review any JSON errors or default-test outputs before relying on results. <br>
Risk: The bundled product database is static and insurance products, rates, and availability can change quickly. <br>
Mitigation: Confirm current product status, premium rates, and eligibility rules with official insurer channels before presenting recommendations as actionable. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/mnetfairy/skills/insurance-advisor-china) <br>
- [Insurance knowledge reference](artifact/references/insurance-knowledge.md) <br>
- [Regulatory compliance reference](artifact/references/compliance.md) <br>
- [Insurance product database](artifact/references/products.json) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, guidance] <br>
**Output Format:** [Chinese Markdown guidance with optional JSON outputs from local helper scripts] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Advisory outputs should include product freshness disclaimers and verification guidance before users act on insurance recommendations.] <br>

## Skill Version(s): <br>
1.8.418 (source: server release metadata; SKILL.md frontmatter reports 1.8.347) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
