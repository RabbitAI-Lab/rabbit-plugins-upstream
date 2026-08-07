## Description:

本象协议（Benxiang）is a persistent object representation layer for AI work that stores project state in .origin packages with objects, relationships, state, constraints, and provenance-backed semantic transactions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dongsheng123132](https://clawhub.ai/user/dongsheng123132)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent builders use this skill to understand and apply the Benxiang Protocol for persistent project state, semantic transactions, provenance queries, diagnostics, and MCP access across AI work sessions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Running the MCP server can expose project state from selected .origin packages to connected agents.

Mitigation: Run the MCP server only against .origin packages whose project state is appropriate for connected agents to access.

Risk: The skill references local node commands that depend on code from the intended repository.

Mitigation: Install only from the intended repository, review the referenced node command implementations before use, and run the documented verification command.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dongsheng123132/skills/benxiang-protocol)
- [Publisher Profile](https://clawhub.ai/user/dongsheng123132)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration]

**Output Format:** [Markdown with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include protocol concepts, MCP tool names, transaction examples, and verification commands.]

## Skill Version(s):

1.0.0 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
