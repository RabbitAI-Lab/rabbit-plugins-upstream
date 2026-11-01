## Description:

Provides OKX Smart Money leaderboard, trader analytics, position tracking, trade-record, closed-position, consensus-signal, and signal-history guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[numpy0001](https://clawhub.ai/user/numpy0001)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to answer user questions about OKX Smart Money traders, rankings, positions, trade history, closed-position performance, and aggregated long/short signals. It helps route read-only OKX CLI queries and format results as human-readable analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks the agent to inspect OKX credential profile and authentication status output.

Mitigation: Use read-only, least-privilege OKX credentials, avoid sharing secrets in chat, and confirm profile/status output redacts sensitive values before use.

Risk: The skill installs and uses a persistent npm OKX CLI for live OKX analytics workflows.

Mitigation: Install only after reviewing the OKX CLI dependency and avoid API keys with trading or withdrawal permissions for this analytics workflow.

## Reference(s):

- [OKX homepage](https://www.okx.com)
- [ClawHub skill page](https://clawhub.ai/numpy0001/skills/okx-cex-smartmoney)
- [Trader Commands Reference](references/trader-commands.md)
- [Signal Commands Reference](references/signal-commands.md)
- [Smart Money Workflows](references/workflows.md)
- [Templates & Formatting Reference](references/templates.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Markdown, Configuration]

**Output Format:** [Markdown responses with inline shell commands and tables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses JSON-formatted OKX CLI command output as input and presents read-only analytics results as Markdown tables.]

## Skill Version(s):

1.3.8 (source: server release metadata; artifact frontmatter and npm package reference list 1.3.7)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
