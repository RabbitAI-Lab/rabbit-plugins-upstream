## Description:

Enables agents to inspect Uniswap API action schemas and run quote, approval-check, and swap-calldata actions through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to request Uniswap trade quotes, check ERC-20 approval requirements, and create swap transaction calldata through an OOMOL-connected Uniswap API account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill includes pipe-to-shell installer commands for the oo CLI.

Mitigation: Use a verified installation method or inspect the installer content before running it.

Risk: Uniswap wallet, quote, trade, transaction, and permit-signature payload data is routed through OOMOL.

Mitigation: Send only payloads the user has approved and use the connector only when the user accepts sharing that data with OOMOL.

Risk: The create_swap action produces transaction calldata that can affect assets if used incorrectly.

Mitigation: Confirm the exact payload, quoted terms, wallet, token pair, amount, and intended effect before generating or using swap calldata.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-uniswap-api)
- [Uniswap API homepage](https://uniswap.org)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with bash commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses are JSON objects with data and meta.executionId fields.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
