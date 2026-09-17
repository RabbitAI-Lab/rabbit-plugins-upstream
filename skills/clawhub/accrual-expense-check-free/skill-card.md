## Description:

预提费用台账逐项核对，每条结论都带原文依据，不需要付款，也不需要注册。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance and accounting staff use this skill around month-end close, reconciliation, or inventory checks to review accrual expense ledgers for arithmetic consistency, totals, duplicates, blanks, and source-cited findings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill advertises a paid upgrade flow that asks an assistant to run an unpinned remote package.

Mitigation: Independently verify the package, version, publisher, payment flow, and filesystem changes before running any payment-related install command.

Risk: The free tier omits several accrual expense checks and may be mistaken for a complete accounting review.

Mitigation: Review the disclosed withheld checks and out-of-scope items before relying on a no-findings result.

## Reference(s):

- [ClawHub skill release page](https://clawhub.ai/chenqg618/skills/accrual-expense-check-free)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Human-readable text or JSON reports with executed checks, findings, missing-input notices, and withheld-check disclosures.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs against user-provided accrual ledger text; the free tier omits five named checks and does not treat insufficient input as a clean result.]

## Skill Version(s):

1.0.7 (source: server release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
