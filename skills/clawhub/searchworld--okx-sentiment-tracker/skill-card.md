## Description:

Provides agent guidance for read-only OKX crypto news aggregation, coin sentiment analysis, social trend checks, and macro-economic calendar queries through the OKX CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[searchworld](https://clawhub.ai/user/searchworld)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to route crypto news, sentiment, social buzz, and economic-calendar requests to the appropriate read-only OKX CLI commands and to format the results as market briefings or analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Live OKX credential use can expose sensitive account access if credentials are over-scoped or entered directly in chat or command lines.

Mitigation: Use read-only, least-privilege API keys, configure credentials outside chat, and review the skill before installation in live-account environments.

Risk: Account-position and trading-impact workflows may be treated as financial decision support.

Mitigation: Require explicit user consent before account-aware analysis and keep any position or TP/SL discussion advisory unless the user separately confirms an action.

Risk: Economic-calendar queries have counterintuitive time-window semantics and sparse or empty results can mislead users.

Mitigation: Use both time bounds for future windows, respect the documented rate limit, and clearly report when results are sparse or supplemented from web search.

## Reference(s):

- [Cross-Skill Workflows & MCP Tool Reference](references/workflows.md)
- [OKX](https://www.okx.com)
- [ClawHub Skill Page](https://clawhub.ai/searchworld/skills/okx-sentiment-tracker)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and optional JSON CLI output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include OKX CLI command sequences, report tables, source labels, and fallback guidance for sparse results.]

## Skill Version(s):

1.4.4 (source: server evidence and artifact metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
