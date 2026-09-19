## Description:

Use Atoll for project, issue, goal, KPI, initiative, milestone, artifact, PRD, implementation plan, comment, dependency, runner, and workflow operations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[doubledipcode](https://clawhub.ai/user/doubledipcode)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to operate Atoll workspaces, including planning, issue management, strategy tracking, artifact workflows, local runners, agent executions, integrations, and API-oriented operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Agents operating this skill can act against live Atoll data.

Mitigation: Install only for intended Atoll use, use a least-privileged Atoll profile, and confirm the selected actor and project before state-changing operations.

Risk: API keys, OAuth selectors, or local configuration values could be exposed through copied commands or chat content.

Mitigation: Keep credentials in approved local configuration or environment variables and avoid pasting real API keys into shell commands or conversation text.

Risk: Destructive deletes, service installation, or external communications can have durable effects.

Mitigation: Require explicit confirmation before destructive actions, service installation, production mutation, or external communication.

Risk: Unpinned package installation may change behavior over time.

Mitigation: Pin npm package versions where possible when installing or operating the Atoll CLI or runner tooling.

## Reference(s):

- [Atoll Skill on ClawHub](https://clawhub.ai/doubledipcode/skills/atoll-api)
- [Atoll](https://atollhq.com)
- [Atoll MCP Endpoint](https://atollhq.com/mcp)
- [Authentication and profiles](references/authentication-and-profiles.md)
- [Artifact workflow](references/artifact-workflow.md)
- [CLI operations](references/cli-operations.md)
- [Local runner](references/local-runner.md)
- [Strategy and heartbeat](references/strategy-and-heartbeat.md)
- [Execution and human attention](references/execution-and-attention.md)
- [Integrations and advanced API use](references/integrations-and-api.md)
- [Atoll API Endpoint Reference](references/api-endpoints.md)
- [Atoll API Field Reference](references/api-fields.md)
- [Platform rules](references/platform-rules.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, JSON examples, and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include API request details, Atoll CLI commands, artifact drafts, implementation plans, status updates, and verification notes.]

## Skill Version(s):

1.0.20 (source: server release metadata, released 2026-09-16)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
