## Description:

Performs a free deterministic check of petty-cash and reimbursement tables, citing source lines for each finding and requiring no payment, registration, API key, or network access.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance and cashier staff use this skill during monthly close, reconciliation, inventory checks, offboarding handoff, and internal control reviews to recalculate petty-cash and reimbursement ledgers. It identifies arithmetic mismatches, total-row issues, duplicate person-period rows, missing placeholders, and negative amounts in the free check scope.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may treat arithmetic reconciliation findings as accounting policy, tax, invoice, or approval compliance decisions.

Mitigation: Use the output as reconciliation assistance only and review results against the organization's accounting policy, tax, invoice, and approval requirements.

Risk: The free release omits several checks and refuses to conclude when required table material is missing.

Mitigation: Review the reported executed checks, checks not run, missing input messages, and source-line citations before relying on the result.

Risk: The tool is Chinese-language and designed as a local Node workflow for petty-cash and reimbursement table checks.

Mitigation: Have users who understand the table format and Chinese output review the findings before operational use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/petty-cash-check-free)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Guidance]

**Output Format:** [Plain text or JSON reconciliation report from a local Node CLI]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings cite input rows; exit codes distinguish completed checks, insufficient input, unreadable input, parse errors, and unexpected errors.]

## Skill Version(s):

1.0.53 (source: evidence.json release.version and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
