## Description:

vortex-notes helps agents read, search, and write a user's Vortex Notes plain-Markdown vault, including semantic search, daily notes, and durable facts with supersession.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vortex-303](https://clawhub.ai/user/vortex-303)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to give an agent controlled access to a local Vortex Notes markdown vault for note search, reading, daily journaling, and durable memory updates.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can read and modify notes in the configured Vortex Notes vault.

Mitigation: Install it only for intended vault access, use a dedicated vault path, and use read-only MCP mode when the agent only needs search or context building.

Risk: Durable facts written to memory notes may become stale or be superseded by later information.

Mitigation: Review remembered facts periodically and preserve supersession history instead of deleting prior entries.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/vortex-303/skills/vortex-notes)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and plain-Markdown note conventions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May read or modify files in the configured Vortex Notes vault; MCP mode can be run read-only for search and context building.]

## Skill Version(s):

1.0.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
