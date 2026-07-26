## Description: <br>
股海罗盘 helps agents collect A-share market data, run quantitative stock analysis, summarize historical signal matching and patterns, and generate DOCX reports with charts. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[sunbinpy](https://clawhub.ai/user/sunbinpy) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this skill to gather public A-share market data, request quantitative signal summaries, review broker research and ETF flow context, and generate stock-analysis reports. It is intended for historical data review and report drafting, not investment advice or guaranteed future-price prediction. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill exposes a local API key in generated links and logs. <br>
Mitigation: Use only isolated test environments with disposable credentials until API keys are removed from URLs, logs, transcripts, reports, and browser history. <br>
Risk: The security scan reports hardcoded database credentials. <br>
Mitigation: Do not deploy in a normal workspace until the publisher removes embedded credentials and replaces them with documented, revocable secret handling. <br>
Risk: The skill performs network calls and writes local configuration, data, chart, and DOCX report files. <br>
Mitigation: Review and constrain network access and filesystem writes before use; require clear documentation of all external endpoints and created files. <br>
Risk: Stock-analysis output may be mistaken for investment advice. <br>
Mitigation: Keep the historical-data disclaimer visible and review generated text so it does not present recommendations, price predictions, or buy/sell/hold guidance. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/sunbinpy/skills/gh-data) <br>
- [Publisher profile](https://clawhub.ai/user/sunbinpy) <br>
- [Product homepage](https://www.oraskl.com/ghdata-admin) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, files] <br>
**Output Format:** [Markdown analysis text, Python snippets or shell commands, configuration JSON, DOCX reports, and chart image files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs may include historical market statistics, signal summaries, generated purchase links, DOCX report paths, and chart image paths.] <br>

## Skill Version(s): <br>
2.2.44 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
