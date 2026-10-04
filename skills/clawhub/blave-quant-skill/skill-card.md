## Description:

Guides agents in retrieving Blave market data and preparing exchange trading requests across crypto, Taiwan equities, and futures markets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[blave-wei](https://clawhub.ai/user/blave-wei)

### License/Terms of Use:

MIT-0

## Use Case:

Traders, analysts, and developers use this skill to access crypto and Taiwan market data, build trading requests for supported exchanges, and work with marketplace strategies.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Marketplace strategies may download and execute untrusted Python code locally.

Mitigation: Independently review strategies and run them only in an isolated sandbox, not on a normal machine with live exchange credentials.

Risk: Trading credentials and exchange actions can expose funds to loss.

Mitigation: Prefer read-only or narrowly scoped keys, disable withdrawals, enable IP allowlisting, use testnet accounts, and confirm each trading action explicitly.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/blave-wei/skills/blave-quant-skill)
- [Blave website](https://blave.org)
- [Blave documentation](https://blave.org/docs/en)
- [Blave API reference](artifact/references/blave-api.md)
- [Marketplace strategy reference](artifact/references/marketplace.md)

## Skill Output:

**Output Type(s):** [Text, Code, Shell commands, Configuration guidance]

**Output Format:** [Markdown with API request examples and code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can include market-data summaries and proposed trading actions; execution requires credentials and explicit confirmation.]

## Skill Version(s):

1.23.15 (source: server-resolved release and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
