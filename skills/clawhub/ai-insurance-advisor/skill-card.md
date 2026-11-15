## Description:

An insurance advisory skill for mainland China that analyzes household coverage needs, compares products, estimates premiums, designs plans, answers insurance and compliance questions, and can draft marketing or training copy for compliance review.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mnetfairy](https://clawhub.ai/user/mnetfairy)

### License/Terms of Use:

MIT-0

## Use Case:

Individuals and families in mainland China use it to understand insurance needs, compare products and estimated premiums, and explore coverage plans; any generated marketing or training copy should receive compliance review.

### Deployment Geography for Use:

Mainland China

## Known Risks and Mitigations:

Risk: ClawScan marks the skill suspicious because treatment exclusion wording could be reused to support an affirmative insurance coverage claim.

Mitigation: Before relying on a coverage statement, check the exact policy wording against official insurer materials and have a qualified professional review it.

Risk: The security evidence is incomplete because some referenced local paths were not found; the separate AIG scan with no reported results does not resolve the SDI-4 finding.

Mitigation: Review the linked security audit and the relevant source material before installing or relying on coverage-related output.

## Reference(s):

- [Insurance knowledge guide](references/insurance-knowledge.md)
- [Compliance guidance](references/compliance.md)
- [Bundled insurance product data](references/products.json)
- [ClawHub release page](https://clawhub.ai/mnetfairy/skills/ai-insurance-advisor)
- [ClawHub security audit](https://clawhub.ai/mnetfairy/skills/ai-insurance-advisor/security-audit)
- [National Financial Regulatory Administration insurance intermediary disclosure search](https://www.nfra.gov.cn/)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Chinese conversational guidance, structured JSON analyses, and Markdown comparison tables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results depend on user-provided information and bundled product data.]

## Skill Version(s):

2.4.11 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
