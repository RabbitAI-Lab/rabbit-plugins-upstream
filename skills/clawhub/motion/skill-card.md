## Description:

Helps agents query and manage Motion tasks, projects, and schedules through a connected Maton account, with optional user-approved automations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Motion users and teams can ask an agent to review scheduled work and manage tasks, projects, workspaces, comments, and recurring tasks. With separate approvals, they can also set up hosted functions and event- or time-based automations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Changes may affect the wrong Motion records or account.

Mitigation: Confirm the exact connection, target records, intended change, and user approval before writes.

Risk: Hosted code or triggers may run actions repeatedly or forward data.

Mitigation: Review the function code, connection scope, trigger, and destination URL; obtain separate approval for ongoing forwarding.

Risk: Exposed API credentials may allow unauthorized access.

Mitigation: Prefer managed sign-in and never print, copy into commands, or put credentials in trigger destinations.

## Reference(s):

- [Motion skill on ClawHub](https://clawhub.ai/byungkyu/skills/motion)
- [Maton homepage](https://maton.ai)
- [Motion API documentation](https://docs.usemotion.com/)
- [Motion API reference](https://docs.usemotion.com/api-reference)
- [Maton documentation](https://docs.maton.ai)
- [Maton CLI manual](https://cli.maton.ai/manual)
- [Time trigger reference](references/time/triggers.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Code, Configuration guidance]

**Output Format:** [Markdown with API results and optional command or code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Actions require a connected Motion account; writes and automations require explicit approval.]

## Skill Version(s):

1.2.5 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
