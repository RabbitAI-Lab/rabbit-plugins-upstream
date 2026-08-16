## Description:

Kiln lets AI agents design, slice, print, monitor, and recover 3D-printing jobs through an MCP server and CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[codeofaxel](https://clawhub.ai/user/codeofaxel)

### License/Terms of Use:

AGPL-3.0

## Use Case:

Developers, makers, and operators use Kiln to let agents control local or fleet 3D printers, generate or find printable models, slice files, queue jobs, monitor progress, and estimate costs from a conversational workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can control real 3D printers and may initiate high-impact physical actions.

Mitigation: Review it before installing on any real printer, keep auto-print environment variables disabled unless explicitly accepted, and rely on confirmation gates for destructive or raw G-code operations.

Risk: Shared or networked deployments without authentication can expose printer-control tools to unintended users.

Mitigation: Enable authentication for shared deployments and scope API keys according to the intended read, write, or admin access.

Risk: Background telemetry or community data sharing may occur by default.

Mitigation: Set KILN_TELEMETRY=false and KILN_COMMUNITY_OPT_IN=false if usage or community data sharing is not desired.

Risk: Printer, marketplace, generation, or fulfillment credentials may be usable by the local MCP server.

Mitigation: Provide only credentials that are appropriate for the deployment and acceptable for the server to use.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/codeofaxel/skills/kiln)
- [Kiln Website](https://kiln3d.com/?utm_source=mcp-registry&utm_medium=listing)
- [Kiln Docs](https://kiln3d.com/docs)
- [Kiln PyPI Package](https://pypi.org/project/kiln3d/)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration, Files, Guidance]

**Output Format:** [MCP tool responses, CLI output, JSON-capable command output, and Markdown guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May interact with printer hardware, slicers, local configuration, marketplace APIs, generation providers, and fulfillment services depending on enabled credentials and environment variables.]

## Skill Version(s):

1.4.0 (source: server.json and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
