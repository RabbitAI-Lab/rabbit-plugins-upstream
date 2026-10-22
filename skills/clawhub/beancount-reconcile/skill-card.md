## Description:

Reconcile one local Beancount account against a CSV or PDF statement, report discrepancies, and—with confirmation—append missing entries and a verified period-end balance assertion.

This skill is ready for commercial/non-commercial use.

## Publisher:

[puncsky](https://clawhub.ai/user/puncsky)

### License/Terms of Use:

MIT No Attribution

## Use Case:

Developers and finance or bookkeeping users use this skill to compare one local Beancount account with a statement, review discrepancies, and confirm proposed ledger additions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An incorrect account selection, proposed entry, or balance calculation could introduce bookkeeping errors.

Mitigation: Review the target file, account, proposed entries, and balance calculation before approving changes.

Risk: The separate account-open, transaction, and assertion writes may leave approved changes partially completed if interrupted.

Mitigation: Keep a ledger backup and inspect the ledger state before retrying after an interruption.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/puncsky/skills/beancount-reconcile)
- [bea command recipes](references/bea-cli.md)
- [Statement formats](references/statement-formats.md)
- [Transaction matching](references/matching.md)
- [Supported formats](references/formats.md)

## Skill Output:

**Output Type(s):** [Markdown, Guidance, Beancount entries, Shell commands]

**Output Format:** [Markdown discrepancy report and, when approved, Beancount transaction and balance-assertion entries.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reviews one account and statement period; only appends approved missing entries and an assertion, while reporting other discrepancies for manual review.]

## Skill Version(s):

1.0.4 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
