## Description: <br>
Fetches Chinese financial-market data and investment research information across A-shares, Hong Kong stocks, funds, indices, financial statements, announcements, research reports, macroeconomics, and related datasets. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kenneth-bro](https://clawhub.ai/user/kenneth-bro) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to retrieve Chinese market data, research information, financial metrics, announcements, reports, macro indicators, and structured datasets for analysis, comparison, and export. It should not be used for direct buy or sell advice, automated trading, or fabricating conclusions when data is unavailable. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The external finance-data CLI may store an API key locally and make network requests to InvestToday. <br>
Mitigation: Use interactive setup where possible, verify the API key source, and avoid using credentials that are broader than needed for the intended research workflow. <br>
Risk: The non-interactive init example includes --auto-update and --skip-verify, which can enable background updates without enough review. <br>
Mitigation: Prefer interactive initialization, inspect or disable auto-update behavior, and use --skip-verify only when the update and verification tradeoff is intentional. <br>
Risk: Financial data can be incomplete, unavailable, permission-limited, or unsuitable for direct investment decisions. <br>
Mitigation: State data-source, permission, time-range, or endpoint limitations clearly, avoid inventing missing conclusions, and do not present outputs as trading advice or order-execution instructions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/kenneth-bro/skills/investoday-finance-data) <br>
- [API reference index](artifact/docs/references-index.en.md) <br>
- [Chinese API reference index](artifact/docs/references-index.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, JSON] <br>
**Output Format:** [Markdown guidance with CLI commands and structured finance-data responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Node.js 18+, the @investoday/investoday-api package, network access, and local InvestToday API configuration.] <br>

## Skill Version(s): <br>
1.8.56 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
