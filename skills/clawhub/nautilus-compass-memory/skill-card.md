## Description:

Local-first long-term memory for AI agents via MCP, with local write-time embedding, typed retrieval at read time, shared filesystem memory, drift checks, and byte-verifiable published claims.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chunxiaoxx](https://clawhub.ai/user/chunxiaoxx)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to add persistent MCP-based memory, shared recall, session search, profile lookup, and drift checks to compatible AI agent clients. It is intended for workflows where decisions, pitfalls, configurations, and post-mortems should remain available across sessions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Install instructions ask users to execute unpinned remote code that may modify agent hooks and MCP configuration and start a local daemon.

Mitigation: Review the referenced install scripts before running them, prefer a pinned release or commit, and check exactly which MCP and Claude Code configuration files will change.

Risk: Using the hosted gateway may send memory content to an external service.

Mitigation: Avoid the hosted gateway for sensitive memory unless its data handling terms meet your requirements; prefer the local daemon when data should remain on the machine.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chunxiaoxx/skills/nautilus-compass-memory)
- [Publisher profile](https://clawhub.ai/user/chunxiaoxx)
- [Nautilus Compass repository](https://github.com/chunxiaoxx/nautilus-compass)
- [Hosted gateway signup](https://compass.nautilus.social/signup)
- [Hosted MCP endpoint](https://compass.nautilus.social/mcp/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and MCP configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose local daemon setup, hosted gateway connection, verification commands, and memory or drift-check usage guidance.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
