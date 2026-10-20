## Description:

Import bank, card, or broker activity exports into an existing Beancount ledger with normalized amounts, duplicate review, user-approved entries, and balance assertions for PDF statements.

This skill is ready for commercial/non-commercial use.

## Publisher:

[puncsky](https://clawhub.ai/user/puncsky)

### License/Terms of Use:

MIT-0

## Use Case:

External users who maintain Beancount ledgers use the skill to review and import bank, card, broker, or statement-export activity into an existing ledger. It stages and checks proposed entries, then writes only after explicit approval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Conflicting instructions extend the workflow to hosted financial tools without clearly defined approval boundaries.

Mitigation: Use a backed-up local ledger and approve the exact entries and destination before writing; clarify hosted-ledger scope and approval requirements before connected server operations.

Risk: A SimpleFIN access URL can expose access to financial data if supplied unintentionally or committed.

Mitigation: Provide the URL only when intentionally enabling that feed, and keep it out of committed files.

## Reference(s):

- [bea CLI guidance](artifact/references/bea-cli.md)
- [CSV import guidance](artifact/references/bea-import.md)
- [Broker activity guidance](artifact/references/broker-activity.md)
- [Categorization guidance](artifact/references/categorization.md)
- [Compatibility guidance](artifact/references/compatibility.md)
- [Deduplication guidance](artifact/references/dedup.md)
- [Export format guidance](artifact/references/formats.md)
- [Getting financial data](artifact/references/getting-data.md)
- [Statement formats](artifact/references/statement-formats.md)
- [Project homepage listed in skill metadata](https://github.com/bex-co/beancount-io/tree/main/skills)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown review tables and Beancount entry proposals, with JSON batches and bea commands for approved writes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Proposed ledger changes require explicit user approval before writing.]

## Skill Version(s):

1.0.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
