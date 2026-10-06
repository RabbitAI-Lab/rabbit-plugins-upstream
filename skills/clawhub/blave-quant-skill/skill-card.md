## Description:

Provides market data analysis and exchange trading workflows for AI agents covering crypto, commodities, and Taiwan markets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[blave-wei](https://clawhub.ai/user/blave-wei)

### License/Terms of Use:

MIT-0

## Use Case:

Traders and developers use this skill to retrieve market and Taiwan equity data, analyze trading signals, and prepare or carry out exchange trades with explicit confirmation for account-changing actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Downloaded marketplace or shared strategies may run unreviewed code on the user's host.

Mitigation: Review strategy code before use and execute only in a sandbox with secrets isolated.

Risk: Exchange credentials or automated trades can expose funds to loss or unauthorized actions.

Mitigation: Prefer read-only or least-privilege API keys, disable withdrawals, and require explicit confirmation before trades, transfers, or funding actions.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/blave-wei/skills/blave-quant-skill)
- [Blave homepage](https://blave.org)
- [Blave documentation](https://blave.org/docs/en)
- [Blave API reference](references/blave-api.md)
- [Marketplace strategy reference](references/marketplace.md)

## Skill Output:

**Output Type(s):** [Analysis, Text, Shell commands, Code, Guidance]

**Output Format:** [Markdown with market data summaries and API or trading examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Exchange write actions require explicit user confirmation.]

## Skill Version(s):

1.23.16 (source: SKILL.md frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
