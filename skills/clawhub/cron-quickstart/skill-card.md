## Description:

Use the OpenClaw cron tool for scheduling reminders, delayed follow-ups, and recurring periodic checks. Covers one-shot and recurring schedules, session targeting, delivery modes, and wake events.

This skill is ready for commercial/non-commercial use.

## Publisher:

[terrycarter1985](https://clawhub.ai/user/terrycarter1985)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to configure reminders, delayed follow-ups, recurring checks, and session wake events with the OpenClaw cron tool.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Scheduled jobs can run later or inject events into a session.

Mitigation: Schedule only intentional jobs, prefer isolated sessions for autonomous work, and remove recurring jobs no longer needed.

Risk: Incorrect session target and payload combinations can produce unexpected cron behavior.

Mitigation: Use systemEvent payloads only with the main session target, and use agentTurn payloads with isolated, current, or explicit session targets.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/terrycarter1985/skills/cron-quickstart)

## Skill Output:

**Output Type(s):** [guidance, configuration, shell commands]

**Output Format:** [Markdown with JSON examples and inline shell command names]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Provides cron schedule examples and session-target constraints; does not execute jobs by itself.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
