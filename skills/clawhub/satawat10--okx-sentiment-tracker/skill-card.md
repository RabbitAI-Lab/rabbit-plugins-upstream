## Description:

Provides OKX CLI workflows for crypto news aggregation, coin sentiment analysis, social trend data, and macro-economic calendar queries using live API credentials.

This skill is ready for commercial/non-commercial use.

## Publisher:

[satawat10](https://clawhub.ai/user/satawat10)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to ask an agent for cryptocurrency news briefings, coin sentiment snapshots, social trend analysis, source-filtered news, and macro-economic calendar checks through the OKX CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill relies on OKX live API credentials and may include workflows that inspect account positions or balances.

Mitigation: Use a dedicated least-privilege read-only API key, avoid secrets in shell commands, consider isolated installation, and review any workflow requesting account data before allowing access.

## Reference(s):

- [Cross-Skill Workflows and MCP Tool Reference](references/workflows.md)
- [OKX](https://www.okx.com)
- [ClawHub skill page](https://clawhub.ai/satawat10/skills/okx-sentiment-tracker)
- [Publisher profile](https://clawhub.ai/user/satawat10)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown responses with inline shell commands and optional JSON CLI output.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May rely on live OKX API credentials and external OKX CLI availability.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
