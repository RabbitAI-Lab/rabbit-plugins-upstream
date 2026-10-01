## Description:

Helps agents manage ClickUp tasks, projects, and webhooks through a user-authorized Maton connection.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Teams and developers use this skill to retrieve and manage ClickUp work items and to set up approved webhooks or connected automations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The authorized connection may expose ClickUp data beyond the immediate task.

Mitigation: Authorize the narrowest available scopes and account, and remove unused connections.

Risk: Writes or deletions can change or remove project data.

Mitigation: Default to read-only operations and confirm the target and effect of each change before execution.

Risk: Webhooks and trigger destinations can continuously forward data until removed.

Mitigation: Require separate approval for each destination, review its recipient and data scope, and remove it when no longer needed.

## Reference(s):

- [ClickUp skill release](https://clawhub.ai/byungkyu/skills/clickup-api)
- [ClickUp API overview](https://developer.clickup.com/docs/Getting%20Started.md)
- [Maton documentation](https://docs.maton.ai)
- [Maton CLI manual](https://cli.maton.ai/manual)
- [Time trigger reference](references/time/triggers.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Code, Configuration guidance]

**Output Format:** [Markdown with inline shell and API examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access and a user-authorized Maton connection.]

## Skill Version(s):

1.2.4 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
