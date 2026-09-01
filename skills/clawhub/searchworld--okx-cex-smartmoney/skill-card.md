## Description:

Provides OKX Smart Money analytics for leaderboard traders, trader performance, positions, trade history, closed-position history, aggregated consensus signals, and signal trends.

This skill is ready for commercial/non-commercial use.

## Publisher:

[searchworld](https://clawhub.ai/user/searchworld)

### License/Terms of Use:

MIT-0

## Use Case:

External users, trading analysts, and agent developers use this skill through the OKX CLI to inspect Smart Money leaderboards, analyze trader activity, and summarize aggregated long/short consensus signals.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill connects to an OKX account for live read-only analytics, which can expose account context if credentials are handled poorly.

Mitigation: Use OAuth or least-privilege credentials on a dedicated sub-account when possible, and do not paste API keys or secrets into chat.

Risk: Smart Money signal aggregation covers USDT- and USDS-margined instruments only, so coin-margined exposure can be absent from consensus signals.

Mitigation: Cross-check a trader's full position book with trader-position commands when complete exposure matters.

## Reference(s):

- [OKX Homepage](https://www.okx.com)
- [ClawHub Skill Page](https://clawhub.ai/searchworld/skills/okx-cex-smartmoney)
- [Signal Commands Reference](artifact/references/signal-commands.md)
- [Trader Commands Reference](artifact/references/trader-commands.md)
- [Smart Money Workflows](artifact/references/workflows.md)
- [Templates and Formatting Reference](artifact/references/templates.md)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, Guidance]

**Output Format:** [Markdown tables with inline shell commands and concise explanatory text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses JSON CLI responses as source data; commands are read-only and require authenticated OKX access.]

## Skill Version(s):

1.4.5 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
