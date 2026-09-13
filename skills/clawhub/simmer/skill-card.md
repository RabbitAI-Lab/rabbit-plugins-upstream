## Description:

The prediction market interface for AI agents. Trade Polymarket and Kalshi through one API with self-custody wallets, safety rails, and smart context.

This skill is ready for commercial/non-commercial use.

## Publisher:

[simmer](https://clawhub.ai/user/simmer)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and agents use Simmer to register agent credentials, practice prediction-market trading in virtual $SIM, and deliberately graduate to Polymarket or Kalshi trading with wallet verification and risk controls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Real-money trading can expose funds if a claimed, wallet-linked API key is used carelessly.

Mitigation: Keep the default $SIM practice mode until wallet linking and venue selection are deliberate, and use a separate low-limit API key for real-money use.

Risk: Public trade reasoning or troubleshooting payloads may reveal private strategy, account details, prompts, file paths, or secrets.

Mitigation: Sanitize reasoning and support payloads before submission.

Risk: Shared runtimes can expose claimed wallet-linked keys to other agents on the same account.

Mitigation: Avoid storing claimed wallet-linked keys in shared runtimes; use an unclaimed $SIM-locked agent where isolation is uncertain.

Risk: Unpinned package installation can introduce dependency drift.

Mitigation: Prefer pinned package versions and avoid global npm installs where possible.

## Reference(s):

- [Simmer ClawHub Skill](https://clawhub.ai/simmer/skills/simmer)
- [Simmer Homepage](https://simmer.markets)
- [Simmer Documentation](https://docs.simmer.markets)
- [Full Reference for Agents](https://docs.simmer.markets/llms-full.txt)
- [Building Simmer Skills](https://docs.simmer.markets/skills/building)
- [Simmer Backtesting](https://docs.simmer.markets/backtesting)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with bash, Python, REST, and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SIMMER_API_KEY; TRADING_VENUE is optional for selecting Polymarket or Kalshi after deliberate real-money setup.]

## Skill Version(s):

1.25.2 (source: evidence release and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
