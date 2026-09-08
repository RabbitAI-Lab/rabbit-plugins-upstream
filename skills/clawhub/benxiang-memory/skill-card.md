## Description:

Benxiang Memory helps agents use an MCP server to persist structured project state in a .origin package, recover that state in later sessions, and trace why stored values changed.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dongsheng123132](https://clawhub.ai/user/dongsheng123132)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to install and operate an MCP-backed project memory workflow for persistent decisions, tasks, risks, verified facts, and module state across agent sessions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The installation flow clones an external repository before running the MCP server.

Mitigation: Review the repository before installation and pin a known commit when repeatability or supply-chain control matters.

Risk: Users may assume ordinary conversation is automatically preserved as durable project state.

Mitigation: Commit important decisions, tasks, risks, and verified facts through the structured tools, then use origin_state or origin_why before relying on recovered state.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dongsheng123132/skills/benxiang-memory)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands, JSON examples, and tool guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill guides use of structured MCP tools for project-state persistence; it does not claim ordinary chat transcript storage.]

## Skill Version(s):

1.1.1 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
