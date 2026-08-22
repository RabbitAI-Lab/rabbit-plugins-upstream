## Description:

zwjh-skill provides a local long-term memory and knowledge graph foundation for agents, with automatic capture, retrieval, health auditing, backup, MCP tools, and optional web visualization.

This skill is ready for commercial/non-commercial use.

## Publisher:

[fyniujin](https://clawhub.ai/user/fyniujin)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to give agents persistent local memory, knowledge graph retrieval, and status/audit workflows across conversations and projects.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Persistent memory can store conversations, logs, file summaries, file paths, and graph data.

Mitigation: Install only when persistent local memory is intended, and review what the skill stores before depositing sensitive information.

Risk: Setup can create recurring background tasks.

Mitigation: Review the scheduled task before enabling setup, and remove or disable it when recurring memory processing is not needed.

Risk: Cloud backup can upload memory data through a locally configured Baidu Netdisk client.

Mitigation: Keep backups local unless cloud upload is explicitly intended, and do not configure cloud tokens unless that upload path is approved.

Risk: The web UI and MCP server expose sensitive local memory interfaces.

Mitigation: Use these interfaces only in trusted local sessions, restrict access to local endpoints, and stop the servers when they are not needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/fyniujin/skills/zwjh-skill)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown and plain text with shell commands; JSON-RPC text results when used through MCP tools]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create persistent local memory, backups, scheduled tasks, and local interface responses when the agent runs its commands.]

## Skill Version(s):

2.4.0 (source: SKILL.md frontmatter, version.json, release evidence; released 2026-08-17)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
