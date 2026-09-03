## Description:

Provides A-share market data, quantitative screening, backtesting, Tonghuashun iFinD, AI4Trade, and constrained multi-agent investment research tools.

This skill is ready for commercial/non-commercial use.

## Publisher:

[frontier-ai-vl](https://clawhub.ai/user/frontier-ai-vl)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agent developers use this skill for A-share market review, stock screening, technical snapshots, lightweight backtests, factor research, portfolio notes, alerts, AI4Trade workflows, and multi-agent investment research. Outputs are for research, simulation, and local recordkeeping, not broker execution or investment advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Finance outputs could be mistaken for investment advice or reliable predictions.

Mitigation: Treat all outputs as research and simulation; independently verify data, assumptions, costs, liquidity, and risk before making decisions.

Risk: The skill can contact external finance, AI, and platform services when configured with host-provided credentials.

Mitigation: Provide tokens only through the host environment or secret manager, review configured providers, and run status checks before workflows that use external services.

Risk: Confirmed AI4Trade actions can publish content or change platform state.

Mitigation: Require explicit approval for each state-changing AI4Trade action and review generated content before confirming.

Risk: Backtests, factor studies, and technical indicators may omit real-world execution constraints or rely on limited public data.

Mitigation: Use out-of-sample checks, random controls, and independent review; account for slippage, fees, suspensions, survivorship bias, and unavailable historical constituents.

## Reference(s):

- [Usage Examples](references/usage-examples.md)
- [ClawHub Skill Page](https://clawhub.ai/frontier-ai-vl/skills/stock-screener-pro)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Structured tool responses and Markdown guidance with occasional shell command snippets.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include market data snapshots, screened candidate lists, backtest metrics, factor research summaries, local portfolio or alert records, and confirmation prompts for external AI or AI4Trade state-changing actions.]

## Skill Version(s):

3.7.1 (source: server evidence release.version and LOCAL_PATCHES.md)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
