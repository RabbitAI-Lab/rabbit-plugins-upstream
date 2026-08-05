## Description: <br>
Fetches Chinese financial-market data and research information across A-shares, Hong Kong stocks, funds, indices, financials, announcements, research reports, news, macroeconomic datasets, and 200+ APIs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kenneth-bro](https://clawhub.ai/user/kenneth-bro) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External agents, developers, and finance researchers use this skill to find and fetch structured Chinese market data for quotes, funds, indices, company financials, announcements, research reports, sector analysis, macro data, and downstream analysis. It is a data-retrieval and research aid, not an investment advisor, trading executor, or automated trading system. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The setup flow includes an auto-update path that can change the CLI and installed skills through a background scheduled task. <br>
Mitigation: Prefer initialization without auto-update unless background updates are intentional, and review installed updates before relying on the skill. <br>
Risk: Some finance reference examples are unreliable or may not match current data behavior. <br>
Mitigation: Verify financial outputs against primary sources before using them for research conclusions or downstream reports. <br>
Risk: Financial data retrieval can be mistaken for investment advice or trading automation. <br>
Mitigation: Use the skill only for data retrieval and research support; do not use it for direct buy or sell advice, automated order placement, or automated trading decisions. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/kenneth-bro/skills/investoday-finance-data) <br>
- [English API Reference Index](docs/references-index.en.md) <br>
- [Chinese API Reference Index](docs/references-index.md) <br>
- [A-share Realtime Quotes](references/沪深京数据/股票行情/实时行情.md) <br>
- [Financial Statement Data](references/沪深京数据/财务数据/三大报表当期数据.md) <br>
- [Announcements](references/公告.md) <br>
- [Research Report Basics](references/研报/基础数据.md) <br>
- [Macro Data](references/宏观经济/国内宏观.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, API calls, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and structured CLI/API responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Node.js 18+, network access, and @investoday/investoday-api; results depend on API permissions, available endpoints, and data coverage.] <br>

## Skill Version(s): <br>
1.8.58 (source: SKILL.md frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
