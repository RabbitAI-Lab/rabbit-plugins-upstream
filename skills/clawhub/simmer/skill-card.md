## Description:

The prediction market interface for AI agents. Trade Polymarket and Kalshi through one API with self-custody wallets, safety rails, and smart context.

This skill is ready for commercial/non-commercial use.

## Publisher:

[simmer](https://clawhub.ai/user/simmer)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external agent operators use Simmer to register an agent, connect it to Simmer's prediction-market API, practice with virtual $SIM, and graduate deliberately toward Polymarket or Kalshi trading with human verification and safety caps.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An agent connected to Simmer can progress from virtual practice to real-money prediction-market trading.

Mitigation: Keep the agent unclaimed or on $SIM practice until real-money use is intended; require human claim_url verification and wallet linking before live trading.

Risk: Setting TRADING_VENUE to Polymarket or Kalshi changes the default target for real-money trades.

Mitigation: Do not set TRADING_VENUE casually; prefer explicit per-trade venue selection after the operator has reviewed caps, wallet status, and strategy readiness.

Risk: Trade reasoning may be publicly visible and can expose sensitive strategy details or user intent.

Mitigation: Write concise reasoning that supports accountability without including secrets, private user data, or confidential strategy information.

Risk: The skill requires installing and using the third-party simmer-sdk package.

Mitigation: Treat package installation like any third-party SDK dependency and review it under the deployment environment's normal dependency controls.

Risk: Dry-run previews do not fully enforce live account limits and may not match executable Polymarket pricing.

Mitigation: Use dry_run only for sizing checks, read account settings before live orders, and use real-venue paper mode with modeled spread when rehearsing strategies.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/simmer/skills/simmer)
- [Simmer Homepage](https://simmer.markets)
- [Simmer Documentation](https://docs.simmer.markets)
- [Full Reference for Agents](https://docs.simmer.markets/llms-full.txt)
- [Build Simmer Skills](https://docs.simmer.markets/skills/building)
- [Simmer Backtesting](https://docs.simmer.markets/backtesting)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown with inline bash and Python code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SIMMER_API_KEY; optional TRADING_VENUE changes the default real-money venue.]

## Skill Version(s):

1.25.0 (source: artifact frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
