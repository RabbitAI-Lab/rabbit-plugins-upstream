## Description: <br>
Track, aggregate, and report OpenClaw token usage and costs across sessions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[space-cadet](https://clawhub.ai/user/space-cadet) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to inspect OpenClaw session token usage, estimate costs, compare usage over time, and export reports for budget monitoring. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill reads local OpenClaw session logs, which may contain sensitive usage metadata or message context. <br>
Mitigation: Install and run it only where local session-log access is acceptable, and prefer standard report commands for lower exposure. <br>
Risk: The --by-cron option inspects the first user message in matching sessions to identify cron jobs. <br>
Mitigation: Avoid --by-cron for sensitive sessions unless first-message inspection is acceptable. <br>
Risk: The pricing updater contacts OpenRouter to refresh model price data. <br>
Mitigation: Run update-pricing.py only when external price lookup is intended. <br>
Risk: Cost reports are estimates and may differ from actual provider billing. <br>
Mitigation: Use estimates for monitoring and anomaly detection, and compare against provider billing records for financial decisions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/space-cadet/skills/token-usage) <br>
- [Project homepage](https://github.com/space-cadet/openclaw-token-usage) <br>
- [OpenRouter models API](https://openrouter.ai/api/v1/models) <br>
- [Kimi pricing documentation](https://platform.kimi.com/docs/pricing/) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, guidance] <br>
**Output Format:** [Markdown-like terminal summaries or JSON reports, with shell commands in the skill guidance.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Reports can include date, model, session, cron job, token count, and estimated cost fields.] <br>

## Skill Version(s): <br>
2.3.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
