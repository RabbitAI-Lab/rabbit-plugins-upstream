## Description:

Guides agents in discovering, monitoring, and controlling TP-Link Tapo smart-home devices through Tapo MCP.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mihai-dinculescu](https://clawhub.ai/user/mihai-dinculescu)

### License/Terms of Use:

MIT-0

## Use Case:

Smart-home users and developers use this skill to discover Tapo devices, inspect their state, control supported devices, and request camera snapshots through a configured Tapo MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Plain HTTP can expose reusable bearer tokens and smart-home commands in transit.

Mitigation: Prefer loopback, VPN, SSH tunneling, or an HTTPS-protected endpoint; avoid sending bearer tokens over unprotected networks.

Risk: Bare npx commands may execute an unpinned mcporter version.

Mitigation: Pin or preinstall a trusted mcporter version before running commands.

Risk: The client configuration stores an access token that other local users may read.

Mitigation: Restrict access to the mcporter configuration file.

Risk: Device-control actions and camera snapshots can affect the home or reveal private imagery.

Mitigation: Require explicit user approval before controlling devices or capturing snapshots.

## Reference(s):

- [Tapo skill setup](artifact/references/setup.md)
- [Tapo MCP server setup](artifact/references/tapo-mcp-setup.md)
- [Tapo MCP documentation](https://github.com/mihai-dinculescu/tapo/tree/main/tapo-mcp)
- [ClawHub Tapo skill](https://clawhub.ai/mihai-dinculescu/skills/tapo)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Device discovery, status checks, control calls, and camera snapshots require access to a configured Tapo MCP server.]

## Skill Version(s):

0.5.1 (source: skill frontmatter and ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
