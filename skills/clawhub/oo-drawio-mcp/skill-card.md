## Description:

Helps agents create editable draw.io diagrams and search diagram shapes through the OOMOL connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other diagram authors use this skill to create editable draw.io diagrams from Mermaid or draw.io XML and find shape styles for diagrams.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup suggests executing a remotely fetched installer script without integrity verification.

Mitigation: Review official installation instructions and the script before use; do not let an agent execute remote installers automatically.

Risk: Connector actions could exceed the requested diagram task or change state in future releases.

Mitigation: Limit actions to the user's request and confirm the payload and effect before any write or destructive action.

## Reference(s):

- [draw.io MCP skill on ClawHub](https://clawhub.ai/oomol/skills/oo-drawio-mcp)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI installation guide](https://cli.oomol.com/install-guide.md)
- [draw.io](https://www.drawio.com)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Diagram editor links, Shape styles]

**Output Format:** [Markdown with shell commands, diagram links, and shape style strings]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Diagram links open editable diagrams; shape searches return styles for draw.io XML.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
