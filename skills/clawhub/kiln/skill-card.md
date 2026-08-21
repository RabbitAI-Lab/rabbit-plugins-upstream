## Description:

Kiln lets AI agents design, slice, print, monitor, and recover physical 3D-printing jobs through an MCP server and CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[codeofaxel](https://clawhub.ai/user/codeofaxel)

### License/Terms of Use:

AGPL-3.0

## Use Case:

Developers, operators, and makers use Kiln to let MCP-capable agents manage 3D-printing workflows, including model search, text-to-3D generation, slicing, printer control, camera monitoring, fleet operations, and fulfillment quotes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Agents can control real 3D printers and related services, creating physical safety and equipment risks.

Mitigation: Keep preview and confirmation gates enabled, supervise first runs, verify emergency-stop access, and avoid unattended prints without fire precautions.

Risk: Fulfillment workflows can create paid external orders.

Mitigation: Set spend limits before use and require explicit review before fulfillment quotes become orders.

Risk: Camera, cloud sync, and webhook features can expose sensitive operational data when enabled.

Mitigation: Disable unused camera, cloud sync, and webhook features, protect API keys, and use scoped credentials where available.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/codeofaxel/skills/kiln)
- [Project repository](https://github.com/codeofaxel/Kiln)
- [PyPI package](https://pypi.org/project/kiln3d/)
- [Kiln website](https://kiln3d.com)
- [Kiln documentation](https://kiln3d.com/docs)
- [Agent guide](https://kiln3d.com/agents)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown and plain text guidance with inline shell commands, JSON configuration, and MCP tool-oriented instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May cause agents to operate real printers, access cameras, manage files, and initiate paid fulfillment workflows when connected to configured services.]

## Skill Version(s):

1.4.1 (source: server release metadata and artifact/server.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
