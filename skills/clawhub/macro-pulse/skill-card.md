## Description: <br>
宏观脉搏 is a daily macroeconomic monitoring skill that checks public data and news sources, summarizes macro releases and policy updates from the past 24 hours, explains indicators for non-specialists, and sends a report. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users such as investors, analysts, financial content creators, and strategy or risk teams use this skill to monitor macroeconomic data and policy developments, receive plain-language explanations, and identify notable surprises or source failures. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may run as an automated daily browsing agent and send reports to external IM, email, or webhook targets. <br>
Mitigation: Use explicit manual triggering or an opt-in schedule, and configure delivery targets deliberately before enabling recurring pushes. <br>
Risk: The skill may modify local reference or report files while updating source health, indicator explanations, or failed-delivery reports. <br>
Mitigation: Run it in an isolated workspace and review generated file changes before reusing them in future runs. <br>
Risk: Macro and financial summaries can be stale, incomplete, or affected by source outages and fallback data. <br>
Mitigation: Review source health notes, prefer official sources for important values, and treat the output as informational rather than financial advice. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/macro-pulse) <br>
- [Trading Economics economic calendar](https://tradingeconomics.com/calendar) <br>
- [FRED releases](https://fred.stlouisfed.org/releases) <br>
- [National Bureau of Statistics of China](http://www.stats.gov.cn/) <br>
- [People's Bank of China](http://www.pbc.gov.cn/) <br>
- [China Securities Regulatory Commission](http://www.csrc.gov.cn/) <br>
- [FRED API key documentation](https://fred.stlouisfed.org/docs/api/api_key.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown macroeconomic report with source health notes, indicator explanations, alerts, and optional delivery or scheduling configuration.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May write source-health or report files and may send reports through IM, email, or webhook when configured.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence and artifact frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
