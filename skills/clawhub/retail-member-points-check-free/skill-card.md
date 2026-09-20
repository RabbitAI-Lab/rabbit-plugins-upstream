## Description:

A free local checker for retail member points and stored-value reconciliation tables that recalculates row balances, checks totals, detects duplicate or incomplete rows, and cites source lines for each finding.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance, cashier, and retail operations staff use this skill during monthly closing, reconciliation, and inventory routines to check member points and stored-value card tables for arithmetic mismatches, total-line errors, duplicate member-period rows, blanks, placeholders, and negative values. It is intended as table arithmetic support, not accounting, tax, or compliance advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The tool analyzes reconciliation-table data and can be mistaken for accounting, tax, or compliance advice.

Mitigation: Use outputs as arithmetic checks only and have qualified staff review accounting, tax, and compliance conclusions.

Risk: Telemetry and help text are inconsistent with the inspected implementation.

Mitigation: Review the current release text before deployment and prefer environments where local execution can be monitored or network access can be restricted.

Risk: The interface and findings are Chinese-language and may be misread by users who do not understand the terminology.

Mitigation: Deploy only to users who can review the Chinese reconciliation terminology or provide a validated translation workflow.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/retail-member-points-check-free)
- [Publisher profile](https://clawhub.ai/user/chenqg618)

## Skill Output:

**Output Type(s):** [Text, JSON, Guidance]

**Output Format:** [Plain text or JSON report with cited row-level findings]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings cite source rows; insufficient input returns missing requirements rather than a reconciliation conclusion.]

## Skill Version(s):

1.0.47 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
