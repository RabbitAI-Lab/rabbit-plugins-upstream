## Description: <br>
Fetches Chinese financial-market data and investment research information across A-shares, Hong Kong stocks, funds, indices, financial statements, announcements, research reports, and macroeconomic datasets. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kenneth-bro](https://clawhub.ai/user/kenneth-bro) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, analysts, and developers use this skill to retrieve and compare structured financial data for China-focused market research, including quotes, fund data, financial statements, announcements, research reports, sectors, themes, and macroeconomic indicators. It should support research workflows and data export, not direct trading advice or order execution. <br>

### Deployment Geography for Use: <br>
Global; data coverage is focused on China and Hong Kong markets. <br>

## Known Risks and Mitigations: <br>
Risk: The CLI requires network access and may require an InvestToday API key. <br>
Mitigation: Install and initialize it only in environments where sharing that API key with the CLI and remote service is acceptable. <br>
Risk: The documented non-interactive initialization path can enable background auto-updates that modify local packages and installed skill files. <br>
Mitigation: Prefer manual initialization and avoid `--auto-update --skip-verify` unless automatic local updates are intentionally allowed. <br>
Risk: Financial data outputs may be mistaken for investment advice. <br>
Mitigation: Use outputs as research data and keep direct buy, sell, order execution, and trading-advice decisions outside the skill. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/kenneth-bro/skills/investoday-finance-data) <br>
- [English reference index](docs/references-index.en.md) <br>
- [Reference index](docs/references-index.md) <br>
- [Basic data reference](references/基础数据.md) <br>
- [Market data reference](references/市场数据.md) <br>
- [Announcements reference](references/公告.md) <br>
- [Research reports reference](references/研报/基础数据.md) <br>
- [Domestic macroeconomics reference](references/宏观经济/国内宏观.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration instructions, API Calls, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and structured CLI output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include finance data returned by the InvestToday CLI; outputs should be treated as research data, not trading advice.] <br>

## Skill Version(s): <br>
1.8.57 (source: SKILL.md frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
