## Description:

Checks outpatient clinic cashier and refund daily reconciliation tables by recalculating rows, verifying totals, detecting duplicate or blank rows, and citing source rows for each finding.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Clinic cashiers and cashier supervisors use this skill before daily close to check outpatient fee and refund reconciliation tables for arithmetic mismatches, total-row errors, duplicate rows, blank placeholders, and negative amounts. It reviews provided exported table text locally and does not decide whether a medical fee or refund is policy-compliant.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill processes clinic cashier reconciliation data that may contain sensitive operational or billing information.

Mitigation: Run it only in an authorized local environment and provide only data you are authorized to process.

Risk: The free version explicitly omits several checks, including system daily report mismatches, over-refund checks, cash deposit mismatches, duplicate refund checks, and insurance settlement/remittance mismatches.

Mitigation: Review the disclosed omitted checks and use separate controls or the complete product when those checks are required.

Risk: Insufficient or malformed table input produces no conclusion rather than a clean result.

Mitigation: Provide table text with headers and review missing-input messages before relying on the result.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/clinic-daily-cashier-check-free)

## Skill Output:

**Output Type(s):** [Text, JSON, Guidance]

**Output Format:** [Human-readable console text or structured JSON with executed checks, findings, missing inputs, and withheld checks.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally with Node.js; every finding cites source rows when checks can be executed.]

## Skill Version(s):

1.0.51 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
