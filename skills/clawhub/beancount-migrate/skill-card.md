## Description:

Migrate full transaction history from Mint, Monarch, QuickBooks Online or another category-tagged finance-app export into a fresh local Beancount ledger. Confirm account/category mappings, pair transfers, preserve source IDs, write through bea and reconcile source counts and balances. Skip ongoing bank imports, populated-ledger merges investment lot reconstruction, and ledgers hosted on Beancount.io.

This skill is ready for commercial/non-commercial use.

## Publisher:

[puncsky](https://clawhub.ai/user/puncsky)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to migrate categorized finance-app exports into a fresh local Beancount ledger, confirm account and category mappings, pair transfers, and reconcile imported counts and balances.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill contains conflicting guidance about using hosted-ledger tools, which could expand a migration beyond the intended local ledger.

Mitigation: Limit work to a fresh local ledger unless the user separately authorizes a specific hosted destination and its permitted changes.

Risk: Incorrect category mappings or proposed entries could produce an inaccurate financial ledger.

Mitigation: Have the user review mappings and proposed entries, retain original exports, and reconcile final counts and balances.

## Reference(s):

- [Beancount CLI guidance](references/bea-cli.md)
- [Beancount import guidance](references/bea-import.md)
- [Compatibility guidance](references/compatibility.md)
- [Deduplication guidance](references/dedup.md)
- [Supported formats](references/formats.md)
- [Account mapping guidance](references/mapping.md)
- [Mint migration guidance](references/mint.md)
- [Monarch migration guidance](references/monarch.md)
- [QuickBooks Online migration guidance](references/qbo.md)
- [Statement formats](references/statement-formats.md)
- [Declared skill documentation homepage](https://github.com/bex-co/beancount-io/tree/main/skills)
- [ClawHub skill release](https://clawhub.ai/puncsky/skills/beancount-migrate)

## Skill Output:

**Output Type(s):** [Files, Markdown, Shell commands, Guidance]

**Output Format:** [Beancount ledger files, a Markdown migration report, and concise command or mapping guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Proposed mappings and converted transactions are reviewed and reconciled against source counts and balances.]

## Skill Version(s):

1.0.2 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
