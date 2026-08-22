## Description:

The prediction market interface for AI agents. Trade Polymarket and Kalshi through one API with self-custody wallets, safety rails, and smart context.

This skill is ready for commercial/non-commercial use.

## Publisher:

[simmer](https://clawhub.ai/user/simmer)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external agent operators use Simmer to register AI agents, practice prediction-market trading with virtual SIM funds, and deliberately graduate to Polymarket or Kalshi trading after human verification and wallet setup.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An agent can reach real-money prediction-market trading after human verification, wallet linking, and venue configuration.

Mitigation: Keep practice mode as the default until the user deliberately completes verification, links a wallet, and understands dashboard limits.

Risk: Trade reasoning is publicly displayed and may expose sensitive strategy or user context.

Mitigation: Require concise trade reasoning that avoids confidential information before submitting trades.

Risk: Virtual SIM practice fills are synthetic and may understate spread, fees, and depth risks on real venues.

Mitigation: Use backtesting and real-venue paper mode before trading with funds.

Risk: The skill depends on an API key for agent access.

Mitigation: Store SIMMER_API_KEY as a secret and verify it is set correctly before running trading code.

## Reference(s):

- [Simmer homepage](https://simmer.markets)
- [Simmer documentation](https://docs.simmer.markets)
- [Full reference for agents](https://docs.simmer.markets/llms-full.txt)
- [Dashboard and limits](https://simmer.markets/dashboard?ref=sdk-skill&utm_campaign=sdk-skill)
- [Wallet setup skill](https://clawhub.ai/skills/simmer-wallet-setup)
- [MCP setup skill](https://clawhub.ai/skills/simmer-mcp-setup)
- [Building Simmer skills](https://docs.simmer.markets/skills/building)
- [Backtesting](https://docs.simmer.markets/backtesting)
- [ClawHub skill page](https://clawhub.ai/simmer/skills/simmer)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, Configuration]

**Output Format:** [Markdown with inline bash and Python code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SIMMER_API_KEY; optional TRADING_VENUE changes the default trading venue after setup.]

## Skill Version(s):

1.24.11 (source: skill metadata, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
