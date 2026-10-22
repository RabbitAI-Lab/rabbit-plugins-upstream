## Description:

Imports and categorizes bank, card, and brokerage transactions into an existing local Beancount ledger, with duplicate checks and explicit approval before writes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[puncsky](https://clawhub.ai/user/puncsky)

### License/Terms of Use:

MIT No Attribution

## Use Case:

External users and developers maintaining a local Beancount ledger use the skill to import bank, card, and broker statements, review categorization and duplicate decisions, and approve ledger entries. PDF imports are checked against statement balances before completion.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Imported amounts, categories, duplicate decisions, or the destination could be incorrect.

Mitigation: Back up the ledger and review the proposed amounts, categories, duplicates, and destination before approving writes.

Risk: An optional SimpleFIN feed uses a secret access link.

Mitigation: Keep the secret URL out of the ledger and repository; use manual exports to avoid providing a financial-feed credential.

## Reference(s):

- [Project Homepage](https://github.com/bex-co/beancount-io/tree/main/skills)
- [ClawHub Skill Page](https://clawhub.ai/puncsky/skills/beancount-import)
- [Import Workflow Reference](references/bea-import.md)
- [Duplicate Review Reference](references/dedup.md)
- [Broker Activity Reference](references/broker-activity.md)
- [Statement Formats Reference](references/statement-formats.md)

## Skill Output:

**Output Type(s):** [Code, JSON, Guidance]

**Output Format:** [Beancount transaction entries and structured JSON batches, with a human-readable review proposal]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Entries are staged for review and written only after explicit confirmation; import IDs support idempotent re-imports.]

## Skill Version(s):

1.0.4 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
