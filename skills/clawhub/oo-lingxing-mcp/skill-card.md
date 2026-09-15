## Description:

Lingxing MCP helps an agent discover and call Lingxing ERP MCP tools through an OOMOL-connected account using schema-first JSON payloads.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and agents use this skill to discover current Lingxing ERP MCP tools and run read or write actions through an OOMOL-connected account. It is intended for Lingxing ERP workflows where the agent should inspect the live schema before constructing JSON arguments.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup instructions include one-line remote installer commands that can execute changing code on the user's machine.

Mitigation: Install the oo CLI only through an inspected, pinned, and verified method before using the skill.

Risk: Some Lingxing ERP MCP tools can create, update, remove, or overwrite ERP data.

Mitigation: Require explicit user confirmation of the exact target, payload, and expected effect before any write or destructive action.

Risk: Calling a Lingxing MCP tool with stale or assumed arguments can produce incorrect results or unintended changes.

Mitigation: Fetch the live tool schema before constructing each payload and validate JSON arguments against that schema.

## Reference(s):

- [Lingxing MCP homepage](https://www.lingxing.com/help/article/mcp)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Lingxing MCP skill on ClawHub](https://clawhub.ai/oomol/skills/oo-lingxing-mcp)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown with inline bash and JSON snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live Lingxing MCP tool schemas before calls; requires an OOMOL account with Lingxing MCP connected.]

## Skill Version(s):

1.0.2 (source: SKILL.md metadata and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
