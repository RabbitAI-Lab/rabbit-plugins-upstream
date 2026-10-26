## Description:

Control TP-Link Tapo smart home devices (lights, plugs, power strips, hubs and their child devices, cameras) via [Tapo MCP](https://github.com/mihai-dinculescu/tapo/tree/main/tapo-mcp).

This skill is ready for commercial/non-commercial use.

## Publisher:

[mihai-dinculescu](https://clawhub.ai/user/mihai-dinculescu)

### License/Terms of Use:

MIT-0

## Use Case:

External users can discover and inspect Tapo smart-home devices, retrieve device and energy state, control supported devices, and capture camera snapshots through a configured Tapo MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup sends a device-control and camera-access token over unencrypted local-network connections.

Mitigation: Use HTTPS or an encrypted tunnel for network connections, protect the saved token, and keep the server private.

Risk: Device controls can affect physical equipment, and camera snapshots may expose private imagery or access links.

Mitigation: Start with read-only tests, use noncritical equipment for power-control testing, enable camera access only when needed, and treat snapshot links as private until they expire.

## Reference(s):

- [Tapo MCP project](https://github.com/mihai-dinculescu/tapo/tree/main/tapo-mcp)
- [ClawHub release](https://clawhub.ai/mihai-dinculescu/skills/tapo)
- [Setup guide](references/setup.md)
- [Tapo MCP setup and configuration](references/tapo-mcp-setup.md)
- [Model Context Protocol](https://modelcontextprotocol.io/)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration guidance, Device state and control results, JSON and text, Camera snapshot links]

**Output Format:** [Markdown setup guidance with shell commands; MCP tool results as structured JSON or text.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Tool results depend on the configured Tapo MCP server and reachable, supported devices.]

## Skill Version(s):

0.6.0 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
