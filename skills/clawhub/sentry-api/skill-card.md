## Description:

Connects an agent to Sentry through Maton to inspect errors and events, manage Sentry resources, and configure approved automations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operations teams use this skill to inspect Sentry issues and events, manage projects, teams, and releases, and set up user-approved workflows through Maton.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The Sentry connection may expose sensitive issues and events within its authorized scope.

Mitigation: Use read-only, least-privilege access where possible and retrieve only data needed for the task.

Risk: Write and delete operations can change or remove Sentry resources.

Mitigation: Confirm each intended write or deletion and its target with the user before execution.

Risk: Functions, triggers, and destinations may keep running or forwarding data after creation.

Mitigation: Get explicit approval for each automation and destination, limit its scope, and remove it when no longer needed.

## Reference(s):

- [Sentry API documentation](https://docs.sentry.io/api/)
- [Maton documentation](https://docs.maton.ai)
- [Maton CLI manual](https://cli.maton.ai/manual)
- [Maton homepage](https://maton.ai)
- [Sentry skill release](https://clawhub.ai/byungkyu/skills/sentry-api)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Code, Configuration guidance]

**Output Format:** [Markdown with command and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a Maton account, network access, and an authorized Sentry connection.]

## Skill Version(s):

1.2.4 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
