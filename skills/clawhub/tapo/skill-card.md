## Description:

Control TP-Link Tapo smart home devices (lights, plugs, power strips, hubs and their child devices, cameras) via [Tapo MCP](https://github.com/mihai-dinculescu/tapo/tree/main/tapo-mcp).

This skill is ready for commercial/non-commercial use.

## Publisher:

[mihai-dinculescu](https://clawhub.ai/user/mihai-dinculescu)

### License/Terms of Use:

MIT-0

## Use Case:

People using OpenClaw with a Tapo MCP server can discover Tapo devices, inspect device state and energy or sensor data, control supported devices, and retrieve camera snapshots.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Smart-home controls can change device state, and camera access or snapshots can expose private images.

Mitigation: Use a server you control, keep bearer authentication enabled, protect stored credentials, and test with a read-only query or a nonessential device. Share snapshot links only with intended recipients because anyone holding a link can view it until it expires.

## Reference(s):

- [Tapo MCP](https://github.com/mihai-dinculescu/tapo/tree/main/tapo-mcp)
- [Model Context Protocol](https://modelcontextprotocol.io/)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Configuration instructions]

**Output Format:** [MCP tool results and concise text; setup guidance in Markdown with shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Device state and control results depend on the connected Tapo MCP server and supported devices; camera snapshots may be provided as short-lived links.]

## Skill Version(s):

0.6.1 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
