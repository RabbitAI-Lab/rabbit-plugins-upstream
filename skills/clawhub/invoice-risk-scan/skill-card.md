## Description:

Pre-screens invoice tax ID format, positive amount, and invoice date before reimbursement or bookkeeping.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT (code only); documentation and methodology all rights reserved

## Use Case:

Employees and finance teams use this local pre-screen to catch basic invoice-field issues before reimbursement or bookkeeping; a passing result still needs human review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Basic field checks can pass invoices with invalid calendar dates or unverified tax identifiers.

Mitigation: Confirm invoice details against authoritative records and use human review before reimbursement or bookkeeping.

Risk: Invoice fields may contain sensitive business information.

Mitigation: Run the scan locally and avoid network access unless separately authorized.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/zhaoxinghua09-cell/skills/invoice-risk-scan)
- [Publisher homepage](https://zhaoxinghua09-cell.github.io/lgd-hub/)

## Skill Output:

**Output Type(s):** [Text, JSON]

**Output Format:** [Plain-text PASS/FAIL checks or JSON with pass, checks, and problems]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Exit code 0 for pass, 1 for failed checks, and 2 for usage errors; Chinese-first output.]

## Skill Version(s):

1.0.2 (source: ClawHub release metadata; bundled SKILL.md lists 1.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
