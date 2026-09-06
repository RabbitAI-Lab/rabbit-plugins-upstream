## Description:

HypeLens Agent Rail helps AI agents check Hyperliquid perpetual futures liquidation-wall and pretrade risk before routing order placement through its MCP rail.

This skill is ready for commercial/non-commercial use.

## Publisher:

[polyparlay](https://clawhub.ai/user/polyparlay)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and agent builders use this skill to add a Hyperliquid perpetuals risk-checking rail that surfaces liquidation-wall context and pretrade warnings before an agent opens a position.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Running unpinned external package code may execute code that differs from the reviewed release.

Mitigation: Verify the npm package identity and exact version independently, then pin the version in deployment configuration.

Risk: The skill flow can require wallet-based trading authority and a 0.02% builder fee.

Mitigation: Use testnet first, avoid valuable wallets, confirm the fee, and verify the process for revoking agent wallet authorization before granting access.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/polyparlay/skills/hypelens-agent-rail)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with MCP tool names, setup environment variables, and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide wallet setup, testnet-first checks, pretrade review, and order-placement flow for Hyperliquid perpetuals.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
