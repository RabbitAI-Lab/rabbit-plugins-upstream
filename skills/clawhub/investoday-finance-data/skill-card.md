## Description: <br>
Fetches Chinese financial-market data and investment research information across A-shares, Hong Kong stocks, funds, indices, financial statements, announcements, research reports, macroeconomic data, and more than 200 related interfaces. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kenneth-bro](https://clawhub.ai/user/kenneth-bro) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, analysts, and research agents use this skill to find InvestToday finance-data endpoints, fetch structured Chinese market datasets, and summarize available quotes, fundamentals, fund, index, announcement, research, sector, industry-chain, and macroeconomic data. It should support research and data retrieval, not direct buy/sell advice, order execution, or conclusions that require inventing missing data. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: API keys may be exposed when passed directly in shell commands or retained in shell history. <br>
Mitigation: Prefer interactive initialization or environment variables for credentials, and avoid command examples that place API keys directly on the command line. <br>
Risk: The auto-update setup path can later change the CLI or installed skills. <br>
Mitigation: Enable auto-update only when the operator accepts that update behavior, and review updated tools or skills before relying on them. <br>
Risk: Returned finance, personnel, contact, watchlist, and trading-signal data may be sensitive or easy to overinterpret. <br>
Mitigation: Treat returned data as informational, protect sensitive outputs, and avoid presenting results as direct investment advice or trading instructions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/kenneth-bro/skills/investoday-finance-data) <br>
- [English skill guide](artifact/SKILL_EN.md) <br>
- [API reference index](artifact/docs/references-index.en.md) <br>
- [Source skill definition](artifact/SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with CLI commands, parameter guidance, and concise data summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May depend on Node.js 18+, the @investoday/investoday-api package, network access, API credentials, and endpoint-specific permissions.] <br>

## Skill Version(s): <br>
1.8.51 (source: server release evidence and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
