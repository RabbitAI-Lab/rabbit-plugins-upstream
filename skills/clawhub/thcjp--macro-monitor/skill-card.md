## Description: <br>
Monitors public macroeconomic data and financial-news sources daily, then prepares a concise report of the prior 24 hours for delivery to the user. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent users use this skill to schedule a daily scan of public macroeconomic calendars, central-bank and regulator websites, and financial-news sources, then receive a summarized macro report with plain-language indicator explanations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill is designed for unattended daily runs that browse public websites and send a report. <br>
Mitigation: Review or disable the cron schedule if unattended execution is not desired, and check notification behavior before enabling it. <br>
Risk: Macro reports can be incomplete or stale when public sources are unavailable or publish delayed data. <br>
Mitigation: Treat the output as a monitoring summary, verify important figures against the cited public sources, and review any skipped-source notes. <br>
Risk: The skill may update local indicator explanations when it encounters unfamiliar metrics. <br>
Mitigation: Review changes to local reference material before relying on new explanations in future reports. <br>


## Reference(s): <br>
- [Macro Monitor on ClawHub](https://clawhub.ai/thcjp/skills/macro-monitor) <br>
- [Trading Economics Economic Calendar](https://tradingeconomics.com/calendar) <br>
- [FRED Economic Data Releases](https://fred.stlouisfed.org/releases) <br>
- [National Bureau of Statistics of China](http://www.stats.gov.cn/) <br>
- [People's Bank of China](http://www.pbc.gov.cn/) <br>
- [China Securities Regulatory Commission](http://www.csrc.gov.cn/) <br>
- [CLS](https://www.cls.cn/) <br>
- [WallstreetCN](https://wallstreetcn.com/) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown-style daily report delivered as text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Report content is based on public sources visited by the agent during the scheduled or manual run.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
