## Description:

Provides market-data guidance and exchange-trading references for agents researching crypto, Taiwan stocks, and futures across multiple venues.

This skill is ready for commercial/non-commercial use.

## Publisher:

[blave-wei](https://clawhub.ai/user/blave-wei)

### License/Terms of Use:

MIT-0

## Use Case:

Traders, researchers, and developers use this skill to query market data, analyze strategies, and prepare exchange trading actions with explicit confirmation before account changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Marketplace instructions may lead an agent to download and run unreviewed third-party Python strategies.

Mitigation: Do not run marketplace strategies unless independently reviewed; use an isolated environment without inherited credentials.

Risk: Exchange credentials and trading actions can expose funds to loss or unauthorized access.

Mitigation: Use read-only or narrowly scoped keys, keep broad secrets out of the agent environment, and require explicit confirmation before each account-changing action.

## Reference(s):

- [ClawHub release](https://clawhub.ai/blave-wei/skills/blave-quant-skill)
- [Blave website](https://blave.org)
- [Blave documentation](https://blave.org/docs/en)
- [Blave API reference](references/blave-api.md)
- [Exchange strategy marketplace](references/marketplace.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration guidance]

**Output Format:** [Markdown with API request examples and code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Market-data access requires Blave credentials; exchange actions require venue credentials and explicit confirmation.]

## Skill Version(s):

1.23.26 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
