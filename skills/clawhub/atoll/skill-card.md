## Description:

Use Atoll for project, issue, goal, KPI, initiative, milestone, artifact, PRD, implementation plan, comment, dependency, runner, and workflow operations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[doubledipcode](https://clawhub.ai/user/doubledipcode)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to plan and execute Atoll project-management workflows, including issue operations, artifacts, strategy tracking, execution records, integrations, and local runner administration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An authenticated curl helper could expose an Atoll API key or be misused with untrusted paths or arguments.

Mitigation: Prefer connected Atoll MCP tools or the typed Atoll CLI, avoid copying the raw helper into untrusted workflows, and keep API keys out of chat, logs, and repositories.

Risk: Unpinned npm package-install commands could run changed package code after publication.

Mitigation: Pin package versions and review package provenance before installing or running the CLI or MCP packages.

Risk: The local runner service can perform unattended background operation if enabled.

Mitigation: Enable the local runner service only when unattended operation is intended and review runner configuration before installation.

## Reference(s):

- [Atoll](https://atollhq.com)
- [Atoll MCP endpoint](https://atollhq.com/mcp)
- [Artifact workflow](references/artifact-workflow.md)
- [Authentication and profiles](references/authentication-and-profiles.md)
- [CLI operations](references/cli-operations.md)
- [Local runner](references/local-runner.md)
- [Strategy and heartbeat](references/strategy-and-heartbeat.md)
- [Execution and human attention](references/execution-and-attention.md)
- [Integrations and advanced API use](references/integrations-and-api.md)
- [Platform rules](references/platform-rules.md)
- [Atoll API Endpoint Reference](references/api-endpoints.md)
- [Atoll API Field Reference](references/api-fields.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, API calls, configuration]

**Output Format:** [Markdown with inline shell commands and structured Atoll operation guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose state-changing Atoll operations that require authorization, readback, and verification.]

## Skill Version(s):

1.0.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
