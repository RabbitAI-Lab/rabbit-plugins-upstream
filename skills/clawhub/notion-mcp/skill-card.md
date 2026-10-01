## Description:

Guides agents in searching and updating authorized Notion workspaces through MCP with Maton-managed authentication and optional automations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

People and developers with an authorized Notion workspace use this skill to find content, manage pages and databases, and optionally set up approved automations through Maton.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authorizing Maton can grant access to selected Notion workspace content.

Mitigation: Authorize only the intended workspace and the minimum scopes needed for the task.

Risk: Writes and hosted automations can change content or forward future workspace data.

Mitigation: Confirm each write, connection, hosted function, trigger, destination, and event watcher before running it; narrowly scope triggers and destinations.

## Reference(s):

- [Notion MCP skill release](https://clawhub.ai/byungkyu/skills/notion-mcp)
- [Maton homepage](https://maton.ai)
- [Notion trigger reference](references/notion/triggers.md)
- [Notion REST API companion skill](https://clawhub.ai/byungkyu/notion-api-skill)

## Skill Output:

**Output Type(s):** [Text, Shell commands, JSON, Code, Configuration guidance]

**Output Format:** [Markdown with command and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read requests are the default; writes, new connections, and automations require user confirmation.]

## Skill Version(s):

1.2.6 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
