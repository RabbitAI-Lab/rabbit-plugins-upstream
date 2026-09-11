## Description:

Set up and diagnose a secure, Nostr-authenticated YunoHost MCP connection in OpenClaw.

This skill is ready for commercial/non-commercial use.

## Publisher:

[imattau](https://clawhub.ai/user/imattau)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and OpenClaw users use this skill to configure and troubleshoot a signed bridge from OpenClaw to a YunoHost MCP endpoint with per-client Nostr identity setup.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Using an untrusted setup package or YunoHost MCP server URL could expose the user to an unsafe connection path.

Mitigation: Confirm trust in the yunohost-mcp-connect package and the YunoHost MCP server URL before running setup.

Risk: The setup creates a per-client private key that could compromise the connection if disclosed.

Mitigation: Do not print, request, or share the private key, and keep the generated key file readable only by the user.

Risk: Incorrect server URL, npub enrollment, or YunoHost role assignment can prevent the MCP connection from working.

Mitigation: Verify the remote URL, confirm the displayed npub has the required YunoHost role, and rerun the printed doctor command.

## Reference(s):

- [YunoHost MCP repository](https://github.com/imattau/yunohost-mcp)
- [ClawHub skill page](https://clawhub.ai/imattau/skills/yunohost-mcp)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes setup steps, identity-handling cautions, and diagnosis checks.]

## Skill Version(s):

0.8.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
