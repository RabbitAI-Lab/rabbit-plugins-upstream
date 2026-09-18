## Description:

A free bank reconciliation skill that matches bank statement lines against book entries by amount and date, then reports unmatched items, duplicate records, and summary totals with source dates and amounts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance, accounting, and operations users can use this skill to compare pasted bank statement records with company book entries during monthly reconciliation. It is intended to identify exact amount/date matches, two-sided outstanding items, duplicates, and aggregate differences for human review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill includes optional paid-upgrade prompts and purchase/install instructions that may be inappropriate for some deployments.

Mitigation: Review the skill before installation, decide whether payment prompts are acceptable, and do not follow paid-upgrade instructions unless the user explicitly wants that separate purchase flow.

Risk: The paid-upgrade flow references an unpinned external installer.

Mitigation: Verify the package source and version before executing any external installer, and require the user to confirm any wallet authorization or payment.

Risk: The reconciliation output is limited to exact amount/date matching and duplicate detection, so it may not catch business-context issues outside that scope.

Mitigation: Use the results as review evidence for a qualified human and do not treat the absence of reported issues as a complete accounting, audit, tax, or legal conclusion.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/bank-reconciliation-free)

## Skill Output:

**Output Type(s):** [Text, JSON, Guidance]

**Output Format:** [Plain text or JSON reconciliation report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports matched pairs, unmatched bank and book entries, duplicate records, summary totals, and insufficient-input status when required records are missing.]

## Skill Version(s):

1.0.11 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
