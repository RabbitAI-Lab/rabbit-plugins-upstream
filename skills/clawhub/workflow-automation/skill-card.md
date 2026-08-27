## Description:

Use when users need workflow automation: validate allowlisted workflows, trigger a fixed Production Webhook after explicit approval, or read status and history for scoped workflow executions; requires WORKFLOW_AUTOMATION_API_KEY.

This skill is ready for commercial/non-commercial use.

## Publisher:

[youteacher](https://clawhub.ai/user/youteacher)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to safely validate preconfigured production workflows, request explicit approval for a trigger, and inspect execution status or recent execution history through the AI Skills platform.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Triggering production workflows may cause downstream business side effects.

Mitigation: Validate the workflow first, show the exact workflow version and input, and require explicit user approval before triggering.

Risk: A timeout or reconciliation-required response may mean the webhook was accepted even if final execution status is unknown.

Mitigation: Do not automatically retry; reconcile against the original task, workflow execution history, and downstream records.

Risk: Credential or target injection could redirect the workflow action or expose secrets.

Mitigation: Use only the preconfigured allowlisted production webhook and reject user-provided URLs, hosts, headers, credentials, tokens, cookies, secrets, or binary payloads.

## Reference(s):

- [API Key Configuration](references/API-KEY.md)
- [Operations Contract](references/OPERATIONS.md)
- [HTTP Requests and Task Polling](references/HTTP-REQUESTS.md)
- [Trigger, Reconciliation, and Safety Rules](references/BEHAVIOR-RULES.md)
- [AI Skills Platform](https://ai-skills.open-idea.net)
- [ClawHub Skill Page](https://clawhub.ai/youteacher/skills/workflow-automation)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, JSON]

**Output Format:** [Markdown guidance with bash and JSON request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires WORKFLOW_AUTOMATION_API_KEY and may return structured workflow validation, trigger, execution, or history results.]

## Skill Version(s):

1.0.0 (source: server release evidence and packageVersion metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
