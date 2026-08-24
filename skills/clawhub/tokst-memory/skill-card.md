## Description:

Use TokST to retrieve, store, govern, and hand off durable context across cloud workspaces or Local SQLite.

This skill is ready for commercial/non-commercial use.

## Publisher:

[anthemty](https://clawhub.ai/user/anthemty)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to give AI agents durable memory across sessions, devices, teams, cloud workspaces, and local SQLite profiles. The skill guides agents to load context, search prior knowledge, store confirmed facts and decisions, manage sessions, and configure CLI or MCP access.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks agents to retrieve and store broad persistent user and project context.

Mitigation: Prefer Local mode for private work, avoid saving secrets or sensitive documents, and regularly review, archive, or delete stored memories.

Risk: Installer examples pipe remote shell or PowerShell scripts directly into an interpreter.

Mitigation: Inspect or verify the installer before execution and install only in environments where TokST persistent memory is intended.

Risk: Automatic memory capture can persist incorrect, stale, or overly broad context.

Mitigation: Capture confirmed durable information only, use reviewable session candidates when human review is needed, and archive superseded information instead of overwriting history.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/anthemty/skills/tokst-memory)
- [TokST Documentation](https://tokst.com/docs)
- [TokST Help Center](https://tokst.com/help)
- [TokST MCP Setup](https://tokst.com/docs/mcp)
- [TokST Sessions](https://tokst.com/docs/sessions)
- [TokST Local](https://tokst.com/docs/local)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration]

**Output Format:** [Markdown instructions with shell commands and JSON configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes cloud and local memory workflows, MCP setup examples, and agent-safe JSON command guidance.]

## Skill Version(s):

0.8.0 (source: server release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
