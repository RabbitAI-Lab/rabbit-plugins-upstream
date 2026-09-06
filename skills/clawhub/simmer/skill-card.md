## Description:

The prediction market interface for AI agents. Trade Polymarket and Kalshi through one API with self-custody wallets, safety rails, and smart context.

This skill is ready for commercial/non-commercial use.

## Publisher:

[simmer](https://clawhub.ai/user/simmer)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and agent operators use this skill to register an agent with Simmer, practice prediction-market trading in $SIM, and intentionally graduate to Polymarket or Kalshi trading with human verification and wallet setup.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires access to a Simmer API key and trading workflows.

Mitigation: Install only when the operator is comfortable granting that access, keep real-money trading disabled until human verification and wallet linking are intentional, and avoid setting TRADING_VENUE unless a real venue is intended.

Risk: Troubleshooting reports may expose secrets, wallet or account identifiers, private strategy details, or conversation context.

Mitigation: Review and redact troubleshooting content before sending it to Simmer.

Risk: SDK behavior can change across releases.

Mitigation: Pin or review the simmer-sdk version where possible before relying on the skill in trading workflows.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/simmer/skills/simmer)
- [Simmer Homepage](https://simmer.markets)
- [Simmer Documentation](https://docs.simmer.markets)
- [Full Reference for Agents](https://docs.simmer.markets/llms-full.txt)
- [Simmer Wallet Setup Skill](https://clawhub.ai/skills/simmer-wallet-setup)
- [Simmer MCP Setup Skill](https://clawhub.ai/skills/simmer-mcp-setup)
- [Building Simmer Skills](https://docs.simmer.markets/skills/building)
- [Simmer Backtesting](https://docs.simmer.markets/backtesting)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline bash, Python, and REST examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SIMMER_API_KEY and the simmer-sdk package; optional TRADING_VENUE changes the default venue for real-money trades.]

## Skill Version(s):

1.25.1 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
