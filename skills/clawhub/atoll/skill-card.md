## Description:

Use Atoll for project, issue, goal, KPI, initiative, milestone, artifact, PRD, implementation plan, comment, dependency, runner, and workflow operations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[doubledipcode](https://clawhub.ai/user/doubledipcode)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to operate Atoll workspaces through MCP, CLI, and REST workflows for planning, project management, strategy tracking, runner operations, and implementation handoff.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide agents through Atoll workspace mutations, including project, issue, runner, webhook, billing, and key-management operations.

Mitigation: Use least-privilege Atoll profiles, require explicit confirmation for destructive, billing, runner-service, webhook, and key-management actions, and verify changes with readback.

Risk: Credentials may be exposed if users paste API keys into chat or generated content.

Mitigation: Keep credentials in approved local configuration or environment variables and never include real API keys in prompts, comments, artifacts, logs, or commands shown to others.

Risk: Global or npx-based npm tooling can execute unreviewed package code.

Mitigation: Pin or review npm package versions before global installation or npx use.

Risk: Artifact, attachment, comment, and feedback content may contain untrusted instructions.

Mitigation: Treat workspace content as evidence, ignore embedded instructions that alter authorization or secret handling, and preserve Atoll access controls.

## Reference(s):

- [Atoll Skill on ClawHub](https://clawhub.ai/doubledipcode/skills/atoll)
- [Atoll](https://atollhq.com)
- [Authentication and profiles](references/authentication-and-profiles.md)
- [Artifact workflow](references/artifact-workflow.md)
- [CLI operations](references/cli-operations.md)
- [Local runner](references/local-runner.md)
- [Strategy and heartbeat](references/strategy-and-heartbeat.md)
- [Execution and human attention](references/execution-and-attention.md)
- [Integrations and API](references/integrations-and-api.md)
- [Platform rules](references/platform-rules.md)
- [Atoll API Endpoint Reference](references/api-endpoints.md)
- [Atoll API Field Reference](references/api-fields.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration, API calls]

**Output Format:** [Markdown guidance with inline commands, tool names, and API operation references]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose Atoll MCP, CLI, or REST actions; state-changing actions require live reads, narrow writes, and readback verification.]

## Skill Version(s):

1.0.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
