## Description:

Provision a YG3 marketing workspace and call 200+ MCP tools for content, SEO, sites, outbound, LinkedIn, and ads. No human signup required.

This skill is ready for commercial/non-commercial use.

## Publisher:

[slamdunkboy17](https://clawhub.ai/user/slamdunkboy17)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external agents use this skill to provision YG3 marketing infrastructure, configure a business profile and brand, and call live MCP tools for content, SEO, sites, outbound, LinkedIn, and ads.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security evidence flags the claim step because it asks an agent to handle and send a human owner's password.

Mitigation: Review the credential claim step before installing; avoid reused passwords and prefer OAuth or a one-time account-linking flow when available.

Risk: The skill provisions live YG3 workspaces and can call marketing APIs that create or publish content.

Mitigation: Use the documented two-step write confirmation flow, retain idempotency keys, and clean up unclaimed test workspaces that are no longer needed.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/slamdunkboy17/skills/yg3-marketing-mcp)
- [YG3 agent guide](https://www.yg3.ai/for-agents)
- [YG3 machine index](https://www.yg3.ai/llms.txt)
- [YG3 live tool catalog](https://mcp.yg3.ai/api/health)
- [YG3 MCP README](https://github.com/YG3-ai/yg3-mcp)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, API calls]

**Output Format:** [Markdown guidance with curl command examples and JSON request bodies]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes two-step write confirmation guidance, workspace token handling, and cleanup limits for unclaimed test workspaces.]

## Skill Version(s):

1.0.1 (source: server release metadata; artifact frontmatter lists 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
