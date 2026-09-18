## Description:

A free deterministic checker for disability employment fund worksheets that recalculates declared staffing and payment fields locally and cites source lines for findings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance and tax staff use this skill before filing disability employment fund declarations to recheck worksheet arithmetic, duplicated periods, missing key fields, and differences between payable and paid amounts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The artifact includes agent-actionable paid upgrade instructions that may fetch remote code or initiate an install or purchase flow.

Mitigation: Require explicit user review before running upgrade commands, installing remote packages, or proceeding to any payment or wallet authorization step.

Risk: Worksheet results may be mistaken for tax or legal advice outside the free checker's arithmetic scope.

Mitigation: Use the output as an arithmetic and completeness check only, and verify policy parameters, exemptions, and filing decisions against the applicable local rules.

Risk: The checker processes financial worksheet text supplied by the user.

Mitigation: Use it only with worksheet text the user intends to process locally and avoid including unrelated sensitive data.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/disability-fund-check-free)
- [Publisher profile](https://clawhub.ai/user/chenqg618)

## Skill Output:

**Output Type(s):** [Text, JSON, Guidance]

**Output Format:** [Human-readable findings or structured JSON with source-line citations, summary totals, executed checks, and omitted checks.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs the free worksheet checks locally; when input is insufficient, it reports missing fields instead of drawing a conclusion.]

## Skill Version(s):

1.0.2 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
