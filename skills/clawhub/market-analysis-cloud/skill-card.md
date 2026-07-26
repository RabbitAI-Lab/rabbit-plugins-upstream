## Description: <br>
每日A股行情研判编排器（纯云端版，无需MCP连接器，无需电脑开机）。分步执行：日历检查、行情数据、新闻简报、持股诊断、自选股分析、ERP计算、组装报告，并上传IMA知识库。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[yyyy10000yyyy](https://clawhub.ai/user/yyyy10000yyyy) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and finance-focused agents use this skill to run a cloud A-share market review workflow, gather market data and news, diagnose holdings and watchlists, calculate ERP, and produce a structured daily report. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The release exposes an API key and depends on external market-data and search services. <br>
Mitigation: Replace the published MX_APIKEY with a securely stored user key before use and review external-service access expectations. <br>
Risk: The skill can read IMA holdings and watchlist content and upload generated reports without a clear per-run consent gate. <br>
Mitigation: Use it only when portfolio-folder access and report upload are intended, and add or require confirmation before holdings access and report upload, especially for scheduled cloud runs. <br>
Risk: Generated finance reports and operation suggestions may be incorrect, stale, or unsuitable for a user's portfolio. <br>
Mitigation: Review market data, assumptions, and recommendations before acting on the report. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/yyyy10000yyyy/skills/market-analysis-cloud) <br>
- [stock-price-query-mx dependency](https://clawhub.ai/skills/stock-price-query-mx) <br>
- [tecent-finance dependency](https://clawhub.ai/skills/tecent-finance) <br>
- [eastmoney-mx-skills-suite dependency](https://clawhub.ai/kooui/skills/eastmoney-mx-skills-suite) <br>
- [china-stock-data dependency](https://longxiaskill.com/skill/china-stock-data) <br>
- [Eastmoney MX API key page](https://ai.eastmoney.com/mxClaw) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown reports and concise text summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces intermediate market, news, portfolio, watchlist, and ERP markdown files before uploading a final IMA knowledge-base report.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
