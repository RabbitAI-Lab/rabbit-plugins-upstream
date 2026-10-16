## Description:

Provides AI agents with Blave market data and exchange-trading guidance for crypto, Taiwan equities, and futures.

This skill is ready for commercial/non-commercial use.

## Publisher:

[blave-wei](https://clawhub.ai/user/blave-wei)

### License/Terms of Use:

MIT-0

## Use Case:

Traders and developers use this skill to research market data, build analyses, and prepare exchange trading actions with explicit confirmation before account changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Marketplace or shared strategies may run untrusted Python code on the host.

Mitigation: Inspect downloaded strategy code before running it; use an isolated environment without exchange credentials or sensitive local files.

Risk: Exchange API credentials and trading actions can expose accounts to loss or misuse.

Mitigation: Use least-privilege keys, disable withdrawals, enable IP allowlisting, and require the explicit CONFIRM flow for each trade or account change.

## Reference(s):

- [Blave homepage](https://blave.org)
- [Blave documentation](https://blave.org/docs/en)
- [Blave Quant ClawHub release](https://clawhub.ai/blave-wei/skills/blave-quant-skill)
- [Blave API reference](references/blave-api.md)
- [BitMart futures trading reference](references/bitmart-futures-skill.md)
- [Strategy marketplace reference](references/marketplace.md)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Code, Shell commands]

**Output Format:** [Text and Markdown with code and command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Trading and account-changing actions require explicit confirmation.]

## Skill Version(s):

1.23.25 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
