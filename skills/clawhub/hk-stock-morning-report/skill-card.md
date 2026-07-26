## Description: <br>
Generates a Hong Kong stock market morning report for bank trading desks using market data, news sources, and a fixed report format. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cjlrestlong-ai](https://clawhub.ai/user/cjlrestlong-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Bank trading desk users and supporting agents use this skill to assemble a daily Hong Kong stock market morning report with market review, southbound capital flow, topical news, and one highlighted HK stock. The skill also defines formatting and pre-send checks for WeChat and Feishu distribution. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can send an internal-labeled report to WeChat and Feishu without clear per-send confirmation or recipient scoping. <br>
Mitigation: Require a preview and explicit approval before sending, confirm the exact recipient or group, and ensure the report contains only information approved for those channels. <br>
Risk: Financial report content can become misleading if market data, trading-day status, or news items are stale, incorrect, or unsupported. <br>
Mitigation: Follow the documented source checks, verify trading-day status and cited numbers, and avoid sending until data sources and report formatting pass the pre-send checklist. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/cjlrestlong-ai/skills/hk-stock-morning-report) <br>
- [Stock report format reference](references/stock_report_format.md) <br>
- [Common errors reference](references/errors.md) <br>
- [Tencent Finance API endpoint pattern](https://qt.gtimg.cn/q={code}) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Text, Files, Shell commands, Guidance] <br>
**Output Format:** [Markdown report text with structured Chinese-language sections and optional saved file output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The report is intended for internal-labeled WeChat and Feishu distribution after preview, recipient confirmation, and source checks.] <br>

## Skill Version(s): <br>
1.4.11 (source: frontmatter, changelog, server release) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
