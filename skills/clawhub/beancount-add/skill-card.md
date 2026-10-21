## Description:

Record one-off entries the user describes in a local Beancount ledger through bea — a purchase, bill, paycheck, or transfer between their own accounts (including splits and pasted receipt text), opening or closing an account, a price, or a note. Propose the exact entries from existing accounts, check whether one is already recorded, and write only after confirmation with a passing check; it never changes existing entries. Skip bank or card export files (beancount-import), statements (beancount-reconcile), finance-app migrations, options trades (beancount-options), investment trades, dividends, splits, and vests (beancount-trade), month-end close, edits to existing entries, and ledgers hosted on Beancount.io.

This skill is ready for commercial/non-commercial use.

## Publisher:

[puncsky](https://clawhub.ai/user/puncsky)

### License/Terms of Use:

MIT-0

## Use Case:

External users can record user-described purchases, income, transfers, account changes, prices, and notes in an existing Beancount ledger after reviewing and confirming a proposed entry.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Conflicting instructions may allow unvalidated changes to financial records or hosted-ledger access despite the stated limits.

Mitigation: Use a backed-up ledger, review every proposed destination and entry, and resolve the conflicting instructions before relying on validation or local-only guarantees.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/puncsky/skills/beancount-add)
- [bea-cli.md](references/bea-cli.md)
- [bea-import.md](references/bea-import.md)
- [bql-recipes.md](references/bql-recipes.md)
- [compatibility.md](references/compatibility.md)
- [dedup.md](references/dedup.md)
- [realized-gains.md](references/realized-gains.md)

## Skill Output:

**Output Type(s):** [Text, Beancount directives, Ledger files]

**Output Format:** [Markdown proposal and Beancount entries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Proposes entries for review and confirmation before writing to the ledger.]

## Skill Version(s):

1.0.2 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
