## Description:

Control TP-Link Tapo smart home devices (lights, plugs, power strips, hubs and their child devices, cameras) via [Tapo MCP](https://github.com/mihai-dinculescu/tapo/tree/main/tapo-mcp).

This skill is ready for commercial/non-commercial use.

## Publisher:

[mihai-dinculescu](https://clawhub.ai/user/mihai-dinculescu)

### License/Terms of Use:

MIT-0

## Use Case:

Home automation users and developers use this skill to connect an agent to a Tapo MCP server, inspect device state, control supported devices, and request camera snapshots.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An exposed bearer token could allow access to smart-home devices and cameras.

Mitigation: Use HTTPS or an encrypted tunnel for LAN access, configure bearer authentication, and protect the saved configuration.

Risk: Anyone holding an optional snapshot link can view its image until the link expires.

Mitigation: Share snapshot links only with intended recipients; links expire after five minutes.

Risk: External runtime packages and server binaries were not audited.

Mitigation: Use reviewed, pinned client and container versions.

## Reference(s):

- [Tapo MCP documentation](https://github.com/mihai-dinculescu/tapo/tree/main/tapo-mcp)
- [Tapo Skill Setup](references/setup.md)
- [Setting Up the Tapo MCP Server](references/tapo-mcp-setup.md)
- [ClawHub release page](https://clawhub.ai/mihai-dinculescu/skills/tapo)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions, API calls]

**Output Format:** [Markdown with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Provides instructions for querying device state, controlling supported devices, and requesting camera snapshots.]

## Skill Version(s):

0.6.2 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
