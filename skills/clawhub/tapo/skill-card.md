## Description: <br>
Control TP-Link Tapo smart-home devices, including lights, plugs, power strips, hubs, sensors, and cameras, through a Tapo MCP server. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mihai-dinculescu](https://clawhub.ai/user/mihai-dinculescu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and smart-home operators use this skill to connect an agent to a trusted Tapo MCP server, inspect device state, control supported Tapo devices, and capture camera snapshots when configured. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can control physical smart-home devices through the configured Tapo MCP server. <br>
Mitigation: Install only for trusted servers, run list_devices before control actions, and use device IDs and IPs from recent discovery instead of guessing values. <br>
Risk: Camera snapshots, trigger logs, device IDs, IP addresses, and sensor records can expose private household data. <br>
Mitigation: Treat outputs as private data, restrict server exposure to the required network scope, and avoid sharing snapshots or logs outside the intended environment. <br>
Risk: A reachable unauthenticated server or overly broad host access could allow unintended device access. <br>
Mitigation: Use bearer authentication, configure TAPO_MCP_ALLOWED_HOSTS for LAN or hostname access, and keep non-loopback binds authenticated. <br>
Risk: Bearer tokens stored in mcporter configuration can grant access to the Tapo MCP server. <br>
Mitigation: Protect the mcporter config file, for example with restrictive local file permissions, and rotate credentials if exposure is suspected. <br>


## Reference(s): <br>
- [Tapo Skill Setup](references/setup.md) <br>
- [Setting Up the Tapo MCP Server](references/tapo-mcp-setup.md) <br>
- [Tapo skill page](https://clawhub.ai/mihai-dinculescu/skills/tapo) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and configuration examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May invoke configured MCP tools that return JSON device data or JPEG camera snapshots.] <br>

## Skill Version(s): <br>
0.5.0 (source: server evidence release.version and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
