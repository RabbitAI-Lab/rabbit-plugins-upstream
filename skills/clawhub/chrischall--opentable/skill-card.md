## Description:

Manage OpenTable reservations via MCP: search restaurants, check slot availability, book tables, list or cancel reservations, and manage favorites from a signed-in opentable.com browser session.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to let an agent help search OpenTable, inspect availability, and manage reservations or saved restaurants through an MCP server connected to their authenticated browser session.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on unpinned external MCP server and browser extension components operating through a signed-in OpenTable browser session.

Mitigation: Pin the MCP server and fetchproxy extension to reviewed versions and use a dedicated browser profile for OpenTable.

Risk: The skill can make real reservation changes, including booking, cancellation, modification, and favorite updates.

Mitigation: Require explicit user confirmation before any booking, cancellation, modification, or favorite change.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/opentable)
- [opentable-mcp npm package](https://www.npmjs.com/package/opentable-mcp)
- [Artifact-stated opentable-mcp source](https://github.com/chrischall/opentable-mcp)
- [fetchproxy browser extension](https://github.com/chrischall/fetchproxy)
- [OpenTable](https://www.opentable.com/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, API calls]

**Output Format:** [Markdown with MCP tool calls, JSON configuration snippets, and concise user-facing guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read tools default to compact responses that strip image and avatar URLs; booking, modification, cancellation, and favorite changes return receipts or status values.]

## Skill Version(s):

0.19.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
