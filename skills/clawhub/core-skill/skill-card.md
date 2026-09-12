## Description:

Core Skill gives an agent a verifiable Ed25519 identity tied to its principal, scoped delegation, signed action receipts, continuity across sessions and handoffs, and approval-gated connection workflows for finding people, companies, and other agents.

This skill is ready for commercial/non-commercial use.

## Publisher:

[aeoess](https://clawhub.ai/user/aeoess)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to add verifiable agent identity, scoped delegation, signed receipts, continuity across sessions, and approval-gated connection workflows to agent operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks users to run unpinned third-party tooling.

Mitigation: Use pinned, reviewed package versions where possible and review the package source before enabling it in sensitive environments.

Risk: The skill can use remote network services for identity and connection workflows.

Mitigation: Prefer a local or self-hosted MCP server for sensitive work, and approve each identity, search, publication, and introduction action explicitly.

Risk: Identity keys, receipts, delegation artifacts, and optional environment variables may be sensitive.

Mitigation: Limit exposed environment variables, protect generated credentials and receipt artifacts, and use short expiries, narrow scopes, and low spend limits.

Risk: Quiet session-start polling can surface pending connection state without a fresh user action.

Mitigation: Disable polling or require approval unless quiet checks are explicitly desired for the deployment.

## Reference(s):

- [APS protocol surface](references/aps.md)
- [Connection layer](references/connect.md)
- [Durable accountable continuity](references/continuity.md)
- [Agent Passport System on npm](https://www.npmjs.com/package/agent-passport-system)
- [Agent Passport System MCP on npm](https://www.npmjs.com/package/agent-passport-system-mcp)
- [Agent Passport System on PyPI](https://pypi.org/project/agent-passport-system/)
- [Agent Passport System repository](https://github.com/aeoess/agent-passport-system)
- [Remote MCP endpoint](https://mcp.aeoess.com/sse)
- [Core Skill on ClawHub](https://clawhub.ai/aeoess/skills/core-skill)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration]

**Output Format:** [Markdown guidance with inline shell commands and reference-module instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide installation and use of npm packages, a remote MCP endpoint, optional GitHub token use, and approval-gated identity, receipt, delegation, and connection workflows.]

## Skill Version(s):

1.0.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
