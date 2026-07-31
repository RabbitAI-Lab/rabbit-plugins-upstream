## Description: <br>
Fetches Chinese financial-market data across A-shares, Hong Kong stocks, funds, indices, market data, financial statements, announcements, research reports, news, real-time quotes, macroeconomics, and related datasets. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kenneth-bro](https://clawhub.ai/user/kenneth-bro) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and analysts use this skill to retrieve and compare Chinese market quotes, company financials, valuation metrics, announcements, research reports, institutional views, sector data, macro indicators, fund data, and structured exports for investment research. It is not intended for direct buy or sell advice, automated trading, order execution, or inventing conclusions when data is unavailable. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: API keys may be exposed through shell history or local setup choices. <br>
Mitigation: Use interactive setup or an environment variable, and avoid placing real API keys directly in command history. <br>
Risk: Verification bypass and automatic updates may change trust assumptions after installation. <br>
Mitigation: Avoid --skip-verify unless the tradeoff is understood, and enable auto-update only when scheduled CLI and skill updates are acceptable. <br>
Risk: Financial examples and returned data may be incomplete, unreliable, permission-limited, or unsuitable for investment decisions. <br>
Mitigation: Treat outputs as research inputs, independently verify investment-relevant information, and do not use the skill for direct trading advice or order execution. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/kenneth-bro/skills/investoday-finance-data) <br>
- [English API Reference Index](docs/references-index.en.md) <br>
- [API Reference Index](docs/references-index.md) <br>
- [Base Data References](references/基础数据.md) <br>
- [Market Data References](references/市场数据.md) <br>
- [Announcement References](references/公告.md) <br>
- [Research Report References](references/研报/基础数据.md) <br>
- [Macro Data References](references/宏观经济/国内宏观.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance, API calls] <br>
**Output Format:** [Markdown guidance with InvestToday CLI commands and structured financial data returned by the API] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Node.js 18+, network access, and the @investoday/investoday-api package; API credentials may be required for data access.] <br>

## Skill Version(s): <br>
1.8.55 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
