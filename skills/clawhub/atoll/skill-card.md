## Description:

Use Atoll for project, issue, goal, KPI, initiative, milestone, comment, dependency, runner, and workflow operations. Activate for Atoll planning, execution, project-management, local-runner, or integration requests.

This skill is ready for commercial/non-commercial use.

## Publisher:

[doubledipcode](https://clawhub.ai/user/doubledipcode)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external agent users use this skill to connect an agent to Atoll for planning and project-management workflows, including issue, goal, KPI, initiative, milestone, runner, and workflow operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide agents through Atoll project-management, runner, inbox, integration, billing, deletion, and admin workflows that may change external state.

Mitigation: Install only when Atoll access is intended, use least-privileged profiles or OAuth grants, and keep high-impact actions limited to trusted, user-directed workflows.

Risk: Atoll API keys, OAuth context, prompts, logs, local paths, or other sensitive payloads could be exposed if copied into commands, chats, comments, tickets, scripts, or attention requests.

Mitigation: Store credentials only in approved local configuration or environment variables, avoid pasting real keys into shared content, and keep attention requests, comments, evidence, and feedback free of sensitive data.

Risk: Ambiguous state-changing operations or retries could duplicate work or apply changes against stale workflow state.

Mitigation: Resolve actor, organization, project, and workflow state from live data; make the smallest required write; read back the changed resource; and verify the stored and user-visible result.

## Reference(s):

- [Atoll skill page](https://clawhub.ai/doubledipcode/skills/atoll)
- [Atoll base URL](https://atollhq.com)
- [Authentication and profiles](references/authentication-and-profiles.md)
- [CLI operations](references/cli-operations.md)
- [Local runner](references/local-runner.md)
- [Strategy and heartbeat](references/strategy-and-heartbeat.md)
- [Execution and human attention](references/execution-and-attention.md)
- [Integrations and advanced API use](references/integrations-and-api.md)
- [Platform rules](references/platform-rules.md)
- [Atoll API Endpoint Reference](references/api-endpoints.md)
- [Atoll API Field Reference](references/api-fields.md)
- [Atoll MCP endpoint](https://atollhq.com/mcp)
- [Atoll OAuth protected resource metadata](https://atollhq.com/.well-known/oauth-protected-resource)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline commands, JSON examples, and API or CLI references]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Atoll API calls, Atoll CLI commands, and configuration snippets; state-changing guidance requires readback verification.]

## Skill Version(s):

1.0.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
