## Description:

Record user-described stock, fund, and crypto investment events in a local Beancount ledger with lot-aware cost basis, review, and confirmation before writes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[puncsky](https://clawhub.ai/user/puncsky)

### License/Terms of Use:

MIT No Attribution

## Use Case:

External users maintaining a local Beancount ledger can record described stock, fund, and crypto events with lot-aware cost basis, or review realized gains. Proposed entries are checked and presented for explicit approval before they are written.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Incorrect destinations, amounts, lot selection, or cost basis could affect sensitive financial records.

Mitigation: Review the destination, amounts, lots, and cost basis before confirming, and keep a ledger backup.

## Reference(s):

- [ClawHub release: beancount-trade 1.0.4](https://clawhub.ai/puncsky/skills/beancount-trade)
- [Publisher profile: puncsky](https://clawhub.ai/user/puncsky)

## Skill Output:

**Output Type(s):** [Text, Code, Guidance]

**Output Format:** [Markdown proposals and Beancount transaction entries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes require explicit user confirmation; realized-gain reporting is read-only.]

## Skill Version(s):

1.0.4 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
