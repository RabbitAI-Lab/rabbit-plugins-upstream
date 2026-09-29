## Description:

Helps agents manage Wrike project work and team resources through a user-authorized Maton connection.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Project teams and their agents use this skill to review and manage Wrike tasks, projects, spaces, time logs, and team resources. Administrative operations and automations require deliberate user authorization.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Writes and administrative actions can alter account access or expose sensitive Wrike data.

Mitigation: Use least-privilege connections, confirm the target and effect before every write, and access audit logs or bulk exports only on explicit request.

Risk: Hosted automations or triggers can forward event data to external destinations.

Mitigation: Review the event source, payload, and destination with the user; obtain explicit approval before creating automations or forwarding data outside Maton.

Risk: A Maton API key can leak if exposed in output, logs, or saved files.

Mitigation: Prefer the CLI credential store; never print or persist keys and use raw HTTP only when the CLI is unavailable.

## Reference(s):

- [Wrike skill release](https://clawhub.ai/byungkyu/skills/wrike-api)
- [Maton](https://maton.ai)
- [Wrike API documentation](https://developers.wrike.com/)
- [Maton documentation](https://docs.maton.ai)
- [Time trigger reference](references/time/triggers.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration]

**Output Format:** [Markdown with command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-first workflows; user approval before writes or new connections.]

## Skill Version(s):

1.2.4 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
