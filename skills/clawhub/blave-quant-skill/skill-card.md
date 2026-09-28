## Description:

Provides agents with reference guidance for Blave market data, quantitative research, and authenticated trading across supported exchanges.

This skill is ready for commercial/non-commercial use.

## Publisher:

[blave-wei](https://clawhub.ai/user/blave-wei)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and traders use this skill to query crypto, Taiwan equity, and futures market data, research strategies, and guide exchange trading or account actions through an agent.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Trading-capable API keys can authorize financial transactions or expose account data.

Mitigation: Use dedicated low-balance, least-privilege keys, disable withdrawals, enable IP allowlisting, and require explicit confirmation for each account-changing action.

Risk: Downloaded marketplace or shared strategy code may be unsafe to run locally.

Mitigation: Do not execute it directly; review its source and immutable provenance, then run only in an isolated sandbox without inherited credentials.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/blave-wei/skills/blave-quant-skill)
- [Blave website](https://blave.org)
- [Blave documentation](https://blave.org/docs/en)
- [Blave API reference](references/blave-api.md)
- [Exchange strategy marketplace reference](references/marketplace.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration guidance]

**Output Format:** [Markdown guidance with API requests and code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Market data requires Blave credentials; exchange actions require separate API keys and user confirmation.]

## Skill Version(s):

1.23.9 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
