## Description:

Guides trading-desk agents in journaling exchange activity, reviewing closed trades and incidents, and preparing weekly desk reviews.

This skill is ready for commercial/non-commercial use.

## Publisher:

[galleonlabs](https://clawhub.ai/user/galleonlabs)

### License/Terms of Use:

MIT

## Use Case:

Trading-desk agents use this skill to maintain an exchange-backed journal, assess trade execution and process separately from results, and summarize weekly activity and incidents for the user and desk lead.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Reading trading records and writing journal or review files can expose sensitive desk information or introduce inaccurate records.

Mitigation: Confirm access to desk records and intended file writes before use; reconcile reviews against timestamped exchange records.

Risk: Direct messages may disclose trade-review details to unintended recipients.

Mitigation: Confirm the desk lead and user recipients before sending review summaries.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/galleonlabs/skills/hypergrok-desk-post-trade-review)

## Skill Output:

**Output Type(s):** [Markdown, Text]

**Output Format:** [Timestamped Markdown journal entries, trade reviews, weekly summaries and incident reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Updates desk files and may send trade-review summaries by direct message to the desk lead and user.]

## Skill Version(s):

1.6.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
