## Description:

Guides agents through Blave quantitative market data, Taiwan stocks and futures, and trading workflows across supported exchanges.

This skill is ready for commercial/non-commercial use.

## Publisher:

[blave-wei](https://clawhub.ai/user/blave-wei)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and traders use this skill to query crypto and Taiwan market data, research or backtest strategies, and prepare exchange trading operations with user confirmation before writes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Marketplace strategies may be downloaded and run locally without isolation.

Mitigation: Review strategy code before use and run it in a sandbox without inherited .env files or exchange credentials.

Risk: Trading API credentials and permitted actions can expose funds to loss.

Mitigation: Use read-only or least-privilege keys where possible, disable withdrawals, and require explicit confirmation before exchange write actions.

Risk: Several exchange request flows include broker or referral attribution.

Mitigation: Review attribution and associated terms before using those exchange integrations.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/blave-wei/skills/blave-quant-skill)
- [Blave website](https://blave.org)
- [Blave documentation](https://blave.org/docs/en)
- [Blave API reference](references/blave-api.md)
- [Exchange trading reference](references/bitmart-futures-skill.md)
- [Strategy marketplace reference](references/marketplace.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration guidance]

**Output Format:** [Markdown with API examples and code or shell snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Exchange write operations require explicit user confirmation.]

## Skill Version(s):

1.23.20 (source: ClawHub release and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
