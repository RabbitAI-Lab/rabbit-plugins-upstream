## Description:

Provides guidance for using OKX CLI news, sentiment, and macro-economic calendar commands for crypto market intelligence; requires OKX API credentials.

This skill is ready for commercial/non-commercial use.

## Publisher:

[searchworld](https://clawhub.ai/user/searchworld)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to map crypto news, sentiment, social trend, and macro-economic calendar requests to OKX CLI commands and structured briefings. It supports read-only market intelligence workflows and may combine OKX results with market data or web search when coverage is sparse.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Use with OKX account credentials can expose live-profile context to the agent.

Mitigation: Review the skill before installation, configure only the intended OKX profile, and run live-profile workflows only when that access is expected.

Risk: Some workflows may read positions and balances and produce personalized trading-risk suggestions.

Mitigation: Use portfolio-aware workflows only by explicit user intent, treat the output as decision support, and require separate user confirmation before any trading action.

Risk: The news module does not support demo mode, so testing may require live-profile credentials.

Mitigation: Confirm live credential use before setup and avoid switching from demo credentials unless the user accepts live-profile access.

## Reference(s):

- [Cross-Skill Workflows & MCP Tool Reference](references/workflows.md)
- [OKX homepage](https://www.okx.com)
- [ClawHub skill page](https://clawhub.ai/searchworld/skills/okx-sentiment-tracker)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands, tables, and optional JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires the okx CLI and OKX API credentials; commands are described as read-only, while some workflows can use live-profile account context.]

## Skill Version(s):

1.4.8 (source: server release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
