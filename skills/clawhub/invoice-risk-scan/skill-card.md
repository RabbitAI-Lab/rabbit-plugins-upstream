## Description:

Pre-screens invoice tax ID format, amount, and date before reimbursement or accounting, flagging anomalies for review.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT-0 (ClawHub listing); MIT (.py code); all rights reserved (documentation and theory)

## Use Case:

Finance staff and developers use this local screening aid to check invoice fields before reimbursement or entry into accounting systems; flagged issues require human review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A passing check may be mistaken for tax or legal compliance approval.

Mitigation: Use results only as a preliminary check; verify consequential decisions against official guidance and qualified professionals.

Risk: Installing from an untrusted GitHub revision or npx package may introduce unwanted code.

Mitigation: Install only from a revision and package source you trust.

Risk: Invoice fields may contain sensitive business information.

Mitigation: Process locally and provide only the minimum invoice details needed for screening.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/zhaoxinghua09-cell/skills/invoice-risk-scan)
- [Publisher homepage](https://zhaoxinghua09-cell.github.io/lgd-hub/)

## Skill Output:

**Output Type(s):** [Text, JSON, Guidance]

**Output Format:** [Plain-text PASS/FAIL checks or JSON check results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Exit code 0 for pass, 1 for flagged issues, and 2 for usage errors; local pre-screening only.]

## Skill Version(s):

1.0.3 (source: ClawHub release; bundled frontmatter states 1.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
