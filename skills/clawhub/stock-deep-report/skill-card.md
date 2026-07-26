## Description: <br>
Generates a single-page HTML stock analysis report for A-share, Hong Kong, and US equities across fundamentals, news, capital flows, technical indicators, valuation, peer comparison, and ownership. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[songxf1024](https://clawhub.ai/user/songxf1024) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Investors, analysts, and agent users use this skill to gather public-market data and produce a printable HTML deep-dive report for a specified stock. The workflow supports A-share, Hong Kong, and US equities and includes source notes and risk disclosures in the generated report. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated HTML can contain active browser code if untrusted web or JSON text is rendered without complete escaping. <br>
Mitigation: Review generated HTML before opening or sharing it, prefer a fixed version that escapes every JSON field before rendering, and confirm before allowing persistent memory updates about stocks or generated reports. <br>
Risk: Market data, news, ratings, and generated commentary can be incomplete, stale, or unsuitable for a user's financial decision. <br>
Mitigation: Verify material facts against cited market sources, keep the report's non-investment-advice disclaimer, and require human review before relying on the report. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/songxf1024/skills/stock-deep-report) <br>
- [Stock data JSON template](references/json_template.md) <br>
- [HTML report renderer](references/build.py) <br>
- [Eastmoney quote page template](https://quote.eastmoney.com/{market}{code}.html) <br>
- [Eastmoney F10 data page template](https://emweb.securities.eastmoney.com/pc_hsf10/pages/index.html?type=web&code={market}{code}) <br>
- [Eastmoney stock research report template](https://data.eastmoney.com/report/stock/{code}.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, code, shell commands, configuration, guidance] <br>
**Output Format:** [HTML report generated from structured JSON, with supporting Markdown instructions and Python command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces workspace-local stock_data.json and an HTML report; requires review of generated HTML before use.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
