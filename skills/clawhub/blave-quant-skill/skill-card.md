## Description:

Provides AI agents with Blave market data and reference guidance for trading across supported crypto exchanges and Taiwan markets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[blave-wei](https://clawhub.ai/user/blave-wei)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and traders use this skill to guide agents in retrieving crypto and Taiwan market data, interpreting indicators, and preparing exchange trading actions subject to user confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Downloaded marketplace or private strategy code could harm the host or access exchange credentials if run directly.

Mitigation: Review strategy code before use and run it only in an isolated sandbox without inherited exchange credentials.

Risk: Exchange credentials may enable high-impact trading or transfers.

Mitigation: Use least-privilege API keys, disable withdrawals unless needed, enable IP allowlisting, and require manual confirmation for every trade, transfer, funding, cancel-all, or leverage change.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/blave-wei/skills/blave-quant-skill)
- [Blave homepage](https://blave.org)
- [Blave API reference](references/blave-api.md)
- [Blave indicator guide](references/blave-indicator-guide.md)
- [Exchange trading references](SKILL.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Guidance]

**Output Format:** [Conversational text or Markdown with code and command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Trade, transfer, funding, cancellation, and leverage changes require explicit user confirmation.]

## Skill Version(s):

1.23.21 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
