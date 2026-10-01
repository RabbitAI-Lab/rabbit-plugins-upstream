## Description:

Helps agents read and manage Google Tasks lists and tasks through a connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

People and teams use this skill to view, create, update, and delete Google Tasks lists and tasks. With separate approval, they can set up scheduled or event-driven task actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A connected account grants access to read and change tasks.

Mitigation: Prefer OAuth and confirm each write and new connection with the user.

Risk: Approved automations can continue acting on tasks or forward matching events to third-party destinations.

Mitigation: Confirm the automation target and forwarded data before approval; delete unused connections, functions, and triggers.

## Reference(s):

- [Google Tasks skill release](https://clawhub.ai/byungkyu/skills/google-tasks-api)
- [Google Tasks API overview](https://developers.google.com/workspace/tasks)
- [Google Tasks API reference](https://developers.google.com/workspace/tasks/reference/rest/v1/tasks)
- [Maton documentation](https://docs.maton.ai)
- [Maton CLI manual](https://cli.maton.ai/manual)
- [Maton homepage](https://maton.ai)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Code, Guidance]

**Output Format:** [Markdown with commands and task results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Task data may include personal information; automation requires separate approval.]

## Skill Version(s):

1.2.4 (source: ClawHub release evidence; skill metadata lists 1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
