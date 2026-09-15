## Description:

A free local expense-claim pre-check that reviews one reimbursement form and a batch of invoices for duplicate invoice numbers, missing invoice fields, and leftover template placeholders, with line-referenced findings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, finance operators, and agents use this skill before submitting expense claims to mechanically flag duplicate invoices, incomplete invoice fields, and unreplaced placeholders. It does not judge whether an expense should be reimbursed or verify invoice authenticity.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The artifact includes an optional paid-upgrade path that directs an agent toward an unpinned external installer and purchase flow.

Mitigation: Use the free local checker without following upgrade or payment instructions unless the SkillPay source, package version, and newly installed onboarding skill are separately verified and the user personally confirms any payment.

Risk: Expense and invoice text can contain sensitive business or personal information.

Mitigation: Only provide documents the user is comfortable analyzing locally, and do not send the input text to external services.

Risk: A clean result is limited to the three checks performed by the free version.

Mitigation: Treat results as a pre-check only; use company policy, approval workflow, and invoice-authenticity controls for reimbursement decisions.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/chenqg618/skills/expense-compliance-free)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, guidance]

**Output Format:** [Human-readable text or JSON findings with line-referenced evidence.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Local Node.js execution; insufficient input returns no compliance conclusion.]

## Skill Version(s):

1.0.4 (source: server release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
