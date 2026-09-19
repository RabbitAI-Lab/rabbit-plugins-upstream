## Description:

Cloudflare MCP helps an agent use the OOMOL-connected Cloudflare MCP connector to search Cloudflare documentation, discover API endpoints, and run connector actions through the oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to interact with Cloudflare MCP through an OOMOL-connected account, including documentation search, API discovery, and connector action execution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The execute action is powerful and can run sandboxed JavaScript against Cloudflare MCP.

Mitigation: Treat execute as privileged, inspect the live action schema first, and require explicit user confirmation before actions that can change or remove Cloudflare resources.

Risk: The documented first-time setup includes remote installer commands.

Mitigation: Verify installer sources before use or choose a safer installation path approved by the deployment environment.

Risk: Cloudflare access is mediated through an OOMOL-connected account.

Mitigation: Install only when the publisher is trusted, use tightly scoped Cloudflare credentials, and confirm account connection status before operational use.

## Reference(s):

- [ClawHub Cloudflare MCP Skill](https://clawhub.ai/oomol/skills/oo-cloudflare-mcp)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [Cloudflare MCP](https://github.com/cloudflare/mcp)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration, Guidance, JSON]

**Output Format:** [Markdown guidance with bash commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector actions may return data with an executionId in response metadata.]

## Skill Version(s):

1.0.2 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
