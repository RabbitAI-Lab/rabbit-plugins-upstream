## Description:

Excalidraw MCP helps agents read, create, and update Excalidraw data through the OOMOL-connected excalidraw_mcp service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to operate Excalidraw through an OOMOL-connected account, including fetching drawing guidance and creating hand-drawn diagrams from JSON element arrays.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands that run downloaded scripts directly in a shell.

Mitigation: Prefer an official package manager or download-and-verify workflow, inspect installer contents before execution, and avoid administrator or root execution unless required.

Risk: The create_view action changes Excalidraw state.

Mitigation: Confirm the exact create_view payload and intended effect with the user before running the write action.

Risk: The skill depends on OOMOL and the oo CLI for Excalidraw access.

Mitigation: Install only when use of OOMOL and the oo CLI is acceptable for the user's environment and security posture.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-excalidraw-mcp)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Excalidraw homepage](https://excalidraw.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON payload patterns]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce connector schema commands, action execution commands, setup guidance, and confirmation prompts for write operations.]

## Skill Version(s):

1.0.2 (source: server release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
