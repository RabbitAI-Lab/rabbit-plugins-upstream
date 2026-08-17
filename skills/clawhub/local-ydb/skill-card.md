## Description:

Operate local-ydb deployments, including Docker setup, YDB schema work, managed SQL, auth hardening, monitoring exposure, storage changes, and troubleshooting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[astandrik](https://clawhub.ai/user/astandrik)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to inspect, configure, harden, and troubleshoot local YDB deployments. It helps plan and generate commands, schemas, verification steps, and rollback-aware operational guidance for local-ydb environments.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can help plan sensitive local-ydb administration tasks such as password handling, auth hardening, Docker restarts, storage cleanup, and stack destruction.

Mitigation: Review commands before confirmed mutations, require explicit confirmation for changes, and test against disposable or backed-up targets.

Risk: A chat-only or remote environment cannot directly inspect a user's Docker daemon, files, or YDB endpoints.

Mitigation: State when the target was not inspected and provide bounded guidance or commands for the user to run instead of reporting inferred health as observed fact.

Risk: Reusable output can accidentally expose secrets, private host details, credential paths, or one-off operational notes.

Mitigation: Use placeholders for secrets and private paths, keep host-specific notes out of reusable docs, and redact sensitive values in examples and results.

## Reference(s):

- [Auth Hardening Reference](references/auth-hardening.md)
- [Topology Reference](references/topology.md)
- [Storage Migration Reference](references/storage-migration.md)
- [Verification Reference](references/verification.md)
- [MCP Tool Scenarios](references/mcp-tool-scenarios.md)
- [History and Non-Goals Reference](references/history-and-non-goals.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline code blocks and structured operational guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include plan-first mutation guidance, verification steps, rollback notes, and redacted placeholders for secrets or host-specific values.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
