## Description:

Self-custody wallet setup for Simmer agents that bring an external key, import a funded Polymarket wallet, or connect an existing dashboard-registered agent to a local runtime.

This skill is ready for commercial/non-commercial use.

## Publisher:

[simmer](https://clawhub.ai/user/simmer)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and agent operators use this skill to configure Simmer trading agents with API keys, local signing wallets, approvals, and verification for Polymarket or Kalshi self-custody flows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A leaked raw private key or API key could let an agent or attacker control a funded trading wallet.

Mitigation: Use OWS or another scoped key store when possible, set secrets only in the agent host environment, and treat any shared key as compromised.

Risk: Approvals and cached trading credentials can allow automated agents to place or exit real-money positions.

Mitigation: Install only for agents intended to control funded trading wallets and review Simmer dashboard auto risk monitor settings before polling get_briefing.

## Reference(s):

- [Simmer Wallet Docs](https://docs.simmer.markets/wallets)
- [Polymarket Wallet Import](https://docs.simmer.markets/polymarket-import)
- [V2 Migration Guide](https://docs.simmer.markets/v2-migration)
- [Open Wallet Standard](https://openwallet.sh)
- [Simmer Dashboard](https://simmer.markets/dashboard?ref=sdk-skill&utm_campaign=sdk-skill)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline Python and shell code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SIMMER_API_KEY and may use WALLET_PRIVATE_KEY or OWS_WALLET for self-custody signing.]

## Skill Version(s):

0.4.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
