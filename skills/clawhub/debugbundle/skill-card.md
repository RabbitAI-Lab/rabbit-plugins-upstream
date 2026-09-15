## Description:

Use DebugBundle for runtime error reporting, crash reporting, incident reporting, incident response, live app monitoring, and production monitoring focused on runtime failures, customer-facing incidents, and endpoint health; investigate exceptions, alerts, logs, observability signals, health checks, debug bundles, product analytics, and evidence-based fixes through MCP and CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[debugbundle](https://clawhub.ai/user/debugbundle)

### License/Terms of Use:

MIT No Attribution

## Use Case:

Developers and engineers use this skill to investigate production runtime failures, customer-facing incidents, endpoint health, product analytics, and DebugBundle evidence through MCP and CLI workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks users to run unpinned npm tooling with access to DebugBundle credentials.

Mitigation: Prefer pinned and vetted DebugBundle MCP and CLI package versions, and run them with least-privilege credentials.

Risk: The skill can guide broad management operations involving members, tokens, webhooks, Slack, GitHub dispatch, billing, monitoring, and incident lifecycle changes.

Mitigation: Confirm sensitive or organization-wide changes before allowing an agent to proceed, and review the skill before installing it in production-connected environments.

## Reference(s):

- [DebugBundle MCP Documentation](https://debugbundle.com/docs/mcp)
- [DebugBundle Analytics Documentation](https://debugbundle.com/docs/analytics)
- [DebugBundle CLI Analytics Documentation](https://debugbundle.com/docs/cli/analytics)
- [DebugBundle MCP Tools Documentation](https://debugbundle.com/docs/mcp/tools)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline JSON and bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide MCP and CLI operations that read or change DebugBundle incidents, health checks, analytics, tokens, webhooks, billing, and related project settings when explicitly requested.]

## Skill Version(s):

1.8.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
