## Description:

Hyperliquid Place helps OpenClaw/MCP agents install and operate a Hyperliquid perpetuals trading rail for placing, canceling, and closing orders with an agent wallet.

This skill is ready for commercial/non-commercial use.

## Publisher:

[polyparlay](https://clawhub.ai/user/polyparlay)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and users use this skill to configure an OpenClaw/MCP agent for Hyperliquid perpetuals trading, including wallet setup, builder-fee approval, order placement, cancellation, position closing, balances, and positions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can enable an agent to place, cancel, and close Hyperliquid perpetuals trades and approve builder fees on mainnet.

Mitigation: Keep HYPELENS_NET on testnet until the package source and behavior are verified, and manually confirm mainnet orders, cancellations, closes, leverage, size, and builder-fee approval.

Risk: The HYPELENS_AGENT_PK environment variable can grant trading authority if exposed or overfunded.

Mitigation: Use a narrowly funded agent wallet for HYPELENS_AGENT_PK and do not expose any master-wallet private key.

Risk: The release depends on unpinned external code executed through npx.

Mitigation: Verify the MCP package source and version before installation or live trading use.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/polyparlay/skills/hyperliquid-place)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands, environment variable guidance, and MCP tool examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires npx; optional environment variables include HYPELENS_NET, HYPELENS_AGENT_PK, and HYPELENS_FEED_URL.]

## Skill Version(s):

1.3.11 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
