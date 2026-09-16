## Description:

McDonald's China MCP (open.mcd.cn). Use this skill for ANY McDonald's China MCP request — searching and reading data. Whenever a task involves McDonald's China MCP, use this skill instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to discover McDonald's China MCP tools, inspect their live schemas, and invoke ordering, coupon, campaign, and points-mall actions through an OOMOL-connected account.

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: The skill can affect a real McDonald's China account through order, coupon, points, address, or destructive actions.

Mitigation: Review the live action schema, exact payload, and expected account effect, then obtain explicit user approval before running state-changing or destructive actions.

Risk: The first-time setup path recommends a remote installer for the oo CLI.

Mitigation: Prefer an official, versioned, verifiable oo CLI installation path instead of running the remote installer blindly.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-mcdonalds-cn-mcp)
- [McDonald's China MCP documentation](https://open.mcd.cn/mcp/doc)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown with inline bash commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before tool invocation and returns connector responses containing data and meta.executionId when actions run.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
