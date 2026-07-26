## Description: <br>
Industry Research v1.3.2 helps an agent collect market, commodity, equity, ETF, technical, valuation, institutional-flow, and news signals and assemble structured industry research reports. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[whitertigerwilson](https://clawhub.ai/user/whitertigerwilson) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and analysts use this skill to produce Chinese-market industry, commodity, ETF, and public-equity research workflows. It is intended to gather public market data, run local CLI analysis, and draft structured reports for human review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill routes research queries to external search and market-data services, including Bocha, Bing, Eastmoney, Tencent, akshare-backed sources, and yfinance. <br>
Mitigation: Use only non-sensitive research queries and review generated reports before relying on them. <br>
Risk: The release describes a workflow that works around disabled platform web_search controls. <br>
Mitigation: Review the search workflow before installation and remove or disable the bypass behavior if it conflicts with local policy. <br>
Risk: The API-key checker can print API-key prefixes in terminal output. <br>
Mitigation: Avoid running the checker in shared or logged sessions, and update it to report only whether keys are present. <br>
Risk: The skill can create local archives and HTML reports under the user's OpenClaw workspace. <br>
Mitigation: Periodically inspect and delete archives and reports, especially after researching confidential or sensitive topics. <br>


## Reference(s): <br>
- [Industry Research Skill Page](https://clawhub.ai/whitertigerwilson/skills/industry-research) <br>
- [Publisher Profile](https://clawhub.ai/user/whitertigerwilson) <br>
- [Industry Research Reference Manual](artifact/references/research_manual.md) <br>
- [Bocha Web Search API](https://api.bochaai.com/v1/web-search) <br>
- [Bing Search](https://www.bing.com/search) <br>
- [Eastmoney Quotes](https://quote.eastmoney.com/) <br>
- [Tencent Quote API](https://qt.gtimg.cn/) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, HTML files, Shell commands, Guidance] <br>
**Output Format:** [Markdown research reports, JSON search results, HTML report files, and terminal output from CLI commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create local archives and report files under the user's OpenClaw workspace.] <br>

## Skill Version(s): <br>
1.3.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
