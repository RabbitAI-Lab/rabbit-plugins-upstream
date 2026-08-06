## Description: <br>
Analyze mutual fund performance, holdings, risk metrics, and investment suitability. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[paudyyin](https://clawhub.ai/user/paudyyin) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Investors, analysts, and agents use this skill to generate Chinese fund market reports, compare fund and A-share market data, and summarize fundamentals, technical indicators, industry flows, and macroeconomic signals. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may fetch financial data from third-party public data providers whose availability, latency, and freshness can vary. <br>
Mitigation: Confirm the data timestamp, retry or downgrade data sources as documented, and verify important figures against the original provider before use. <br>
Risk: Generated market and fund analysis could be mistaken for investment advice. <br>
Mitigation: Treat outputs as informational analysis only and require independent review before making investment decisions. <br>
Risk: Using the skill may require installing financial data packages such as akshare and pywencai. <br>
Mitigation: Review package sources and install dependencies only in an approved environment. <br>


## Reference(s): <br>
- [ClawHub fund-analysis skill page](https://clawhub.ai/paudyyin/skills/fund-analysis) <br>
- [Eastmoney fund data](https://fund.eastmoney.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown reports with tables, code snippets, shell commands, and explanatory guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Financial analysis is informational and depends on third-party public data provider availability and freshness.] <br>

## Skill Version(s): <br>
1.1.0 (source: SKILL.md frontmatter, package.json, release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
