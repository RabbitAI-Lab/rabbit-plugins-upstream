## Description:

DCC-CUA routes explicitly named UI automation requests to the project-owned DCC-CUA and DCC-MCP UI Control stack with exact-target binding and fail-closed provider selection.

This skill is ready for commercial/non-commercial use.

## Publisher:

[loonghao](https://clawhub.ai/user/loonghao)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill when a user explicitly requests DCC-CUA so UI automation stays on the project-owned DCC-CUA route, binds the exact target, and verifies final state before completion.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authorized UI automation may observe application or browser state and send inputs to the bound target.

Mitigation: Use the skill only for explicit DCC-CUA requests, bind the exact target, keep sessions scoped, and verify the final state after actions.

Risk: A provider substitution or stale target binding could route actions outside the intended DCC-CUA surface.

Mitigation: Fail closed when DCC-CUA is unavailable, attest the provider and target before observing or acting, and require a fresh observation when the PID, window handle, tab target, or session owner changes.

## Reference(s):

- [DCC-CUA Skill Source](https://github.com/dcc-mcp/dcc-mcp-agent-plugins/blob/main/plugins/dcc-mcp/skills/dcc-cua/SKILL.md)
- [ClawHub Skill Page](https://clawhub.ai/loonghao/skills/dcc-cua)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration]

**Output Format:** [Markdown with inline bash and text blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Provider routing guidance with exact target-binding, readiness, interruption, and final-state verification requirements.]

## Skill Version(s):

0.19.103 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
