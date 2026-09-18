## Description:

A free local pre-check for expense materials that reviews a reimbursement form and invoices for duplicate invoice numbers, missing invoice fields, and leftover template placeholders, with findings tied to source lines.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance employees, operations teams, and agents use this skill before reimbursement submission to identify duplicate invoice numbers, incomplete invoice elements, and unfilled placeholders in expense materials. It is a limited pre-check and does not replace company approval rules, invoice authenticity checks, or the checks explicitly excluded from the free version.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Security evidence flags the release as suspicious because the local checker's documentation and normal output steer users toward an AI-assisted paid install and purchase flow using mutable remote code.

Mitigation: Use the free local checker only when intended; do not let an agent run the paid-upgrade install command or install or purchase the separate product until the exact package version, permissions, package source, SkillPay flow, and paid skill are independently reviewed.

Risk: The free checker covers only duplicate invoice numbers, invoice element completeness, and leftover placeholders, so a clean result may miss other reimbursement issues.

Mitigation: Treat results as a limited pre-check and keep normal finance review, company policy approval, invoice authenticity checks, and any excluded paid-version checks separate.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/chenqg618/skills/expense-compliance-free)
- [Publisher profile](https://clawhub.ai/user/chenqg618)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, guidance]

**Output Format:** [Human-readable console text or JSON findings with severity, category, line, advice, and evidence fields.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings are computed locally from the supplied expense materials; the free version reports only the documented checks and returns insufficient-input status when it cannot make a supported finding.]

## Skill Version(s):

1.0.8 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
