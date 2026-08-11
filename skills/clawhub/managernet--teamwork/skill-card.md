## Description:

Teamwork defines an OpenClaw multi-agent coordination workflow with a lead coordinator, task files, audit fallback, cron scheduling, and immediate Git pushes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[managernet](https://clawhub.ai/user/managernet)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and project coordinators use this skill to structure multi-agent OpenClaw work into isolated task files, scheduled coordinator runs, audit review, human escalation, and visible Git-based delivery.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill instructs agents to automatically commit and push repository changes, which can publish unintended or unreviewed work.

Mitigation: Require a human review gate, use protected branches or pull requests, and avoid repository-wide git add -A before deployment.

Risk: Scheduled coordinator runs can continue changing task state or publishing work without timely human oversight.

Mitigation: Make cron scheduling opt-in, keep human escalation configured, and review task status and generated changes before publication.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/managernet/skills/teamwork)
- [Publisher profile](https://clawhub.ai/user/managernet)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration]

**Output Format:** [Markdown guidance with task JSON schema excerpts and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Coordinates .agent-coordination task files, cron scheduling, human notifications, and Git commit/push expectations.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
