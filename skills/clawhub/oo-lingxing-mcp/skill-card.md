## Description:

Enables agents to inspect and run Lingxing MCP tools through the OOMOL oo CLI for reading, creating, and updating Lingxing ERP data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and developers use this skill to discover Lingxing ERP MCP tools, validate live input schemas, and run approved read or write operations through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can perform business-data writes through a connected Lingxing MCP account.

Mitigation: Confirm the exact payload and intended effect with the user before running write or destructive actions.

Risk: The first-time setup path includes a remote oo CLI installer command.

Mitigation: Verify the OOMOL CLI installation instructions or installer source before running the installer.

Risk: Using the skill gives the agent access to actions available through the user's connected Lingxing MCP account.

Mitigation: Install and use the skill only when the user trusts OOMOL and intends the agent to operate through that connected account.

## Reference(s):

- [Lingxing MCP homepage](https://www.lingxing.com/help/article/mcp)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-lingxing-mcp)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance, Configuration instructions]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before execution and returns JSON response data when actions are run.]

## Skill Version(s):

1.0.3 (source: server release metadata and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
