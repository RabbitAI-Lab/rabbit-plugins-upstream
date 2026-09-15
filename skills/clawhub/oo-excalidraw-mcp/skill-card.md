## Description:

Excalidraw MCP lets an agent inspect connector schemas, run OOMOL-connected Excalidraw actions, create diagram views, and retrieve drawing guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to operate an OOMOL-connected Excalidraw MCP service, create Excalidraw views from JSON element arrays, and retrieve Excalidraw formatting guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands that can execute changing code on the user's machine.

Mitigation: Do not let an agent automatically run installer commands; install the oo CLI manually from a trusted, versioned source and verify it where possible.

Risk: The create_view action changes Excalidraw MCP state.

Mitigation: Confirm the exact payload and intended effect with the user before running write actions.

## Reference(s):

- [Excalidraw MCP ClawHub page](https://clawhub.ai/oomol/skills/oo-excalidraw-mcp)
- [Excalidraw homepage](https://excalidraw.com)
- [OOMOL oo CLI repository](https://github.com/oomol-lab/oo-cli)
- [OOMOL oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, Text]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include connector schemas, JSON payloads, and connector execution results.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
