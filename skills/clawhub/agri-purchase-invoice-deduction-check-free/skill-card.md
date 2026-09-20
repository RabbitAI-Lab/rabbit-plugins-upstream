## Description:

Checks Chinese agricultural purchase invoice and VAT deduction reconciliation tables for row-level arithmetic, total tie-outs, duplicate voucher numbers, blanks, and negative values, with findings tied to source material.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

External finance and accounting users can use this skill during month-end reconciliation to check agricultural purchase invoice and VAT deduction tables for deterministic arithmetic and completeness issues. It is a reconciliation aid, not tax advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill is a narrow reconciliation aid and the free version omits several policy and compliance checks.

Mitigation: Use it for deterministic table checks only; review omitted checks and consult qualified tax guidance for policy or compliance decisions.

Risk: Insufficient or malformed input can prevent checks from running and should not be treated as a clean result.

Mitigation: Provide the complete table with required headers and treat insufficient-input output as missing evidence, not as a pass.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/agri-purchase-invoice-deduction-check-free)
- [Publisher profile](https://clawhub.ai/user/chenqg618)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Guidance]

**Output Format:** [Plain text or JSON findings with source line references and Node.js command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally; when input is insufficient it withholds conclusions and reports missing material.]

## Skill Version(s):

1.0.60 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
