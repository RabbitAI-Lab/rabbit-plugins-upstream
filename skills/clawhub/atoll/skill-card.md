## Description:

Guides agents through Atoll project planning, issue and goal management, execution workflows, integrations, and optional local runner operations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[doubledipcode](https://clawhub.ai/user/doubledipcode)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and project teams use this skill to plan and manage Atoll projects, issues, goals, artifacts, and agent work through authorized Atoll connections. It also guides integration setup and optional local runner operation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad Atoll permissions can change or delete project data and trigger automation or external communications.

Mitigation: Use a scoped agent or OAuth profile and review before enabling automation, webhooks, destructive deletes, or billing and admin actions.

Risk: The optional unattended local runner can act without interactive supervision.

Mitigation: Enable the runner only when unattended operation is intended and review its configuration and permissions first.

Risk: Exposed API keys or sensitive project content can disclose access or private information.

Mitigation: Keep credentials out of chat and project content and use approved local configuration or environment variables.

## Reference(s):

- [Atoll skill release](https://clawhub.ai/doubledipcode/skills/atoll)
- [Authentication and profiles](references/authentication-and-profiles.md)
- [CLI operations](references/cli-operations.md)
- [API endpoints](references/api-endpoints.md)
- [Execution and attention](references/execution-and-attention.md)
- [Local runner](references/local-runner.md)
- [Integrations and API](references/integrations-and-api.md)
- [Atoll Vercel integration documentation](https://docs.atollhq.com/integrations/vercel)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown with optional commands and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide authorized Atoll reads and writes; no credentials in output.]

## Skill Version(s):

1.0.5 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
