## Description:

A free local checker for invoice and expense-claim text that reports recomputable arithmetic, date, duplicate, placeholder, and entity-name consistency findings with evidence.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

External users, finance reviewers, and operations teams use this skill to check invoice or reimbursement text before submission. It identifies internally inconsistent amounts, taxes, dates, titles, duplicate invoices, and placeholders, but it does not determine invoice authenticity, tax legality, or reimbursement approval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The documentation includes a separate paid-upgrade flow that asks users or agents to run an unpinned external installer and begin a paid skill-install workflow.

Mitigation: Use the local free checker only unless the user explicitly chooses the paid workflow; verify the Alipay/SkillPay source, pin or review installers where possible, and require explicit confirmation for each purchase or additional skill installation.

Risk: A clean result can be mistaken for proof that an invoice is authentic, compliant, or reimbursable.

Mitigation: Treat the output as limited consistency evidence and keep tax, audit, authenticity, and reimbursement approval checks in separate human or system review steps.

Risk: The checker relies on text input with recognizable labels or table structure, so PDFs, images, OCR noise, or weakly labeled materials can produce insufficient input or missed checks.

Mitigation: Convert source documents to labeled text, review missing-input messages and withheld checks, and manually inspect any fields the checker could not parse.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/invoice-consistency-check-free)
- [Publisher profile](https://clawhub.ai/user/chenqg618)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, guidance]

**Output Format:** [Plain text or JSON with findings, summary, executed checks, and withheld checks.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally on provided invoice text; insufficient material returns missing-input guidance without a consistency verdict.]

## Skill Version(s):

1.0.12 (source: release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
