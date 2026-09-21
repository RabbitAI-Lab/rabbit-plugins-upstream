## Description:

Nautilus Compass Memory provides local-first long-term memory for MCP-capable AI agents with local write-time embeddings, hybrid retrieval, drift detection, and byte-recomputable signed evidence for published claims.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chunxiaoxx](https://clawhub.ai/user/chunxiaoxx)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to connect MCP-capable agents to a long-term memory layer that preserves decisions, pitfalls, shared project facts, and drift checks across sessions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill enables agent activity and memory content to persist across sessions.

Mitigation: Install it only when cross-session memory is desired, and avoid using prior context for one-shot tasks or when the user opts out.

Risk: The hosted gateway sends memories and recall queries to compass.nautilus.social.

Mitigation: Use the local daemon when memory content must remain on the user's machine.

Risk: Installer workflows can change Claude and other MCP client configuration files.

Mitigation: Review the pinned repository code before running installers and confirm configuration backups are available.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chunxiaoxx/skills/nautilus-compass-memory)
- [Nautilus Compass hosted signup](https://compass.nautilus.social/signup)
- [Nautilus Compass hosted MCP endpoint](https://compass.nautilus.social/mcp/)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration]

**Output Format:** [Markdown with inline bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Provides setup, verification, and MCP configuration guidance for local daemon or hosted gateway use.]

## Skill Version(s):

1.0.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
