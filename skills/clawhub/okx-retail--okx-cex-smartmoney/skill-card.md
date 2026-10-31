## Description:

Provides OKX smart money analytics, including trader rankings, position and trade histories, and aggregated market signals.

This skill is ready for commercial/non-commercial use.

## Publisher:

[okx-retail](https://clawhub.ai/user/okx-retail)

### License/Terms of Use:

MIT

## Use Case:

Traders and market analysts use this skill to review OKX leaderboard performance, inspect selected traders' positions and histories, and summarize smart money signals for chosen assets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The required credential check can expose saved OKX account secrets to the agent.

Mitigation: Replace the full configuration dump with a check that returns only authentication status and the selected profile; use read-only credentials, verify the CLI version, and obtain the missing shared preflight instructions.

## Reference(s):

- [Trader Commands Reference](artifact/references/trader-commands.md)
- [Signal Commands Reference](artifact/references/signal-commands.md)
- [Smart Money Workflows](artifact/references/workflows.md)
- [Templates and Formatting Reference](artifact/references/templates.md)
- [OKX](https://www.okx.com)
- [ClawHub Skill Release](https://clawhub.ai/okx-retail/skills/okx-cex-smartmoney)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown tables with concise analytical summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only analytics; signal aggregation covers linear contracts only.]

## Skill Version(s):

1.5.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
