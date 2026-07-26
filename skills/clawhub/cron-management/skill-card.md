## Description: <br>
Manage OpenClaw cron jobs \u2014 list, pause, resume, maintenance mode, and health checks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[space-cadet](https://clawhub.ai/user/space-cadet) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to inspect, pause, resume, and troubleshoot OpenClaw cron jobs without manually editing raw cron JSON. It is also useful for adding maintenance-mode checks to shell, Python, Node.js, and agentTurn cron payloads. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Bulk pause or resume operations can affect every OpenClaw cron job, including jobs that were intentionally disabled before maintenance. <br>
Mitigation: Run list or status before bulk operations, and prefer pause or resume for a single named job when the target is important. <br>
Risk: Maintenance mode uses a /tmp/cron-paused flag, so jobs only skip reliably when their payloads include the documented maintenance check. <br>
Mitigation: Add the maintenance-mode check to new cron payloads and roll it out incrementally to existing shell, Python, Node.js, and agentTurn jobs. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/space-cadet/skills/cron-management) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with shell commands and shell, Python, JavaScript, and agentTurn snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes a Bash CLI entrypoint that invokes OpenClaw cron commands and jq for JSON inspection.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and artifact _meta.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
