## Description:

A free local checker for store sales report tables that recalculates channel totals, verifies reported-sales differences, detects duplicate or missing rows, and cites source line numbers for each finding.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Operations, finance, and audit teams can use this skill to check daily or monthly store sales report tables before consolidation. It verifies whether POS cash, POS card, mobile payment, delivery-platform, and coupon channels reconcile with channel totals and reported revenue.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill includes optional paid-upgrade instructions that direct the user toward an unpinned remote installer.

Mitigation: Use the bundled local checker for free checks, and independently verify the package, source, and payment flow before running remote install commands or authorizing payment.

Risk: Blank, malformed, or incomplete financial cells can make reconciliation output incomplete.

Mitigation: Treat such results as incomplete rather than authoritative totals, and rerun the checker after supplying the required table headers and source rows.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/store-sales-report-check-free)
- [ClawHub publisher profile](https://clawhub.ai/user/chenqg618)

## Skill Output:

**Output Type(s):** [Text, JSON, Guidance, Shell commands]

**Output Format:** [Plain text or JSON containing reconciliation findings, summaries, source line numbers, and missing-input guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally with bundled Node.js code and does not require network access, registration, payment, API keys, or external services for the free checks.]

## Skill Version(s):

1.0.4 (source: SKILL.md frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
