## Description:

Guides the design of agent-native applications, including MCP tools, agent loops, prompts, hooks, shared workspaces, and self-modifying systems.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to design and review agent-native applications, including tool access, execution loops, workspace coordination, and approval boundaries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An implementation based on the guidance could give agents excessive access to files, secrets, or external actions.

Mitigation: Enforce workspace scoping, secret redaction, and approval for destructive or external actions.

Risk: Self-modifying or deployment workflows could make unsafe changes that are difficult to trace or undo.

Mitigation: Require human review, audit logs, and rollback for self-modification and deployment paths.

## Reference(s):

- [Architecture Review Checklist](references/architecture-review-checklist.md)
- [Core Principles](references/core-principles.md)
- [MCP Tool Design](references/mcp-tool-design.md)
- [Agent Execution Patterns](references/agent-execution-patterns.md)
- [Hooks Patterns](references/hooks-patterns.md)
- [Self-Modification](references/self-modification.md)

## Skill Output:

**Output Type(s):** [Architecture guidance, Markdown, Code and configuration examples]

**Output Format:** [Markdown with optional code or configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Documentation guidance; does not itself install code or run commands.]

## Skill Version(s):

5.1.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
