## Description:

Excalidraw MCP helps agents operate an OOMOL-connected Excalidraw MCP account by fetching connector schemas, running connector actions, creating Excalidraw diagrams from JSON element arrays, and reading Excalidraw element guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to create Excalidraw diagrams and retrieve Excalidraw element guidance through OOMOL's Excalidraw MCP connector.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The create_view action creates Excalidraw content and may be run without a clear write label.

Mitigation: Confirm the exact diagram payload and expected effect with the user before running create_view.

Risk: The setup instructions include remote install commands for the OOMOL CLI.

Mitigation: Do not execute remote install commands unless the user independently trusts and verifies the OOMOL CLI installer.

Risk: The security verdict is suspicious.

Mitigation: Review the skill before installing or deploying it, using the scanner summary and guidance as the authoritative risk source.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-excalidraw-mcp)
- [Excalidraw](https://excalidraw.com)
- [OOMOL CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [Skill icon](https://static.oomol.com/logo/third-party/excalidraw_mcp.png)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May trigger oo CLI connector calls that return JSON responses containing data and execution metadata.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
