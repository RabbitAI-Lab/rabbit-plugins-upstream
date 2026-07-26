## Description: <br>
Generates a structured Markdown daily review of A-share market activity using TDX market data, westock-data, and web cross-checks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jlfan966-tech](https://clawhub.ai/user/jlfan966-tech) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and market analysts use this skill after A-share trading sessions to generate a daily recap report with index movement, limit-up and limit-down statistics, sector rotation, volume leaders, news context, and beginner-oriented strategy notes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Market data and web-sourced context may be unavailable, stale, or inconsistent across providers. <br>
Mitigation: Review the generated data-check section and verify important market figures before relying on the report. <br>
Risk: Beginner strategy notes and position sizing are non-personalized financial commentary. <br>
Mitigation: Treat generated suggestions as informational only and review them against the user's own investment constraints. <br>
Risk: The skill saves generated reports to a stated local Windows path. <br>
Mitigation: Install only when that file write behavior is expected and the target path is appropriate for the user's environment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/jlfan966-tech/skills/a-stock-daily-review-a) <br>
- [Server-resolved GitHub provenance](https://github.com/jlfan966-tech/a-stock-daily-review-a-) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Text, Files, Guidance] <br>
**Output Format:** [Markdown report file plus concise text summary] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Saves the daily recap to the configured local Windows path when generation succeeds.] <br>

## Skill Version(s): <br>
0.1.0 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
