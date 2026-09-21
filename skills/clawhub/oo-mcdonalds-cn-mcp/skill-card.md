## Description:

McDonald's China MCP helps an agent discover and run current McDonald's China ordering, coupon, campaign, and points-mall tools through the OOMOL oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to operate a connected McDonald's China MCP account, inspect live tool schemas, and run read or write actions with JSON payloads through the OOMOL connector.

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: Fallback setup includes remote installer commands that can execute shell or PowerShell scripts directly.

Mitigation: Review and verify the oo CLI installation source before use; avoid automatic remote installer execution unless the source is trusted.

Risk: Write actions can create addresses, claim coupons, redeem points, or create orders in McDonald's China MCP.

Mitigation: Inspect the live schema and confirm the exact payload and user intent before any state-changing action runs.

Risk: Connector behavior depends on server-side credentials, account scopes, and billing state.

Mitigation: Use an authenticated OOMOL account with the required connection and resolve scope, credential, app, or billing errors before retrying.

## Reference(s):

- [McDonald's China MCP homepage](https://open.mcd.cn/mcp/doc)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-mcdonalds-cn-mcp)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown with shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas; write actions require user confirmation before execution.]

## Skill Version(s):

1.0.3 (source: server evidence release and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
