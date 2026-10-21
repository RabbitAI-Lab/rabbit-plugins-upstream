## Description:

Imports bank, card, brokerage, or statement-export transactions into an existing local Beancount ledger, normalizing and categorizing entries, reviewing duplicates, and requiring approval before writing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[puncsky](https://clawhub.ai/user/puncsky)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to stage and import bank, card, brokerage, or statement transactions into an existing local Beancount ledger. It normalizes transaction data, suggests categories from existing accounts, reviews duplicates, and writes only after explicit approval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An incorrect destination, amount, category, or duplicate decision could create inaccurate ledger records.

Mitigation: Review the destination, amounts, categories, and duplicate decisions before approving the import.

Risk: Separate write steps may partially succeed.

Mitigation: Keep a ledger backup before approving writes.

Risk: A SimpleFIN access URL is sensitive and could expose account and transaction data if disclosed.

Mitigation: Use optional online paths only when intended and keep the access URL secret.

## Reference(s):

- [bea CLI recipes](references/bea-cli.md)
- [CSV import through bea](references/bea-import.md)
- [Broker activity exports](references/broker-activity.md)
- [Categorization](references/categorization.md)
- [Compatibility paths](references/compatibility.md)
- [Dedup and import IDs](references/dedup.md)
- [Export formats](references/formats.md)
- [Getting export files](references/getting-data.md)
- [Statement normalization](references/statement-formats.md)
- [SimpleFIN Bridge](https://beta-bridge.simplefin.org/)
- [Project homepage (skill metadata link)](https://github.com/bex-co/beancount-io/tree/main/skills)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Files]

**Output Format:** [Markdown guidance and shell commands; JSON batches and Beancount ledger entries for approved imports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Staged for review; ledger writes require explicit confirmation]

## Skill Version(s):

1.0.2 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
