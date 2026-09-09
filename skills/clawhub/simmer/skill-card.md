## Description:

The prediction market interface for AI agents. Trade Polymarket and Kalshi through one API with self-custody wallets, safety rails, and smart context.

This skill is ready for commercial/non-commercial use.

## Publisher:

[simmer](https://clawhub.ai/user/simmer)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to register agents with Simmer, practice prediction-market trading in the simulated $SIM venue, and graduate deliberately to Polymarket or Kalshi workflows with documented safety rails.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Agents can interact with prediction markets, including real-money venues after explicit graduation.

Mitigation: Keep the default $SIM practice mode until ready, require human wallet verification before real-money trading, and start with small capped trades.

Risk: Trading credentials may expose wallet-linked capabilities if stored in shared or reused runtimes.

Mitigation: Use a narrowly scoped SIMMER_API_KEY, avoid shared runtimes for wallet-linked keys, and keep unclaimed practice agents on shared machines.

Risk: The runtime dependency is an unpinned simmer-sdk package.

Mitigation: Install a pinned or otherwise verified simmer-sdk version in an isolated virtual environment.

Risk: Trade reasoning may be publicly visible on Simmer trade pages.

Mitigation: Review reasoning text before trades and avoid including confidential or sensitive information.

## Reference(s):

- [Simmer homepage](https://simmer.markets)
- [Simmer documentation](https://docs.simmer.markets)
- [Full Simmer reference for agents](https://docs.simmer.markets/llms-full.txt)
- [Simmer skill page](https://clawhub.ai/simmer/skills/simmer)
- [Simmer wallet setup skill](https://clawhub.ai/skills/simmer-wallet-setup)
- [Simmer MCP setup skill](https://clawhub.ai/skills/simmer-mcp-setup)
- [Building Simmer skills](https://docs.simmer.markets/skills/building)
- [Simmer backtesting](https://docs.simmer.markets/backtesting)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, Python code examples, REST examples, and configuration notes.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SIMMER_API_KEY. TRADING_VENUE can optionally select Polymarket or Kalshi instead of the default simulated venue.]

## Skill Version(s):

1.25.2 (source: server release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
