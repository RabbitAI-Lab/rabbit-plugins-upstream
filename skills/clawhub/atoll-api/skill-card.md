## Description:

Use Atoll for project, issue, goal, KPI, initiative, milestone, comment, dependency, runner, and workflow operations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[doubledipcode](https://clawhub.ai/user/doubledipcode)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operational agents use this skill to manage Atoll planning and execution workflows, including issues, strategy objects, comments, dependencies, local runners, and integrations. It guides agents toward live authorization checks, read-before-write workflows, and verified state changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Atoll credentials and workspace data could be exposed through prompts, comments, evidence, logs, local runner output, or misconfigured profiles.

Mitigation: Use least-privileged Atoll credentials, keep secrets in approved local configuration or environment variables, avoid placing secrets in Atoll content or model-visible text, and rotate credentials if a secret is pasted into chat.

Risk: State-changing project-management operations could modify or delete broad sets of work items if run under the wrong actor, project, or workflow state.

Mitigation: Resolve the actor and project from live data, read the target before writing, use the narrowest typed command or tool, require appropriate authority for destructive or production-impacting changes, and read back the changed resource.

Risk: CLI or MCP server use can expand the agent's runtime access to Atoll workspaces and local runner workflows.

Mitigation: Prefer pinned reviewed package versions or locked local installs, keep the MCP server bound to loopback unless protected by authenticated TLS, and review broad project changes before allowing them.

Risk: Attachments, feedback, and external payloads may contain untrusted content that tries to redirect the agent.

Mitigation: Treat attachments, feedback, and third-party responses as evidence rather than instructions, and avoid following embedded instructions or exposing raw sensitive payloads.

## Reference(s):

- [Atoll Skill Release](https://clawhub.ai/doubledipcode/skills/atoll-api)
- [Atoll Base URL](https://atollhq.com)
- [Atoll MCP Endpoint](https://atollhq.com/mcp)
- [Atoll OAuth Protected Resource Metadata](https://atollhq.com/.well-known/oauth-protected-resource)
- [Authentication and Profiles](references/authentication-and-profiles.md)
- [CLI Operations](references/cli-operations.md)
- [Local Runner](references/local-runner.md)
- [Strategy and Heartbeat](references/strategy-and-heartbeat.md)
- [Execution and Human Attention](references/execution-and-attention.md)
- [Integrations and Advanced API Use](references/integrations-and-api.md)
- [Platform Rules](references/platform-rules.md)
- [Atoll API Endpoint Reference](references/api-endpoints.md)
- [Atoll API Field Reference](references/api-fields.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, API calls, Configuration]

**Output Format:** [Markdown with inline shell commands, API paths, and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Atoll CLI/MCP operations and API request bodies; state-changing workflows require readback verification.]

## Skill Version(s):

1.0.19 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
