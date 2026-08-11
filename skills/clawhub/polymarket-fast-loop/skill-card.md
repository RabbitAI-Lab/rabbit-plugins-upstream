## Description:

Trade Polymarket BTC 5-minute and 15-minute fast markets using CEX price momentum signals via Simmer API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[simmer](https://clawhub.ai/user/simmer)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and trading operators use this skill to configure and run an agent-managed Polymarket fast-market trading loop using crypto price momentum signals.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Live execution can place real Polymarket orders and expose funds to trading losses.

Mitigation: Start in paper or dry-run mode, use small max-position and daily-budget limits, and enable --live only after reviewing the configuration and wallet setup.

Risk: The security evidence reports account-level redemption behavior that may change financial state even when the user expects read-only operation.

Mitigation: Review or remove the auto_redeem step before treating dry-run as strictly read-only, and run the skill with a wallet funded only for the intended strategy.

Risk: A leaked WALLET_PRIVATE_KEY can compromise the wallet used for live trading.

Mitigation: Keep WALLET_PRIVATE_KEY out of chat logs and shared files, prefer managed-wallet operation when appropriate, and isolate credentials to the runtime environment.

Risk: Sub-15-minute markets may resolve before stop-loss or take-profit monitors can act.

Mitigation: Use conservative sizing and daily budgets because position sizing is the primary risk control for these fast markets.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/simmer/skills/polymarket-fast-loop)
- [Simmer Dashboard](https://simmer.markets/dashboard?ref=sdk-skill&utm_campaign=sdk-skill)
- [Simmer V2 Migration Guide](https://docs.simmer.markets/v2-migration)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands, configuration examples, and command output summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can guide setup, update configuration, report paper-mode opportunities, and execute live order workflows only when configured and invoked for live trading.]

## Skill Version(s):

1.7.3 (source: evidence.release.version and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
