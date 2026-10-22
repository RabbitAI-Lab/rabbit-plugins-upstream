## Description:

Prepare accrual and reversal drafts from explicitly stated schedules, requiring approval before posting and stable identities to prevent duplicate entries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[puncsky](https://clawhub.ai/user/puncsky)

### License/Terms of Use:

MIT-0

## Use Case:

External Beancount users can calculate supported period-end accruals and reversals from an explicitly stated schedule, review a balanced draft, and post it to a local ledger only after confirming.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A draft may use an incorrect schedule, calculation, account, or destination; ledger validation does not establish whether the accounting policy is correct.

Mitigation: Review the schedule, calculations, accounts, and destination before approving each draft, and keep a ledger backup.

## Reference(s):

- [Accrual schedule contract and calculation](references/schedule-contract.md)
- [Shared bea command recipes](references/bea-cli.md)
- [Dedup and import-id convention](references/dedup.md)
- [Explicit compatibility paths](references/compatibility.md)
- [Beancount.io skills homepage](https://github.com/bex-co/beancount-io/tree/main/skills)
- [ClawHub skill page](https://clawhub.ai/puncsky/skills/beancount-accruals)

## Skill Output:

**Output Type(s):** [Guidance, Text, Markdown, Shell commands]

**Output Format:** [Markdown with accounting calculations, balanced Beancount draft entries, and optional shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Drafts are based on stated schedules and ledger queries; ledger writes require explicit approval.]

## Skill Version(s):

1.0.4 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
