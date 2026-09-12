## Description:

Watchdog for this OpenClaw agent: report run start/end, evidence and cost to RunVouch so missed runs, loops and runaway spend alert you on Telegram.

This skill is ready for commercial/non-commercial use.

## Publisher:

[runvouch](https://clawhub.ai/user/runvouch)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators of unattended OpenClaw agents use this skill to report run status, heartbeats, tool calls, costs, and outcome evidence to RunVouch for monitoring and alerting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill instructs agents to send exact tool inputs to an external RunVouch service, which can expose secrets, customer data, private prompts, credentials, or proprietary code.

Mitigation: Use only in environments where telemetry contents are approved for external reporting, or modify the integration to redact or hash sensitive tool inputs before sending them.

Risk: The release security verdict is suspicious because detailed agent telemetry is disclosed as part of normal operation.

Mitigation: Review data-handling requirements, network access, and the RunVouch service relationship before enabling this skill in production workflows.

## Reference(s):

- [RunVouch](https://runvouch.com)
- [RunVouch API](https://api.runvouch.com)
- [RunVouch MCP](https://api.runvouch.com/mcp)
- [ClawHub Skill Page](https://clawhub.ai/runvouch/skills/runvouch)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, API Calls]

**Output Format:** [Markdown with inline shell commands and JSON request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Instructs agents to send run telemetry, tool-call details, cost values, heartbeats, and outcome evidence to RunVouch.]

## Skill Version(s):

0.1.0 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
