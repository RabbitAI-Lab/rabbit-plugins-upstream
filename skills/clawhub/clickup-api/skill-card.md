## Description:

ClickUp API integration with managed OAuth for accessing tasks, lists, folders, spaces, workspaces, users, and managing webhooks through the Maton CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, project operators, and developers use this skill to inspect and manage ClickUp work items, hierarchy resources, users, and webhooks through authenticated Maton API calls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Unpinned third-party package installation can install unexpected Maton CLI changes.

Mitigation: Verify the official Maton package source before installing, avoid elevated package-manager privileges, and review the installed CLI before use.

Risk: Broad ClickUp authorization can expose more workspace data than the task requires.

Mitigation: Prefer OAuth, choose the minimum ClickUp scopes needed, and revoke unused connections.

Risk: Write, delete, and webhook operations can modify ClickUp data or trigger downstream effects.

Mitigation: Review the target resource, payload, and intended effect before approving any write, delete, or webhook action.

## Reference(s):

- [ClickUp Skill on ClawHub](https://clawhub.ai/byungkyu/skills/clickup-api)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [ClickUp API Overview](https://developer.clickup.com/docs/Getting%20Started.md)
- [ClickUp Get Tasks](https://developer.clickup.com/reference/gettasks.md)
- [ClickUp Create Task](https://developer.clickup.com/reference/createtask.md)
- [ClickUp Create Webhook](https://developer.clickup.com/reference/createwebhook.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces API-call guidance and command examples; normal operation requires network access, a Maton account, and an authorized ClickUp connection.]

## Skill Version(s):

1.2.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
