## Description:

Guides agents through OpenSea data queries, NFT trades, token swaps, wallet setup, and building gated agent tools.

This skill is ready for commercial/non-commercial use.

## Publisher:

[opensea](https://clawhub.ai/user/opensea)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to research OpenSea assets and prepare or execute marketplace trades, token swaps, wallet operations, and agent-tool integrations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Trades, swaps, cancellations, and account changes can have high-impact financial or access consequences.

Mitigation: Require explicit review before executing any trade, swap, cancellation, save or remove action, or account relationship change.

Risk: An agent with wallet or policy-administration credentials could exceed intended spending limits.

Mitigation: Use managed wallet providers with strict policies and keep administrator credentials off the agent host.

Risk: Changing CLI or package dependencies can alter transaction behavior.

Mitigation: Pin CLI and package versions where possible and review updates before use.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/opensea/skills/opensea-marketplace)
- [Listed project homepage](https://github.com/ProjectOpenSea/opensea-skill)
- [OpenSea API key documentation](https://docs.opensea.io/reference/api-keys)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Code, Configuration guidance]

**Output Format:** [Markdown with command and code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include API responses and transaction instructions; actions require appropriate credentials and wallet authorization.]

## Skill Version(s):

2.26.1 (source: server release evidence and package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
