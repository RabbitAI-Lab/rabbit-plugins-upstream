## Description:

Provision a YG3 marketing workspace and call 200+ MCP tools for content, SEO, sites, outbound, LinkedIn, and ads. No human signup required.

This skill is ready for commercial/non-commercial use.

## Publisher:

[slamdunkboy17](https://clawhub.ai/user/slamdunkboy17)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent builders use this skill to provision YG3 marketing workspaces, inspect available MCP tools, configure business and brand data, publish marketing content, and clean up test workspaces.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill includes a workspace-claiming flow where an agent may handle a human owner's password.

Mitigation: Prefer the YG3 OAuth connection for existing accounts; if credentials are required, provide them only through a secure, user-directed flow with clear consent and no logging or long-term storage.

Risk: The skill can publish or modify marketing content through live MCP tools.

Mitigation: Review planned writes before confirmation, use the documented two-step confirm flow with an idempotency key, and keep human approval for externally visible content.

Risk: Unclaimed sandbox workspaces expire after 14 days and have publishing and channel restrictions.

Mitigation: Use unclaimed workspaces for temporary testing only, claim or upgrade workspaces needed for continued use, and clean up test workspaces when finished.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/slamdunkboy17/skills/yg3-marketing-mcp)
- [YG3 agent guide](https://www.yg3.ai/for-agents)
- [YG3 machine index](https://www.yg3.ai/llms.txt)
- [YG3 live tool catalog](https://mcp.yg3.ai/api/health)
- [YG3 MCP README](https://github.com/YG3-ai/yg3-mcp)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, API Calls, Configuration instructions]

**Output Format:** [Markdown with bash and JSON request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires curl for the documented provisioning and MCP examples.]

## Skill Version(s):

1.0.0 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
