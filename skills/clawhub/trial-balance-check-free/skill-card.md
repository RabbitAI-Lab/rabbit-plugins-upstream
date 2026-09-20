## Description:

A local Chinese-style trial-balance checker that recomputes closing balances, checks profit-and-loss closing, compares debit and credit totals, verifies parent and detail-account subtotals, and flags duplicate, blank, or non-numeric cells with source-line citations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Accounting staff, finance managers, and auditors use this skill to check a pasted trial-balance/account-balance table before monthly close or audit review. It is intended to identify arithmetic, closing, subtotal, duplicate-account, and missing-value issues while refusing to conclude when required input is missing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The help text mentions anonymous usage statistics and a --no-stats option even though the security evidence says those are not implemented.

Mitigation: Treat the package as local-only based on the security verdict, and clean up or confirm the help text before relying on those usage-statistics statements.

Risk: Incorrect table headers, incomplete rows, or inconsistent debit/credit sign conventions can prevent a reliable accounting check.

Mitigation: Provide a complete trial-balance table with the required headers and documented sign convention, then review each source-line finding before using it for close or audit decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/trial-balance-check-free)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, guidance]

**Output Format:** [Plain text or JSON report with source-line references]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally over user-provided table text; insufficient input produces a missing-information response instead of a clean finding.]

## Skill Version(s):

1.0.49 (source: SKILL.md frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
