## Description:

CoinMarketCap (coinmarketcap.com). Use this skill for CoinMarketCap requests involving cryptocurrency search, pricing, listings, market metrics, conversion, and API key usage data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and crypto analysts use this skill to retrieve CoinMarketCap data through an OOMOL-connected account. It supports asset discovery, latest quotes, ranked listings, global market metrics, price conversion, and API key usage checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup instructions include remote installer scripts that can execute mutable code on a user's machine.

Mitigation: Prefer official package-manager or verified installer steps, and review what the oo CLI installation persists before running installer commands.

Risk: CoinMarketCap access is brokered through OOMOL, so account connection and credential handling depend on that service.

Mitigation: Install only when comfortable using OOMOL as the broker, and confirm the CoinMarketCap connection scope before running connector actions.

## Reference(s):

- [CoinMarketCap Homepage](https://coinmarketcap.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-coinmarketcap)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands inspect the live connector schema before sending JSON payloads; connector responses include data and meta.executionId.]

## Skill Version(s):

1.0.3 (source: server release evidence and artifact metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
