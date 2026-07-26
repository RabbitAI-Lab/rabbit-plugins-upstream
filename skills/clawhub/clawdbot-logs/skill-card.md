## Description: <br>
Analyze Clawdbot logs and diagnostics. Use when the user asks about bot performance, response times, errors, session stats, token usage, API costs, or wants to debug slow responses. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[satriapamudji](https://clawhub.ai/user/satriapamudji) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and operators use this skill to inspect local Clawdbot logs, session statistics, token usage, API costs, gateway status, and response timing when debugging performance or errors. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can surface local log and session data that may include conversation text, identifiers, token usage, costs, and tool details. <br>
Mitigation: Review and redact diagnostic output before sharing it outside the local troubleshooting context. <br>
Risk: The skill relies on local journal and session files, so results may expose private operational state from the Clawdbot environment. <br>
Mitigation: Install and run it only in environments where agent access to local Clawdbot diagnostics is acceptable. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/satriapamudji/skills/clawdbot-logs) <br>
- [ClawHub publisher profile](https://clawhub.ai/user/satriapamudji) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown with inline shell commands and diagnostic summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include local log excerpts, session identifiers, token counts, cost data, and gateway status when the agent runs the documented commands.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
