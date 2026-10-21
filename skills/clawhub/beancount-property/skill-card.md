## Description:

Record buying, holding, and selling a home or rental property in a local Beancount ledger through bea — the property as a priced lot, its mortgage liability, escrow, and closing costs split exactly as the closing statement states; each mortgage payment's split read from the loan statement and tied to its printed new balance; rent and deposits per property; and a sale whose gain the booking produces — proposed first and written only after confirmation. Skip paying rent as a tenant (beancount-add), bank or loan statement files (beancount-import), statement comparison (beancount-reconcile), tax treatment and depreciation advice, and ledgers hosted on Beancount.io.

This skill is ready for commercial/non-commercial use.

## Publisher:

[puncsky](https://clawhub.ai/user/puncsky)

### License/Terms of Use:

MIT No Attribution

## Use Case:

Beancount users use this skill to record property purchases, mortgages, escrow, rental income and deposits, mortgage payments, and property sales in a local ledger. It proposes entries for review before writing them.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Conflicting instructions could redirect an intended local-ledger workflow to a hosted financial account.

Mitigation: Remove the hosted-ledger fallback or make it explicitly opt-in before granting access to a connected financial account.

Risk: Approved ledger writes could target unintended entries or destinations.

Mitigation: Keep a ledger backup and review the exact proposed entries and destination paths before approving writes.

## Reference(s):

- [bea CLI reference](references/bea-cli.md)
- [bea import reference](references/bea-import.md)
- [Compatibility reference](references/compatibility.md)
- [Deduplication reference](references/dedup.md)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands]

**Output Format:** [Markdown with Beancount entries and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Entries are proposed for user review and confirmation before being written.]

## Skill Version(s):

1.0.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
