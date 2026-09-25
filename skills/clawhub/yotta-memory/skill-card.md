## Description:

Provides file-based memory for AI agents to retain, retrieve, and organize context across sessions with separate shared and private records.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT-0

## Use Case:

AI agents and their developers use this skill to restore context at the start of a session, save relevant facts and preferences, search past memories, and archive work for future sessions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Network service and autostart can expose a memory store beyond the local agent.

Mitigation: Review network and autostart settings before enabling them; never use --no-auth on a non-loopback interface.

Risk: Tokens, private keys, and MCP configuration may expose access to private memories.

Mitigation: Review credential and MCP settings; keep tokens out of remembered content and use the core MCP tools for routine work.

Risk: Destructive maintenance can remove or change stored memories.

Mitigation: Review maintenance actions before running them and maintain recoverable backups.

Risk: Installation or upgrades can execute a changing runtime package.

Mitigation: Review installation behavior and pin package versions.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/yottameta/skills/yotta-memory)
- [Project homepage (listed in metadata)](https://github.com/YottaMeta/yotta-memory)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files, Shell commands, Configuration guidance]

**Output Format:** [Plain text or Markdown, with optional command and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can read and update local memory files and provide retrieved context to the agent.]

## Skill Version(s):

0.17.0 (source: skill frontmatter, package.json, ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
