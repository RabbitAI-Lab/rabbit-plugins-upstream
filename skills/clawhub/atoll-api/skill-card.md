## Description:

Helps agents plan, inspect, and manage Atoll projects, issues, strategy, artifacts, executions, and integrations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[doubledipcode](https://clawhub.ai/user/doubledipcode)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and project teams use this skill to inspect and update authorized Atoll work, coordinate planning and execution, and configure supported integrations or a local runner when needed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Agent actions can change or delete Atoll project-management data.

Mitigation: Use the least-privileged authorized profile and review destructive or administrative changes before execution.

Risk: API keys or sensitive content could be exposed in chat, comments, or commands.

Mitigation: Keep credentials in approved local configuration or environment variables; do not place real secret values in messages or Atoll content.

Risk: Enabling a local runner or outbound webhooks can trigger actions beyond a single chat response.

Mitigation: Review configuration, destination, permissions, and intended behavior before enabling either feature.

## Reference(s):

- [Atoll skill release](https://clawhub.ai/doubledipcode/skills/atoll-api)
- [Authentication and profiles](artifact/references/authentication-and-profiles.md)
- [CLI operations](artifact/references/cli-operations.md)
- [Execution and attention](artifact/references/execution-and-attention.md)
- [Local runner](artifact/references/local-runner.md)
- [Integrations and API](artifact/references/integrations-and-api.md)
- [Atoll Vercel integration documentation](https://docs.atollhq.com/integrations/vercel)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown with inline commands and API examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can guide authorized Atoll reads and writes; changes require task-appropriate access.]

## Skill Version(s):

1.0.22 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
