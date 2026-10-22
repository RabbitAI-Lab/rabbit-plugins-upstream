## Description:

Migrate full transaction history from Mint, Monarch, QuickBooks Online or another category-tagged finance-app export into a fresh local Beancount ledger, including requests to create a new ledger and bring in that history.

This skill is ready for commercial/non-commercial use.

## Publisher:

[puncsky](https://clawhub.ai/user/puncsky)

### License/Terms of Use:

MIT-0

## Use Case:

Migrate categorized transaction history from financial apps into a fresh local Beancount ledger, preserving source identifiers, pairing transfers, and reconciling source counts and balances before relying on the result.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Incorrect account or category mappings, transfer pairing, balance dates, or splits can make imported ledger history misleading.

Mitigation: Review mappings, balance dates, splits, row counts, and reconciliation results against the source export before relying on the ledger.

Risk: An interrupted multi-step migration may leave completed writes that could be duplicated on retry.

Mitigation: Inspect completed changes before resuming, and keep the original export while working in a separate fresh ledger directory.

## Reference(s):

- [ClawHub release](https://clawhub.ai/puncsky/skills/beancount-migrate)
- [Publisher profile](https://clawhub.ai/user/puncsky)
- [Project homepage (skill metadata)](https://github.com/bex-co/beancount-io/tree/main/skills)
- [Migration mapping guidance](artifact/references/mapping.md)
- [Beancount CLI guidance](artifact/references/bea-cli.md)

## Skill Output:

**Output Type(s):** [Guidance, Configuration, Code, Shell commands]

**Output Format:** [Markdown guidance with Beancount entries, JSON transaction batches, and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Migration writes are staged; review mappings, source IDs, balance assertions, and reconciliation results before relying on changes.]

## Skill Version(s):

1.0.4 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
