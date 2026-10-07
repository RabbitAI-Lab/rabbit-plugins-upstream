## Description:

Guides developers in designing agent-native applications where agents are primary actors, including tool interfaces, execution loops, shared workspaces, and approval patterns.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to plan or review agent-native products, tool designs, execution patterns, and safety controls against an architecture checklist.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Architecture advice may be mistaken for an enforceable permission boundary.

Mitigation: Enforce workspace scope, external authorization, and secret protection outside the prompt.

Risk: Self-modification or agent-initiated actions may cause destructive or public changes.

Mitigation: Require human approval for high-impact actions and maintain audit logs and rollback paths.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/iliaal/skills/compound-eng-agent-native-architecture)
- [Core principles](artifact/references/core-principles.md)
- [Architecture review checklist](artifact/references/architecture-review-checklist.md)
- [MCP tools specification](https://modelcontextprotocol.io/specification/2025-11-25/server/tools#tool)

## Skill Output:

**Output Type(s):** [Guidance, Analysis, Markdown, Code]

**Output Format:** [Markdown design guidance, checklists, and optional code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Tailored to the selected architecture topic and the user's application context.]

## Skill Version(s):

5.0.1 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
