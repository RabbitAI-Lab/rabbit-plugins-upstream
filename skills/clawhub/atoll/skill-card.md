## Description:

Guides agents through authorized Atoll planning, project management, execution, runner, and integration workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[doubledipcode](https://clawhub.ai/user/doubledipcode)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and their operators use this skill to plan and manage Atoll projects, issues, goals, KPIs, artifacts, and workflows through authorized connections, including local runner and integration operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Writes or deletions may affect the wrong workspace, project, or resource.

Mitigation: Confirm the authorized profile and target, inspect current state before writing, and read back changes; take particular care with project deletion.

Risk: Automation rules, webhooks, or local runner setup can trigger unintended actions.

Mitigation: Review scope and effects before enabling automation or changing webhooks or runner services; reconcile uncertain writes before retrying.

Risk: API keys or OAuth secrets could be exposed in chat or Atoll records.

Mitigation: Keep credentials in approved configuration rather than chat messages or Atoll records.

## Reference(s):

- [Atoll skill release](https://clawhub.ai/doubledipcode/skills/atoll)
- [Atoll](https://atollhq.com)
- [Authentication and profiles](references/authentication-and-profiles.md)
- [CLI operations](references/cli-operations.md)
- [Local runner](references/local-runner.md)
- [Integrations and API](references/integrations-and-api.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Text or Markdown with commands and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide authorized changes to Atoll resources; verify resulting state after writes.]

## Skill Version(s):

1.0.6 (source: server-resolved ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
