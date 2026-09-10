## Description:

CoinGecko lets an agent search and read cryptocurrency market, historical, onchain, pool, trend, category, currency, and platform data through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to retrieve CoinGecko data for crypto asset lookup, market analysis, historical charting, onchain token review, DEX pool inspection, and trend discovery through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup guidance includes mutable remote installer scripts that run directly in a shell.

Mitigation: Review the installer path first; prefer a signed or package-manager install, or download and inspect or verify the installer before running it.

Risk: CoinGecko request payloads and execution metadata pass through OOMOL rather than going directly to CoinGecko.

Mitigation: Use the skill only where sending those payloads and metadata through OOMOL is acceptable for the user's data handling requirements.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-coingecko)
- [CoinGecko Homepage](https://www.coingecko.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with oo CLI shell commands and JSON request and response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill instructs agents to inspect live connector schemas before execution and to expect connector responses with data plus execution metadata.]

## Skill Version(s):

1.0.0 (source: server release evidence and artifact metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
