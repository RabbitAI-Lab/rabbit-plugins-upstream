## Description:

This skill locally checks clinic outpatient cashier and refund daily reconciliation tables for row arithmetic, totals, duplicate rows, blank placeholders, and negative amounts, with findings tied to source rows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Clinic cashiers and cashier-office leads use this skill before daily close to check outpatient collection and refund reconciliation tables. It helps identify arithmetic mismatches, total-row errors, duplicate cashier-shift rows, missing required fields, and negative amount entries without sending materials over the network.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release documentation includes an optional paid-upgrade flow that asks an agent to run mutable remote code and follow newly installed instructions.

Mitigation: Do not paste the purchase/install prompt into an agent unless the SkillPay package source and version have been separately verified and the user intentionally approves each install and payment step.

Risk: The free checker omits several reconciliation checks that may matter during daily close.

Mitigation: Treat findings as limited to the listed free checks and separately review checks that are not run, out-of-scope policy decisions, and accounting judgments.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/chenqg618/skills/clinic-daily-cashier-check-free)

## Skill Output:

**Output Type(s):** [text, JSON, guidance]

**Output Format:** [Human-readable text or JSON findings with source-row references]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally with Node.js standard library; reports insufficient input instead of issuing conclusions when required table data is missing.]

## Skill Version(s):

1.0.3 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
