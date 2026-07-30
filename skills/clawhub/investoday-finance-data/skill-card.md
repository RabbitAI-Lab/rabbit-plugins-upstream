## Description: <br>
Fetches Chinese financial-market data and investment-research information across A-shares, Hong Kong stocks, funds, indices, financial statements, announcements, research reports, and macroeconomic datasets. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kenneth-bro](https://clawhub.ai/user/kenneth-bro) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and finance researchers use this skill to retrieve, compare, and export structured Chinese market data for research workflows. It supports quote lookup, financial analysis, fund and index research, announcement and report discovery, macroeconomic data review, and sector or industry-chain analysis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The CLI stores a local API key during initialization. <br>
Mitigation: Initialize interactively where possible and manage the API key as a local secret with normal credential-handling controls. <br>
Risk: Initialization with --auto-update can create a user-level background updater that changes the CLI and installed skills. <br>
Mitigation: Prefer interactive initialization or --no-auto-update unless background updates have been reviewed and approved. <br>
Risk: The --skip-verify option reduces setup verification. <br>
Mitigation: Avoid --skip-verify unless the operator understands and accepts the verification tradeoff. <br>
Risk: Trading-signal or investment-value outputs may be mistaken for personalized investment advice. <br>
Mitigation: Treat outputs as research data, clearly state data limitations, and avoid direct buy, sell, or order-execution recommendations. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/kenneth-bro/skills/investoday-finance-data) <br>
- [API Reference Index](docs/references-index.en.md) <br>
- [Chinese API Reference Index](docs/references-index.md) <br>
- [Market Data Reference](references/市场数据.md) <br>
- [A-share Stock Quote References](references/沪深京数据/股票行情/实时行情.md) <br>
- [Fund Data References](references/基金/基金资料/基金概况.md) <br>
- [Macroeconomic Data References](references/宏观经济/国内宏观.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, API calls, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and structured data summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May require Node.js 18+, the @investoday/investoday-api package, network access, and local CLI initialization.] <br>

## Skill Version(s): <br>
1.8.54 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
