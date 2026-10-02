## Description:

Connects agents to Notion through Maton-managed authentication to search content, manage pages and databases, and support approved automations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

People and teams use this skill to let an agent search and manage authorized Notion workspace content. With separate user approval, they can also set up hosted functions and event-driven workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An authorized connection can expose sensitive Notion workspace content or change pages and databases.

Mitigation: Approve the connection and its minimum necessary access; default to reading and confirm each write.

Risk: Hosted functions, triggers, and destinations can run repeatedly or forward workspace data.

Mitigation: Review and approve each deployment, trigger, and destination; avoid unscoped triggers or third-party URLs unless intentional, and restrict function network access.

Risk: A local event watcher using --exec can execute commands on the user's machine.

Mitigation: Review the command and explicitly approve the watcher before enabling it.

## Reference(s):

- [Notion MCP on ClawHub](https://clawhub.ai/byungkyu/skills/notion-mcp)
- [Maton](https://maton.ai)
- [Notion trigger reference](references/notion/triggers.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration guidance]

**Output Format:** [Text or Markdown, including structured Notion results and command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Notion operations require an authorized Maton connection; writes and automation require user approval.]

## Skill Version(s):

1.2.7 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
